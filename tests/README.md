# Test Suite for FAQ Site Generator

This directory contains comprehensive tests for both the static site generator (`generate_website.py`) and the FAQ automation system (`faq_automation/`), organized into focused test files for maintainability and clarity.

## Test Structure

### Unit Tests (`tests/unit/`)
Tests for individual functions and components:

- **`test_frontmatter.py`** - YAML frontmatter parsing
  - Valid/invalid YAML handling
  - Edge cases (empty, malformed, special characters)
  - Multiline values and nested structures

- **`test_url_conversion.py`** - URL detection and conversion
  - HTTP/HTTPS URL detection
  - Code block and inline code preservation  
  - Trailing punctuation handling
  - Complex mixed scenarios

- **`test_markdown.py`** - Markdown processing
  - Basic markdown to HTML conversion
  - Image placeholder replacement
  - Table and task list processing
  - Syntax highlighting integration

- **`test_renderer.py`** - HighlightRenderer class
  - Language alias handling
  - Syntax highlighting functionality
  - Code span and link rendering
  - Error handling for invalid languages

- **`test_course_processing.py`** - Course and metadata processing
  - Course metadata loading
  - Section and question file processing
  - Error recovery and validation

- **`test_jinja_setup.py`** - Jinja2 template environment
  - Template loading and rendering
  - Custom filter functionality
  - Auto-escaping behavior

- **`test_sorting.py`** - Sorting and organization
  - Question sorting by sort_order
  - Section ordering by metadata
  - Handling missing sections

- **`test_faq_automation.py`** - FAQ automation core functions
  - Frontmatter parsing and writing
  - Document ID generation
  - Content filtering and relevance

- **`test_cli_parsing.py`** - CLI issue body parsing
  - Full issue parsing (course + question + answer)
  - Extra section handling (Checklist)
  - Error handling for missing fields

- **`test_faq_actions.py`** - GitHub Actions integration
  - PR body generation for NEW/UPDATE actions
  - Duplicate comment generation
  - Section placement and reasoning

- **`test_github_actions.py`** - GitHub Actions helpers
  - Writing multiline and single-line outputs
  - GitHub Actions environment detection
  - Output path retrieval
  - Local testing mode behavior

### Integration Tests (`tests/integration/`)
End-to-end workflow tests:

- **`test_site_generation.py`** - Complete site generation
  - Full pipeline from questions to HTML
  - Multiple course handling
  - Asset copying and file structure

- **`test_real_world.py`** - Real-world scenarios
  - Large courses with many sections
  - Unicode and special character handling
  - Complex markdown features
  - Error recovery and partial processing

- **`test_faq_automation_workflow.py`** - FAQ automation end-to-end workflows
  - FAQ agent initialization with real course structure
  - Search and retrieval from existing FAQs
  - Complete NEW/UPDATE/DUPLICATE decision workflows
  - File creation and modification with proper formatting
  - PR body and comment generation
  - CLI integration with full issue body parsing
  - Complete multi-step workflows from issue to file

## Running Tests

### Run All Tests
```bash
# Run all tests
make test

# Or run pytest directly
uv run pytest tests/ -v
```

### Run Specific Test Categories
```bash
# Unit tests only
make test-unit
# Or: uv run pytest tests/unit/ -v

# Integration tests only
make test-int
# Or: uv run pytest tests/integration/ -v
```

### Run Specific Test Files
```bash
# Test URL conversion functionality
uv run pytest tests/unit/test_url_conversion.py -v

# Test FAQ automation functionality
uv run pytest tests/unit/test_faq_automation.py -v

# Test CLI parsing functionality
uv run pytest tests/unit/test_cli_parsing.py -v

# Test GitHub Actions helpers
uv run pytest tests/unit/test_github_actions.py -v

# Test site generation
uv run pytest tests/integration/test_site_generation.py -v

# Test FAQ automation workflows
uv run pytest tests/integration/test_faq_automation_workflow.py -v
```

### Run Specific Test Methods
```bash
# Test specific URL conversion functionality
uv run pytest tests/unit/test_url_conversion.py::TestConvertPlainUrlsToLinks::test_preserve_urls_in_code_blocks -v

# Test specific FAQ automation functionality
uv run pytest tests/unit/test_faq_automation.py::TestParseFrontmatter::test_parse_frontmatter -v

# Test full issue body parsing (course + question + answer)
uv run pytest tests/unit/test_cli_parsing.py::TestParseFullIssueBody::test_parse_full_issue_body_simple -v

# Test GitHub Actions output writing
uv run pytest tests/unit/test_github_actions.py::TestWriteGithubOutput::test_write_github_output_multiline -v

# Test FAQ automation end-to-end workflow
uv run pytest tests/integration/test_faq_automation_workflow.py::TestEndToEndWorkflow::test_new_faq_complete_workflow -v
```

## Test Coverage

The test suite provides comprehensive coverage of:

### Core Functionality
- ✅ YAML frontmatter parsing (10 tests)
- ✅ URL detection and conversion (15 tests)
- ✅ Markdown processing (14 tests)
- ✅ Syntax highlighting (15 tests)
- ✅ Course metadata handling (8 tests)
- ✅ Template rendering (7 tests)
- ✅ Sorting and organization (8 tests)
- ✅ FAQ automation core (6 tests)
- ✅ CLI issue parsing (6 tests)
- ✅ GitHub Actions integration (13 tests)

### Integration Scenarios
- ✅ Complete site generation (4 tests)
- ✅ Large-scale processing (3 tests)
- ✅ Unicode and special characters (1 test)
- ✅ Complex markdown features (1 test)
- ✅ Error recovery (1 test)
- ✅ FAQ automation workflows (26 tests)
  - FAQ agent integration (5 tests)
  - File creation and updates (3 tests)
  - PR and comment generation (5 tests)
  - CLI integration (2 tests)
  - Error handling and edge cases (4 tests)
  - Site generator integration (3 tests)
  - End-to-end workflows (3 tests)

### Edge Cases
- ✅ Empty files and directories
- ✅ Invalid YAML frontmatter
- ✅ Missing required fields
- ✅ Binary files in question directories
- ✅ Unicode characters and emojis
- ✅ Complex nested markdown structures
- ✅ Multiple courses and sections
- ✅ Large datasets (50+ questions)

## Key Test Features

### URL Detection Testing
The URL conversion tests ensure that:
- Plain text URLs are converted to clickable links
- URLs in code blocks remain untouched
- URLs in inline code are preserved
- Existing markdown links are not double-converted
- Trailing punctuation is handled correctly

### Error Handling
Tests verify graceful handling of:
- Invalid YAML frontmatter
- Missing required fields
- Non-existent files and directories
- Binary files in question directories
- Malformed markdown content

### Real-World Scenarios
Integration tests simulate:
- Large courses with 10+ sections and 50+ questions
- International content with unicode characters
- Complex markdown with tables, task lists, and code blocks
- Mixed valid/invalid content in the same course

### FAQ Automation Integration Testing
The FAQ automation integration tests verify complete end-to-end workflows:
- **Agent Initialization**: Loading real course structure with FAQs and metadata
- **Search & Retrieval**: Building search index and finding similar FAQs
- **Decision Making**: Processing proposals through mocked LLM to get NEW/UPDATE/DUPLICATE decisions
- **File Operations**: Creating new FAQ files and updating existing ones with correct formatting
- **Output Generation**: Generating PR bodies and duplicate comments
- **CLI Execution**: Running the complete CLI workflow from issue body to file creation
- **Multi-Step Workflows**: Testing the full pipeline from GitHub issue to final FAQ file

These tests use:
- Temporary test course directories with sample FAQs
- Mocked OpenAI API responses for consistent test results
- Real file I/O operations to verify file format compatibility
- Validation that created files work with the site generator

**Key test scenarios:**
- Creating FAQs in empty section directories (edge case)
- Handling non-existent document updates (error handling)
- Agent initialization with empty courses
- Appending FAQs with order=-1 (end of section)
- Integration with `generate_website.py` to verify created FAQs render correctly

## Adding New Tests

When adding new functionality to `generate_website.py`:

1. **Add unit tests** for new functions in appropriate `test_*.py` files
2. **Add integration tests** if the change affects the complete workflow
3. **Test edge cases** and error conditions
4. **Update this README** if new test categories are added

When adding new functionality to the FAQ automation system (`faq_automation/`):

1. **Add unit tests** for new functions in the corresponding test file:
   - `test_cli_parsing.py` for CLI argument and issue body parsing
   - `test_faq_automation.py` for core FAQ processing functions
   - `test_faq_actions.py` for GitHub Actions integration logic
   - `test_github_actions.py` for GitHub Actions output helpers
2. **Add integration tests** for complete workflows in `test_faq_automation_workflow.py`:
   - Test with real course directory structures
   - Mock OpenAI API responses for consistent results
   - Verify file creation and modification
   - Test complete multi-step workflows
3. **Test with real issue bodies** to ensure parsing handles various formats
4. **Mock external dependencies** (e.g., OpenAI API calls) in unit tests
5. **Update this README** if new test categories are added

### Test Naming Convention
- Test files: `test_<functionality>.py`
- Test classes: `Test<ClassName>`
- Test methods: `test_<specific_behavior>`

### Example Test Structure
```python
class TestNewFeature:
    """Test the new feature functionality"""
    
    def test_basic_functionality(self):
        """Test basic feature behavior"""
        pass
        
    def test_edge_cases(self):
        """Test edge cases and error conditions"""
        pass
        
    def test_integration_with_existing_features(self):
        """Test how feature integrates with existing code"""
        pass
```

## Dependencies

The test suite requires:
- `pytest>=7.0.0` (defined in pyproject.toml dev dependencies)
- All main project dependencies for testing the actual functionality

## Configuration

Test configuration is defined in `pyproject.toml`:
- Test discovery paths
- Test file patterns
- Output formatting
- Custom markers for test categorization