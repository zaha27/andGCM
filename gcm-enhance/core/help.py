def show_help_menu():
    print("=== GCM Help Menu ===")
    print("1. Show Git Help")
    print("2. Show GCM Help")
    print("=======================")

    choice = input("Select an option (1–2): ").strip()

    if choice == "1":
        from core.help_menu.help_git import show_git_commands
        show_git_commands()
    elif choice == "2":
        from core.help_menu.help_gcm import show_gcm_help
        show_gcm_help()
    else:
        print("❌ Invalid option. Please enter 1 or 2.")
