#!/usr/bin/env python3
"""
Validate Questions Script
Tests that all markdown files in _questions directory are readable by generate.py
and have valid frontmatter with required fields.
"""

import yaml
from pathlib import Path
import sys

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content - same as generate.py"""
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

def validate_question_file(file_path):
    """Validate a single question file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, markdown_content = parse_frontmatter(content)
        
        # Check required fields
        required_fields = ['id', 'question', 'section', 'course', 'sort_order']
        missing_fields = []
        
        for field in required_fields:
            if not frontmatter.get(field):
                missing_fields.append(field)
        
        if missing_fields:
            return False, f"Missing required fields: {', '.join(missing_fields)}"
        
        # Additional validation
        if not isinstance(frontmatter.get('sort_order'), int):
            return False, "sort_order must be an integer"
        
        if not markdown_content.strip():
            return False, "No content after frontmatter"
        
        return True, "Valid"
        
    except Exception as e:
        return False, f"Error reading file: {e}"

def validate_questions_directory():
    """Validate all question files in _questions directory"""
    questions_dir = Path('_questions')
    
    if not questions_dir.exists():
        print("❌ No _questions directory found")
        return False
    
    total_files = 0
    valid_files = 0
    invalid_files = []
    
    print("Validating question files...")
    print("=" * 50)
    
    for course_dir in questions_dir.iterdir():
        if not course_dir.is_dir():
            continue
        
        course_name = course_dir.name
        print(f"\n📁 Course: {course_name}")
        
        course_files = 0
        course_valid = 0
        
        for question_file in sorted(course_dir.glob('*.md')):
            total_files += 1
            course_files += 1
            
            is_valid, message = validate_question_file(question_file)
            
            if is_valid:
                valid_files += 1
                course_valid += 1
            else:
                invalid_files.append((question_file, message))
                print(f"  ❌ {question_file.name}: {message}")
        
        print(f"  ✅ {course_valid}/{course_files} files valid")
    
    print("\n" + "=" * 50)
    print(f"📊 Summary:")
    print(f"  Total files: {total_files}")
    print(f"  Valid files: {valid_files}")
    print(f"  Invalid files: {len(invalid_files)}")
    
    if invalid_files:
        print(f"\n❌ Found {len(invalid_files)} invalid files:")
        for file_path, message in invalid_files[:10]:  # Show first 10
            print(f"  - {file_path.relative_to(questions_dir)}: {message}")
        if len(invalid_files) > 10:
            print(f"  ... and {len(invalid_files) - 10} more")
    
    success = len(invalid_files) == 0
    if success:
        print("\n✅ All files are valid and compatible with generate.py!")
    else:
        print(f"\n❌ {len(invalid_files)} files need to be fixed")
    
    return success

def main():
    """Main execution function"""
    print("DataTalks.Club FAQ Questions Validator")
    print("=" * 50)
    
    success = validate_questions_directory()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()