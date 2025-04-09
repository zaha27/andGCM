import subprocess

def generate_commit_message_with_ollama(diff_text: str, model: str = "codellama"):
    prompt = f"""You are an expert software engineer.

Generate a short and meaningful Git commit message in imperative mood
(e.g., 'Fix login bug', 'Add user validation', 'Update API endpoint') based ONLY on this git diff.

Rules:
- Do NOT include filenames, code, or explanations.
- ONLY return the message.
- ONE LINE. Max 100 characters.
- Do NOT return this prompt or repeat anything from it.

Git diff:
{diff_text}

--- Commit message starts below this line ---
"""


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
