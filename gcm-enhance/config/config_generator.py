import json
from config.config_loader import save_config # type: ignore

def launch_config_menu():
    print("=== GCM Config Menu ===")

    style = input("Preferred style (conventional/corporate/fun): ").strip()
    auto_commit = input("Enable auto-commit? (yes/no): ").strip().lower()
    visual_preview = input("Preview style (default/markdown/minimal/boxed): ").strip()
    llm_model = input("LLM model (codellama/mistral/tinyllama): ").strip()
    auto_add = input("Enable auto git add? (yes/no): ").strip().lower()

    config = {
        "default_style": style,
        "auto_commit": auto_commit in ["yes", "true", "1"],
        "visual_preview": visual_preview,
        "llm_model": llm_model,
        "auto_git_add": auto_add in ["yes", "true", "1"]

    }

    save_config(config)
    print("[✓] Config saved to ~/.gcmconfig")
