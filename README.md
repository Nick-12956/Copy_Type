# Copy_Type — Clipboard & Auto-Type Utility

A small Python utility that pastes (auto-types) text where a normal paste operation is not available or is blocked. It can type the current clipboard contents, OCR text from an image, or the text currently selected/highlighted — useful in secure fields, remote desktops, virtual machines, or web forms that block Ctrl+V.

## Download
- Available in "Releases" tab (only for Windows OS).
- The .exe file present in unpacked ZIP file in recent release.

## Features
- Auto-type recent clipboard contents with configurable speed and modes (normal / coding).
- OCR from image files and auto-type the extracted text.
- Capture currently selected text (Ctrl/Cmd+C) and type it automatically.
- Global `Esc` to stop the program immediately.

## When to use
- Web pages or secure input fields that block pasting.
- Remote desktops, VMs, or terminal sessions where clipboard paste is unavailable.
- Demonstrations, typing automation for repetitive text entry, or accessibility workflows.

## Prerequisites
- Python 3.8+
- The script depends on these Python packages: `pyperclip`, `keyboard`, `easyocr`, and their dependencies.

Recommended install (Windows / PowerShell):
```powershell
python -m pip install --upgrade pip
pip install pyperclip keyboard easyocr
```

Note: `easyocr` usually requires PyTorch and may install heavy binaries. If you only need clipboard or selection typing, you can skip installing `easyocr`.

## Usage
1. Open a terminal in the folder containing `Copy_Type.py`.
2. Run:
```powershell
python Copy_Type.py
```
3. Follow the interactive prompts:
- Enter `1` to auto-type the recent clipboard text. Choose a typing speed (1–10). Modes:
  - Normal: types text as-is.
  - Coding: preserves line structure and sends Enter/Home between lines.
- Enter `2` to extract text from an image (image must be in the script folder). Enter the image filename when prompted.
- Enter `3` to capture currently selected text (you get 5 seconds to select/highlight), then the program restores clipboard and types the captured selection.

Important: The program emulates keyboard input — focus the target window before the 5-second countdown ends so the typed text lands in the right place.

Press `Esc` at any time to stop the program.

## Security & Permissions
- The `keyboard` library may require running the terminal as Administrator on Windows to capture/send global key events. If the script cannot send keystrokes, try running the shell as Administrator.
- The script reads and (briefly) uses the system clipboard. It does not transmit clipboard data anywhere.

## Troubleshooting
- If OCR (`easyocr`) fails to install, see EasyOCR documentation or install PyTorch separately (CPU builds are available).
- If clipboard capture or emulated typing doesn't work, ensure no other clipboard manager or security software is blocking access and try running with elevated privileges.

## Contributing
- Small fixes, better error handling, or an optional `pytesseract` OCR fallback are welcome. Open a PR with a short description.

---
File: `Copy_Type.py` — interactive auto-type helper located in this folder.
