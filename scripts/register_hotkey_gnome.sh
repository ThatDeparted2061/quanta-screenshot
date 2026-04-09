#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_SCRIPT="$ROOT_DIR/scripts/run_once.sh"

KEYBIND_PATH="/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/"

gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "['${KEYBIND_PATH}']"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:${KEYBIND_PATH} name 'Quiz Assistant'
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:${KEYBIND_PATH} command "bash $RUN_SCRIPT"
gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:${KEYBIND_PATH} binding '<Ctrl><Shift>x'

echo "[+] Registered hotkey Ctrl+Shift+X for Quiz Assistant"
