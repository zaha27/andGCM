#!/bin/bash

INSTALL_DIR="$HOME/gcm"
SHELL_RC=""

# Detect shell rc file
CURRENT_SHELL=$(basename "$SHELL")
if [[ "$CURRENT_SHELL" == "zsh" ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$CURRENT_SHELL" == "bash" ]]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

echo "[!] This will remove GCM CLI from your system."

read -p "Are you sure you want to uninstall GCM? (y/n): " confirm
if [[ "$confirm" != "y" ]]; then
    echo "❌ Uninstall cancelled."
    exit 0
fi

# Remove install dir
if [[ -d "$INSTALL_DIR" ]]; then
    rm -rf "$INSTALL_DIR"
    echo "[✓] Removed $INSTALL_DIR"
else
    echo "[!] Install directory not found: $INSTALL_DIR"
fi

# Remove PATH line from shell rc
if grep -q 'export PATH="$HOME/gcm:$PATH"' "$SHELL_RC"; then
    sed -i.bak '/export PATH="\$HOME\/gcm:\$PATH"/d' "$SHELL_RC"
    echo "[✓] Removed PATH entry from $SHELL_RC"
    echo "[ℹ️] A backup was created at $SHELL_RC.bak"
else
    echo "[!] No PATH entry found in $SHELL_RC"
fi

# Final message
echo ""
echo "[✅] GCM has been uninstalled."
echo "[➡️] To apply changes, run:"
echo "     source $SHELL_RC"
echo ""
