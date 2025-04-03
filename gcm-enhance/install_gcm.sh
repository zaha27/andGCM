#!/bin/bash

INSTALL_DIR="$HOME/gcm"
SCRIPT_NAME="gcm"
TARGET_PATH="$INSTALL_DIR/$SCRIPT_NAME"

echo "[+] Creating folder: $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

echo "[+] Copying script to $TARGET_PATH"
cp -r core config gcm "$INSTALL_DIR"
chmod +x "$TARGET_PATH"

# Detect shell config file
if [[ "$SHELL" == *"zsh" ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$SHELL" == *"bash" ]]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

echo "[+] Using shell config file: $SHELL_RC"

# Add to PATH if not already there
if ! grep -Fxq 'export PATH="$HOME/gcm:$PATH"' "$SHELL_RC"; then
    echo "" >> "$SHELL_RC"
    echo "# GCM Enhancer CLI" >> "$SHELL_RC"
    echo 'export PATH="$HOME/gcm:$PATH"' >> "$SHELL_RC"
    echo "[+] Added $INSTALL_DIR to PATH in $SHELL_RC"
else
    echo "[✓] PATH already includes $INSTALL_DIR"
fi

# Reload shell config
echo "[+] Reloading shell config..."
source "$SHELL_RC"

# Check if colorama is installed
python3 -c "import colorama" 2>/dev/null
if [[ $? -ne 0 ]]; then
    echo "[+] Installing Python dependency: colorama"
    python3 -m pip install --user colorama
else
    echo "[✓] Python dependency 'colorama' is already installed."
fi

echo ""
echo "[✅] Installation complete!"
echo "You can now run:"
echo ""
echo "    gcm --smart --auto"
echo ""
