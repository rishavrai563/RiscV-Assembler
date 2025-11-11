.text
# --- R-format ---
add x1, x2, x3        # x1 = x2 + x3
sub x4, x1, x5        # x4 = x1 - x5
and x6, x2, x7        # x6 = x2 & x7
or  x8, x3, x9        # x8 = x3 | x9
mul x10, x11, x12     # x10 = x11 * x12

# --- I-format ---
addi x13, x1, 10      # x13 = x1 + 10
andi x14, x2, 15      # x14 = x2 & 15
ori  x15, x3, 7       # x15 = x3 | 7
lw   x16, 0(x2)       # x16 = Mem[x2 + 0]
jalr x0, x1, 0        # Jump to x1

# --- S-format ---
sw x5, 8(x2)          # Mem[x2 + 8] = x5
sd x6, 16(x2)         # Mem[x2 + 16] = x6

# --- SB-format (branch) ---
beq x1, x2, label     # if x1 == x2 jump to label
bne x3, x4, label     # if x3 != x4 jump to label

# --- U-format ---
lui x17, 0x10000      # x17 = 0x10000000
auipc x18, 0x20000    # x18 = PC + 0x20000000

# --- UJ-format ---
jal x19, label         # Jump and link

# --- Label & Data Section ---
label:
.data
word1: .word 10
