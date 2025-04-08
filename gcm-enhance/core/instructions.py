from typing import Dict
from colorama import Fore, Style, init # type: ignore

init(autoreset=True)

def print_commit_preview(message: str, summaries: Dict[str, str]):
    print("\n" + "=" * 50)
    print(f"{Fore.CYAN}{Style.BRIGHT}🔍 Suggested commit:")
    print(f"{Fore.GREEN}{message}")
    print("=" * 50)

    if summaries:
        print(f"\n{Fore.CYAN}{Style.BRIGHT}📁 Modified files summary:\n")
        for file, summary in summaries.items():
            print(f"{Fore.YELLOW}- {file}: {Fore.WHITE}{summary}")
    else:
        print(f"{Fore.LIGHTBLACK_EX}(No modified files detected.)")

    print("\n" + "=" * 50 + "\n")

def render_preview(message: str, summaries: Dict[str, str], style: str = "default"):
    if style == "minimal":
        print(f"\n{Fore.GREEN}✅ Commit: {message}\n")
        return
    elif style == "markdown":
        print("\n### Suggested Commit\n")
        print(f"`{message}`\n")
        if summaries:
            print("**Modified Files:**")
            for f, s in summaries.items():
                print(f"- `{f}`: _{s}_")
        return
    elif style == "boxed":
        border = "+" + "-" * (len(message) + 4) + "+"
        print("\n" + border)
        print(f"|  {Fore.GREEN}{message}{Style.RESET_ALL}  |")
        print(border + "\n")
        return
    print_commit_preview(message, summaries)