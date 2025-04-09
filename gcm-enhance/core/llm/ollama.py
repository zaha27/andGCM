import subprocess

def generate_commit_message_with_ollama(diff_text: str, model: str = "codellama"):
    prompt = f"""You are a senior software engineer.
Generate a concise Git commit message in imperative mood (like 'Fix login bug') based on this diff:

{diff_text}

Commit message:"""

    print("⏳ Asking the model via Ollama...")

    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60  # max 60 sec
        )

        if result.returncode != 0:
            print("❌ Ollama failed.")
            print(result.stderr)
            return None

        return result.stdout.strip().split("\n")[0]

    except subprocess.TimeoutExpired:
        print("⏱️ Ollama took too long to respond. Commit not generated.")
        return None

    except Exception as e:
        print(f"❌ Error using Ollama: {e}")
        return None
