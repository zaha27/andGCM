#!/bin/bash

INSTALL_DIR="$HOME/gcm"
TARGET_PATH="$INSTALL_DIR/gcm"

echo "[+] Creating install directory at $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

echo "[+] Copying CLI files..."
cp -r gcm core config "$INSTALL_DIR"
chmod +x "$TARGET_PATH"

# Detect user's shell and choose RC file
CURRENT_SHELL=$(basename "$SHELL")
if [[ "$CURRENT_SHELL" == "zsh" ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$CURRENT_SHELL" == "bash" ]]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

echo "[+] Using shell config file: $SHELL_RC"

# Add to PATH if not already added
if ! grep -q 'export PATH="$HOME/gcm:$PATH"' "$SHELL_RC"; then
    echo "" >> "$SHELL_RC"
    echo "# GCM Enhance CLI" >> "$SHELL_RC"
    echo 'export PATH="$HOME/gcm:$PATH"' >> "$SHELL_RC"
    echo "[+] Added GCM to PATH in $SHELL_RC"
else
    echo "[✓] PATH already contains GCM"
fi

# Spinner animation function
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

# Install Python dependency: colorama
python3 -c "import colorama" 2>/dev/null
if [[ $? -ne 0 ]]; then
    echo "[+] Installing Python dependency: colorama"
    python3 -m pip install --user colorama &> /dev/null &
    spinner $!
else
    echo "[✓] 'colorama' is already installed"
fi

# Final instructions
echo ""
echo "[✅] Installation complete!"
echo ""
echo "[➡️] To finalize setup, run this in your terminal:"
echo ""
echo "     source $SHELL_RC"
echo ""
echo "[🧪] Then test GCM with:"
echo ""
echo "     gcm --smart"
echo ""
echo "[💡] Tip: personalize with:"
echo "     gcm --set default_style corporate"
echo ""
