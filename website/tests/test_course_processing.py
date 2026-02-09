"""
Tests for course and metadata processing functionality
"""
import pytest
import sys
import tempfile
import os
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from generate_website import (
    load_course_metadata,
    find_section_name,
    process_question_file,
    process_section,
    process_course
)


class TestLoadCourseMetadata:
    """Test course metadata loading functionality"""
    
    def test_load_course_metadata_valid_file(self):
        """Test loading valid metadata file"""
        with tempfile.TemporaryDirectory() as temp_dir:
            course_dir = Path(temp_dir)
            metadata_file = course_dir / "_metadata.yaml"
            
            metadata_content = """
course_name: "Test Course"
sections:
  - id: "general"
    name: "General Questions"
  - id: "module-1"
    name: "Module 1: Introduction"
"""
            metadata_file.write_text(metadata_content)
            
            result = load_course_metadata(course_dir)
            
            assert result["course_name"] == "Test Course"
            assert len(result["sections"]) == 2
            assert result["sections"][0]["id"] == "general"
            assert result["sections"][0]["name"] == "General Questions"
            assert result["sections"][1]["id"] == "module-1"
            assert result["sections"][1]["name"] == "Module 1: Introduction"
    
    def test_load_course_metadata_missing_file(self):
        """Test loading metadata when file doesn't exist"""
        with tempfile.TemporaryDirectory() as temp_dir:
            course_dir = Path(temp_dir)
            
            result = load_course_metadata(course_dir)
            
            assert result["course_name"] == course_dir.name
            assert result["sections"] == []
    
    def test_load_course_metadata_invalid_yaml(self):
        """Test loading metadata with invalid YAML"""
        with tempfile.TemporaryDirectory() as temp_dir:
            course_dir = Path(temp_dir)
            metadata_file = course_dir / "_metadata.yaml"
            
            # Invalid YAML content
            metadata_content = """
course_name: "Test Course"
sections:
  - id: "general"
    name: "General Questions
  - invalid yaml structure here
"""
            metadata_file.write_text(metadata_content)
            
            # Should handle the error gracefully
            with pytest.raises((Exception,)):
                load_course_metadata(course_dir)
    
    def test_load_course_metadata_empty_file(self):
        """Test loading empty metadata file"""
        with tempfile.TemporaryDirectory() as temp_dir:
            course_dir = Path(temp_dir)
            metadata_file = course_dir / "_metadata.yaml"
            metadata_file.write_text("")
            
            result = load_course_metadata(course_dir)
            
            # Should use defaults when file is empty
            assert result["course_name"] == course_dir.name
            assert result["sections"] == []
    
    def test_load_course_metadata_minimal_valid(self):
        """Test loading metadata with minimal valid content"""
        with tempfile.TemporaryDirectory() as temp_dir:
            course_dir = Path(temp_dir)
            metadata_file = course_dir / "_metadata.yaml"
            
            metadata_content = """
course_name: "Minimal Course"
"""
            metadata_file.write_text(metadata_content)
            
            result = load_course_metadata(course_dir)
            
            assert result["course_name"] == "Minimal Course"
            assert result["sections"] == []


class TestFindSectionName:
    """Test the section name finding functionality"""
    
    def test_find_section_name_existing(self):
        """Test finding an existing section name"""
        section_order = [
            {"id": "general", "name": "General Questions"},
            {"id": "module-1", "name": "Module 1: Introduction"},
            {"id": "advanced", "name": "Advanced Topics"}
        ]
        
        result = find_section_name(section_order, "module-1")
        assert result == "Module 1: Introduction"
    
    def test_find_section_name_missing(self):
        """Test finding a non-existing section name"""
        section_order = [
            {"id": "general", "name": "General Questions"},
            {"id": "module-1", "name": "Module 1: Introduction"}
        ]
        
        result = find_section_name(section_order, "module-2")
        assert result == "module-2"
    
    def test_find_section_name_empty_list(self):
        """Test finding section name in empty list"""
        section_order = []
        
        result = find_section_name(section_order, "test")
        assert result == "test"
    
    def test_find_section_name_case_sensitive(self):
        """Test that section name finding is case sensitive"""
        section_order = [
            {"id": "general", "name": "General Questions"},
            {"id": "General", "name": "Different General"}
        ]
        
        result1 = find_section_name(section_order, "general")
        result2 = find_section_name(section_order, "General")
        
        assert result1 == "General Questions"
        assert result2 == "Different General"


class TestProcessQuestionFile:
    """Test question file processing functionality"""
    
    def test_process_question_file_valid(self):
        """Test processing a valid question file"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                questions_dir = Path("_questions") / "test-course" / "general"
                questions_dir.mkdir(parents=True)
                question_file = questions_dir / "test_question.md"
                
                content = """---
question: "How do I install Python?"
id: "test123"
sort_order: 1
---
You can install Python from https://python.org

Use the following command:
```bash
wget https://python.org/downloads/python.tar.gz
```
"""
                question_file.write_text(content)
                
                result = process_question_file("test-course", "General", question_file)
                
                assert result is not None
                assert result["question"] == "How do I install Python?"
                assert result["id"] == "test123"
                assert result["sort_order"] == 1
                assert result["section"] == "General"
                assert result["course"] == "test-course"
                assert 'href="https://python.org"' in result["content"]
                assert "https://python.org/downloads/python.tar.gz" in result["content"]
            finally:
                os.chdir(original_cwd)
    
    def test_process_question_file_missing_question(self):
        """Test processing a file missing the required question field"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                questions_dir = Path("_questions") / "test-course" / "general"
                questions_dir.mkdir(parents=True)
                question_file = questions_dir / "test_question.md"
                
                content = """---
id: "test123"
sort_order: 1
---
Some content without a question field."""
                question_file.write_text(content)
                
                result = process_question_file("test-course", "General", question_file)
                
                assert result is None
            finally:
                os.chdir(original_cwd)
    
    def test_process_question_file_with_images(self):
        """Test processing a file with image placeholders"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                questions_dir = Path("_questions") / "test-course" / "general"
                questions_dir.mkdir(parents=True)
                question_file = questions_dir / "test_question.md"
                
                content = """---
question: "How to use images?"
id: "img123"
sort_order: 1
images:
  - id: "diagram1"
    description: "Architecture diagram"
    path: "/images/arch.png"
---
Here's the architecture: <{IMAGE:diagram1}>

Visit https://example.com for more info."""
                question_file.write_text(content)
                
                result = process_question_file("test-course", "General", question_file)
                
                assert result is not None
                assert result["question"] == "How to use images?"
                assert len(result["images"]) == 1
                assert result["images"][0]["id"] == "diagram1"
                assert 'alt="Architecture diagram"' in result["content"]
                assert 'src="/images/arch.png"' in result["content"]
                assert 'href="https://example.com"' in result["content"]
            finally:
                os.chdir(original_cwd)
    
    def test_process_question_file_complex_frontmatter(self):
        """Test processing file with complex frontmatter"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                questions_dir = Path("_questions") / "test-course" / "general"
                questions_dir.mkdir(parents=True)
                question_file = questions_dir / "test_question.md"
                
                content = """---
question: "Complex question with metadata"
id: "complex123"
sort_order: 5
tags: ["advanced", "complex"]
metadata:
  author: "John Doe"
  difficulty: "hard"
  estimated_time: "30 minutes"
---
This is a complex question with nested metadata."""
                question_file.write_text(content)
                
                result = process_question_file("test-course", "General", question_file)
                
                assert result is not None
                assert result["question"] == "Complex question with metadata"
                assert result["sort_order"] == 5
                # The file path should be properly calculated
                assert "test-course/general/test_question.md" in result["file_path"]
            finally:
                os.chdir(original_cwd)


class TestProcessSection:
    """Test section processing functionality"""
    
    def test_process_section_basic(self):
        """Test basic section processing"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                # Create section directory with questions
                section_dir = Path("_questions") / "test-course" / "general"
                section_dir.mkdir(parents=True)
                
                # Create test question files
                q1_file = section_dir / "001_question1.md"
                q1_content = """---
question: "First question"
id: "q1"
sort_order: 1
---
First question content."""
                q1_file.write_text(q1_content)
                
                q2_file = section_dir / "002_question2.md"
                q2_content = """---
question: "Second question"
id: "q2"
sort_order: 2
---
Second question content."""
                q2_file.write_text(q2_content)
                
                section_order = [
                    {"id": "general", "name": "General Questions"}
                ]
                
                section_data, section_name = process_section(
                    "test-course", section_order, section_dir
                )
                
                assert section_name == "General Questions"
                assert len(section_data) == 2
                assert section_data[0]["question"] == "First question"
                assert section_data[1]["question"] == "Second question"
            finally:
                os.chdir(original_cwd)
    
    def test_process_section_with_invalid_files(self):
        """Test section processing with some invalid files"""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = os.getcwd()
            os.chdir(temp_dir)
            
            try:
                section_dir = Path("_questions") / "test-course" / "general"
                section_dir.mkdir(parents=True)
                
                # Valid question file
                valid_file = section_dir / "001_valid.md"
                valid_content = """---
question: "Valid question"
id: "valid1"
---
Valid content."""
                valid_file.write_text(valid_content)
                
                # Invalid question file (missing question field)
                invalid_file = section_dir / "002_invalid.md"
                invalid_content = """---
id: "invalid1"
---
Invalid content without question."""
                invalid_file.write_text(invalid_content)
                
                # Non-markdown file (should be ignored)
                other_file = section_dir / "readme.txt"
                other_file.write_text("This is not a markdown file")
                
                section_order = [
                    {"id": "general", "name": "General Questions"}
                ]
                
                section_data, section_name = process_section(
                    "test-course", section_order, section_dir
                )
                
                # Should only include the valid question
                assert len(section_data) == 1
                assert section_data[0]["question"] == "Valid question"
            finally:
                os.chdir(original_cwd)