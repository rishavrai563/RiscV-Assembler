# 🚀 RISC-V 64-bit Assembler  
*A two-pass assembler for the RV64I base instruction set, built in modern C++ with an integrated Flask-based web interface.*

<p align="center">
  <img src="https://img.shields.io/badge/Language-C%2B%2B20-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Framework-Flask-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/UI-VS%20Code%20Dark%20Mode-9cf?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Architecture-RISC--V-yellow?style=flat-square"/>
</p>

---

## 📋 Overview
This project implements a **two-pass assembler** for the **RISC-V 64-bit Instruction Set Architecture (RV64I)**.  
It translates assembly source code (`.asm`) into machine-code output (`.mc`), handling labels, directives, and instruction encoding with high accuracy.

Additionally, it features a **web-based interface** built with **Flask** and **HTML/CSS** that allows users to upload `.asm` files, process them through the assembler, and download the resulting `.mc` file — all through a **VS Code–style dark mode UI**.

---

## 👨‍💻 Authors

- **Rishav Kumar** — 2024AIB1014  
- **Path** — 2024AIB1012  

---

## ✨ Features
- ✅ Full support for **R, I, S, SB, U, and UJ formats**  
- ✅ Handles directives: `.text`, `.data`, `.byte`, `.half`, `.word`, `.dword`, `.asciz`  
- ✅ Builds and uses a **symbol table** for label resolution  
- ✅ Clear **error diagnostics** with color-coded messages  
- ✅ Produces a neatly formatted `.mc` output file  
- ✅ Modular structure: `Lexer → Parser → Assembler`  
- ✅ Integrated **Flask web app** to assemble and download machine code visually  

---


---

## 🧩 Instruction Coverage

| Format | Instructions Supported |
|:--------|:-----------------------|
| **R-Type** | `add`, `sub`, `mul`, `div`, `rem`, `and`, `or`, `xor`, `sll`, `slt`, `sra`, `srl` |
| **I-Type** | `addi`, `andi`, `ori`, `lb`, `lh`, `lw`, `jalr` |
| **S-Type** | `sb`, `sh`, `sw` |
| **SB-Type** | `beq`, `bne`, `bge`, `blt` |
| **U-Type** | `lui`, `auipc` |
| **UJ-Type** | `jal` |

> ⚙️ *Pseudo-instructions and floating-point operations are intentionally excluded per project requirements.*

---

## 🧱 Supported Directives

| Directive | Description |
|------------|-------------|
| `.text` | Start of code section |
| `.data` | Start of data section |
| `.byte`, `.half`, `.word`, `.dword` | Define integer data |
| `.asciz`, `.ascii`, `.asciiz` | Define string data (null-terminated if asciz/asciiz) |

---

## 🧠 Internal Flow Diagram

      ┌─────────────────────┐
      │     assembler.cpp   │
      │ (Driver + I/O layer)│
      └──────────┬──────────┘
                 │
       ┌─────────▼─────────┐
       │      Lexer        │
       │  (Token Generator)│
       └─────────┬─────────┘
                 │
       ┌─────────▼─────────┐
       │      Parser       │
       │ (Label + Symbol   │
       │   Table Builder)  │
       └─────────┬─────────┘
                 │
       ┌─────────▼─────────┐
       │     Assembler     │
       │ (Binary Encoder + │
       │   File Writer)    │
       └─────────┬─────────┘
                 │
       ┌─────────▼─────────┐
       │     Flask App     │
       │ (Upload + Run +   │
       │  Download Output) │
       └───────────────────┘

---

## ⚙️ Build and Run

### 🧰 Prerequisites
- **C++20 compiler** (`g++ 10+`, `clang++`, or `MinGW-w64`)
- **Python 3.9+**
- Flask (`pip install flask`)
- Command-line terminal / PowerShell

---

### 💻 Command-Line Mode

```bash
# Step 1: Navigate to the src directory
cd src

# Step 2: Compile the assembler
g++ assembler.cpp -o assembler -std=c++20

# Step 3: Run with input file
# Syntax:
#   ./assembler <input.asm> [output.mc]

# Example:
./assembler ../examples/sample.asm

# Default output: ../examples/sample.mc
# Or specify:
./assembler ../examples/sample.asm output/my_output.mc
```
🌐 Web Mode (Flask Interface)
```bash
# Step 1: Navigate to project root
cd RiscV-Assembler

# Step 2: Run Flask server
python app.py

# Step 3: Open your browser
Visit http://127.0.0.1:5000

Upload your .asm file in the left panel

View the generated .mc machine code in the right panel

Click Download Machine Code to save it locally
```
⚠️ Known Limitations

- No pseudo-instruction (mv, nop, etc.) support

- No floating-point operations

- Only supports RV64I integer instructions

- Assumes syntactically valid input

📚 References

- RISC-V ISA Manual (Volume I: User-Level ISA)

- RISC-V Assembly Programmer’s Manual

- IIT Ropar FCS Mini Project Specification (2025)

🧾 License
```
Distributed under the MIT License.
```

