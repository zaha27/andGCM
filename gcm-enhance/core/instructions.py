def launch_instruction_menu():
    print("=== GCM Advanced Menu ===")
    print("1. [ View the tree history]")
    print("2. [ Reserved for future ]")
    print("3. [ Reserved for future ]")
    print("4. [ Reserved for future ]")
    print("5. [ Reserved for future ]")
    print("==========================")

    choice = input("Select an option (1-5): ").strip()

    if choice == "1":
        from core.tree import generate_commit_tree
        generate_commit_tree()
    elif choice == "2":
        print("a")
    elif choice == "3":
        print("a")
    else:
        print("❌ Invalid option. Please enter a number between 1 and 5.")
