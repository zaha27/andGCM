import subprocess
from config.config_loader import load_config  # type: ignore
from core.llm.ollama import generate_commit_message_with_ollama, is_ollama_running

def main_gcm():
    if not is_ollama_running():
        print("❌ Ollama daemon is not running.")
        print("💡 Tip: run 'open -a Ollama' or 'ollama serve' to start it.")
        return

    config = load_config()

    if config.get("auto_git_add", False):
        print("📦 Running 'git add .' automatically...")
        subprocess.run(["git", "add", "."], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    diff = subprocess.run(["git", "diff", "--cached"], stdout=subprocess.PIPE, text=True).stdout

    if not diff.strip():
        print("⚠️  No staged changes detected. Use 'git add' before running gcm.")
        return

    model = config.get("llm_model", "codellama")
    print(f"🤖 Generating commit message using model: {model}...\n")

    message = generate_commit_message_with_ollama(diff, model=model)

    if not message:
        print("❌ Commit message generation failed.")
        return

    print("🔍 Suggested commit message:")
    print(f"\"{message}\"\n")

    if config.get("auto_commit", False):
        subprocess.run(["git", "commit", "-m", message])
        print("✅ Auto-commit completed.")
    else:
        choice = input("Do you want to use this message? (y/n): ").strip().lower()
        if choice == "y":
            subprocess.run(["git", "commit", "-m", message])
            print("✅ Commit created.")
        else:
            print("❌ Commit cancelled.")
