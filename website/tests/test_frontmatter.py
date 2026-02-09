"""
Tests for frontmatter parsing functionality
"""
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from generate_website import parse_frontmatter


class TestParseFrontmatter:
    """Test the YAML frontmatter parsing functionality"""
    
    def test_parse_frontmatter_valid_yaml(self):
        """Test parsing valid YAML frontmatter"""
        content = """---
question: "How do I install Python?"
id: "abc123"
sort_order: 1
tags: ["python", "installation"]
---
This is the markdown content.
More content here.
"""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter["question"] == "How do I install Python?"
        assert frontmatter["id"] == "abc123"
        assert frontmatter["sort_order"] == 1
        assert frontmatter["tags"] == ["python", "installation"]
        assert markdown == "This is the markdown content.\nMore content here."
    
    def test_parse_frontmatter_no_frontmatter(self):
        """Test content with no frontmatter"""
        content = "Just regular markdown content here."
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert markdown == content
    
    def test_parse_frontmatter_empty_frontmatter(self):
        """Test content with empty frontmatter"""
        content = """---
---
Some markdown content."""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert markdown == "Some markdown content."
    
    def test_parse_frontmatter_invalid_yaml(self):
        """Test content with invalid YAML frontmatter"""
        content = """---
invalid: yaml: content: here
---
Markdown content."""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert markdown == content
    
    def test_parse_frontmatter_incomplete_frontmatter(self):
        """Test content with incomplete frontmatter delimiter"""
        content = """---
question: "Test question"
Some content without closing delimiter."""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter == {}
        assert markdown == content
    
    def test_parse_frontmatter_multiline_values(self):
        """Test frontmatter with multiline string values"""
        content = """---
question: "How do I do this?"
description: |
  This is a multiline
  description that spans
  multiple lines
tags: ["multi", "line"]
---
Content here."""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter["question"] == "How do I do this?"
        assert "This is a multiline" in frontmatter["description"]
        assert "multiple lines" in frontmatter["description"]
        assert frontmatter["tags"] == ["multi", "line"]
        assert markdown == "Content here."
    
    def test_parse_frontmatter_special_characters(self):
        """Test frontmatter with special characters and quotes"""
        content = '''---
question: "How to use 'single quotes' and \\"double quotes\\"?"
special_chars: "Characters like @#$%^&*()!"
unicode: "Émojis and unicode: 🎉 café naïve"
---
Content with special chars.'''
        frontmatter, markdown = parse_frontmatter(content)
        
        assert 'single quotes' in frontmatter["question"]
        assert 'double quotes' in frontmatter["question"]
        assert frontmatter["special_chars"] == "Characters like @#$%^&*()!"
        assert "🎉" in frontmatter["unicode"]
        assert "café" in frontmatter["unicode"]
        assert markdown == "Content with special chars."
    
    def test_parse_frontmatter_nested_structures(self):
        """Test frontmatter with nested YAML structures"""
        content = """---
question: "Complex structure test"
metadata:
  author: "John Doe"
  date: "2023-01-01"
  tags: ["nested", "structure"]
images:
  - id: "img1"
    path: "/images/test1.png"
    description: "First image"
  - id: "img2"  
    path: "/images/test2.png"
    description: "Second image"
---
Content here."""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter["question"] == "Complex structure test"
        assert frontmatter["metadata"]["author"] == "John Doe"
        assert frontmatter["metadata"]["tags"] == ["nested", "structure"]
        assert len(frontmatter["images"]) == 2
        assert frontmatter["images"][0]["id"] == "img1"
        assert frontmatter["images"][1]["description"] == "Second image"
        assert markdown == "Content here."
    
    def test_parse_frontmatter_only_frontmatter(self):
        """Test content with only frontmatter and no content"""
        content = """---
question: "Only frontmatter"
id: "test123"
---"""
        frontmatter, markdown = parse_frontmatter(content)
        
        assert frontmatter["question"] == "Only frontmatter"
        assert frontmatter["id"] == "test123"
        assert markdown == ""