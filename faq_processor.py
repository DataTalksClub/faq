import hashlib
import re
from pathlib import Path
import yaml

import requests
import docx

def clean_line(line):
    line = line.strip()
    line = line.strip('\uFEFF')
    return line

def sanitize_filename(text):
    """Convert text to safe filename with length limits"""
    # Remove special characters and replace spaces with hyphens
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    text = text.lower().strip('-')
    
    # Limit filename length (Windows has ~260 character path limit)
    if len(text) > 100:
        text = text[:100].rstrip('-')
    
    return text

def download_docx_file(file_id, course_name):
    """Download and cache docx file locally"""
    cache_dir = Path('cache')
    cache_dir.mkdir(exist_ok=True)
    
    cache_file = cache_dir / f'{course_name}.docx'
    
    if cache_file.exists():
        print(f"Using cached file for {course_name}")
        return cache_file
    
    print(f"Downloading {course_name}...")
    url = f'https://docs.google.com/document/d/{file_id}/export?format=docx'
    
    response = requests.get(url)
    response.raise_for_status()
    
    with open(cache_file, 'wb') as f:
        f.write(response.content)
    
    return cache_file

def extract_images_from_docx(doc, course_name):
    """Extract images from docx and save them to images directory"""
    images_dir = Path('images') / course_name
    images_dir.mkdir(parents=True, exist_ok=True)
    
    image_mapping = {}
    
    for rel_id, rel in doc.part.rels.items():
        # Check if this is actually an image relationship by checking the relationship type
        # Image relationships should have content types like image/png, image/jpeg, etc.
        try:
            # Skip external relationships entirely
            if hasattr(rel, 'is_external') and rel.is_external:
                continue
            
            # Check if the target part has an image content type
            if not hasattr(rel, 'target_part') or not hasattr(rel.target_part, 'content_type'):
                continue
                
            content_type = rel.target_part.content_type
            if not content_type or not content_type.startswith('image/'):
                continue
                
            image_data = rel.target_part.blob
            
            # Generate filename based on content hash
            image_hash = hashlib.md5(image_data).hexdigest()[:8]
            
            # Determine file extension from content type
            if 'png' in content_type:
                ext = 'png'
            elif 'jpeg' in content_type or 'jpg' in content_type:
                ext = 'jpg'
            elif 'gif' in content_type:
                ext = 'gif'
            elif 'webp' in content_type:
                ext = 'webp'
            else:
                ext = 'png'  # Default fallback
            
            image_filename = f'image_{image_hash}.{ext}'
            image_path = images_dir / image_filename
            
            with open(image_path, 'wb') as f:
                f.write(image_data)
            
            # Map using the relationship ID with relative path
            image_mapping[rel_id] = f'images/{course_name}/{image_filename}'
            print(f"Extracted image: {rel_id} -> {image_filename}")
        except (ValueError, AttributeError, Exception):
            # Skip any relationships that can't be processed as images
            continue
    
    return image_mapping

def extract_paragraph_content(paragraph):
    """Extract text and hyperlinks from a paragraph"""
    content_parts = []
    
    for run in paragraph.runs:
        text = run.text
        if not text:
            continue
            
        # Check if this run is part of a hyperlink
        hyperlink = None
        element = run._element
        
        # Look for hyperlink in the run's parent elements
        parent = element.getparent()
        while parent is not None:
            if parent.tag.endswith('}hyperlink'):
                # Found hyperlink element, get the relationship ID
                rel_id = parent.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                if rel_id:
                    try:
                        # Get the hyperlink target from document relationships
                        rel = paragraph._parent.part.rels[rel_id]
                        hyperlink = rel.target_ref
                    except (KeyError, AttributeError):
                        pass
                break
            parent = parent.getparent()
        
        # Add text with optional hyperlink
        if hyperlink:
            content_parts.append(f'[{text}]({hyperlink})')
        else:
            content_parts.append(text)
    
    return ''.join(content_parts)

def read_faq(cache_file, course_name):
    """Read FAQ from cached docx file and extract content with images and links"""
    doc = docx.Document(cache_file)
    
    # Extract images
    image_mapping = extract_images_from_docx(doc, course_name)
    
    questions = []

    question_heading_style = 'heading 2'
    section_heading_style = 'heading 1'
    
    section_title = ''
    question_title = ''
    answer_content = []
     
    for p in doc.paragraphs:
        style = p.style.name.lower()
        
        # Extract text with hyperlinks
        p_text = clean_line(extract_paragraph_content(p))
    
        # Check for images in paragraph using a simpler approach
        images_in_paragraph = []
        
        # Look for images in runs
        for run in p.runs:
            # Check for embedded images using element inspection
            element = run._element
            # Look for any blip elements that contain image references
            for blip in element.iter():
                if blip.tag.endswith('}blip'):
                    embed_attr = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if embed_attr and embed_attr in image_mapping:
                        images_in_paragraph.append(image_mapping[embed_attr])
    
        # Skip only if paragraph has no text AND no images
        if len(p_text) == 0 and len(images_in_paragraph) == 0:
            continue
    
        # Handle section headings (but still check for images)
        if style == section_heading_style:
            # Add any images from this heading paragraph before moving to new section
            for image_path in images_in_paragraph:
                answer_content.append({'type': 'image', 'content': image_path})
            section_title = p_text
            continue
    
        # Handle question headings (but still check for images)
        if style == question_heading_style:
            # Save previous question if it exists
            if answer_content and section_title and question_title:
                questions.append({
                    'content': answer_content,
                    'section': section_title,
                    'question': question_title,
                })
                answer_content = []
            
            # Add any images from this heading paragraph before moving to new question
            for image_path in images_in_paragraph:
                answer_content.append({'type': 'image', 'content': image_path})
    
            question_title = p_text
            continue
        
        # Add text content if present
        if p_text:
            answer_content.append({'type': 'text', 'content': p_text})
        
        # Add images (regardless of whether there's text)
        for image_path in images_in_paragraph:
            answer_content.append({'type': 'image', 'content': image_path})
    
    # Add the last question
    if answer_content and section_title and question_title:
        questions.append({
            'content': answer_content,
            'section': section_title,
            'question': question_title,
        })

    return questions





def generate_unique_id(course_name, section, question, used_ids):
    """Generate a unique ID for a question, ensuring no collisions"""
    base_text = f"{course_name}_{section}_{question}"
    base_id = hashlib.md5(base_text.encode()).hexdigest()[:10]
    
    if base_id not in used_ids:
        used_ids.add(base_id)
        return base_id
    
    # If collision, try with incrementing suffix
    counter = 1
    while True:
        collision_text = f"{base_text}_{counter}"
        collision_id = hashlib.md5(collision_text.encode()).hexdigest()[:10]
        if collision_id not in used_ids:
            used_ids.add(collision_id)
            return collision_id
        counter += 1

def create_question_file(question_data, course_name, question_index, question_id):
    """Create individual question markdown file with frontmatter in course folder"""
    course_dir = Path('_questions') / course_name
    course_dir.mkdir(parents=True, exist_ok=True)
    
    # Create short name for filename (truncate to 30 chars)
    question_title = question_data['question'][:30] if len(question_data['question']) > 30 else question_data['question']
    short_name = sanitize_filename(question_title)
    
    # Use ID + short name as filename
    filename = f'{question_id}_{short_name}.md'
    
    question_file = course_dir / filename
    
    # Calculate sort order: question index * 10 to allow for future insertion
    sort_order = question_index * 10
    
    with open(question_file, 'w', encoding='utf-8') as f:
        # Create frontmatter data
        frontmatter_data = {
            'id': question_id,
            'question': question_data["question"],
            'section': question_data["section"],
            'course': course_name,
            'sort_order': sort_order
        }
        
        # Write properly formatted YAML frontmatter
        f.write('---\n')
        yaml.dump(frontmatter_data, f, default_flow_style=False, allow_unicode=True)
        f.write('---\n\n')
        
        # Write answer content
        for item in question_data['content']:
            if item['type'] == 'text':
                f.write(f'{item["content"]}\n\n')
            elif item['type'] == 'image':
                f.write(f'![Image]({item["content"]})\n\n')
    
    return filename

def create_metadata_file(course_data):
    """Create _metadata.yaml file with section order for the course"""
    course_dir = Path('_questions') / course_data['course']
    course_dir.mkdir(parents=True, exist_ok=True)
    
    metadata_file = course_dir / '_metadata.yaml'
    
    # Extract sections in order of appearance
    sections = []
    seen_sections = set()
    
    for question in course_data['questions']:
        section = question['section']
        if section not in seen_sections:
            sections.append(section)
            seen_sections.add(section)
    
    with open(metadata_file, 'w', encoding='utf-8') as f:
        f.write(f'course: {course_data["course"]}\n')
        f.write('sections:\n')
        for section in sections:
            f.write(f'  - "{section}"\n')
    
    print(f"Generated metadata: {metadata_file}")


# Main execution
faq_documents = {
    'data-engineering-zoomcamp': '19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw',
    'machine-learning-zoomcamp': '1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8',
    'mlops-zoomcamp': '12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0',
}

documents = []
used_ids = set()  # Track used IDs across all courses

for course, file_id in faq_documents.items():
    print(f"\nProcessing {course}...")
    
    # Download and cache docx file
    cache_file = download_docx_file(file_id, course)
    
    # Read FAQ with images
    course_documents = read_faq(cache_file, course)
    
    course_data = {'course': course, 'questions': course_documents}
    documents.append(course_data)
    
    # Create individual question files with unique IDs
    print(f"Creating question files for {course}...")
    for i, question_data in enumerate(course_documents):
        question_id = generate_unique_id(course, question_data['section'], question_data['question'], used_ids)
        create_question_file(question_data, course, i + 1, question_id)
    
    # Create metadata file with section order
    create_metadata_file(course_data)
    
    # Create course index page - function not implemented yet
    # create_course_index(course_data)

print(f"\nProcessed {len(documents)} courses successfully!")
print("Generated files:")
print("- _questions/ - Individual question files")
print("- index.md - Main index page")
print("- [course].md - Course index pages")
print("- images/ - Extracted images organized by course")