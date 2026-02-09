"""
Tests for Jinja2 template environment setup and filtering
"""
import pytest
import sys
from pathlib import Path
import tempfile

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from generate_website import setup_jinja_environment


class TestJinjaEnvironment:
    """Test Jinja2 environment setup and custom filters"""
    
    def test_setup_jinja_environment_basic(self):
        """Test basic Jinja environment setup"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            temp_path = Path(temp_dir)
            
            try:
                # Change to temp directory and create layouts
                import os
                os.chdir(temp_path)
                layouts_dir = temp_path / "_layouts"
                layouts_dir.mkdir(exist_ok=True)
                
                # Create a simple template
                template_content = """<html>
<head><title>{{ page_title }}</title></head>
<body>{{ content }}</body>
</html>"""
                (layouts_dir / "base.html").write_text(template_content)
                
                env = setup_jinja_environment()
                
                assert env is not None
                assert hasattr(env, 'get_template')
                assert hasattr(env, 'filters')
                
                # Test that we can load a template
                template = env.get_template('base.html')
                assert template is not None
                
            finally:
                os.chdir(original_cwd)
    
    def test_title_case_filter(self):
        """Test the custom title_case filter"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            temp_path = Path(temp_dir)
            
            try:
                import os
                os.chdir(temp_path)
                layouts_dir = temp_path / "_layouts"
                layouts_dir.mkdir(exist_ok=True)
                
                env = setup_jinja_environment()
                title_case_filter = env.filters['title_case']
                
                # Test various cases
                assert title_case_filter("hello-world") == "Hello World"
                assert title_case_filter("test_function") == "Test Function"
                assert title_case_filter("module-1-homework") == "Module 1 Homework"
                assert title_case_filter("data_engineering_zoomcamp") == "Data Engineering Zoomcamp"
                assert title_case_filter("normal-text") == "Normal Text"
                
            finally:
                os.chdir(original_cwd)
    
    def test_title_case_filter_edge_cases(self):
        """Test title_case filter with edge cases"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            temp_path = Path(temp_dir)
            
            try:
                import os
                os.chdir(temp_path)
                layouts_dir = temp_path / "_layouts"
                layouts_dir.mkdir(exist_ok=True)
                
                env = setup_jinja_environment()
                title_case_filter = env.filters['title_case']
                
                # Edge cases
                assert title_case_filter("") == ""
                assert title_case_filter("single") == "Single"
                assert title_case_filter("UPPERCASE-TEXT") == "Uppercase Text"
                assert title_case_filter("mixed_Case-Text") == "Mixed Case Text"
                assert title_case_filter("text-with-many-hyphens") == "Text With Many Hyphens"
                assert title_case_filter("text_with_many_underscores") == "Text With Many Underscores"
                assert title_case_filter("mixed-_-separators") == "Mixed   Separators"
                
            finally:
                os.chdir(original_cwd)
    
    def test_jinja_environment_autoescape(self):
        """Test that autoescape is enabled in the environment"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            temp_path = Path(temp_dir)
            
            try:
                import os
                os.chdir(temp_path)
                layouts_dir = temp_path / "_layouts"
                layouts_dir.mkdir(exist_ok=True)
                
                # Create a template that will test autoescaping
                template_content = """<div>{{ user_input }}</div>"""
                (layouts_dir / "test.html").write_text(template_content)
                
                env = setup_jinja_environment()
                template = env.get_template('test.html')
                
                # Test with potentially dangerous input
                dangerous_input = '<script>alert("xss")</script>'
                result = template.render(user_input=dangerous_input)
                
                # Should be escaped - check for the actual escaping format
                assert '&lt;script&gt;' in result
                assert '&#34;' in result or '&quot;' in result  # Accept either format
                assert '<script>' not in result
                
            finally:
                os.chdir(original_cwd)
    
    def test_jinja_environment_template_loading(self):
        """Test that templates can be loaded from the layouts directory"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            temp_path = Path(temp_dir)
            
            try:
                import os
                os.chdir(temp_path)
                layouts_dir = temp_path / "_layouts"
                layouts_dir.mkdir(exist_ok=True)
                
                # Create multiple templates
                base_template = """<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>{% block content %}{% endblock %}</body>
</html>"""
                (layouts_dir / "base.html").write_text(base_template)
                
                course_template = """{% extends "base.html" %}
{% block content %}
<h1>{{ course_name }}</h1>
<div>{{ content }}</div>
{% endblock %}"""
                (layouts_dir / "course.html").write_text(course_template)
                
                env = setup_jinja_environment()
                
                # Test loading base template
                base = env.get_template('base.html')
                assert base is not None
                
                # Test loading course template with inheritance
                course = env.get_template('course.html')
                assert course is not None
                
                # Test rendering with inheritance
                result = course.render(
                    title="Test Course",
                    course_name="Machine Learning",
                    content="Course content here"
                )
                
                assert "Test Course" in result
                assert "Machine Learning" in result
                assert "Course content here" in result
                assert "<!DOCTYPE html>" in result
                
            finally:
                os.chdir(original_cwd)
    
    def test_jinja_environment_creates_layouts_dir(self):
        """Test that setup creates _layouts directory if it doesn't exist"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            temp_path = Path(temp_dir)
            
            try:
                import os
                os.chdir(temp_path)
                
                # Ensure _layouts doesn't exist initially
                layouts_dir = temp_path / "_layouts"
                assert not layouts_dir.exists()
                
                env = setup_jinja_environment()
                
                # Should have created the directory
                assert layouts_dir.exists()
                assert layouts_dir.is_dir()
                
            finally:
                os.chdir(original_cwd)
    
    def test_jinja_environment_with_complex_template(self):
        """Test Jinja environment with a complex template using filters"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            temp_path = Path(temp_dir)
            
            try:
                import os
                os.chdir(temp_path)
                layouts_dir = temp_path / "_layouts"
                layouts_dir.mkdir(exist_ok=True)
                
                # Create a template that uses our custom filter
                template_content = """<h1>{{ course_id | title_case }}</h1>
<p>Course sections:</p>
<ul>
{% for section in sections %}
    <li>{{ section.id | title_case }}: {{ section.name }}</li>
{% endfor %}
</ul>"""
                (layouts_dir / "complex.html").write_text(template_content)
                
                env = setup_jinja_environment()
                template = env.get_template('complex.html')
                
                # Test rendering with data
                result = template.render(
                    course_id="machine-learning-zoomcamp",
                    sections=[
                        {"id": "module-1", "name": "Introduction"},
                        {"id": "module-2-homework", "name": "Regression Homework"}
                    ]
                )
                
                assert "Machine Learning Zoomcamp" in result
                assert "Module 1: Introduction" in result
                assert "Module 2 Homework: Regression Homework" in result
                
            finally:
                os.chdir(original_cwd)