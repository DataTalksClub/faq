"""
Tests for markdown processing functionality
"""
import pytest
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from generate_website import process_markdown


class TestProcessMarkdown:
    """Test markdown processing functionality"""
    
    def test_process_markdown_basic(self):
        """Test basic markdown processing without images"""
        content = "# Title\n\nThis is **bold** text with https://example.com link."
        result = process_markdown(content)
        
        assert "<h1>Title</h1>" in result
        assert "<strong>bold</strong>" in result
        assert 'href="https://example.com"' in result
        assert 'target="_blank"' in result
    
    def test_process_markdown_with_image_placeholders(self):
        """Test markdown processing with image placeholders"""
        content = "Here's an image: <{IMAGE:img1}>\n\nAnd some text."
        images = [
            {"id": "img1", "description": "Test image", "path": "/images/test.png"}
        ]
        result = process_markdown(content, images)
        
        # The markdown processor converts the image to HTML
        assert 'alt="Test image"' in result
        assert 'src="/images/test.png"' in result
    
    def test_process_markdown_with_code_and_urls(self):
        """Test that markdown processing preserves URLs in code blocks"""
        content = """# Instructions

```bash
wget https://example.com/file.txt
```

Visit https://docs.example.com for more info."""
        result = process_markdown(content)
        
        # URL in code should remain as plain text in HTML (may have syntax highlighting)
        assert "https://example.com/file.txt" in result
        # URL in plain text should be converted to link
        assert 'href="https://docs.example.com"' in result
    
    def test_process_markdown_with_multiple_images(self):
        """Test processing multiple image placeholders"""
        content = """# Gallery

First image: <{IMAGE:img1}>

Second image: <{IMAGE:img2}>

Some text here."""
        images = [
            {"id": "img1", "description": "First image", "path": "/images/first.png"},
            {"id": "img2", "description": "Second image", "path": "/images/second.jpg"}
        ]
        result = process_markdown(content, images)
        
        assert 'alt="First image"' in result
        assert 'src="/images/first.png"' in result
        assert 'alt="Second image"' in result  
        assert 'src="/images/second.jpg"' in result
    
    def test_process_markdown_with_tables(self):
        """Test markdown table processing"""
        content = """# Table Example

| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | https://example.com |
| Row 2    | More     | Data     |

Visit https://github.com for more info."""
        result = process_markdown(content)
        
        assert "<table>" in result
        assert "<thead>" in result
        assert "<tbody>" in result
        assert "<th>Column 1</th>" in result
        assert "<td>Row 1</td>" in result
        # URL in table should be converted
        assert 'href="https://example.com"' in result
        # URL outside table should also be converted
        assert 'href="https://github.com"' in result
    
    def test_process_markdown_with_task_lists(self):
        """Test markdown task list processing"""
        content = """# TODO List

- [x] Completed task with https://example.com
- [ ] Pending task
- [x] Another completed task

Check https://github.com for updates."""
        result = process_markdown(content)
        
        assert 'type="checkbox"' in result
        assert 'checked' in result  # Accept any form of checked attribute  
        # URL in task list should be converted
        assert 'href="https://example.com"' in result
        # URL outside task list should also be converted  
        assert 'href="https://github.com"' in result
    
    def test_process_markdown_with_code_syntax_highlighting(self):
        """Test that code blocks get proper syntax highlighting"""
        content = """# Code Example

```python
def hello():
    print("Hello World")
    url = "https://example.com"
    return url
```

Visit https://python.org for docs."""
        result = process_markdown(content)
        
        assert 'class="highlight"' in result
        assert "<span" in result  # Syntax highlighting spans
        # URL in code should not be converted to link - it gets syntax highlighted
        assert '<span class="s2">&quot;https://example.com&quot;</span>' in result
        assert 'href="https://example.com"' not in result
        # URL outside code should be converted
        assert 'href="https://python.org"' in result
    
    def test_process_markdown_with_inline_code(self):
        """Test inline code processing"""
        content = "Use `pip install requests` to install. Visit https://pypi.org for packages."
        result = process_markdown(content)
        
        assert '<code class="inline-code">pip install requests</code>' in result
        assert 'href="https://pypi.org"' in result
    
    def test_process_markdown_empty_content(self):
        """Test processing empty content"""
        result = process_markdown("")
        assert result == ""
    
    def test_process_markdown_only_whitespace(self):
        """Test processing content with only whitespace"""
        content = "   \n\n   \t  \n"
        result = process_markdown(content)
        # Should return minimal HTML or empty string
        assert len(result.strip()) == 0 or result.strip() in ["", "<p></p>"]
    
    def test_process_markdown_with_html_entities(self):
        """Test markdown with HTML entities and special characters"""
        content = """# Special Characters

Text with &amp; entities and <script> tags.
Also visit https://example.com/path?param=value&other=test for data."""
        result = process_markdown(content)
        
        # HTML entities should be properly handled
        assert "&amp;" in result
        # Script tags should be escaped
        assert "&lt;script&gt;" in result
        # URL should still be converted (& gets escaped as &amp; in HTML)
        assert 'href="https://example.com/path?param=value&amp;other=test"' in result
    
    def test_process_markdown_with_missing_image(self):
        """Test handling of image placeholders without corresponding image data"""
        content = "Image here: <{IMAGE:missing}>\n\nText continues."
        images = [
            {"id": "other", "description": "Other image", "path": "/images/other.png"}
        ]
        result = process_markdown(content)
        
        # Missing image placeholder should remain unchanged (HTML escaped)
        assert "&lt;{IMAGE:missing}&gt;" in result
    
    def test_process_markdown_with_nested_formatting(self):
        """Test complex nested markdown formatting"""
        content = """# Main Title

## Subtitle with **bold** and *italic*

- List item with `code` and [link](https://example.com)
- Another item with https://github.com

> Blockquote with **bold text** and https://quote.com

Final paragraph."""
        result = process_markdown(content)
        
        assert "<h1>Main Title</h1>" in result
        assert "<h2>Subtitle" in result
        assert "<strong>bold</strong>" in result
        assert "<em>italic</em>" in result
        assert "<blockquote>" in result
        assert '<code class="inline-code">code</code>' in result
        # URLs should be converted appropriately
        assert 'href="https://github.com"' in result
        assert 'href="https://quote.com"' in result
        # Existing markdown link should be preserved
        assert 'href="https://example.com"' in result