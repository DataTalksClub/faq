"""
Unit tests for CLI issue body parsing
"""

import pytest
from faq_automation.cli import parse_full_issue_body


class TestParseFullIssueBody:
    """Test the parse_full_issue_body function"""

    def test_parse_full_issue_body_simple(self):
        """Test parsing simple issue body with all fields"""
        issue_body = """### Course
machine-learning-zoomcamp

### Question
How do I install dependencies?

### Answer
Run: pip install -r requirements.txt
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "machine-learning-zoomcamp"
        assert question == "How do I install dependencies?"
        assert "pip install -r requirements.txt" in answer

    def test_parse_full_issue_body_multiline(self):
        """Test parsing issue body with multiline content"""
        issue_body = """### Course
data-engineering-zoomcamp

### Question
How do I set up
the development environment
for this project?

### Answer
First, clone the repository:
```bash
git clone https://github.com/...
```

Then install dependencies:
```bash
pip install -r requirements.txt
```
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "data-engineering-zoomcamp"
        assert "set up" in question
        assert "development environment" in question
        assert "git clone" in answer
        assert "pip install" in answer

    def test_parse_full_issue_body_with_checklist(self):
        """Test parsing with checklist section that should be ignored"""
        issue_body = """### Course
machine-learning-zoomcamp

### Question
What is the deadline?

### Answer
The deadline is March 1st.

### Checklist
- [x] Searched existing FAQs
- [x] Accurate information
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == "machine-learning-zoomcamp"
        assert question == "What is the deadline?"
        assert answer == "The deadline is March 1st."
        assert "Checklist" not in answer

    def test_parse_full_issue_body_missing_course(self):
        """Test parsing with missing course raises error"""
        issue_body = """### Question
Some question

### Answer
Some answer
"""

        with pytest.raises(ValueError, match="Could not parse"):
            parse_full_issue_body(issue_body)

    def test_parse_full_issue_body_missing_question(self):
        """Test parsing with missing question raises error"""
        issue_body = """### Course
machine-learning-zoomcamp

### Answer
Some answer
"""

        with pytest.raises(ValueError, match="Could not parse"):
            parse_full_issue_body(issue_body)

    def test_parse_full_issue_body_missing_answer(self):
        """Test parsing with missing answer raises error"""
        issue_body = """### Course
machine-learning-zoomcamp

### Question
Some question
"""

        with pytest.raises(ValueError, match="Could not parse"):
            parse_full_issue_body(issue_body)
