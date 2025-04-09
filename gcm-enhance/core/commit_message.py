import subprocess
from config.config_loader import load_config
from core.diff_parser import analyze_diff
from core.formatter import render_preview

def main_gcm():
    # Check for staged changes
    diff = subprocess.run(["git", "diff", "--cached"], stdout=subprocess.PIPE, text=True).stdout
    if not diff.strip():
        print("⚠️  No staged changes detected. Use 'git add' before running gcm.")
        return

    config = load_config()
    style = config.get("default_style", "conventional")
    visual = config.get("visual_preview", "default")
    auto = config.get("auto_commit", False)

    message, summaries, commit_type = analyze_diff(style=style)
    render_preview(message, summaries, style=visual)

    if auto:
        subprocess.run(["git", "commit", "-m", message])
        print("✅ Auto-commit completed.")
    else:
        choice = input("Do you want to commit this? (y/n): ").strip().lower()
        if choice == "y":
            subprocess.run(["git", "commit", "-m", message])
            print("✅ Commit completed.")
        else:
            print("❌ Commit canceled.")
