#!/bin/bash

INSTALL_DIR="$HOME/gcm"
TARGET_PATH="$INSTALL_DIR/gcm"

echo "[+] Creating install directory at $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

echo "[+] Copying CLI files..."
cp -r gcm core config "$INSTALL_DIR"
chmod +x "$TARGET_PATH"

# Detect shell
CURRENT_SHELL=$(basename "$SHELL")
if [[ "$CURRENT_SHELL" == "zsh" ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$CURRENT_SHELL" == "bash" ]]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

echo "[+] Using shell config file: $SHELL_RC"

# Add to PATH if needed
if ! grep -q 'export PATH="$HOME/gcm:$PATH"' "$SHELL_RC"; then
    echo "" >> "$SHELL_RC"
    echo "# GCM Enhance CLI" >> "$SHELL_RC"
    echo 'export PATH="$HOME/gcm:$PATH"' >> "$SHELL_RC"
    echo "[+] Added GCM to PATH in $SHELL_RC"
else
    echo "[✓] PATH already contains GCM"
fi

# Spinner animation
spinner() {
    local pid=$1
    local delay=0.1
    local spinstr='|/-\\'
    echo -n "     "
    while ps -p "$pid" > /dev/null 2>&1; do
        local temp=${spinstr#?}
        printf " [%c]  Installing colorama..." "$spinstr"
        spinstr=$temp${spinstr%"$temp"}
        sleep $delay
        printf "\r"
    done
    echo " [✓]  Colorama installed!"
}

# Install colorama
python3 -c "import colorama" 2>/dev/null
if [[ $? -ne 0 ]]; then
    echo "[+] Installing Python dependency: colorama"
    python3 -m pip install --user colorama &> /dev/null &
    spinner $!
else
    echo "[✓] 'colorama' is already installed"
fi

# Ollama check
echo ""
echo "[🤖] Checking for Ollama..."

if ! command -v ollama &> /dev/null; then
    echo "[!] Ollama is not installed."

    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "[+] Attempting to install Ollama using Homebrew..."
        if command -v brew &> /dev/null; then
            brew install ollama
            echo "[✓] Ollama installed. You must run it once: open -a Ollama"
        else
            echo "[❌] Homebrew not found. Please install Ollama manually from https://ollama.com"
        fi
    else
        echo "[❌] Automatic install not supported on this OS. Please install manually from: https://ollama.com"
    fi
else
    echo "[✓] Ollama is already installed."

    echo "[📦] Checking for codellama model..."
    ollama list | grep -q codellama
    if [[ $? -ne 0 ]]; then
        echo "[+] Downloading codellama model..."
        ollama pull codellama
    else
        echo "[✓] codellama model already available."
    fi
fi

# Done
echo ""
echo "[✅] GCM installation complete!"
echo ""
echo "[➡️] Run this command to finalize setup:"
echo "     source $SHELL_RC"
echo ""
echo "[🚀] Then launch with:"
echo "     gcm           # run commit generator"
echo "     gcm -config   # open configuration"
echo "     gcm -a        # advanced tools"
echo ""
