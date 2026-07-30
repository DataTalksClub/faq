"""
Core FAQ processing functions: frontmatter, course metadata, and sort order.
"""

import frontmatter
import hashlib
import yaml
from pathlib import Path
from typing import Dict, List, Tuple


def parse_metadata(content: str) -> dict:
    """Parse YAML metadata content"""
    return yaml.safe_load(content)


def parse_frontmatter(content: str) -> Tuple[dict, str]:
    """
    Parse YAML frontmatter from markdown content using python-frontmatter

    Returns:
        Tuple of (frontmatter_dict, markdown_content)
    """
    try:
        post = frontmatter.loads(content)
        return post.metadata, post.content.strip()
    except Exception:
        return {}, content


def write_frontmatter(question_file: Path, frontmatter_data: dict, content: str) -> None:
    """Write frontmatter and content to a markdown file"""
    post = frontmatter.Post(content, **frontmatter_data)
    with open(question_file, 'w', encoding='utf-8') as f:
        f.write(frontmatter.dumps(post))


def read_metadata(course_dir: Path) -> dict:
    """Read course metadata from _metadata.yaml"""
    content = (course_dir / '_metadata.yaml').read_text(encoding='utf8')
    return parse_metadata(content)


def read_course_catalog(questions_dir: Path) -> List[dict]:
    """
    Read the id and display name of every course under questions_dir.

    Used to tell the agent which other courses exist, so a proposal filed
    against the wrong course can be pointed at the right one.

    Returns:
        List of {'course': id, 'course_name': name} sorted by id
    """
    catalog = []

    for course_dir in sorted(questions_dir.iterdir()):
        if not (course_dir / '_metadata.yaml').exists():
            continue
        metadata = read_metadata(course_dir)
        catalog.append({
            'course': metadata['course'],
            'course_name': metadata['course_name'],
        })

    return catalog


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
        section_id = question_file.parent.name

        documents.append({
            'course': course_id,
            'section': course_sections.get(section_id, section_id),
            'section_id': section_id,
            'question': fm['question'],
            'answer': answer,
            'document_id': fm['id'],
            'sort_order': fm['sort_order'],
        })

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
    question_files = sorted(section_dir.glob('*.md'))
    if not question_files:
        return 1

    last = question_files[-1]
    sort_order, _ = last.name.split('_', maxsplit=1)
    return int(sort_order) + 1


def keep_relevant(results: List[dict]) -> List[dict]:
    """Drop the 'course' and 'section' fields from each search result."""
    new_results = []
    for d in results:
        d = d.copy()
        d.pop('course', None)
        d.pop('section', None)
        new_results.append(d)
    return new_results


def reciprocal_rank_fusion(
    result_sets: List[List[dict]],
    weights: List[float],
    limit: int,
    rank_constant: int = 60,
) -> List[dict]:
    """Combine ranked search results while preserving the original documents."""
    if len(result_sets) != len(weights):
        raise ValueError("result_sets and weights must have the same length")

    scores = {}
    documents = {}

    for weight, results in zip(weights, result_sets):
        for rank, result in enumerate(results, start=1):
            document_id = result.get("document_id")
            if not document_id:
                continue
            documents.setdefault(document_id, result)
            scores[document_id] = (
                scores.get(document_id, 0.0)
                + weight / (rank_constant + rank)
            )

    ranked_ids = sorted(scores, key=scores.get, reverse=True)
    return [documents[document_id] for document_id in ranked_ids[:limit]]
