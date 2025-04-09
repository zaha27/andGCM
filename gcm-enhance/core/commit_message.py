import subprocess
from core.llm.ollama import generate_commit_message_with_ollama

def main_gcm():
    diff = subprocess.run(["git", "diff", "--cached"], stdout=subprocess.PIPE, text=True).stdout
    if not diff.strip():
        print("⚠️  No staged changes detected. Use 'git add' before running gcm.")
        return

    print("🤖 Generating commit message with Ollama...")

    message = generate_commit_message_with_ollama(diff)

    if not message:
        print("❌ Failed to generate commit message with Ollama.")
        return

    print("\n🔍 Suggested commit message:")
    print(f"\"{message}\"\n")

    confirm = input("Do you want to use this commit message? (y/n): ").strip().lower()
    if confirm == "y":
        subprocess.run(["git", "commit", "-m", message])
        print("✅ Commit created.")
    else:
        print("❌ Commit cancelled.")
