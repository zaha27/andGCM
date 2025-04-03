#!/bin/bash

INSTALL_DIR="$HOME/gcm"
SCRIPT_NAME="gcm"
TARGET_PATH="$INSTALL_DIR/$SCRIPT_NAME"

echo "[+] Creăm folderul $INSTALL_DIR..."
mkdir -p "$INSTALL_DIR"

echo "[+] Copiem scriptul..."
cp gcm "$TARGET_PATH"
chmod +x "$TARGET_PATH"

if [[ "$SHELL" == *"zsh" ]]; then
    SHELL_RC="$HOME/.zshrc"
elif [[ "$SHELL" == *"bash" ]]; then
    SHELL_RC="$HOME/.bashrc"
else
    SHELL_RC="$HOME/.profile"
fi

echo "[+] Detectat shell config: $SHELL_RC"

if grep -Fxq "export PATH=\"\$HOME/gcm:\$PATH\"" "$SHELL_RC"; then
    echo "[✓] PATH deja setat în $SHELL_RC"
else
    echo "" >> "$SHELL_RC"
    echo "# GCM Enhancer tool" >> "$SHELL_RC"
    echo "export PATH=\"\$HOME/gcm:\$PATH\"" >> "$SHELL_RC"
    echo "[+] Am adăugat $INSTALL_DIR în PATH în $SHELL_RC"
fi

echo ""
echo "[ℹ️] Rulează comanda asta pentru a activa imediat:"
echo "     source $SHELL_RC"
echo ""
echo "[✓] După aceea, poți folosi:"
echo "     gcm --smart --auto"
