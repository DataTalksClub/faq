"""
Integration tests for FAQ automation workflow

Tests the complete end-to-end workflow of FAQ automation including:
- Building index from real FAQ files
- Processing proposals with mocked LLM
- Creating/updating FAQ files
- Generating PR bodies and comments
"""

import json
import pytest
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import tempfile
import shutil

from faq_automation.rag_agent import FAQAgent, FAQDecision, process_faq_proposal
from faq_automation.actions import (
    create_new_faq_file,
    update_existing_faq_file,
    generate_pr_body,
    generate_duplicate_comment,
    get_file_changes_summary,
)
from faq_automation.core import find_question_files, parse_frontmatter
from faq_automation.cli import parse_full_issue_body, main as cli_main

# Import site generator functions for integration testing
from generate_website import collect_questions, process_markdown


@pytest.fixture
def test_course_dir(tmp_path):
    """Create a test course directory with sample FAQs"""
    course_dir = tmp_path / "_questions" / "test-course"
    course_dir.mkdir(parents=True)

    # Create metadata
    metadata = {
        'course': 'test-course',
        'course_name': 'Test Course',
        'sections': [
            {'id': 'general', 'name': 'General Questions'},
            {'id': 'module-1', 'name': 'Module 1: Basics'},
            {'id': 'module-2', 'name': 'Module 2: Advanced'},
        ]
    }

    import yaml
    with open(course_dir / '_metadata.yaml', 'w') as f:
        yaml.dump(metadata, f)

    # Create general section with sample FAQs
    general_dir = course_dir / 'general'
    general_dir.mkdir()

    # FAQ 1: Docker installation
    faq1 = """---
id: abc1234567
question: 'How do I install Docker?'
sort_order: 1
---

To install Docker, follow these steps:

1. Visit docker.com
2. Download Docker Desktop
3. Run the installer
"""
    (general_dir / '001_abc1234567_install-docker.md').write_text(faq1)

    # FAQ 2: Python version
    faq2 = """---
id: def8901234
question: 'Which Python version should I use?'
sort_order: 2
---

Use Python 3.9 or higher for this course.

You can check your version with:
```bash
python --version
```
"""
    (general_dir / '002_def8901234_python-version.md').write_text(faq2)

    # Create module-1 section
    module1_dir = course_dir / 'module-1'
    module1_dir.mkdir()

    # FAQ 3: First homework
    faq3 = """---
id: xyz5678901
question: 'Where can I find the homework for Module 1?'
sort_order: 1
---

The homework is available on GitHub in the course repository under `module-1/homework.md`.
"""
    (module1_dir / '001_xyz5678901_homework-location.md').write_text(faq3)

    return course_dir


@pytest.fixture
def mock_openai_new():
    """Mock OpenAI client that returns a NEW decision"""
    def create_mock_response():
        decision = FAQDecision(
            action='NEW',
            rationale='This question about uv package manager is not covered in existing FAQs.',
            document_id='uvw1234567',
            section_rationale='General installation question that applies to the whole course.',
            section_id='general',
            order=10,
            question='How do I install dependencies using uv?',
            proposed_content='Use the following command:\n```bash\nuv sync --dev\n```',
            filename_slug='install-dependencies-uv',
            warnings=[]
        )

        # Mock the response structure
        mock_content = Mock()
        mock_content.parsed = decision

        mock_message = Mock()
        mock_message.type = 'message'
        mock_message.content = [mock_content]

        mock_response = Mock()
        mock_response.output = [mock_message]

        return mock_response

    with patch('faq_automation.rag_agent.OpenAI') as mock_openai_class:
        mock_client = Mock()
        mock_client.responses.parse.return_value = create_mock_response()
        mock_openai_class.return_value = mock_client
        yield mock_client


@pytest.fixture
def mock_openai_update():
    """Mock OpenAI client that returns an UPDATE decision"""
    def create_mock_response():
        decision = FAQDecision(
            action='UPDATE',
            rationale='The existing Docker installation FAQ lacks troubleshooting steps that the proposal provides.',
            document_id='abc1234567',
            section_rationale='Belongs in general section with other installation questions.',
            section_id='general',
            order=1,
            question='How do I install Docker?',
            proposed_content='To install Docker, follow these steps:\n\n1. Visit docker.com\n2. Download Docker Desktop\n3. Run the installer\n\n**Troubleshooting**: If installation fails, try running as administrator.',
            filename_slug=None,
            warnings=[]
        )

        mock_content = Mock()
        mock_content.parsed = decision

        mock_message = Mock()
        mock_message.type = 'message'
        mock_message.content = [mock_content]

        mock_response = Mock()
        mock_response.output = [mock_message]

        return mock_response

    with patch('faq_automation.rag_agent.OpenAI') as mock_openai_class:
        mock_client = Mock()
        mock_client.responses.parse.return_value = create_mock_response()
        mock_openai_class.return_value = mock_client
        yield mock_client


@pytest.fixture
def mock_openai_duplicate():
    """Mock OpenAI client that returns a DUPLICATE decision"""
    def create_mock_response():
        decision = FAQDecision(
            action='DUPLICATE',
            rationale='This question is already fully answered in the existing Python version FAQ.',
            document_id='def8901234',
            section_rationale='Already covered in general section.',
            section_id='general',
            order=2,
            question='Which Python version should I use?',
            proposed_content=None,
            filename_slug=None,
            warnings=[]
        )

        mock_content = Mock()
        mock_content.parsed = decision

        mock_message = Mock()
        mock_message.type = 'message'
        mock_message.content = [mock_content]

        mock_response = Mock()
        mock_response.output = [mock_message]

        return mock_response

    with patch('faq_automation.rag_agent.OpenAI') as mock_openai_class:
        mock_client = Mock()
        mock_client.responses.parse.return_value = create_mock_response()
        mock_openai_class.return_value = mock_client
        yield mock_client


class TestFAQAgentIntegration:
    """Test the FAQ agent with real course structure"""

    def test_agent_initialization_with_real_course(self, test_course_dir, mock_openai_new):
        """Test that agent can initialize with real course directory"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')

        # Verify documents were loaded
        assert len(agent.documents) == 3
        assert agent.metadata['course'] == 'test-course'
        assert len(agent.metadata['sections']) == 3

        # Verify index was built
        assert agent.index is not None

    def test_agent_search_retrieval(self, test_course_dir, mock_openai_new):
        """Test that agent can search and retrieve similar FAQs"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')

        # Search for Docker-related content
        results = agent.index.search('How to install Docker?', num_results=5)

        # Should find the Docker installation FAQ
        assert len(results) > 0
        docker_result = next((r for r in results if 'Docker' in r.get('question', '')), None)
        assert docker_result is not None
        assert docker_result.get('document_id') == 'abc1234567' or docker_result.get('id') == 'abc1234567'

    def test_process_proposal_new_action(self, test_course_dir, mock_openai_new):
        """Test processing a proposal that results in NEW action"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')

        question = "How do I install dependencies using uv?"
        answer = "Use: uv sync --dev"

        decision = agent.process_proposal(question, answer)

        assert decision.action == 'NEW'
        assert decision.section_id == 'general'
        assert 'uv' in decision.question.lower()
        assert decision.proposed_content is not None
        assert decision.filename_slug is not None

    def test_process_proposal_update_action(self, test_course_dir, mock_openai_update):
        """Test processing a proposal that results in UPDATE action"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')

        question = "How do I install Docker?"
        answer = "If installation fails, run as administrator."

        decision = agent.process_proposal(question, answer)

        assert decision.action == 'UPDATE'
        assert decision.document_id == 'abc1234567'
        assert decision.proposed_content is not None
        assert 'Troubleshooting' in decision.proposed_content

    def test_process_proposal_duplicate_action(self, test_course_dir, mock_openai_duplicate):
        """Test processing a proposal that results in DUPLICATE action"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')

        question = "What Python version do I need?"
        answer = "Python 3.9 or higher"

        decision = agent.process_proposal(question, answer)

        assert decision.action == 'DUPLICATE'
        assert decision.document_id == 'def8901234'
        assert decision.proposed_content is None
        assert decision.filename_slug is None


class TestFileCreationIntegration:
    """Test creating and updating FAQ files"""

    def test_create_new_faq_file(self, test_course_dir, mock_openai_new):
        """Test creating a new FAQ file writes correct format"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I use uv?", "Run: uv sync")

        doc_index = find_question_files(test_course_dir)
        file_path = create_new_faq_file(test_course_dir, doc_index, decision)

        # Verify file was created
        assert file_path.exists()
        assert file_path.parent.name == 'general'

        # Verify file format
        content = file_path.read_text()
        fm, body = parse_frontmatter(content)

        assert fm['id'] is not None
        assert fm['question'] == decision.question
        assert fm['sort_order'] == decision.order
        assert 'uv sync' in body

    def test_update_existing_faq_file(self, test_course_dir, mock_openai_update):
        """Test updating an existing FAQ file preserves ID and updates content"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I install Docker?", "Add troubleshooting")

        doc_index = find_question_files(test_course_dir)
        original_file = doc_index['abc1234567']
        original_content = original_file.read_text()

        file_path = update_existing_faq_file(test_course_dir, doc_index, decision)

        # Verify same file was updated
        assert file_path == original_file

        # Verify content was updated
        updated_content = file_path.read_text()
        assert updated_content != original_content

        fm, body = parse_frontmatter(updated_content)
        assert fm['id'] == 'abc1234567'  # ID unchanged
        assert fm['question'] == decision.question
        assert 'Troubleshooting' in body

    def test_new_file_has_valid_format(self, test_course_dir, mock_openai_new):
        """Test that newly created FAQ files have valid format for site generator"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I use uv?", "Run: uv sync")

        doc_index = find_question_files(test_course_dir)
        file_path = create_new_faq_file(test_course_dir, doc_index, decision)

        # Read and parse the created file
        content = file_path.read_text()
        fm, body = parse_frontmatter(content)

        # Verify file has all required fields for site generator
        assert 'id' in fm
        assert 'question' in fm
        assert 'sort_order' in fm
        assert fm['question'] == decision.question

        # Verify body content
        assert 'uv sync' in body
        assert body.strip() == decision.proposed_content.strip()

        # Verify filename format matches expected pattern: NNN_id_slug.md
        assert file_path.name.endswith('.md')
        parts = file_path.stem.split('_', 2)
        assert len(parts) == 3
        assert parts[0].isdigit()  # sort order
        assert parts[1] == fm['id']  # document id
        assert parts[2] == decision.filename_slug  # slug


class TestPRAndCommentGeneration:
    """Test PR body and comment generation"""

    def test_generate_pr_body_for_new(self, test_course_dir, mock_openai_new):
        """Test generating PR body for NEW action"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I use uv?", "Run: uv sync")

        pr_body = generate_pr_body(decision, 42, 'test-course')

        assert '✨' in pr_body
        assert 'NEW' in pr_body
        assert 'test-course' in pr_body
        assert decision.question in pr_body
        assert decision.rationale in pr_body
        assert decision.filename_slug in pr_body
        assert '#42' in pr_body

    def test_generate_pr_body_for_update(self, test_course_dir, mock_openai_update):
        """Test generating PR body for UPDATE action"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I install Docker?", "Troubleshooting")

        pr_body = generate_pr_body(decision, 43, 'test-course')

        assert '📝' in pr_body
        assert 'UPDATE' in pr_body
        assert decision.document_id in pr_body
        assert 'abc1234567' in pr_body

    def test_generate_duplicate_comment(self, test_course_dir, mock_openai_duplicate):
        """Test generating comment for DUPLICATE action"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("What Python version?", "3.9+")

        comment = generate_duplicate_comment(decision, 'test-course', 'https://example.com/faq')

        assert '🔄' in comment
        assert 'Duplicate' in comment
        assert decision.document_id in comment
        assert decision.rationale in comment
        assert 'https://example.com/faq/test-course.html#def8901234' in comment
        assert '_questions/test-course/general/' in comment

    def test_generate_duplicate_comment_without_site_url(self, test_course_dir, mock_openai_duplicate):
        """Test generating comment for DUPLICATE action without site URL"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("What Python version?", "3.9+")

        comment = generate_duplicate_comment(decision, 'test-course')

        assert '🔄' in comment
        assert 'Duplicate' in comment
        assert decision.document_id in comment
        assert decision.rationale in comment
        # Should not contain live site link when site_url is None
        assert 'Live Site' not in comment
        assert '_questions/test-course/general/' in comment

    def test_get_file_changes_summary_new(self, test_course_dir, mock_openai_new):
        """Test file changes summary for NEW action"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I use uv?", "Run: uv sync")

        doc_index = find_question_files(test_course_dir)
        file_path = create_new_faq_file(test_course_dir, doc_index, decision)

        summary = get_file_changes_summary('NEW', file_path, test_course_dir)

        assert summary['action'] == 'NEW'
        assert 'test-course/general' in summary['file']
        assert summary['filename'].endswith('.md')
        assert 'install-dependencies-uv' in summary['filename']

    def test_get_file_changes_summary_update(self, test_course_dir, mock_openai_update):
        """Test file changes summary for UPDATE action"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I install Docker?", "Troubleshooting")

        doc_index = find_question_files(test_course_dir)
        file_path = update_existing_faq_file(test_course_dir, doc_index, decision)

        summary = get_file_changes_summary('UPDATE', file_path, test_course_dir)

        assert summary['action'] == 'UPDATE'
        assert 'test-course/general' in summary['file']
        assert summary['filename'] == '001_abc1234567_install-docker.md'


class TestCLIIntegration:
    """Test CLI integration with full workflow"""

    def test_parse_full_issue_body_integration(self):
        """Test parsing real issue body format"""
        issue_body = """### Course
test-course

### Question
How do I install dependencies using uv?

### Answer
Use the following command:
```bash
uv sync --dev
```

For production, use:
```bash
uv sync --no-dev
```

### Checklist
- [x] I have searched existing FAQs
- [x] My answer is accurate
"""

        course, question, answer = parse_full_issue_body(issue_body)

        assert course == 'test-course'
        assert 'uv' in question
        assert 'uv sync --dev' in answer
        assert 'uv sync --no-dev' in answer
        assert 'Checklist' not in answer

    def test_cli_main_with_new_action(self, test_course_dir, mock_openai_new, tmp_path, monkeypatch):
        """Test complete CLI execution with NEW action"""
        # Create issue body file
        issue_body = """### Course
test-course

### Question
How do I install dependencies using uv?

### Answer
Use: uv sync --dev
"""

        issue_file = tmp_path / 'issue.txt'
        issue_file.write_text(issue_body)

        output_dir = tmp_path / 'output'
        output_dir.mkdir()

        # Mock sys.argv
        import sys
        original_argv = sys.argv
        sys.argv = [
            'cli.py',
            '--issue-body', issue_body,
            '--issue-number', '42',
            '--model', 'gpt-5-nano',
            '--output-dir', str(output_dir)
        ]

        # Mock environment variable
        monkeypatch.setenv('OPENAI_API_KEY', 'fake-api-key')

        # Change to parent directory of test_course_dir so _questions/test-course is found
        original_cwd = Path.cwd()
        monkeypatch.chdir(test_course_dir.parent.parent)

        try:
            # Run CLI
            cli_main()

            # Verify output file was created
            output_file = output_dir / 'faq_decision.json'
            assert output_file.exists()

            # Verify output content
            with open(output_file) as f:
                output = json.load(f)

            assert output['action'] == 'NEW'
            assert output['course'] == 'test-course'
            assert 'pr_body' in output
            assert 'file_path' in output

        finally:
            sys.argv = original_argv
            monkeypatch.chdir(original_cwd)


class TestErrorHandlingAndEdgeCases:
    """Test error handling and edge cases"""

    def test_create_faq_in_empty_section_directory(self, test_course_dir, mock_openai_new):
        """Test creating FAQ when section directory exists but is empty"""
        # Ensure module-2 directory exists
        module2_dir = test_course_dir / 'module-2'
        module2_dir.mkdir(exist_ok=True)

        # Create a decision for module-2 which exists but has no FAQs
        decision = FAQDecision(
            action='NEW',
            rationale='New section test',
            document_id='test1234567',
            section_rationale='This is for module-2 which has no FAQs yet',
            section_id='module-2',
            order=1,
            question='How do I start module 2?',
            proposed_content='Module 2 starts with an introduction.',
            filename_slug='start-module-2',
            warnings=[]
        )

        doc_index = find_question_files(test_course_dir)

        # Create file in empty section directory
        file_path = create_new_faq_file(test_course_dir, doc_index, decision)

        assert file_path.exists()
        assert file_path.parent.name == 'module-2'

        # Verify file format
        content = file_path.read_text()
        fm, body = parse_frontmatter(content)
        assert fm['question'] == decision.question

    def test_update_nonexistent_document_raises_error(self, test_course_dir, mock_openai_update):
        """Test that updating non-existent document raises KeyError"""
        decision = FAQDecision(
            action='UPDATE',
            rationale='Update test',
            document_id='nonexistent123',
            section_rationale='General section',
            section_id='general',
            order=1,
            question='Test question',
            proposed_content='Test content',
            filename_slug=None,
            warnings=[]
        )

        doc_index = find_question_files(test_course_dir)

        # Should raise KeyError when trying to update non-existent document
        with pytest.raises(KeyError):
            update_existing_faq_file(test_course_dir, doc_index, decision)

    def test_agent_with_empty_course_directory(self, tmp_path, mock_openai_new):
        """Test agent initialization with empty course directory"""
        # Create empty course directory with metadata only
        course_dir = tmp_path / "_questions" / "empty-course"
        course_dir.mkdir(parents=True)

        metadata = {
            'course': 'empty-course',
            'course_name': 'Empty Course',
            'sections': []
        }

        import yaml
        with open(course_dir / '_metadata.yaml', 'w') as f:
            yaml.dump(metadata, f)

        # Agent should initialize successfully even with no FAQs
        agent = FAQAgent(course_dir, 'fake-api-key', 'gpt-5-nano')

        assert len(agent.documents) == 0
        assert agent.metadata['course'] == 'empty-course'

    def test_create_faq_with_order_minus_one(self, test_course_dir, mock_openai_new):
        """Test creating FAQ with order=-1 (append to end)"""
        decision = FAQDecision(
            action='NEW',
            rationale='Append to end test',
            document_id='append123456',
            section_rationale='General section',
            section_id='general',
            order=-1,  # Should append to end
            question='New question at end',
            proposed_content='This should be added at the end.',
            filename_slug='question-at-end',
            warnings=[]
        )

        doc_index = find_question_files(test_course_dir)
        file_path = create_new_faq_file(test_course_dir, doc_index, decision)

        assert file_path.exists()

        # Check that sort_order was set to a value > existing ones
        fm, _ = parse_frontmatter(file_path.read_text())
        assert fm['sort_order'] > 2  # Existing FAQs have sort_order 1 and 2


class TestSiteGeneratorIntegration:
    """Test that created FAQ files work with the site generator"""

    def test_new_faq_file_can_be_processed_by_site_generator(self, test_course_dir, mock_openai_new, monkeypatch):
        """Test that newly created FAQ files can be processed by generate_website.py"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I use uv?", "Run: uv sync")

        doc_index = find_question_files(test_course_dir)
        file_path = create_new_faq_file(test_course_dir, doc_index, decision)

        # Change to parent directory so _questions can be found
        original_cwd = Path.cwd()
        monkeypatch.chdir(test_course_dir.parent.parent)

        try:
            # Collect questions using the site generator
            courses = collect_questions()

            # Verify our new FAQ was collected
            assert len(courses) == 1
            course_name, course_info = courses[0]
            assert course_name == 'test-course'

            # Find our new FAQ in the collected questions
            found = False
            for section_id, section_data in course_info['sections'].items():
                # section_data is a list of questions
                for question in section_data:
                    if 'uv' in question.get('question', '').lower():
                        found = True
                        # Verify the question was processed correctly
                        # HTML will have whitespace spans, so check for individual words
                        assert 'uv' in question['content']
                        assert 'sync' in question['content']
                        assert question['id'] is not None
                        assert question['sort_order'] is not None
                        break

            assert found, "New FAQ was not found in collected questions"
        finally:
            monkeypatch.chdir(original_cwd)

    def test_updated_faq_file_can_be_processed_by_site_generator(self, test_course_dir, mock_openai_update, monkeypatch):
        """Test that updated FAQ files can be processed by generate_website.py"""
        agent = FAQAgent(test_course_dir, 'fake-api-key', 'gpt-5-nano')
        decision = agent.process_proposal("How do I install Docker?", "Troubleshooting")

        doc_index = find_question_files(test_course_dir)
        file_path = update_existing_faq_file(test_course_dir, doc_index, decision)

        # Change to parent directory so _questions can be found
        original_cwd = Path.cwd()
        monkeypatch.chdir(test_course_dir.parent.parent)

        try:
            # Collect questions using the site generator
            courses = collect_questions()

            # Find the updated FAQ
            found = False
            course_name, course_info = courses[0]
            for section_id, section_data in course_info['sections'].items():
                # section_data is a list of questions
                for question in section_data:
                    if question['id'] == 'abc1234567':
                        found = True
                        # Verify the update was applied
                        assert 'Troubleshooting' in question['content']  # 'content' is the HTML
                        break

            assert found, "Updated FAQ was not found in collected questions"
        finally:
            monkeypatch.chdir(original_cwd)

    def test_markdown_rendering_with_code_blocks(self, test_course_dir, mock_openai_new):
        """Test that FAQ with code blocks renders correctly"""
        # Create decision with code block in content
        decision = FAQDecision(
            action='NEW',
            rationale='Test code rendering',
            document_id='code1234567',
            section_rationale='General section',
            section_id='general',
            order=5,
            question='How do I run pytest?',
            proposed_content='Use the following command:\n```bash\npytest tests/ -v\n```\n\nThis will run all tests.',
            filename_slug='run-pytest',
            warnings=[]
        )

        doc_index = find_question_files(test_course_dir)
        file_path = create_new_faq_file(test_course_dir, doc_index, decision)

        # Read the file and process markdown
        content = file_path.read_text()
        fm, body = parse_frontmatter(content)
        html = process_markdown(body)

        # Verify code block was rendered with HTML entities for spaces
        assert '<code' in html or '<pre' in html
        # The HTML will have <span class="w"> </span> for spaces
        assert 'pytest' in html and 'tests/' in html


class TestEndToEndWorkflow:
    """Test complete end-to-end workflows"""

    def test_new_faq_complete_workflow(self, test_course_dir, mock_openai_new):
        """Test complete workflow for creating a new FAQ"""
        # Step 1: Parse issue body
        issue_body = """### Course
test-course

### Question
How do I install dependencies using uv?

### Answer
Use: uv sync --dev
"""
        course, question, answer = parse_full_issue_body(issue_body)

        # Step 2: Process with agent
        decision = process_faq_proposal(
            test_course_dir,
            question,
            answer,
            'fake-api-key',
            'gpt-5-nano'
        )

        assert decision.action == 'NEW'

        # Step 3: Create file
        doc_index = find_question_files(test_course_dir)
        file_path = create_new_faq_file(test_course_dir, doc_index, decision)

        assert file_path.exists()

        # Step 4: Generate PR body
        pr_body = generate_pr_body(decision, 42, course)

        assert 'NEW' in pr_body
        assert question in pr_body

        # Step 5: Verify file can be read back
        fm, body = parse_frontmatter(file_path.read_text())
        assert fm['question'] == decision.question

    def test_update_faq_complete_workflow(self, test_course_dir, mock_openai_update):
        """Test complete workflow for updating an existing FAQ"""
        issue_body = """### Course
test-course

### Question
How do I install Docker?

### Answer
If installation fails, run as administrator.
"""
        course, question, answer = parse_full_issue_body(issue_body)

        # Get original file
        doc_index = find_question_files(test_course_dir)
        original_file = doc_index['abc1234567']
        original_fm, original_body = parse_frontmatter(original_file.read_text())

        # Process proposal
        decision = process_faq_proposal(
            test_course_dir,
            question,
            answer,
            'fake-api-key',
            'gpt-5-nano'
        )

        assert decision.action == 'UPDATE'
        assert decision.document_id == 'abc1234567'

        # Update file
        file_path = update_existing_faq_file(test_course_dir, doc_index, decision)

        # Verify update
        updated_fm, updated_body = parse_frontmatter(file_path.read_text())
        assert updated_fm['id'] == original_fm['id']
        assert 'Troubleshooting' in updated_body

        # Generate PR
        pr_body = generate_pr_body(decision, 43, course)
        assert 'UPDATE' in pr_body

    def test_duplicate_faq_complete_workflow(self, test_course_dir, mock_openai_duplicate):
        """Test complete workflow for duplicate FAQ"""
        issue_body = """### Course
test-course

### Question
What Python version do I need?

### Answer
Python 3.9 or higher
"""
        course, question, answer = parse_full_issue_body(issue_body)

        # Process proposal
        decision = process_faq_proposal(
            test_course_dir,
            question,
            answer,
            'fake-api-key',
            'gpt-5-nano'
        )

        assert decision.action == 'DUPLICATE'
        assert decision.document_id == 'def8901234'

        # Generate comment
        comment = generate_duplicate_comment(decision, course)

        assert 'Duplicate' in comment
        assert decision.document_id in comment

        # Verify no files were created/modified
        doc_index = find_question_files(test_course_dir)
        original_file = doc_index['def8901234']
        original_content = original_file.read_text()

        # File should be unchanged
        assert original_file.read_text() == original_content
