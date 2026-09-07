# Prompt Skills Repo

A centralized repository for managing agent prompts, skills, and supporting resources used across multiple agents.

## 📁 Repository Structure

```
prompt-skills-repo/
├── README.md
├── .gitignore
├── prompts/
│   ├── README.md
│   ├── system-prompts/
│   └── task-prompts/
├── skills/
│   ├── README.md
│   ├── examples/
│   └── templates/
├── scripts/
│   ├── README.md
│   ├── setup/
│   └── utilities/
├── docs/
│   ├── README.md
│   ├── CONTRIBUTING.md
│   └── ARCHITECTURE.md
└── templates/
    ├── prompt-template.md
    └── skill-template.md
```

## 📚 Directories

### `/prompts`
Stores various prompt files organized by type:
- **system-prompts/**: Base system prompts for different agent roles
- **task-prompts/**: Task-specific prompts and instructions

### `/skills`
Ability definitions and skill implementations:
- **examples/**: Example skills and their implementations
- **templates/**: Reusable skill templates

### `/agents`
Reusable agent role prompts, including [the GitHub MCP Demonstrator](agents/github_mcp_demonstrator.md).

### `/scripts`
Utility scripts and automation tools:
- **setup/**: Initial setup and configuration scripts
- **utilities/**: Helper scripts for processing and managing resources

### `/docs`
Documentation and guides:
- **CONTRIBUTING.md**: Guidelines for contributing
- **ARCHITECTURE.md**: Overview of the repo architecture

### `/templates`
Template files for creating new prompts and skills

## 🚀 Quick Start

1. Clone the repository
   ```bash
   git clone https://github.com/sharathmg-sap/prompt-skills-repo.git
   cd prompt-skills-repo
   ```

2. Explore the structure
   ```bash
   ls -la
   ```

3. Create a new prompt or skill using the templates in `/templates`

## 📝 Usage

### Adding a New Prompt
1. Navigate to the appropriate subdirectory in `/prompts`
2. Create a new file using the template from `/templates/prompt-template.md`
3. Follow the naming convention: `[purpose]-[version].md`

### Adding a New Skill
1. Navigate to `/skills`
2. Create a new directory for your skill
3. Use the template from `/templates/skill-template.md`
4. Include documentation and examples

## 🔄 Integration with Agents

These resources are designed to be:
- **Modular**: Use individual prompts and skills independently
- **Reusable**: Share across multiple agent implementations
- **Maintainable**: Centralized management reduces duplication
- **Versioned**: Track changes and maintain backward compatibility

## 📖 Documentation

- [Contributing Guidelines](docs/CONTRIBUTING.md)
- [Architecture Overview](docs/ARCHITECTURE.md)
- [GitHub MCP usage guide](docs/github-mcp-usage.md)
- [Prompt Guide](prompts/README.md)
- [Skills Guide](skills/README.md)
- [Scripts Guide](scripts/README.md)

## 📄 License

MIT License - feel free to use and modify as needed.

## 👤 Author

Created and maintained by sharathmg-sap

---

For more information and detailed guides, see the documentation in the `/docs` directory.