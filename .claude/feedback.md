# FAQ Bot Feedback - PR Review Corrections

## 1. Wrong Section Placement

Kestra-related FAQs were incorrectly placed in `general` or `module-1` instead of `module-2` (workflow orchestration):

| PR | Issue | Correction |
|----|-------|------------|
| #141 | Kestra IANA timezones | general → module-2, sort_order 20 |
| #137 | Kestra stdout variables | general → module-2, sort_order 21 |
| #135 | Kestra outputFiles visibility | general → module-2, sort_order 22 |
| #118 | Kestra Docker socket | module-1 → module-2, sort_order 23 |

**Rule**: Kestra questions belong in `module-2` (workflow orchestration), not `general` or `module-1`.

---

## 2. Not Relevant for Course (closed)

| PR | Topic | Reason |
|----|-------|--------|
| #123 | Installing vim on Ubuntu | Basic Linux admin, outside course scope |
| #116 | SQL LEFT JOIN returns NULL | Basic SQL concept, not course-specific |

**Rule**: Fundamental tool/SQL concepts that aren't course-specific should be rejected.

---

## 3. Duplicates (closed)

| PR | Issue | Duplicate of |
|----|-------|--------------|
| #114 | Docker localhost/pgnetwork | PR #104 (DE zoomcamp) |
| #99 | Spark Global Temporary Views | PR #100 (DE zoomcamp) |

**Rule**: Check for duplicates across both DE and ML zoomcamp before creating new entries. Same content should not exist in both courses.

---

## 4. Content Merges

| PR | Issue | Action |
|----|-------|--------|
| #110 | Codespaces pgAdmin blank screen | Merged into existing DE zoomcamp FAQ instead of creating separate ML zoomcamp entry |

**Rule**: Enhance existing entries rather than duplicating across courses.

---

## 5. Sort Order Issues (fixed before merge)

| PR | Issue | Fix |
|----|-------|-----|
| #159 | Set sort_order to 1, highest in module-3 is 045 | Changed to 046 |
| #157 | Set sort_order to 46, conflicted with #159 | Changed to 047 |

**Rule**: Always check existing files in target section and use next sequential number.

---

## 6. Code/File Issues (fixed before merge)

| PR | Issue | Fix |
|----|-------|-----|
| #102 | Kafka Python code had no indentation | Fixed proper Python indentation |
| #94 | File corruption (extra closing braces at end) | Removed garbage characters |

---

## 7. Bot Failure - Issue #128

The FAQ bot crashed with:
```
ValueError: invalid literal for int() with base 10: '05727a95dd'
```

**Root cause**: Malformed filename `05727a95dd_homework-and-leaderboard-wha.md` - missing underscore between sort_order and doc_id. Should be `057_27a95dd_...`.

The `find_largest_sort_order()` function in `faq_automation/core.py` doesn't handle malformed filenames robustly.

---

## Implementation Details for Bot Fixes

### Fix 1: Robust Sort Order Parsing (`faq_automation/core.py`)

**Current code (line 134-143)**:
```python
def find_largest_sort_order(section_dir: Path) -> int:
    last = sorted(section_dir.iterdir())[-1]
    sort_order, _ = last.name.split('_', maxsplit=1)
    return int(sort_order) + 1
```

**Fixed code**:
```python
import re

def find_largest_sort_order(section_dir: Path) -> int:
    """
    Find the next available sort order number in a section

    Handles malformed filenames by extracting the numeric prefix only.
    """
    files = list(section_dir.glob('*.md'))
    if not files:
        return 1

    max_order = 0
    for f in files:
        # Extract numeric prefix from filename (e.g., "123_" from "123_abc.md")
        match = re.match(r'^(\d+)', f.name)
        if match:
            order = int(match.group(1))
            max_order = max(max_order, order)

    return max_order + 1
```

---

### Fix 2: Section Placement Rules (`faq_automation/rag_agent.py`)

**Add to SYSTEM_PROMPT** (after line 50):
```python
Section Placement Rules:
- Kestra-related questions (workflows, tasks, outputs, Docker socket) → module-2 (workflow orchestration)
- Docker + Kestra → module-2 (Kestra is the primary topic)
- Docker-only questions (pgAdmin, Postgres, etc.) → module-1
- BigQuery, GCP, data warehousing → module-3
- Kafka, streaming → module-6
- Spark → module-5
- Generic questions that truly don't fit any module → general
```

---

### Fix 3: Relevance Filtering (`faq_automation/rag_agent.py`)

**Add to SYSTEM_PROMPT** (after Section Placement Rules):
```python
Rejection Rules:
- Basic Linux administration (vim installation, package management) → REJECT
- Fundamental SQL concepts (LEFT JOIN behavior, basic syntax) → REJECT
- Generic DevOps best practices (scaling FastAPI, Docker reproducibility) without course-specific context → REJECT
- Content that is general programming documentation rather than course-specific troubleshooting → REJECT
```

---

### Fix 4: Cross-Course Duplicate Check

**New function in `faq_automation/core.py`**:
```python
def check_cross_course_duplicates(question: str, answer: str, course_dirs: List[Path]) -> Optional[dict]:
    """
    Check if similar content exists in other courses

    Returns the first matching document across all courses, or None
    """
    from minsearch import Index

    all_docs = []
    for course_dir in course_dirs:
        all_docs.extend(read_questions(course_dir))

    if not all_docs:
        return None

    # Build combined index
    index = Index(
        text_fields=['section', 'question', 'answer'],
        keyword_fields=['course', 'section_id'],
    )
    index.fit(all_docs)

    # Search for duplicates
    proposal = f"## {question}\n\n{answer}"
    results = index.search(proposal, num_results=3)

    # High similarity threshold for duplicate detection
    if results and results[0].get('score', 0) > 0.85:
        return results[0]

    return None
```

---

### Fix 5: Sort Order When order == -1

**In `faq_automation/actions.py`**, modify `create_new_faq_file()`:
```python
def create_new_faq_file(course_dir: Path, doc_index: dict, faq_decision):
    # ... existing code ...

    # Handle sort_order
    if faq_decision.order == -1:
        sort_order = find_largest_sort_order(section_dir)
    else:
        sort_order = faq_decision.order
        # Validate the requested order doesn't conflict
        existing = section_dir.glob(f"{sort_order:03d}_*.md")
        if list(existing):
            faq_decision.warnings.append(f"Sort order {sort_order} conflicts with existing file")
            sort_order = find_largest_sort_order(section_dir)
```

---

## Recommendations for FAQ Bot

1. **Kestra questions** → `module-2` (workflow orchestration)
2. **Basic Linux/SQL tutorials** → reject as not course-specific
3. **Check for duplicates** across both DE and ML zoomcamp before creating new entries
4. **ML zoomcamp** should only get content that's actually ML-specific; Docker/infrastructure questions belong in DE zoomcamp
5. **Sort order** - always find highest number in target section first (`ls _questions/<course>/<section>/`), use next sequential number
6. **Validate code blocks** - ensure proper indentation for Python and other languages
7. **Check for file corruption** - validate file content doesn't have garbage at the end
