# Contributing Guidelines

Thank you for contributing to the prompt-skills-repo! This document outlines how to maintain quality and consistency across the repository.

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Commit with clear messages
5. Push to your fork
6. Open a pull request

## Naming Conventions

### Prompts
- Format: `[purpose]-[version].md`
- Examples: `code-review-v1.md`, `api-documentation-v2.md`

### Skills
- Format: `[domain]-[capability]-[version]`
- Examples: `code-analysis-v1`, `text-generation-v1`

### Scripts
- Format: `[action]-[target].sh` or `.py`
- Examples: `validate-prompts.py`, `setup-env.sh`

## File Format Standards

### Markdown Files
- Use UTF-8 encoding
- 2-space indentation
- Max line length: 100 characters (where possible)
- Consistent heading hierarchy (start with #)
- Include metadata section with version, author, date

### Code Files
- Follow language-specific style guides
- Include docstrings/comments
- Test before committing
- Use meaningful variable names

## Content Guidelines

### Prompts
- Clear, concise instructions
- Specify expected behavior
- Include examples when helpful
- Document any constraints
- Version appropriately

### Skills
- Complete documentation
- Include examples
- Describe dependencies
- Provide error handling guidance
- Add usage instructions

### Scripts
- Executable and tested
- Error handling included
- Clear usage documentation
- Shebang line present
- Comments for complex logic

## Commit Messages

Use clear, descriptive commit messages:
```
Type: Brief description

Optional longer explanation if needed.

- List specific changes
- One per line
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

Examples:
- `feat: Add code-review prompt template`
- `fix: Correct validation logic in skill example`
- `docs: Update prompt naming conventions`

## Pull Request Process

1. **Title**: Descriptive and concise
2. **Description**: Explain what and why
3. **Related Issues**: Reference any related issues
4. **Testing**: Confirm changes work as expected
5. **Documentation**: Update relevant docs

Template:
```markdown
## Description
Brief description of changes

## Changes
- Change 1
- Change 2

## Related Issues
Fixes #123

## Testing
- [ ] Tested locally
- [ ] No breaking changes
```

## Review Process

- At least one review required
- Address feedback constructively
- Keep discussions professional
- Resolve conflicts before merging

## Versioning

Use semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Significant changes, breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, minor improvements

Example progression: `v1.0.0` → `v1.1.0` → `v1.1.1` → `v2.0.0`

## Directory Structure

Keep the repository organized:
```
prompts/
├── system-prompts/
└── task-prompts/

skills/
├── examples/
└── templates/

scripts/
├── setup/
└── utilities/

docs/
templates/
```

## Questions?

- Check existing documentation first
- Open an issue for clarification
- Discuss in pull request comments

Thank you for improving this repository!