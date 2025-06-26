# ForcePushTool

A Python CLI tool that automates the process of adding GitHub Copilot instructions to repositories.
This tool resets a repository to a specific commit, adds copilot instructions, and force pushes the changes.

## What It Does

ForcePushTool performs the following operations:

1. Resets the current repository to a specified commit SHA (only if the working directory is clean)
2. Copies a `copilot-instructions.md` file to `.github/copilot-instructions.md` in the target repository
3. Commits the changes with the message "Add .github/copilot-instructions.md"
4. Force pushes the changes to the specified branch

## Installation

### Requirements

- Python 3.6+
- Git installed and configured

### Dependencies

Install the required Python packages using the provided requirements file:

    pip install -r requirements.txt

Or install manually:

    pip install click GitPython

## Usage

### Basic Usage

    python force_push.py <commit_sha> [branch]

### Arguments

- `commit_sha` (required): The commit SHA to reset to
- `branch` (optional): The target branch name (defaults to "main")

### Options

- `--source-file`: Path to the copilot-instructions.md file to add (defaults to `./copilot-instructions.md`)

### Examples

Reset to a specific commit and push to main branch:

    python force_push.py abc123def456

Reset to a commit and push to a different branch:

    python force_push.py abc123def456 feature-branch

Use a different source file:

    python force_push.py abc123def456 main --source-file /path/to/my-instructions.md

### Help

Get help and see all available options:

    python force_push.py --help

## Safety Features

- **Dirty Repository Check**: The tool will skip the reset operation if there are uncommitted changes in the working directory
- **File Validation**: Ensures the source copilot-instructions.md file exists before proceeding
- **Error Handling**: Provides clear error messages for Git operations and file system issues

## Warning

⚠️ **CAUTION**: This tool performs a **force push** operation, which can overwrite remote repository history.
Only use this tool when you understand the implications and have proper backups.

## How It Works

1. **Repository State Check**: Verifies if the current directory is a Git repository and checks for uncommitted changes
2. **Reset Operation**: If the repository is clean, performs a hard reset to the specified commit
3. **File Operations**: Creates the `.github` directory if it doesn't exist and copies the copilot instructions file
4. **Git Operations**: Stages the new file, commits it, and force pushes to the specified branch

## Use Cases

This tool is designed for scenarios where you need to:

- Add standardized GitHub Copilot instructions to multiple repositories
- Ensure consistent copilot configuration across projects
- Automate the deployment of copilot instructions to existing repositories

## Error Handling

The tool handles common error scenarios:

- Missing source file
- Git command failures
- Repository access issues
- Network connectivity problems during push operations

All errors are reported with descriptive messages using emoji indicators:
- ✅ Success operations
- ⚠️ Warning conditions
- ❌ Error situations

## File Structure

    ForcePushTool/
    ├── force_push.py              # Main CLI script
    ├── copilot-instructions.md    # Default copilot instructions
    ├── requirements.txt           # Python dependencies
    └── README.md                  # This documentation

## Contributing

When contributing to this project, please follow the guidelines in `copilot-instructions.md` for code style and documentation standards.

## License

This project follows standard open source practices.
Check with the repository owner for specific license information.