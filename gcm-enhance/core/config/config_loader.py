import json
import os
from pathlib import Path

DEFAULT_CONFIG = {
    "default_style": "conventional",
    "visual_preview": "default",
    "auto_commit": False
}

CONFIG_PATH = Path.home() / ".gcmconfig"

def load_config():
    if CONFIG_PATH.exists():
        try:
            with open(CONFIG_PATH, "r") as f:
                data = json.load(f)
                return {**DEFAULT_CONFIG, **data}
        except json.JSONDecodeError:
            print("⚠️  Invalid .gcmconfig file. Using defaults.")
    return DEFAULT_CONFIG

def save_config(config_dict):
    with open(CONFIG_PATH, "w") as f:
        json.dump(config_dict, f, indent=4)

def update_config_key(key: str, value):
    config = load_config()
    if key not in DEFAULT_CONFIG:
        print(f"❌ Unknown config key: {key}")
        return
    if isinstance(DEFAULT_CONFIG[key], bool):
        value = value.lower() in ("true", "1", "yes", "on")
    config[key] = value
    save_config(config)
    print(f"✅ Updated '{key}' to '{value}' in .gcmconfig")
