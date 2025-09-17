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
    """Parse YAML frontmatter from markdown content with improved error handling"""
    if not content.startswith('---'):
        return {}, content, None
    
    try:
        # Split frontmatter and content
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}, content, "Invalid frontmatter format: missing closing ---"
        
        frontmatter = yaml.safe_load(parts[1])
        markdown_content = parts[2].strip()
        
        return frontmatter or {}, markdown_content, None
    except yaml.YAMLError as e:
        # Try to fix common YAML issues by quoting unquoted values
        try:
            frontmatter_text = parts[1].strip()
            lines = frontmatter_text.split('\n')
            fixed_lines = []
            
            for line in lines:
                if ':' in line and not line.strip().startswith('#'):
                    key, value = line.split(':', 1)
                    value = value.strip()
                    
                    # If value is not already quoted and contains special characters, quote it
                    if value and not (value.startswith('"') and value.endswith('"')) and not (value.startswith("'") and value.endswith("'")):
                        # Quote values that contain special characters
                        if any(char in value for char in [':', '[', ']', '{', '}', '|', '>', '&', '*', '!', '%', '@', '`', '\\', '/', '?', '<', '=', '+', '-', '^', '~']):
                            value = f'"{value.replace('"', '\\"')}"'
                    
                    fixed_lines.append(f"{key}: {value}")
                else:
                    fixed_lines.append(line)
            
            fixed_frontmatter_text = '\n'.join(fixed_lines)
            frontmatter = yaml.safe_load(fixed_frontmatter_text)
            markdown_content = parts[2].strip()
            
            return frontmatter or {}, markdown_content, None
            
        except Exception:
            return {}, content, f"YAML parsing error: {str(e)}"


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
    skipped_files = []
    processing_stats = {
        'total_files': 0,
        'processed_files': 0,
        'skipped_yaml_errors': 0,
        'skipped_missing_question': 0,
        'skipped_exceptions': 0
    }
    
    for course_dir in questions_dir.iterdir():
        if not course_dir.is_dir():
            continue
            
        course_name = course_dir.name
        print(f"Processing course: {course_name}")
        
        # Process all markdown files in course directory
        for question_file in sorted(course_dir.glob('*.md')):
            processing_stats['total_files'] += 1
            
            try:
                with open(question_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                frontmatter, markdown_content, error = parse_frontmatter(content)
                
                # Handle YAML parsing errors
                if error:
                    processing_stats['skipped_yaml_errors'] += 1
                    skipped_files.append({
                        'file': question_file,
                        'reason': 'YAML parsing error',
                        'details': error
                    })
                    print(f"⚠️  Skipping {question_file.name}: {error}")
                    continue
                
                # Handle missing question field - include with placeholder
                if not frontmatter.get('question'):
                    processing_stats['skipped_missing_question'] += 1
                    skipped_files.append({
                        'file': question_file,
                        'reason': 'Missing question field',
                        'details': 'No question field found in frontmatter - including with placeholder'
                    })
                    print(f"⚠️  Including {question_file.name} with placeholder: missing question field")
                    
                    # Create placeholder question
                    placeholder_question = f"Question from {question_file.name}"
                    
                    # Process markdown to HTML
                    html_content = process_markdown(markdown_content)
                    
                    question_data = {
                        'question': placeholder_question,
                        'section': frontmatter.get('section', 'Unknown Section'),
                        'course': course_name,
                        'content': html_content + '<p><em>Note: This question was missing a title and has been given a placeholder.</em></p>',
                        'file': question_file.name,
                        'is_placeholder': True
                    }
                    
                    section_name = frontmatter.get('section', 'Unknown Section')
                    courses[course_name][section_name].append(question_data)
                    processing_stats['processed_files'] += 1
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
                processing_stats['processed_files'] += 1
                
            except Exception as e:
                processing_stats['skipped_exceptions'] += 1
                skipped_files.append({
                    'file': question_file,
                    'reason': 'Processing exception',
                    'details': str(e)
                })
                print(f"❌ Error processing {question_file.name}: {e}")
    
    # Print summary of processing
    print(f"\n📊 Processing Summary:")
    print(f"   Total files found: {processing_stats['total_files']}")
    print(f"   Successfully processed: {processing_stats['processed_files']}")
    print(f"   Skipped due to YAML errors: {processing_stats['skipped_yaml_errors']}")
    print(f"   Skipped due to missing question field: {processing_stats['skipped_missing_question']}")
    print(f"   Skipped due to other errors: {processing_stats['skipped_exceptions']}")
    
    # Store skipped files information for later reporting
    if hasattr(collect_questions, 'skipped_files'):
        collect_questions.skipped_files = skipped_files
    else:
        setattr(collect_questions, 'skipped_files', skipped_files)
    
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


def print_skipped_files_summary():
    """Print detailed summary of skipped files"""
    if not hasattr(collect_questions, 'skipped_files') or not collect_questions.skipped_files:
        return
    
    skipped_files = collect_questions.skipped_files
    print(f"\n📋 Detailed Report of Skipped Files ({len(skipped_files)} total):")
    print("=" * 60)
    
    # Group by reason
    by_reason = defaultdict(list)
    for item in skipped_files:
        by_reason[item['reason']].append(item)
    
    for reason, files in by_reason.items():
        print(f"\n{reason} ({len(files)} files):")
        for item in files[:10]:  # Show first 10 files for each reason
            print(f"  • {item['file'].name}")
            if len(item['details']) < 100:
                print(f"    {item['details']}")
            else:
                print(f"    {item['details'][:100]}...")
        
        if len(files) > 10:
            print(f"  ... and {len(files) - 10} more files")
    
    print("\n💡 Recommendations:")
    if by_reason.get('YAML parsing error'):
        print("  • For YAML parsing errors: Check for unquoted special characters in frontmatter values")
        print("  • Consider quoting values that contain colons, brackets, or other special characters")
    if by_reason.get('Missing question field'):
        print("  • For missing question fields: Add 'question: <your question>' to the frontmatter")


def main():
    """Main execution function"""
    print("DataTalks.Club FAQ Static Site Generator")
    print("=" * 50)
    
    # Collect questions from _questions directory
    print("\n1. Collecting questions...")
    courses = collect_questions()
    
    if not courses:
        print("No courses or questions found!")
        print_skipped_files_summary()
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
    
    # Print summary of skipped files
    print_skipped_files_summary()


if __name__ == '__main__':
    main()