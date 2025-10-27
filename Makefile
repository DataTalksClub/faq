.PHONY: faq website test test-unit test-int test-fast help

website:
	uv run python generate_website.py

test-unit:
	@echo "🔬 Running unit tests..."
	uv run pytest tests/unit/ -v

test-int:
	@echo "🔄 Running integration tests..."
	uv run pytest tests/integration/ -v

test:
	@echo "🧪 Running all tests..."
	uv run pytest tests/ -v
