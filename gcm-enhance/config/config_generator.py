def launch_config_menu():
    print("=== GCM Config Menu ===")
    style = input("Preferred style (formal/fun/minimal): ")
    auto_commit = input("Enable auto-commit? (yes/no): ")

    config = {
        "style": style,
        "auto_commit": auto_commit.lower() in ["yes", "true", "1"]
    }

    import json
    with open("config/config.json", "w") as f:
        json.dump(config, f, indent=4)

    print("[✓] Config saved to config/config.json")
