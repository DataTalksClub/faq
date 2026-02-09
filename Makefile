.PHONY: website test test-website test-faq-automation help

website:
	@echo "🌐 Generating website..."
	cd website && uv run python generate_website.py

test-website:
	@echo "🌐 Running website tests..."
	cd website && uv run pytest tests/ tests_integration/ -v

test-faq-automation:
	@echo "🤖 Running FAQ automation tests..."
	cd faq_automation && uv run pytest tests/ tests_integration/ -v

test:
	@echo "🧪 Running all tests..."
	$(MAKE) test-website
	$(MAKE) test-faq-automation

help:
	@echo "Available targets:"
	@echo "  make website         - Generate the website"
	@echo "  make test-website    - Run website tests"
	@echo "  make test-faq-automation - Run FAQ automation tests"
	@echo "  make test            - Run all tests"
