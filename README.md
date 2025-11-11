# RISC-V 64-bit Assembler  
*A two-pass assembler for the RV64I base instruction set, built in modern C++.*

<p align="center">
  <img src="https://img.shields.io/badge/Language-C%2B%2B20-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square"/>
  <img src="https://img.shields.io/badge/Platform-Cross--Platform-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Architecture-RISC--V-9cf?style=flat-square"/>
</p>

---

## 🚀 Overview
This project implements a **two-pass assembler** for the **RISC-V 64-bit Instruction Set Architecture (RV64I)**.  
It translates assembly source code (`.asm`) into machine-code output (`.mc`), handling labels, directives, and instruction encoding with high accuracy.

## 👨‍💻 Authors

- Rishav Kumar — 2024AIB1014  
- Parth — 2024AIB1012
### ✨ Features
- ✅ Full support for **R, I, S, SB, U, and UJ formats**  
- ✅ Handles directives: `.text`, `.data`, `.byte`, `.half`, `.word`, `.dword`, `.asciz`  
- ✅ Builds and uses a **symbol table** for label resolution  
- ✅ Clear **error diagnostics** with color-coded messages  
- ✅ Produces a neatly formatted `.mc` output file  
- ✅ Modular structure: `Lexer → Parser → Assembler`  

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

## ⚙️ Build and Run

### 🧰 Prerequisites
- **C++17/20 compiler** (`g++ 10+`, `MinGW-w64`, or `clang++`)
- Command line terminal / PowerShell

# 🧠 Internal Flow Diagram
          ┌─────────────────────┐
          │     assembler.cpp    │
          │ (Driver + I/O layer) │
          └──────────┬───────────┘
                     │
           ┌─────────▼─────────┐
           │      Lexer         │
           │  (Token Generator) │
           └─────────┬─────────┘
                     │
           ┌─────────▼─────────┐
           │      Parser        │
           │ (Label + Symbol    │
           │   Table Builder)   │
           └─────────┬─────────┘
                     │
           ┌─────────▼─────────┐
           │     Assembler      │
           │ (Binary Encoder +  │
           │   File Writer)     │
           └───────────────────┘
### 💻 Commands

```bash
# ============================
# 🔧 Build and Run Instructions
# ============================

# Step 1: Compile
g++ assembler.cpp -o assembler -std=c++20

# Step 2: Run with input file
# Syntax:
#   ./assembler <input.asm> [output.mc]

# Example:
./assembler examples/sample.asm

# Default output: examples/sample.mc
# Or specify:
./assembler examples/sample.asm output/my_output.mc
```


# ⚠️ Known Limitations

Does not implement pseudo-instructions (mv, nop, etc.)

RV64 “W” variants (addw, mulw, divw, etc.) can be added easily

No floating-point instruction support (as specified)

Input assumes valid RISC-V syntax

# 📚 References

RISC-V ISA Manual (Volume I: User-Level ISA)

RISC-V Assembly Programmer’s Manual

IIT Ropar FCS Mini Project Specification (2025)

🧾 License

Distributed under the MIT License
.




```
