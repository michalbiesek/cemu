import capstone
import keystone
import unicorn

from cemu.arch import Architecture, Endianness

class RISCV64(Architecture):
    name = "RISCV-64"
    pc = "PC"
    sp = "SP"
    flag = "NZCV"
    endianness = Endianness.LITTLE_ENDIAN
    registers = [
        "X0",
        "X1",
        "X2",
        "X3",
        "X4",
        "X5",
        "X6",
        "X7",
        "X8",
        "X9",
        "X10",
        "X11",
        "X12",
        "X13",
        "X14",
        "X15",
        "X16",
        "X17",
        "X18",
        "X19",
        "X20",
        "X21",
        "X22",
        "X23",
        "X24",
        "X25",
        "X26",
        "X27",
        "X28",
        "X29",
        "X30",
        sp,
        flag,
        pc,
    ]
    syscall_filename = "riscv64"
    ptrsize = 8
    ptrsize = 8

    def keystone(self) -> tuple[int, int, int]:
        return (keystone.KS_ARCH_RISCV, 0, keystone.KS_MODE_RISCV64)

    def capstone(self) -> tuple[int, int, int]:
        return (
            capstone.CS_ARCH_RISCV,
            capstone.CS_MODE_RISCV64 | CS_MODE_RISCVC,
            capstone.CS_MODE_LITTLE_ENDIAN,
        )

    def unicorn(self) -> tuple[int, int, int]:
        return (
            unicorn.UC_ARCH_RISCV,
            unicorn.UC_MODE_RISCV64,
            unicorn.UC_MODE_LITTLE_ENDIAN,
        )

    def uc_register(self, name: str) -> int:
        return getattr(unicorn.riscv_const, f"UC_RISCV_REG_{name.upper()}")
