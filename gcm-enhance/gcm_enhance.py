#!/usr/bin/env python3

import argparse
import subprocess

def get_git_diff():
    result = subprocess.run(['git', 'diff', '--cached'], stdout=subprocess.PIPE, text=True)
    return result.stdout

def parse_diff(diff_text):
    summary_keywords = set()
    added_lines = []
    for line in diff_text.splitlines():
        if line.startswith('+') and not line.startswith('+++'):
            added_lines.append(line[1:].strip())

    if not added_lines:
        return "chore: update code"

    context_words = {
        "auth": ["login", "logout", "session", "token", "auth"],
        "error": ["exception", "try", "catch", "error", "fail", "raise"],
        "ui": ["button", "click", "page", "render", "input", "form"],
        "db": ["query", "insert", "delete", "update", "select", "db", "database"],
        "api": ["fetch", "request", "response", "endpoint", "api", "http"],
        "logic": ["if", "else", "while", "loop", "calc", "validate"],
        "config": ["config", "settings", "env", "parameter"]
    }

    detected_tags = []

    for line in added_lines:
        for tag, keywords in context_words.items():
            if any(word in line.lower() for word in keywords):
                detected_tags.append(tag)
                summary_keywords.update([word for word in keywords if word in line.lower()])

    detected_tags = list(set(detected_tags))
    commit_type = detected_tags[0] if detected_tags else "feat"
    summary = ", ".join(sorted(summary_keywords)) if summary_keywords else "code"

    return f"{commit_type}: update {summary} logic"

def main():
    parser = argparse.ArgumentParser(description="Smart Git Commit Enhancer")
    parser.add_argument("--smart", action="store_true", help="Enable smart diff-based analysis")
    parser.add_argument("--auto-commit", action="store_true", help="Automatically commit with enhanced message")
    args = parser.parse_args()

    if args.smart:
        diff = get_git_diff()
        message = parse_diff(diff)
        print(f"Generated commit message: {message}")
        if args.auto_commit:
            subprocess.run(['git', 'commit', '-m', message])
    else:
        print("Use --smart to generate message from staged changes.")

if __name__ == "__main__":
    main()
