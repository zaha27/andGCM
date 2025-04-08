import subprocess

def show_git_status():
    print("=== Git Status Overview ===\n")

    try:
        result = subprocess.run(["git", "status", "--porcelain"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("❌ Error: This is not a Git repository or Git is not initialized.")
            return

        lines = result.stdout.strip().splitlines()

        if not lines:
            print("✅ Working directory clean. No changes to show.")
            return

        staged = []
        unstaged = []
        untracked = []

        for line in lines:
            code = line[:2]
            file = line[3:]

            if code[0] != " ":
                staged.append(file)
            elif code[1] != " ":
                unstaged.append(file)
            elif code == "??":
                untracked.append(file)

        if staged:
            print("🟢 Staged for commit:")
            for f in staged:
                print(f"   + {f}")
            print("")

        if unstaged:
            print("🟡 Modified but not staged:")
            for f in unstaged:
                print(f"   ~ {f}")
            print("")

        if untracked:
            print("🔴 Untracked files:")
            for f in untracked:
                print(f"   ? {f}")
            print("")

    except Exception as e:
        print(f"❌ Exception while checking git status: {e}")
