"""
Tests for sorting and organizing functionality
"""
import pytest
import sys
from pathlib import Path

# Add the project root to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from generate_website import sort_sections_and_questions


class TestSortSectionsAndQuestions:
    """Test the sorting functionality for sections and questions"""
    
    def test_sort_questions_by_sort_order(self):
        """Test that questions are sorted by sort_order within sections"""
        courses = [
            ("test-course", {
                "sections": {
                    "general": [
                        {"question": "Third question", "sort_order": 3},
                        {"question": "First question", "sort_order": 1},
                        {"question": "Second question", "sort_order": 2}
                    ]
                },
                "section_order": [
                    {"id": "general", "name": "General Questions"}
                ]
            })
        ]
        
        result = sort_sections_and_questions(courses)
        
        ordered_sections = result[0][1]["ordered_sections"]
        assert len(ordered_sections) == 1
        
        questions = ordered_sections[0]["questions"]
        assert len(questions) == 3
        assert questions[0]["question"] == "First question"
        assert questions[1]["question"] == "Second question"
        assert questions[2]["question"] == "Third question"
    
    def test_sort_sections_by_metadata_order(self):
        """Test that sections are ordered according to metadata"""
        courses = [
            ("test-course", {
                "sections": {
                    "module-2": [{"question": "Q2", "sort_order": 1}],
                    "general": [{"question": "Q1", "sort_order": 1}],
                    "module-1": [{"question": "Q3", "sort_order": 1}]
                },
                "section_order": [
                    {"id": "general", "name": "General Questions"},
                    {"id": "module-1", "name": "Module 1"},
                    {"id": "module-2", "name": "Module 2"}
                ]
            })
        ]
        
        result = sort_sections_and_questions(courses)
        
        ordered_sections = result[0][1]["ordered_sections"]
        assert len(ordered_sections) == 3
        
        # Should be in metadata order
        assert ordered_sections[0]["id"] == "general"
        assert ordered_sections[0]["name"] == "general"  # Uses ID as name when not found in metadata
        assert ordered_sections[1]["id"] == "module-1"
        assert ordered_sections[1]["name"] == "module-1"  # Uses ID as name when not found in metadata
        assert ordered_sections[2]["id"] == "module-2"
        assert ordered_sections[2]["name"] == "module-2"  # Uses ID as name when not found in metadata
    
    def test_sort_handles_missing_sections_in_metadata(self):
        """Test that sections not in metadata are added alphabetically at the end"""
        courses = [
            ("test-course", {
                "sections": {
                    "zzz-extra": [{"question": "Extra Q", "sort_order": 1}],
                    "general": [{"question": "General Q", "sort_order": 1}],
                    "aaa-bonus": [{"question": "Bonus Q", "sort_order": 1}]
                },
                "section_order": [
                    {"id": "general", "name": "General Questions"}
                ]
            })
        ]
        
        result = sort_sections_and_questions(courses)
        
        ordered_sections = result[0][1]["ordered_sections"]
        assert len(ordered_sections) == 3
        
        # Missing sections come first in alphabetical order, then metadata ones
        assert ordered_sections[0]["id"] == "aaa-bonus"
        assert ordered_sections[0]["name"] == "aaa-bonus"  # Should use ID as name
        
        # Then the metadata one
        assert ordered_sections[1]["id"] == "general"
        assert ordered_sections[1]["name"] == "general"  # Uses ID as name when not found in metadata
        
        # Then remaining missing ones
        assert ordered_sections[2]["id"] == "zzz-extra"
        assert ordered_sections[2]["name"] == "zzz-extra"
    
    def test_sort_generates_section_ids_for_missing(self):
        """Test that proper IDs are generated for sections not in metadata"""
        courses = [
            ("test-course", {
                "sections": {
                    "Module 1: Introduction": [{"question": "Q1", "sort_order": 1}],
                    "Advanced Topics.": [{"question": "Q2", "sort_order": 1}]
                },
                "section_order": []  # Empty metadata
            })
        ]
        
        result = sort_sections_and_questions(courses)
        
        ordered_sections = result[0][1]["ordered_sections"]
        assert len(ordered_sections) == 2
        
        # Should be alphabetically ordered
        section_names = [s["name"] for s in ordered_sections]
        assert "Advanced Topics." in section_names
        assert "Module 1: Introduction" in section_names
        
        # Should generate proper IDs
        for section in ordered_sections:
            if section["name"] == "Module 1: Introduction":
                assert section["id"] == "module-1-introduction"
            elif section["name"] == "Advanced Topics.":
                assert section["id"] == "advanced-topics"
    
    def test_sort_multiple_courses(self):
        """Test sorting functionality with multiple courses"""
        courses = [
            ("course-a", {
                "sections": {
                    "module-2": [
                        {"question": "Q2", "sort_order": 2},
                        {"question": "Q1", "sort_order": 1}
                    ]
                },
                "section_order": [
                    {"id": "module-2", "name": "Module 2"}
                ]
            }),
            ("course-b", {
                "sections": {
                    "general": [
                        {"question": "Q3", "sort_order": 1}
                    ]
                },
                "section_order": [
                    {"id": "general", "name": "General"}
                ]
            })
        ]
        
        result = sort_sections_and_questions(courses)
        
        assert len(result) == 2
        
        # Check first course
        course_a_sections = result[0][1]["ordered_sections"]
        assert len(course_a_sections) == 1
        assert course_a_sections[0]["questions"][0]["question"] == "Q1"
        assert course_a_sections[0]["questions"][1]["question"] == "Q2"
        
        # Check second course
        course_b_sections = result[1][1]["ordered_sections"]
        assert len(course_b_sections) == 1
        assert course_b_sections[0]["questions"][0]["question"] == "Q3"
    
    def test_sort_empty_sections(self):
        """Test sorting with empty sections"""
        courses = [
            ("test-course", {
                "sections": {},
                "section_order": [
                    {"id": "general", "name": "General Questions"},
                    {"id": "module-1", "name": "Module 1"}
                ]
            })
        ]
        
        result = sort_sections_and_questions(courses)
        
        ordered_sections = result[0][1]["ordered_sections"]
        assert len(ordered_sections) == 0
    
    def test_sort_preserves_question_data(self):
        """Test that all question data is preserved during sorting"""
        courses = [
            ("test-course", {
                "sections": {
                    "general": [
                        {
                            "question": "How to test?",
                            "sort_order": 2,
                            "id": "test123",
                            "section": "General",
                            "course": "test-course",
                            "content": "<p>Test content</p>",
                            "file_path": "test/path.md",
                            "images": [{"id": "img1", "path": "/test.png"}]
                        },
                        {
                            "question": "What is testing?",
                            "sort_order": 1,
                            "id": "test456",
                            "section": "General",
                            "course": "test-course",
                            "content": "<p>Other content</p>",
                            "file_path": "test/other.md",
                            "images": []
                        }
                    ]
                },
                "section_order": [
                    {"id": "general", "name": "General Questions"}
                ]
            })
        ]
        
        result = sort_sections_and_questions(courses)
        
        questions = result[0][1]["ordered_sections"][0]["questions"]
        
        # Should be sorted by sort_order (1, then 2)
        assert questions[0]["question"] == "What is testing?"
        assert questions[1]["question"] == "How to test?"
        
        # All data should be preserved
        for question in questions:
            assert "id" in question
            assert "section" in question
            assert "course" in question
            assert "content" in question
            assert "file_path" in question
            assert "images" in question
    
    def test_sort_modifies_courses_in_place(self):
        """Test that sorting modifies the courses data structure in place"""
        original_courses = [
            ("test-course", {
                "sections": {
                    "general": [
                        {"question": "Second", "sort_order": 2},
                        {"question": "First", "sort_order": 1}
                    ]
                },
                "section_order": [
                    {"id": "general", "name": "General Questions"}
                ]
            })
        ]
        
        # Create a reference to check modification
        course_data = original_courses[0][1]
        
        result = sort_sections_and_questions(original_courses)
        
        # Should return the same object
        assert result is original_courses
        
        # Should have added ordered_sections to the original data
        assert "ordered_sections" in course_data
        assert len(course_data["ordered_sections"]) == 1