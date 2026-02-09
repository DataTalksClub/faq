#!/usr/bin/env python3
"""
Static Site Generator for FAQ Content
Processes markdown files from _questions/ and generates static HTML site in _site/
"""

import shutil
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader
import mistune
from mistune.plugins.table import table
from mistune.plugins.task_lists import task_lists
from pygments import highlight
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound
from datetime import datetime
import re
import json


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content"""
    if not content.startswith('---'):
        return {}, content
    
    try:
        # Split frontmatter and content
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}, content
        
        frontmatter = yaml.safe_load(parts[1])
        markdown_content = parts[2].strip()
        
        return frontmatter or {}, markdown_content
    except yaml.YAMLError:
        return {}, content


def convert_plain_urls_to_links(text):
    """Convert plain text URLs to markdown links, avoiding code blocks and inline code"""
    
    # Split content by code blocks first
    code_block_pattern = r'(```.*?```)'
    parts = re.split(code_block_pattern, text, flags=re.DOTALL)
    
    result_parts = []
    
    for i, part in enumerate(parts):
        # If this is a code block (odd indices in split result), don't process URLs
        if i % 2 == 1 and part.startswith('```'):
            result_parts.append(part)
        else:
            # For non-code-block parts, split by inline code
            inline_code_pattern = r'(`[^`]+`)'
            inline_parts = re.split(inline_code_pattern, part)
            
            processed_inline_parts = []
            for j, inline_part in enumerate(inline_parts):
                # If this is inline code (odd indices), don't process URLs
                if j % 2 == 1 and inline_part.startswith('`'):
                    processed_inline_parts.append(inline_part)
                else:
                    # Process URLs in plain text only
                    # Avoid URLs already in markdown links [text](url) or <url>
                    url_pattern = r'(?<!\[)(?<!\()(?<!<)(https?://[^\s<>\)]+)(?!\])(?!\))(?!>)'
                    
                    def replace_url(match):
                        full_url = match.group(1)
                        # Extract trailing punctuation
                        trailing_punct = ''
                        url = full_url
                        while url and url[-1] in '.,;:!?':
                            trailing_punct = url[-1] + trailing_punct
                            url = url[:-1]
                        return f'[{url}]({url}){trailing_punct}'
                    
                    processed_part = re.sub(url_pattern, replace_url, inline_part)
                    processed_inline_parts.append(processed_part)
            
            result_parts.append(''.join(processed_inline_parts))
    
    return ''.join(result_parts)


# Configure mistune with plugins for syntax highlighting and tables
class HighlightRenderer(mistune.HTMLRenderer):
    # Language aliases for better compatibility
    LANGUAGE_ALIASES = {
        'sh': 'bash',
        'shell': 'bash',
        'dockerfile': 'docker',
        'yml': 'yaml',
        'py': 'python',
        'js': 'javascript',
        'ts': 'typescript',
        'c++': 'cpp',
        'psql': 'postgresql',
    }
    
    def block_code(self, code, info=None):
        # Clean and normalize the language info
        language = None
        if info:
            language = info.strip().lower()
            # Apply language aliases
            language = self.LANGUAGE_ALIASES.get(language, language)
        
        # Try to get the appropriate lexer
        lexer = self.get_lexer(code, language)

        # Generate highlighted HTML
        formatter = HtmlFormatter(
            cssclass='highlight',
            wrapcode=True
        )
        return highlight(code, lexer, formatter)

    def get_lexer(self, code, language):
        if not language:
            return get_lexer_by_name('text')

        try:
            return get_lexer_by_name(language)
        except ClassNotFound:
            return get_lexer_by_name('text')
    
    def codespan(self, text):
        """Render inline code with CSS class"""
        return f'<code class="inline-code">{mistune.escape(text)}</code>'
    
    def link(self, text, url, title=None):
        """Render links to open in new window"""
        # Escape the URL
        url = mistune.escape(url, quote=True)
        
        # Don't escape text if it contains HTML tags
        # This allows code elements inside links to render properly
        if '<' not in text or '>' not in text:
            text = mistune.escape(text)
        
        if title:
            title = mistune.escape(title, quote=True)
            return f'<a href="{url}" title="{title}" target="_blank">{text}</a>'
        else:
            return f'<a href="{url}" target="_blank">{text}</a>'

markdown_processor = mistune.create_markdown(
    renderer=HighlightRenderer(),
    plugins=[table, task_lists]
)

def process_markdown(content, images=None):
    """Convert markdown to HTML while replacing image placeholders with actual image tags"""
    # Replace image placeholders with markdown image syntax
    images = images or []

    for image in images:
        # Create proper markdown image syntax
        image_markdown = f'![{image["description"]}]({image["path"]})'
        content = content.replace(f'<{{IMAGE:{image["id"]}}}>', image_markdown)

    # Convert plain text URLs to clickable markdown links
    content = convert_plain_urls_to_links(content)

    return markdown_processor(content)


def load_course_metadata(course_dir):
    """Load metadata for a course to get section ordering and course name"""
    metadata_file = course_dir / '_metadata.yaml'

    if not metadata_file.exists():
        print(f"Warning: No metadata file found for {course_dir.name}, using defaults")
        return {
            'sections': [],
            'course_name': course_dir.name
        }

    with open(metadata_file, 'r', encoding='utf-8') as f:
        metadata = yaml.safe_load(f) or {}
        sections = metadata.get('sections', [])
        course_name = metadata.get('course_name', course_dir.name)

        return {
            'sections': sections,
            'course_name': course_name
        }

def collect_questions():
    questions_dir = Path('_questions')
    if not questions_dir.exists():
        print("No questions directory found")
        return {}

    courses = []

    for course_dir in questions_dir.iterdir():
        if not course_dir.is_dir():
            continue

        course_dir_name = course_dir.name

        course_info = process_course(course_dir)
        courses.append((course_dir_name, course_info))

    return courses


def process_course(course_dir):
    course_dir_name = course_dir.name
    print(f"Processing course: {course_dir_name}")

    # Load course metadata to get section ordering and course name
    metadata = load_course_metadata(course_dir)
    section_order = metadata['sections']
    course_display_name = metadata['course_name']
    print(f"  Found {len(section_order)} sections in metadata, display name: {course_display_name}")

    # Collect questions by section
    sections = {}

    # New nested structure: _questions/course/section/question.md
    print(f"  Using nested directory structure for {course_dir_name}")
        
    for section_dir in course_dir.iterdir():
        if not section_dir.is_dir() or section_dir.name.startswith('_'):
            continue

        section_data, section_name = process_section(course_dir_name, section_order, section_dir)
        sections[section_name] = section_data

    return {
        'sections': sections,
        'section_order': section_order,
        'course_name': course_display_name
    }


def process_section(course_name, section_order, section_dir):
    section_data = []

    section_id = section_dir.name
    print(f"    Processing section: {section_id}")

    section_name = find_section_name(section_order, section_id)
  
    for question_file in sorted(section_dir.glob('*.md')):
        try:
            question_data = process_question_file(course_name, section_name, question_file)
            if question_data:
                section_data.append(question_data)

        except Exception as e:
            print(f"Error processing {question_file}: {e}")

    return section_data, section_name


def find_section_name(section_order, section_id):
    for section_info in section_order:
        if section_info['id'] == section_id:
            return section_info['name']

    print(f"Warning: Section {section_id} not found in metadata, using ID as name")
    return section_id


def process_question_file(course_name, section_name, question_file):
    with open(question_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, markdown_content = parse_frontmatter(content)
    
    if not frontmatter.get('question'):
        print(f"Skipping {question_file}: missing question field in frontmatter")
        return None
    
    # Process markdown to HTML with image placeholders
    images = frontmatter.get('images', [])
    html_content = process_markdown(markdown_content, images)
    
    # Get relative path from _questions directory
    relative_path = question_file.relative_to(Path('_questions'))
    
    question_data = {
        'id': frontmatter.get('id', ''),
        'question': frontmatter['question'],
        'section': section_name,
        'sort_order': frontmatter.get('sort_order', 999999),
        'course': course_name,
        'content': html_content,
        'answer': markdown_content,  # Store raw markdown for JSON export
        'file_path': str(relative_path).replace('\\', '/'),  # Full path for GitHub link
        'images': images
    }

    return question_data


def setup_jinja_environment():
    """Set up Jinja2 environment with templates from _layouts"""
    layouts_dir = Path('_layouts')
    if not layouts_dir.exists():
        layouts_dir.mkdir(exist_ok=True)
    
    env = Environment(
        loader=FileSystemLoader(str(layouts_dir)),
        autoescape=True
    )
    
    # Add custom filters
    def title_case(text):
        return text.replace('-', ' ').replace('_', ' ').title()
    
    env.filters['title_case'] = title_case
    
    return env


def sort_sections_and_questions(courses):
    # TODO: side-effect: modifies course_data
    """Sort sections according to metadata order and questions by sort_order"""

    for course_name, course_data in courses:
        sections = course_data['sections']
        section_order = course_data['section_order']
        
        # Sort questions within each section by sort_order
        for section_name, questions in sections.items():
            questions.sort(key=lambda q: q['sort_order'])
        
        # Create ordered sections list with both ID and name information
        ordered_sections = []
        
        # First, add sections in metadata order
        # section_order now contains dicts with 'id' and 'name' keys
        for section_info in section_order:
            section_name = section_info['name']
            section_id = section_info['id']
            if section_name in sections:
                ordered_sections.append({
                    'id': section_id,
                    'name': section_name,
                    'questions': sections[section_name]
                })
        
        # Then add any sections not in metadata (in alphabetical order)
        metadata_section_names = {s['name'] for s in section_order}
        remaining_sections = sorted([s for s in sections.keys() if s not in metadata_section_names])
        for section_name in remaining_sections:
            # Generate ID from name for sections not in metadata
            section_id = section_name.lower().replace(' ', '-').replace(':', '').replace('.', '')
            ordered_sections.append({
                'id': section_id,
                'name': section_name,
                'questions': sections[section_name]
            })

        course_data['ordered_sections'] = ordered_sections

    return courses


def generate_site(courses):
    """Generate the complete static site"""
    site_dir = Path('_site')
    
    # Clean and create site directory
    if site_dir.exists():
        shutil.rmtree(site_dir)
    site_dir.mkdir(exist_ok=True)

    # Create assets directory
    assets_dir = site_dir / 'assets' / 'css'
    assets_dir.mkdir(parents=True, exist_ok=True)

    # Copy CSS files
    css_src = Path('assets') / 'css'
    if css_src.exists():
        for css_file in css_src.glob('*.css'):
            css_dest = assets_dir / css_file.name
            shutil.copy2(css_file, css_dest)
            print(f"Copied {css_file.name} to {css_dest}")
    
    # Copy images
    images_src = Path('images')
    if images_src.exists():
        images_dest = site_dir / 'images'
        shutil.copytree(images_src, images_dest)
        print(f"Copied images to {images_dest}")
    
    # Setup Jinja environment
    env = setup_jinja_environment()
    
    # Sort sections and questions
    courses = sort_sections_and_questions(courses)
    
    # Prepare course list for navigation
    course_list = [
        {'name': course_data['course_name'], 'id': name}
        for name, course_data in courses
    ]

    # Generate course pages using external templates
    course_template = env.get_template('course.html')
    
    for course_name, course_data in courses:
        ordered_sections = course_data['ordered_sections']
        
        html = course_template.render(
            course_name=course_data['course_name'],
            course_id=course_name,
            sections=ordered_sections,
            courses=course_list,
            show_nav=True,
            page_title=course_data['course_name'],
            generation_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

        course_file = site_dir / f'{course_name}.html'
        with open(course_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"Generated {course_file}")
    
    # Generate index page using external template
    index_template = env.get_template('index.html')
    
    # Prepare courses data for index page
    index_courses = []
    for course_name, course_data in courses:
        ordered_sections = course_data['ordered_sections']
        num_sections = len(ordered_sections)
        num_questions = sum(len(section['questions']) for section in ordered_sections)

        index_courses.append({
            'name': course_data['course_name'],
            'id': course_name,
            'num_sections': num_sections,
            'num_questions': num_questions,
        })
    
    index_html = index_template.render(
        courses=index_courses,
        generation_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    index_file = site_dir / 'index.html'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f"Generated {index_file}")
    
    print(f"\nSite generated successfully in {site_dir}")
    return site_dir


def generate_json_data(courses, site_dir):
    """Generate JSON files for each course and a courses index
    
    Args:
        courses: List of tuples (course_name, course_data) with already sorted sections
        site_dir: Path to the site directory
    """
    json_dir = site_dir / 'json'
    json_dir.mkdir(exist_ok=True)
    
    # List to track all course JSON files
    courses_index = []
    
    for course_name, course_data in courses:
        ordered_sections = course_data['ordered_sections']
        
        # Build JSON data for this course
        course_json_data = []
        
        for section in ordered_sections:
            section_name = section['name']
            
            for question in section['questions']:
                # Create question entry with markdown answer
                question_entry = {
                    'id': question['id'],
                    'course': course_name,
                    'section': section_name,
                    'question': question['question'],
                    'answer': question['answer']  # Raw markdown content
                }
                course_json_data.append(question_entry)
        
        # Write course JSON file
        course_json_file = json_dir / f'{course_name}.json'
        with open(course_json_file, 'w', encoding='utf-8') as f:
            json.dump(course_json_data, f, indent=2, ensure_ascii=False)
        
        print(f"Generated {course_json_file}")
        
        # Add to courses index
        courses_index.append({
            'course': course_name,
            'course_name': course_data['course_name'],
            'path': f'/json/{course_name}.json',
            'questions_count': len(course_json_data)
        })
    
    # Write courses index JSON file
    courses_json_file = json_dir / 'courses.json'
    with open(courses_json_file, 'w', encoding='utf-8') as f:
        json.dump(courses_index, f, indent=2, ensure_ascii=False)
    
    print(f"Generated {courses_json_file}")
    print(f"\nJSON data generated successfully in {json_dir}")


def main():
    """Main execution function"""
    print("DataTalks.Club FAQ Static Site Generator")
    print("=" * 50)
    
    # Collect questions from _questions directory
    print("\n1. Collecting questions...")
    courses = collect_questions()
    
    if not courses:
        print("No courses or questions found!")
        return
    
    # Print summary
    total_questions = 0
    for course_name, course_data in courses:
        sections = course_data['sections']
        course_questions = sum(len(questions) for questions in sections.values())
        total_questions += course_questions
        print(f"  - {course_name}: {len(sections)} sections, {course_questions} questions")
    
    print(f"Found {len(courses)} courses with {total_questions} total questions")

    # Generate static site
    print("\n2. Generating static site...")
    site_dir = generate_site(courses)
    
    # Generate JSON data
    print("\n3. Generating JSON data...")
    generate_json_data(courses, site_dir)
    
    print("\nSite generation complete!")
    print(f"Output directory: {site_dir.absolute()}")
    print(f"Open {site_dir.absolute() / 'index.html'} in your browser")


if __name__ == '__main__':
    main()