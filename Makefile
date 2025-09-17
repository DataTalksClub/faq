.PHONY: extract website clean clean_questions validate help

# Default target
help:
	@echo "Available targets:"
	@echo "  extract        - Extract FAQ data from Google Docs and generate markdown files"
	@echo "  website        - Generate static website from markdown files"
	@echo "  clean_questions - Remove all files in _questions directory before extraction"
	@echo "  validate       - Validate all question files are compatible with generate.py"
	@echo "  clean          - Remove generated files"
	@echo "  help           - Show this help message"

# Clean questions directory before extraction
clean_questions:
	python clean_questions.py

# Extract FAQ data from Google Docs (with cleanup)
extract: clean_questions
	python faq_processor.py

# Validate question files
validate:
	python validate_questions.py

# Generate static website
website:
	python generate.py