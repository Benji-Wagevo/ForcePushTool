import os
import click
import os
from git import Repo, GitCommandError

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
@click.command()
@click.argument("commit_sha")
@click.argument("branch", default="main")
@click.option(
    "--source-file",
    default=os.path.join(SCRIPT_DIR, "copilot-instructions.md"),
    help="Path to the copilot-instructions.md file to add."
)
def force_push(commit_sha, branch, source_file):
    """
    Reset current repo to COMMIT_SHA (unless dirty), add .github/copilot-instructions.md, commit, and force-push to BRANCH.
    """
    try:
        repo = Repo(os.getcwd())
        git = repo.git

        if repo.is_dirty():
            click.echo("⚠️ Repo has uncommitted changes — skipping reset.")
        else:
            # Safe to reset
            click.echo(f"Resetting to commit {commit_sha}")
            git.reset("--hard", commit_sha)

        # Ensure source markdown file exists
        if not os.path.isfile(source_file):
            raise FileNotFoundError(f"Markdown file '{source_file}' not found.")

        # Ensure .github directory exists
        github_dir = os.path.join(os.getcwd(), ".github")
        os.makedirs(github_dir, exist_ok=True)

        # Copy markdown file to .github/copilot-instructions.md
        dest_path = os.path.join(github_dir, "copilot-instructions.md")
        with open(source_file, "rb") as src, open(dest_path, "wb") as dst:
            dst.write(src.read())

        # Stage and commit
        repo.index.add([dest_path])
        repo.index.commit("Add .github/copilot-instructions.md")

        # Force push to remote
        click.echo(f"Force pushing to origin/{branch}...")
        git.push("origin", f"HEAD:{branch}", force=True)

        click.echo("✅ Force push complete.")

    except GitCommandError as e:
        click.echo(f"❌ Git error: {e}")
    except Exception as e:
        click.echo(f"❌ Error: {e}")

if __name__ == "__main__":
    force_push()
