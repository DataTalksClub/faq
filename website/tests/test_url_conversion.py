"""
Tests for URL detection and conversion functionality
"""
import pytest
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from generate_website import convert_plain_urls_to_links


class TestConvertPlainUrlsToLinks:
    """Test the URL detection and conversion functionality"""
    
    def test_convert_single_http_url(self):
        """Test converting a single HTTP URL"""
        text = "Visit http://example.com for more info."
        result = convert_plain_urls_to_links(text)
        expected = "Visit [http://example.com](http://example.com) for more info."
        assert result == expected
    
    def test_convert_single_https_url(self):
        """Test converting a single HTTPS URL"""
        text = "Check out https://github.com/example/repo"
        result = convert_plain_urls_to_links(text)
        expected = "Check out [https://github.com/example/repo](https://github.com/example/repo)"
        assert result == expected
    
    def test_convert_multiple_urls(self):
        """Test converting multiple URLs in one text"""
        text = "Visit https://example.com and http://test.org for info."
        result = convert_plain_urls_to_links(text)
        expected = "Visit [https://example.com](https://example.com) and [http://test.org](http://test.org) for info."
        assert result == expected
    
    def test_preserve_urls_in_code_blocks(self):
        """Test that URLs inside code blocks are not converted"""
        text = """Here's how to download:
```bash
wget https://example.com/file.txt
curl -o data.csv https://raw.githubusercontent.com/user/repo/main/data.csv
```
Visit https://example.com for more info."""
        result = convert_plain_urls_to_links(text)
        
        # URLs in code blocks should remain unchanged
        assert "wget https://example.com/file.txt" in result
        assert "curl -o data.csv https://raw.githubusercontent.com/user/repo/main/data.csv" in result
        # URL outside code block should be converted
        assert "[https://example.com](https://example.com)" in result
    
    def test_preserve_urls_in_inline_code(self):
        """Test that URLs inside inline code are not converted"""
        text = "Use `curl https://api.example.com/data` to fetch data. Visit https://example.com for docs."
        result = convert_plain_urls_to_links(text)
        
        # URL in inline code should remain unchanged
        assert "`curl https://api.example.com/data`" in result
        # URL outside inline code should be converted
        assert "[https://example.com](https://example.com)" in result
    
    def test_preserve_existing_markdown_links(self):
        """Test that existing markdown links are not double-converted"""
        text = "Check [the docs](https://docs.example.com) and visit https://example.com"
        result = convert_plain_urls_to_links(text)
        
        # Existing markdown link should remain unchanged
        assert "[the docs](https://docs.example.com)" in result
        # Plain URL should be converted
        assert "[https://example.com](https://example.com)" in result
    
    def test_handle_urls_with_trailing_punctuation(self):
        """Test that trailing punctuation is handled correctly"""
        text = "Visit https://example.com. Also check https://test.org!"
        result = convert_plain_urls_to_links(text)
        expected = "Visit [https://example.com](https://example.com). Also check [https://test.org](https://test.org)!"
        assert result == expected
    
    def test_handle_complex_code_and_text_mix(self):
        """Test complex scenarios with mixed code blocks, inline code, and plain text"""
        text = """Download a CSV file:

```python
url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv'
df = pd.read_csv(url)
```

You can also use `wget https://example.com/data.csv` command.

For more info visit https://github.com/example/repo."""
        result = convert_plain_urls_to_links(text)
        
        # URL in code block should remain unchanged
        assert "url = 'https://raw.githubusercontent.com/alexeygrigorev/datasets/master/housing.csv'" in result
        # URL in inline code should remain unchanged
        assert "`wget https://example.com/data.csv`" in result
        # Plain URL should be converted
        assert "[https://github.com/example/repo](https://github.com/example/repo)" in result
    
    def test_no_urls_present(self):
        """Test text with no URLs"""
        text = "This is just regular text with no URLs."
        result = convert_plain_urls_to_links(text)
        assert result == text
    
    def test_empty_string(self):
        """Test empty string input"""
        result = convert_plain_urls_to_links("")
        assert result == ""
    
    def test_urls_with_query_parameters(self):
        """Test URLs with query parameters and fragments"""
        text = "Search at https://google.com/search?q=python&lang=en#results for results."
        result = convert_plain_urls_to_links(text)
        expected = "Search at [https://google.com/search?q=python&lang=en#results](https://google.com/search?q=python&lang=en#results) for results."
        assert result == expected
    
    def test_urls_with_ports(self):
        """Test URLs with port numbers"""
        text = "Local server at http://localhost:8080 and https://api.example.com:443/data"
        result = convert_plain_urls_to_links(text)
        expected = "Local server at [http://localhost:8080](http://localhost:8080) and [https://api.example.com:443/data](https://api.example.com:443/data)"
        assert result == expected
    
    def test_urls_in_nested_code_blocks(self):
        """Test URLs in nested code structures"""
        text = """Example with nested structures:
```python
def download_data():
    # This URL should not be converted
    url = "https://api.example.com/data"
    
    # Neither should this one in a comment
    # See: https://docs.example.com/api
    return requests.get(url)
```

But this URL should be converted: https://github.com/example"""
        result = convert_plain_urls_to_links(text)
        
        # URLs in code block should remain unchanged
        assert 'url = "https://api.example.com/data"' in result
        assert '# See: https://docs.example.com/api' in result
        # Plain URL should be converted
        assert "[https://github.com/example](https://github.com/example)" in result
    
    def test_multiple_trailing_punctuation(self):
        """Test URLs with multiple trailing punctuation marks"""
        text = "Check this out: https://example.com!!! And this: https://test.org..."
        result = convert_plain_urls_to_links(text)
        expected = "Check this out: [https://example.com](https://example.com)!!! And this: [https://test.org](https://test.org)..."
        assert result == expected
    
    def test_urls_in_mixed_quote_styles(self):
        """Test URLs within different quote styles in code"""
        text = '''Code examples:
```python
url1 = "https://example.com/api"
url2 = 'https://test.org/data'  
url3 = f"https://dynamic.com/{variable}"
```
Plain URL: https://github.com/user/repo'''
        result = convert_plain_urls_to_links(text)
        
        # URLs in code should remain unchanged
        assert 'url1 = "https://example.com/api"' in result
        assert "url2 = 'https://test.org/data'" in result
        assert 'url3 = f"https://dynamic.com/{variable}"' in result
        # Plain URL should be converted
        assert "[https://github.com/user/repo](https://github.com/user/repo)" in result