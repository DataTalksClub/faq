"""
Core FAQ processing functions extracted from notebooks/rag.ipynb
"""

import hashlib
import yaml
from pathlib import Path
from typing import Dict, List, Tuple


def parse_metadata(content: str) -> dict:
    """Parse YAML metadata content"""
    return yaml.safe_load(content)


def parse_frontmatter(content: str) -> Tuple[dict, str]:
    """
    Parse YAML frontmatter from markdown content

    Returns:
        Tuple of (frontmatter_dict, markdown_content)
    """
    if not content.startswith('---'):
        return {}, content

    try:
        # Split frontmatter and content
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}, content

        frontmatter = yaml.safe_load(parts[1])
        markdown_content = parts[2].strip()

        return frontmatter or {}, markdown_content
    except yaml.YAMLError:
        return {}, content


def write_frontmatter(question_file: Path, frontmatter_data: dict, content: str) -> None:
    """Write frontmatter and content to a markdown file"""
    with open(question_file, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(frontmatter_data, f, default_flow_style=False, allow_unicode=True)
        f.write('---\n\n')
        f.write(f'{content}')


def read_metadata(course_dir: Path) -> dict:
    """Read course metadata from _metadata.yaml"""
    metadata_file = course_dir / '_metadata.yaml'
    content = metadata_file.read_text(encoding='utf8')
    metadata = parse_metadata(content)
    return metadata


def read_questions(course_dir: Path) -> List[dict]:
    """
    Read all questions from a course directory

    Returns:
        List of document dictionaries with course, section, question, answer, etc.
    """
    course_id = course_dir.name

    metadata = read_metadata(course_dir)
    course_sections = {d['id']: d['name'] for d in metadata['sections']}

    documents = []

    for question_file in course_dir.glob('*/*.md'):
        content = question_file.read_text(encoding='utf8')
        fm, answer = parse_frontmatter(content)

        section_dir = question_file.parent
        section_id = section_dir.name
        course_dir_from_file = section_dir.parent
        course_id = course_dir_from_file.name

        section_name = course_sections.get(section_id, section_id)

        document = {
            'course': course_id,
            'section': section_name,
            'section_id': section_id,
            'question': fm['question'],
            'answer': answer,
            'document_id': fm['id'],
            'sort_order': fm['sort_order']
        }

        documents.append(document)

    return documents


def find_question_files(course_dir: Path) -> Dict[str, Path]:
    """
    Create a mapping of document IDs to file paths

    Returns:
        Dictionary mapping document_id -> Path
    """
    docs = {}
    for question_file in course_dir.glob('*/*.md'):
        parts = question_file.name.split('_', maxsplit=3)
        doc_id = parts[1]
        docs[doc_id] = question_file
    return docs


def generate_document_id(question: str, answer: str, existing_ids: dict) -> str:
    """
    Generate a unique 10-character document ID using MD5 hash

    Handles collisions by appending a counter to the base text
    """
    base_text = question + ' ' + answer

    document_id = hashlib.md5(base_text.encode()).hexdigest()[:10]

    if document_id not in existing_ids:
        return document_id

    counter = 1
    while True:
        collision_text = f"{base_text}_{counter}"
        collision_id = hashlib.md5(collision_text.encode()).hexdigest()[:10]
        if collision_id not in existing_ids:
            return collision_id
        counter += 1


def find_largest_sort_order(section_dir: Path) -> int:
    """
    Find the next available sort order number in a section

    Returns:
        Next sort_order number (largest + 1)
    """
    last = sorted(section_dir.iterdir())[-1]
    sort_order, _ = last.name.split('_', maxsplit=1)
    return int(sort_order) + 1


def keep_relevant(results: List[dict]) -> List[dict]:
    """
    Filter search results to keep only relevant fields

    Removes 'course' and 'section' fields from results
    """
    new_results = []

    for d in results:
        d = d.copy()
        del d['course']
        del d['section']
        new_results.append(d)

    return new_results
