import subprocess
from collections import defaultdict
from core.styles import apply_style

COMMIT_KEYWORDS = {
    "fix": ["error", "exception", "fail", "raise", "bug", "catch"],
    "feat": ["add", "create", "implement", "new", "introduce", "feature"],
    "refactor": ["optimize", "cleanup", "restructure", "refactor"],
    "chore": ["config", "settings", "env", "setup", "deps", "build"]
}

CONTEXT_TAGS = {
    "auth": ["login", "logout", "session", "auth", "token"],
    "ui": ["render", "button", "page", "form", "input"],
    "db": ["query", "insert", "delete", "update", "select", "database"],
    "api": ["http", "request", "response", "fetch", "endpoint"]
}

def get_staged_diff():
    result = subprocess.run(['git', 'diff', '--cached'], stdout=subprocess.PIPE, text=True)
    return result.stdout

def parse_diff_by_file(diff_text):
    file_changes = defaultdict(list)
    current_file = None

    for line in diff_text.splitlines():
        if line.startswith("+++ b/"):
            current_file = line[6:]
        elif line.startswith('+') and not line.startswith('+++'):
            if current_file:
                file_changes[current_file].append(line[1:].strip())

    file_summaries = {}
    commit_type_counter = defaultdict(int)

    for file, lines in file_changes.items():
        tag_count = defaultdict(int)
        for line in lines:
            lowered = line.lower()
            for ctype, keywords in COMMIT_KEYWORDS.items():
                if any(kw in lowered for kw in keywords):
                    commit_type_counter[ctype] += 1
            for tag, keywords in CONTEXT_TAGS.items():
                if any(kw in lowered for kw in keywords):
                    tag_count[tag] += 1

        sorted_tags = sorted(tag_count.items(), key=lambda x: x[1], reverse=True)
        top_tags = [tag for tag, _ in sorted_tags[:2]]
        summary = " and ".join(top_tags) if top_tags else "general changes"
        file_summaries[file] = summary

    final_type = "feat"
    if commit_type_counter:
        final_type = max(commit_type_counter, key=commit_type_counter.get)

    return final_type, file_summaries

def analyze_diff(style="conventional"):
    diff_text = get_staged_diff()
    commit_type, summaries = parse_diff_by_file(diff_text)
    unique_summaries = list(set(summaries.values()))
    summary_title = " and ".join(unique_summaries[:2]) if unique_summaries else "code"
    message = apply_style(commit_type, summary_title, style=style)
    return message, summaries, commit_type