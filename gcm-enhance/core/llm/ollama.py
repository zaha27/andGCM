import subprocess

def generate_commit_message_with_ollama(diff_text: str, model: str = "codellama"):
    prompt = f"""Generate a single-line Git commit message in imperative mood 
(like 'Fix crash on login', 'Add logout button') based on the following git diff.

Rules:
- DO NOT include file names, code, or explanations.
- DO NOT return anything else. Just the commit message.
- Maximum ONE LINE.

Git diff:
{diff_text}

Commit:"""

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

        for line in response.splitlines():
            line = line.strip()
            if (
                line
                and len(line) < 120
                and not line.lower().startswith("verse")
                and not line.lower().startswith("you are")
                and "generate" not in line.lower()
            ):
                return line

        return None

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
