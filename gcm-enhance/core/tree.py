import subprocess

def generate_commit_tree(limit=10):
    try:
        result = subprocess.run(
            ["git", "log", f"--oneline", f"-n {limit}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode != 0:
            print("❌ Not a Git repository or no commits found.")
            return

        lines = result.stdout.strip().splitlines()
        print("=== Recent Commit Tree ===")
        for i, line in enumerate(lines):
            prefix = "o" if i == 0 else "|"
            print(f"{prefix} {line}")

    except Exception as e:
        print(f"❌ Error generating commit tree: {e}")
