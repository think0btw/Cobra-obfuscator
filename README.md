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

Cobra Obfuscator uses **AST (Abstract Syntax Tree) transformations** and **runtime encryption** to make your Python code extremely difficult to reverse engineer. It combines multiple obfuscation techniques to provide strong protection for your source code.

---

## ✨ Features

- **🔐 Multi-Layer Obfuscation**
  - AST-based code transformation
  - Variable and function renaming
  - String obfuscation
  - Number obfuscation
  - XOR encryption with Base64 encoding

- **🎯 Smart Processing**
  - Preserves Python built-ins
  - Handles imports correctly
  - Multi-pass obfuscation (up to 2 passes)

- **⚙️ Additional Tools**
  - Nuitka compilation support
    
---

## 🔧 Installation

```bash

git clone https://github.com/think0btw/Cobra-obfuscator.git
cd Cobra-obfuscator
pip install -r requirements.txt
python3 main.py
```

---

## 🚀 Usage

### Interactive Mode

Run the tool and use the interactive commands:

```bash
python3 main.py
```

### Available Commands

| Command | Description |
|---------|-------------|
| `drag` | Drag and drop a Python file to obfuscate |
| `manualpath` | Enter file path manually |
| `compile` | Compile obfuscated file with Nuitka |
| `path` | Show current working directory |
| `clear` | Clear the screen |
| `help` | Show help menu |
| `exit` | Exit the program |

### Example Workflow

```bash
[>] drag
Glisse un fichier ici : /path/to/your/script.py
[+] /path/to/your/script_packed.py
```

---

## 📊 How It Works

```
┌─────────────────────┐
│  Original Python    │
│      Code          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   AST Transform     │
│ • Rename variables  │
│ • Rename functions  │
│ • Split strings     │
│ • Obfuscate numbers │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Base64 Encoding    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   XOR Encryption    │
│   (with key)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Runtime Loader     │
│  • Decrypt at run   │
│  • Execute code     │
└─────────────────────┘
```
## ⚠️ Important Notes

- **Always backup** your original code before obfuscation
-   Obfuscated code may run **slightly slower** than original
-   Keep your **original source code** for future modifications
-   This tool is for **legitimate protection** purposes only


## 📜 License & Ethics

This project is released under the MIT License and is intended for
intellectual property protection, software distribution,
and educational purposes.

It is not designed for malware development or malicious code concealment.

## 👥 Authors

- **think0btw**
- **Nat11-n1**

---

## 🌟 Support

If you find this project helpful, please give it a ⭐ on GitHub!

---

**Made with 🐍 and ❤️**
