import subprocess

def generate_commit_message_with_ollama(diff_text: str, model: str = "codellama"):
    prompt = f"""You are a senior software engineer.
Generate a concise, clear Git commit message in imperative mood based on the following git diff:

{diff_text}

Commit message:"""

    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if result.returncode != 0:
            print("❌ Failed to connect to Ollama or run the model.")
            print(result.stderr)
            return None

        return result.stdout.strip()

    except Exception as e:
        print(f"❌ Error using Ollama: {e}")
        return None
