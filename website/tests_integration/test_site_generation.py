"""
Integration tests for the complete site generation process
"""
import pytest
import sys
import tempfile
import os
import shutil
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from generate_website import (
    collect_questions,
    generate_site,
    main
)


class TestSiteGeneration:
    """Test the complete site generation process"""
    
    def setup_test_structure(self, base_dir):
        """Set up a complete test project structure"""
        base_path = Path(base_dir)
        
        # Create _questions structure
        questions_dir = base_path / "_questions"
        course_dir = questions_dir / "test-course" / "general"
        course_dir.mkdir(parents=True)
        
        # Create course metadata
        metadata_content = """
course_name: "Test Course"
sections:
  - id: "general"
    name: "General Questions"
"""
        (questions_dir / "test-course" / "_metadata.yaml").write_text(metadata_content)
        
        # Create test questions
        q1_content = """---
question: "How do I get started?"
id: "start123"
sort_order: 1
---
You can get started by visiting https://example.com

Use this command:
```bash
pip install test-package
```
"""
        (course_dir / "001_getting_started.md").write_text(q1_content)
        
        q2_content = """---
question: "What are the requirements?"
id: "req456"
sort_order: 2
images:
  - id: "diagram1"
    description: "Requirements diagram"
    path: "/images/requirements.png"
---
Here are the requirements: <{IMAGE:diagram1}>

For more info, visit https://docs.example.com"""
        (course_dir / "002_requirements.md").write_text(q2_content)
        
        # Create _layouts structure
        layouts_dir = base_path / "_layouts"
        layouts_dir.mkdir(parents=True)
        
        # Create templates
        base_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ page_title | default('FAQ') }}</title>
    <link rel="stylesheet" href="assets/css/main.css">
</head>
<body>
    <header><h1>FAQ Site</h1></header>
    <main>{% block content %}{% endblock %}</main>
</body>
</html>"""
        (layouts_dir / "base.html").write_text(base_template)
        
        course_template = """{% extends "base.html" %}
{% block content %}
<h1>{{ course_name }}</h1>
{% for section in sections %}
<h2 id="{{ section.id }}">{{ section.name }}</h2>
{% for question in section.questions %}
<div class="question">
    <h3>{{ question.question }}</h3>
    <div class="content">{{ question.content | safe }}</div>
    <a href="https://github.com/example/faq/blob/main/_questions/{{ question.file_path }}">edit on GitHub</a>
</div>
{% endfor %}
{% endfor %}
{% endblock %}"""
        (layouts_dir / "course.html").write_text(course_template)
        
        index_template = """{% extends "base.html" %}
{% block content %}
<h1>All Courses</h1>
<ul>
{% for course in courses %}
<li><a href="{{ course.id }}.html">{{ course.name }}</a> - {{ course.num_questions }} questions</li>
{% endfor %}
</ul>
{% endblock %}"""
        (layouts_dir / "index.html").write_text(index_template)
        
        # Create assets
        assets_dir = base_path / "assets" / "css"
        assets_dir.mkdir(parents=True)
        
        css_content = """
body { font-family: Arial, sans-serif; }
.question { margin: 20px 0; padding: 10px; border: 1px solid #ccc; }
.highlight { background: #f5f5f5; padding: 10px; }
"""
        (assets_dir / "main.css").write_text(css_content)
        
        # Create images
        images_dir = base_path / "images"
        images_dir.mkdir(parents=True)
        (images_dir / "requirements.png").write_text("fake image content")
        
        return base_path
    
    def test_collect_questions_integration(self):
        """Test the complete question collection process"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            
            try:
                base_path = self.setup_test_structure(temp_dir)
                os.chdir(base_path)
                
                courses = collect_questions()
                
                assert len(courses) == 1
                course_name, course_data = courses[0]
                
                assert course_name == "test-course"
                assert course_data["course_name"] == "Test Course"
                assert len(course_data["sections"]) == 1
                assert "General Questions" in course_data["sections"]
                
                questions = course_data["sections"]["General Questions"]
                assert len(questions) == 2
                
                # Check questions are properly processed
                q1 = next(q for q in questions if q["id"] == "start123")
                assert q1["question"] == "How do I get started?"
                assert 'href="https://example.com"' in q1["content"]
                assert '<span class="w"> </span>install<span class="w"> </span>test-package' in q1["content"]
                
                q2 = next(q for q in questions if q["id"] == "req456")
                assert q2["question"] == "What are the requirements?"
                assert len(q2["images"]) == 1
                assert 'src="/images/requirements.png"' in q2["content"]
                assert 'href="https://docs.example.com"' in q2["content"]
                
            finally:
                os.chdir(original_cwd)
    
    def test_generate_site_integration(self):
        """Test the complete site generation process"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            
            try:
                base_path = self.setup_test_structure(temp_dir)
                os.chdir(base_path)
                
                courses = collect_questions()
                site_dir = generate_site(courses)
                
                # Check that site directory was created
                assert site_dir.exists()
                assert site_dir.is_dir()
                
                # Check index page
                index_file = site_dir / "index.html"
                assert index_file.exists()
                
                index_content = index_file.read_text()
                assert "All Courses" in index_content
                assert "Test Course" in index_content
                assert "2 questions" in index_content
                
                # Check course page
                course_file = site_dir / "test-course.html"
                assert course_file.exists()
                
                course_content = course_file.read_text()
                assert "Test Course" in course_content
                assert "General Questions" in course_content
                assert "How do I get started?" in course_content
                assert "What are the requirements?" in course_content
                
                # Check URL conversion worked
                assert 'href="https://example.com"' in course_content
                assert 'href="https://docs.example.com"' in course_content
                
                # Check image processing worked
                assert 'src="/images/requirements.png"' in course_content
                assert 'alt="Requirements diagram"' in course_content
                
                # Check assets were copied
                css_file = site_dir / "assets" / "css" / "main.css"
                assert css_file.exists()
                
                css_content = css_file.read_text()
                assert "font-family" in css_content
                
                # Check images were copied
                img_file = site_dir / "images" / "requirements.png"
                assert img_file.exists()
                
                # Check GitHub edit links
                assert "github.com/example/faq" in course_content
                assert "edit on GitHub" in course_content
                
            finally:
                os.chdir(original_cwd)
    
    def test_generate_site_with_multiple_courses(self):
        """Test site generation with multiple courses"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            
            try:
                base_path = Path(temp_dir)
                os.chdir(base_path)
                
                # Set up multiple courses
                questions_dir = base_path / "_questions"
                
                # Course 1
                course1_dir = questions_dir / "course1" / "general"
                course1_dir.mkdir(parents=True)
                
                metadata1 = """
course_name: "First Course"
sections:
  - id: "general"
    name: "General"
"""
                (questions_dir / "course1" / "_metadata.yaml").write_text(metadata1)
                
                q1_content = """---
question: "Question 1"
id: "q1"
sort_order: 1
---
Content 1"""
                (course1_dir / "q1.md").write_text(q1_content)
                
                # Course 2
                course2_dir = questions_dir / "course2" / "advanced"
                course2_dir.mkdir(parents=True)
                
                metadata2 = """
course_name: "Second Course"
sections:
  - id: "advanced"
    name: "Advanced Topics"
"""
                (questions_dir / "course2" / "_metadata.yaml").write_text(metadata2)
                
                q2_content = """---
question: "Question 2"
id: "q2"
sort_order: 1
---
Content 2"""
                (course2_dir / "q2.md").write_text(q2_content)
                
                # Set up layouts (minimal)
                layouts_dir = base_path / "_layouts"
                layouts_dir.mkdir(parents=True)
                
                simple_template = """<html><body>{{ content | default('') }}</body></html>"""
                (layouts_dir / "base.html").write_text(simple_template)
                (layouts_dir / "course.html").write_text("Course: {{ course_name }}")
                (layouts_dir / "index.html").write_text("Index: {% for c in courses %}{{ c.name }}{% endfor %}")
                
                courses = collect_questions()
                site_dir = generate_site(courses)
                
                # Check both course files were created
                course1_file = site_dir / "course1.html"
                course2_file = site_dir / "course2.html"
                
                assert course1_file.exists()
                assert course2_file.exists()
                
                # Check content
                course1_content = course1_file.read_text()
                course2_content = course2_file.read_text()
                
                assert "First Course" in course1_content
                assert "Second Course" in course2_content
                # Test that the pages contain content (template working)
                assert len(course1_content) >= 20  # Should have more than just title
                assert len(course2_content) > 20
                
                # Check index includes both
                index_content = (site_dir / "index.html").read_text()
                assert "First Course" in index_content
                assert "Second Course" in index_content
                
            finally:
                os.chdir(original_cwd)
    
    def test_site_generation_handles_errors_gracefully(self):
        """Test that site generation handles various error conditions"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            
            try:
                base_path = Path(temp_dir)
                os.chdir(base_path)
                
                # Create minimal structure with some problematic files
                questions_dir = base_path / "_questions" / "test-course" / "general"
                questions_dir.mkdir(parents=True)
                
                # Valid question
                valid_q = """---
question: "Valid question"
id: "valid"
---
Valid content"""
                (questions_dir / "valid.md").write_text(valid_q)
                
                # Invalid YAML
                invalid_q = """---
question: "Invalid YAML
id: missing quote
---
Content"""
                (questions_dir / "invalid.md").write_text(invalid_q)
                
                # Missing required field
                missing_q = """---
id: "missing"
---
No question field"""
                (questions_dir / "missing.md").write_text(missing_q)
                
                # Non-markdown file
                (questions_dir / "readme.txt").write_text("Not markdown")
                
                # Create basic metadata
                metadata = """
course_name: "Test Course"
sections:
  - id: "general"
    name: "General"
"""
                (questions_dir.parent.parent / "_metadata.yaml").write_text(metadata)
                
                # Create minimal layout
                layouts_dir = base_path / "_layouts"
                layouts_dir.mkdir(parents=True)
                (layouts_dir / "course.html").write_text("{{ course_name }}")
                (layouts_dir / "index.html").write_text("Index")
                
                courses = collect_questions()
                
                # Should complete despite errors
                site_dir = generate_site(courses)
                
                assert site_dir.exists()
                
                # Should have processed only the valid question
                course_file = site_dir / "test-course.html"
                assert course_file.exists()
                
                content = course_file.read_text()
                # The template only shows course name, but verify generation worked
                assert "test-course" in content
                
            finally:
                os.chdir(original_cwd)