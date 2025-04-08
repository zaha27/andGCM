def launch_instruction_menu():
    print("=== GCM Advanced Menu ===")
    print("1. [ View the tree history ]")
    print("2. [ Show help menu ]")
    print("3. [ Git Status Overview ]")
    print("4. [ Reserved for future ]")
    print("5. [ Reserved for future ]")
    print("===========================")

    choice = input("Select an option (1–5): ").strip()

    if choice == "1":
        from core.tree import generate_commit_tree
        generate_commit_tree()
    elif choice == "2":
        from core.help import show_help_menu
        show_help_menu()
    elif choice == "3":
        from core.status import show_git_status
        show_git_status()
    elif choice == "4":
        print("Option 4 selected – feature coming soon.")
    elif choice == "5":
        print("Option 5 selected – feature coming soon.")
    else:
        print("❌ Invalid option. Please enter a number between 1 and 5.")
