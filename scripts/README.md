# Scripts Directory

Utility scripts and automation tools for managing prompts and skills.

## Organization

### `/setup`
Initialization and configuration scripts.

Examples:
- `init-repo.sh` - Initial repository setup
- `setup-env.sh` - Environment configuration

### `/utilities`
Helper scripts for common tasks.

Examples:
- `validate-prompts.py` - Validate prompt files
- `generate-index.py` - Generate index of all resources
- `format-check.sh` - Check formatting compliance

## Script Guidelines

1. **Documentation**: Every script should have a clear header comment
2. **Shebang**: Use appropriate shebang (`#!/bin/bash`, `#!/usr/bin/env python3`)
3. **Error Handling**: Include proper error checking
4. **Usage**: Provide usage instructions
5. **Dependencies**: List required dependencies

## Example Script Template

```bash
#!/bin/bash
# 
# Script Name: script-name.sh
# Description: What this script does
# Usage: ./script-name.sh [options]
# Dependencies: List any required tools/packages
#

set -e  # Exit on error

# Script logic here
```

## Running Scripts

Make scripts executable:
```bash
chmod +x scripts/utilities/script-name.sh
```

Run scripts from repository root:
```bash
./scripts/utilities/script-name.sh
```

## Contributing Scripts

When adding new scripts:
1. Follow the template structure
2. Test thoroughly
3. Add documentation
4. Include error handling
5. Update this README