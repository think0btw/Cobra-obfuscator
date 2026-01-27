<h1 align="center">Cobra-obfuscator 🐍</h1>

## Preview
<p align="center">
  <img width="568" height="328" alt="2026-01-24_12-29" src="https://github.com/user-attachments/assets/4e51cb0f-4903-49c1-b3c7-41457c967682" />
</p>

![License](https://img.shields.io/badge/license-MIT-green?logo=open-source-initiative&logoColor=white)
![Python](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)
![CLI Tool](https://img.shields.io/badge/interface-CLI-informational?logo=terminal&logoColor=white)
![Maintained](https://img.shields.io/badge/status-maintained-brightgreen)
![Educational](https://img.shields.io/badge/purpose-educational-blue)
![Linux](https://img.shields.io/badge/os-linux-FCC624?logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/os-windows-0078D6?logo=windows&logoColor=white)
![Cross Platform](https://img.shields.io/badge/platform-cross--platform-lightgrey)
![Obfuscation](https://img.shields.io/badge/focus-code%20obfuscation-purple)
![AST](https://img.shields.io/badge/AST-transformations-orange)
![Crypto](https://img.shields.io/badge/crypto-AES%20runtime-black)
![Nuitka](https://img.shields.io/badge/nuitka-compatible-blueviolet)


## 📖 About
Cobra-Obfuscator makes your Python code unreadable while keeping it functional. Perfect for protecting your intellectual property when distributing software.
✨ Features

🔤 Rename identifiers - Variables, functions, classes
🔐 Encrypt strings - AES encryption for all strings
🔀 Transform AST - Restructure code syntax tree
🎲 Dead code injection - Add fake code to confuse analysis

## Shéma 📜
┌──────────────────────────────────────────────────┐
│          YOUR PYTHON SOURCE CODE                 │
│              script.py                           │
└─────────────────┬────────────────────────────────┘
                  │
                  ▼
         ┌────────────────┐
         │  Parse & AST   │
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │ Rename All IDs │
         │  user → _0x4a  │
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │ Encrypt Strings│
         │ "Hi" → base64  │
         └────────┬───────┘
                  │
                  ▼
         ┌────────────────┐
         │ Xor layer      │
         │                │
         └────────┬───────┘
                  │
                  ▼
┌──────────────────────────────────────────────────┐
│        OBFUSCATED PYTHON CODE                    │
│         script_obfuscated.py                     │
│         (Unreadable but works! ✅)               │
└──────────────────────────────────────────────────┘


## 📜 License & Ethics

This project is released under the MIT License and is intended for
intellectual property protection, software distribution,
and educational purposes.

It is not designed for malware development or malicious code concealment.
