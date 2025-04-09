import subprocess

def generate_commit_message_with_ollama(diff_text: str, model: str = "codellama"):
    prompt = f"""You are an expert software engineer.

Your task is to write a short and meaningful Git commit message in imperative mood
(like 'Fix login issue' or 'Add user validation') based ONLY on the staged git diff.

Guidelines:
- Do NOT include file names or code.
- DO write only the purpose of the change.
- Maximum one sentence. Maximum 100 characters.
- Be precise, concise, and professional.

Git diff:
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
