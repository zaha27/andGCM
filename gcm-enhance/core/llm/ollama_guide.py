def print_ollama_install_guide():
    print("=== Ollama Installation Guide ===\n")

    print("▶️ Option 1: Using Homebrew (macOS only)")
    print("1. Open Terminal")
    print("2. Run the following command:")
    print("   brew install ollama")
    print("3. After installation, start the Ollama service:")
    print("   brew services start ollama")
    print("4. Optionally, run it manually once:")
    print("   open -a Ollama\n")

    print("▶️ Option 2: Manual Installation")
    print("1. Go to https://ollama.com/download")
    print("2. Download the installer for your OS (macOS, Windows, or Linux)")
    print("3. Follow the installation instructions")
    print("4. After installation, make sure `ollama` is available in your terminal")
    print("5. Start the server if needed:")
    print("   ollama serve\n")

    print("✅ Once installed and running, you can test it with:")
    print("   ollama list\n")

    print("💡 Tip: If you use a firewall or VPN, ensure localhost access is allowed.\n")
    print("===========================================")
