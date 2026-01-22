"""
Tests for JSON generation functionality
"""
import pytest
import sys
import tempfile
import os
import json
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from generate_website import (
    generate_json_data,
    sort_sections_and_questions
)


class TestJSONGeneration:
    """Test JSON generation functionality"""
    
    def test_generate_json_data_basic(self):
        """Test basic JSON generation for courses"""
        with tempfile.TemporaryDirectory() as temp_dir:
            site_dir = Path(temp_dir)
            
            # Create mock courses data
            courses = [
                ('test-course', {
                    'course_name': 'Test Course',
                    'sections': {
                        'General Questions': [
                            {
                                'id': 'q1',
                                'question': 'What is Python?',
                                'section': 'General Questions',
                                'sort_order': 1,
                                'course': 'test-course',
                                'content': '<p>Python is a programming language</p>',
                                'answer': 'Python is a programming language',
                                'file_path': 'test-course/general/q1.md',
                                'images': []
                            },
                            {
                                'id': 'q2',
                                'question': 'How to install Python?',
                                'section': 'General Questions',
                                'sort_order': 2,
                                'course': 'test-course',
                                'content': '<p>Download from python.org</p>',
                                'answer': 'Download from python.org',
                                'file_path': 'test-course/general/q2.md',
                                'images': []
                            }
                        ]
                    },
                    'section_order': [
                        {'id': 'general', 'name': 'General Questions'}
                    ]
                })
            ]
            
            # Generate JSON data
            generate_json_data(courses, site_dir)
            
            # Verify JSON directory was created
            json_dir = site_dir / 'json'
            assert json_dir.exists()
            assert json_dir.is_dir()
            
            # Verify course JSON file was created
            course_json_file = json_dir / 'test-course.json'
            assert course_json_file.exists()
            
            # Verify courses.json was created
            courses_json_file = json_dir / 'courses.json'
            assert courses_json_file.exists()
            
            # Verify course JSON content
            with open(course_json_file, 'r', encoding='utf-8') as f:
                course_data = json.load(f)
            
            assert len(course_data) == 2
            assert course_data[0]['id'] == 'q1'
            assert course_data[0]['course'] == 'test-course'
            assert course_data[0]['section'] == 'General Questions'
            assert course_data[0]['question'] == 'What is Python?'
            assert course_data[0]['answer'] == 'Python is a programming language'
            
            assert course_data[1]['id'] == 'q2'
            assert course_data[1]['question'] == 'How to install Python?'
            assert course_data[1]['answer'] == 'Download from python.org'
            
            # Verify courses index JSON content
            with open(courses_json_file, 'r', encoding='utf-8') as f:
                courses_index = json.load(f)
            
            assert len(courses_index) == 1
            assert courses_index[0]['course'] == 'test-course'
            assert courses_index[0]['course_name'] == 'Test Course'
            assert courses_index[0]['path'] == '/json/test-course.json'
            assert courses_index[0]['questions_count'] == 2
    
    def test_generate_json_data_multiple_courses(self):
        """Test JSON generation for multiple courses"""
        with tempfile.TemporaryDirectory() as temp_dir:
            site_dir = Path(temp_dir)
            
            # Create mock data for multiple courses
            courses = [
                ('course-1', {
                    'course_name': 'Course One',
                    'sections': {
                        'Section 1': [
                            {
                                'id': 'c1q1',
                                'question': 'Question 1',
                                'section': 'Section 1',
                                'sort_order': 1,
                                'course': 'course-1',
                                'content': '<p>Answer 1</p>',
                                'answer': 'Answer 1',
                                'file_path': 'course-1/section-1/q1.md',
                                'images': []
                            }
                        ]
                    },
                    'section_order': [
                        {'id': 'section-1', 'name': 'Section 1'}
                    ]
                }),
                ('course-2', {
                    'course_name': 'Course Two',
                    'sections': {
                        'Section A': [
                            {
                                'id': 'c2q1',
                                'question': 'Question A',
                                'section': 'Section A',
                                'sort_order': 1,
                                'course': 'course-2',
                                'content': '<p>Answer A</p>',
                                'answer': 'Answer A',
                                'file_path': 'course-2/section-a/q1.md',
                                'images': []
                            }
                        ]
                    },
                    'section_order': [
                        {'id': 'section-a', 'name': 'Section A'}
                    ]
                })
            ]
            
            # Generate JSON data
            generate_json_data(courses, site_dir)
            
            json_dir = site_dir / 'json'
            
            # Verify both course JSON files exist
            assert (json_dir / 'course-1.json').exists()
            assert (json_dir / 'course-2.json').exists()
            
            # Verify courses index contains both courses
            with open(json_dir / 'courses.json', 'r', encoding='utf-8') as f:
                courses_index = json.load(f)
            
            assert len(courses_index) == 2
            assert courses_index[0]['course'] == 'course-1'
            assert courses_index[0]['course_name'] == 'Course One'
            assert courses_index[1]['course'] == 'course-2'
            assert courses_index[1]['course_name'] == 'Course Two'
    
    def test_generate_json_data_multiple_sections(self):
        """Test JSON generation with multiple sections"""
        with tempfile.TemporaryDirectory() as temp_dir:
            site_dir = Path(temp_dir)
            
            courses = [
                ('test-course', {
                    'course_name': 'Test Course',
                    'sections': {
                        'General': [
                            {
                                'id': 'g1',
                                'question': 'General Question 1',
                                'section': 'General',
                                'sort_order': 1,
                                'course': 'test-course',
                                'content': '<p>General Answer 1</p>',
                                'answer': 'General Answer 1',
                                'file_path': 'test-course/general/g1.md',
                                'images': []
                            }
                        ],
                        'Module 1': [
                            {
                                'id': 'm1',
                                'question': 'Module 1 Question',
                                'section': 'Module 1',
                                'sort_order': 1,
                                'course': 'test-course',
                                'content': '<p>Module 1 Answer</p>',
                                'answer': 'Module 1 Answer',
                                'file_path': 'test-course/module-1/m1.md',
                                'images': []
                            }
                        ]
                    },
                    'section_order': [
                        {'id': 'general', 'name': 'General'},
                        {'id': 'module-1', 'name': 'Module 1'}
                    ]
                })
            ]
            
            # Generate JSON data
            generate_json_data(courses, site_dir)
            
            # Verify JSON contains questions from all sections
            with open(site_dir / 'json' / 'test-course.json', 'r', encoding='utf-8') as f:
                course_data = json.load(f)
            
            assert len(course_data) == 2
            
            # Verify questions from different sections
            sections_found = {q['section'] for q in course_data}
            assert 'General' in sections_found
            assert 'Module 1' in sections_found
    
    def test_generate_json_data_empty_course(self):
        """Test JSON generation with empty course (no questions)"""
        with tempfile.TemporaryDirectory() as temp_dir:
            site_dir = Path(temp_dir)
            
            courses = [
                ('empty-course', {
                    'course_name': 'Empty Course',
                    'sections': {},
                    'section_order': []
                })
            ]
            
            # Generate JSON data
            generate_json_data(courses, site_dir)
            
            # Verify course JSON file exists but is empty list
            with open(site_dir / 'json' / 'empty-course.json', 'r', encoding='utf-8') as f:
                course_data = json.load(f)
            
            assert course_data == []
            
            # Verify courses index shows 0 questions
            with open(site_dir / 'json' / 'courses.json', 'r', encoding='utf-8') as f:
                courses_index = json.load(f)
            
            assert courses_index[0]['questions_count'] == 0
    
    def test_json_structure_fields(self):
        """Test that JSON has all required fields"""
        with tempfile.TemporaryDirectory() as temp_dir:
            site_dir = Path(temp_dir)
            
            courses = [
                ('test-course', {
                    'course_name': 'Test Course',
                    'sections': {
                        'General': [
                            {
                                'id': 'test123',
                                'question': 'Test Question',
                                'section': 'General',
                                'sort_order': 1,
                                'course': 'test-course',
                                'content': '<p>Test Answer</p>',
                                'answer': 'Test Answer',
                                'file_path': 'test-course/general/test.md',
                                'images': []
                            }
                        ]
                    },
                    'section_order': [
                        {'id': 'general', 'name': 'General'}
                    ]
                })
            ]
            
            # Generate JSON data
            generate_json_data(courses, site_dir)
            
            # Verify all required fields are present
            with open(site_dir / 'json' / 'test-course.json', 'r', encoding='utf-8') as f:
                course_data = json.load(f)
            
            required_fields = ['id', 'course', 'section', 'question', 'answer']
            
            for question in course_data:
                for field in required_fields:
                    assert field in question, f"Missing required field: {field}"
    
    def test_json_unicode_handling(self):
        """Test that JSON properly handles unicode characters"""
        with tempfile.TemporaryDirectory() as temp_dir:
            site_dir = Path(temp_dir)
            
            courses = [
                ('test-course', {
                    'course_name': 'Test Course',
                    'sections': {
                        'General': [
                            {
                                'id': 'unicode1',
                                'question': 'What is café?',
                                'section': 'General',
                                'sort_order': 1,
                                'course': 'test-course',
                                'content': '<p>Café is a place with ñ and 日本語</p>',
                                'answer': 'Café is a place with ñ and 日本語',
                                'file_path': 'test-course/general/unicode.md',
                                'images': []
                            }
                        ]
                    },
                    'section_order': [
                        {'id': 'general', 'name': 'General'}
                    ]
                })
            ]
            
            # Generate JSON data
            generate_json_data(courses, site_dir)
            
            # Verify unicode is preserved
            with open(site_dir / 'json' / 'test-course.json', 'r', encoding='utf-8') as f:
                course_data = json.load(f)
            
            assert course_data[0]['question'] == 'What is café?'
            assert 'ñ' in course_data[0]['answer']
            assert '日本語' in course_data[0]['answer']
