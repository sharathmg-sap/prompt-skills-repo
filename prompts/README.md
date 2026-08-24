# Prompts Directory

This directory contains prompt files used by various agents.

## Organization

### `/system-prompts`
System-level prompts that define agent behavior, capabilities, and constraints.

**Naming Convention**: `[agent-type]-[version].md`

Example files:
- `coding-assistant-v1.md`
- `code-reviewer-v1.md`
- `documentation-writer-v1.md`

### `/task-prompts`
Task-specific prompts for particular operations or workflows.

**Naming Convention**: `[task-name]-[version].md`

Example files:
- `bug-fix-workflow-v1.md`
- `code-review-checklist-v1.md`
- `refactoring-guide-v1.md`

## Prompt Structure

Each prompt file should include:
1. **Title**: Clear description of the prompt's purpose
2. **Version**: Version number for tracking changes
3. **Context**: When and how this prompt should be used
4. **Instructions**: Clear directives for the agent
5. **Examples** (optional): Sample inputs/outputs
6. **Constraints** (optional): Limitations or guidelines

## Usage Tips

- Keep prompts concise and focused
- Use clear formatting with sections
- Include examples when the task is complex
- Version your prompts when making significant changes
- Add comments explaining specific directives

## Related Documentation

See `/templates/prompt-template.md` for a template structure.