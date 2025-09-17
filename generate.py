#!/usr/bin/env python3
"""
Static Site Generator for FAQ Content
Processes markdown files from _questions/ and generates static HTML site in _site/
"""

import shutil
from pathlib import Path
import yaml
from collections import defaultdict
from jinja2 import Environment, FileSystemLoader
import markdown
from datetime import datetime


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


def process_markdown(content):
    """Convert markdown to HTML while preserving template syntax as literal text"""
    # Configure markdown with basic extensions
    md = markdown.Markdown(extensions=['nl2br', 'tables'])
    return md.convert(content)


def collect_questions():
    """Collect all questions from _questions directory"""
    questions_dir = Path('_questions')
    if not questions_dir.exists():
        print("No questions directory found")
        return {}
    
    courses = defaultdict(lambda: defaultdict(list))
    
    for course_dir in questions_dir.iterdir():
        if not course_dir.is_dir():
            continue
            
        course_name = course_dir.name
        print(f"Processing course: {course_name}")
        
        # Process all markdown files in course directory
        for question_file in sorted(course_dir.glob('*.md')):
            try:
                with open(question_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                frontmatter, markdown_content = parse_frontmatter(content)
                
                if not frontmatter.get('question'):
                    print(f"Skipping {question_file}: missing question field in frontmatter")
                    continue
                
                # Process markdown to HTML
                html_content = process_markdown(markdown_content)
                
                question_data = {
                    'question': frontmatter['question'],
                    'section': frontmatter.get('section', 'Unknown Section'),
                    'course': course_name,
                    'content': html_content,
                    'file': question_file.name
                }
                
                section_name = frontmatter.get('section', 'Unknown Section')
                courses[course_name][section_name].append(question_data)
                
            except Exception as e:
                print(f"Error processing {question_file}: {e}")
    
    return courses


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


def create_default_templates():
    """Check if templates exist, create minimal ones if missing"""
    layouts_dir = Path('_layouts')
    if not layouts_dir.exists():
        layouts_dir.mkdir(exist_ok=True)
        print(f"Created {layouts_dir} directory")
    
    required_templates = ['base.html', 'index.html', 'course.html']
    missing_templates = [tmpl for tmpl in required_templates if not (layouts_dir / tmpl).exists()]
    
    if missing_templates:
        print(f"Warning: Missing templates: {missing_templates}")
        print("Templates should be created in _layouts/ directory")
    else:
        print("All required templates found in _layouts/")
    
    return True


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
    
    # Copy images
    images_src = Path('images')
    if images_src.exists():
        images_dest = site_dir / 'images'
        shutil.copytree(images_src, images_dest)
        print(f"Copied images to {images_dest}")
    
    # Setup Jinja environment
    create_default_templates()
    env = setup_jinja_environment()
    
    # Prepare course list for navigation
    course_list = [{'name': name} for name in courses.keys()]
    
    # Generate course pages using external templates
    course_template = env.get_template('course.html')
    
    for course_name, sections in courses.items():
        html = course_template.render(
            course_name=course_name,
            sections=sections,
            courses=course_list,
            show_nav=True,
            page_title=course_name.replace('-', ' ').title(),
            generation_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        
        course_file = site_dir / f'{course_name}.html'
        with open(course_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"Generated {course_file}")
    
    # Generate index page using external template
    index_template = env.get_template('index.html')
    
    index_html = index_template.render(
        courses=courses,
        generation_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    )
    
    index_file = site_dir / 'index.html'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f"Generated {index_file}")
    
    print(f"\nSite generated successfully in {site_dir}")
    return site_dir


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
    total_questions = sum(len(questions) for sections in courses.values() for questions in sections.values())
    print(f"Found {len(courses)} courses with {total_questions} total questions")
    
    for course_name, sections in courses.items():
        course_questions = sum(len(questions) for questions in sections.values())
        print(f"  - {course_name}: {len(sections)} sections, {course_questions} questions")
    
    # Generate static site
    print("\n2. Generating static site...")
    site_dir = generate_site(courses)
    
    print("\n✅ Site generation complete!")
    print(f"📁 Output directory: {site_dir.absolute()}")
    print(f"🌐 Open {site_dir.absolute() / 'index.html'} in your browser")


if __name__ == '__main__':
    main()