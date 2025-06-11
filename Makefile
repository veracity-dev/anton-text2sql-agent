.PHONY: commit-src commit-utils commit-docs commit-all help

# Default target
help:
	@echo "Available targets:"
	@echo "  commit-src    - Commit changes in src directory"
	@echo "  commit-utils  - Commit changes in utils directory"
	@echo "  commit-docs   - Commit changes in documentation files (README.md, requirements.txt)"
	@echo "  commit-all    - Commit all changes"
	@echo "  help         - Show this help message"

# Commit changes in src directory
commit-src:
	@echo "Committing changes in src directory..."
	git add src/
	git commit -m "feat(src): update source code"

# Commit changes in utils directory
commit-utils:
	@echo "Committing changes in utils directory..."
	git add utils/
	git commit -m "feat(utils): update utility functions"

# Commit changes in documentation files
commit-docs:
	@echo "Committing changes in documentation files..."
	git add README.md requirements.txt
	git commit -m "docs: update documentation and dependencies"

# Commit all changes
commit-all: commit-src commit-utils commit-docs
	@echo "All changes committed successfully" 