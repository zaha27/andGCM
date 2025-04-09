import subprocess

def generate_commit_message_with_ollama(diff_text: str, model: str = "codellama"):
    prompt = f"""You are an expert software engineer.

Your task is to write a short and meaningful Git commit message in imperative mood
(like 'Fix login issue' or 'Add user validation') based ONLY on the staged git diff.

Guidelines:
- DO NOT include file names or code.
- DO NOT explain the change, just summarize it as a title.
- Only return the commit message. No introduction, no formatting.
- ONE line only. MAX 100 characters.

Git diff:
{diff_text}

Return only the commit message below:"""

    print("⏳ Asking the model via Ollama...")

    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )

        if result.returncode != 0:
            print("❌ Ollama failed.")
            print(result.stderr)
            return None

        response = result.stdout.strip()
        return response.splitlines()[0] if response else None

    except subprocess.TimeoutExpired:
        print("⏱️ Ollama took too long to respond. Commit not generated.")
        return None

    except Exception as e:
        print(f"❌ Error using Ollama: {e}")
        return None


def is_ollama_running():
    try:
        result = subprocess.run(
            ["ollama", "list"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.returncode == 0
    except Exception:
        return False
