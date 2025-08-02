# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb
from z3 import And


class example_env(avl.Env):

    def test_avl_int(self):
        self.info("Testing signed logic and arithmetic operations...")

        a = avl.Int(10, width=8)
        b = avl.Int(5, width=8)

        # Arithmetic
        assert a + b == 15             # 10 + 5 = 15
        c = avl.Int(a, width=8)
        c += b
        assert c == 15                 # 10 + 5 = 15

        assert a - b == 5              # 10 - 5 = 5
        assert b - a == -5             # 5 - 10 = -5
        c = avl.Int(b, width=8)
        c -= a
        assert c == -5                 # 5 - 10 = -5

        assert a * b == 50             # 10 * 5 = 50
        c = avl.Int(a, width=8)
        c *= b
        assert c == 50                 # 10 * 5 = 50

        assert a // b == 2             # 10 // 5 = 2
        c = avl.Int(a, width=8)
        c //= b
        assert c == 2                  # 10 // 5 = 2

        assert a % b == 0              # 10 % 5 = 0
        c = avl.Int(a, width=8)
        c %= b
        assert c == 0                  # 10 % 5 = 0

        base = avl.Int(2, width=8)
        exp = avl.Int(4, width=8)
        assert base ** exp == 16       # 2 ** 4 = 16
        c = avl.Int(base, width=8)
        c **= exp
        assert c == 16                 # 2 ** 4 = 16

        assert b << 1 == 10            # 5 << 1 = 10
        c = avl.Int(b, width=8)
        c <<= 1
        assert c == 10                 # 5 << 1 = 10

        assert a >> 1 == 5             # 10 >> 1 = 5
        c = avl.Int(a, width=8)
        c >>= 1
        assert c == 5                  # 10 >> 1 = 5

        # RDivMod
        r = divmod(23, a)
        assert r == (2, 3)             # 23 // 10 = 2, 23 % 10 = 3
        r = divmod(a, 3)
        assert r == (3, 1)             # 10 // 3 = 3, 10 % 3 = 1

        # Comparisons
        assert a > b                   # 10 > 5
        assert not (a < b)
        assert a >= b
        assert not (a <= b)
        assert a != b
        assert a == avl.Int(10, width=8)

        # String conversion
        assert str(a) == "10"          # String representation
        assert hex(a) == "0xa"         # 10 in hex
        assert isinstance(repr(a), str)

        # === Wrapping Tests ===

        # Overflow: 130 wraps to -126 (130 - 256 = -126)
        assert avl.Int(130, width=8) == -126

        # Underflow: -140 wraps to 116 (-140 + 256 = 116)
        assert avl.Int(-140, width=8) == 116

        # Add overflow: 100 + 100 = 200 -> wraps to -56
        x = avl.Int(100, width=8)
        y = avl.Int(100, width=8)
        assert x + y == -56            # 200 - 256 = -56

        # Sub underflow: -100 - 50 = -150 -> wraps to 106
        x = avl.Int(-100, width=8)
        y = avl.Int(50, width=8)
        assert x - y == 106            # -150 + 256 = 106

        # Multiply overflow: 20 * 20 = 400 -> wraps to -112
        x = avl.Int(20, width=8)
        y = avl.Int(20, width=8)
        assert x * y == -112           # 400 - 256*2 = -112

        # Small width test: 4-bit signed range = [-8, 7]
        x = avl.Int(9, width=4)
        assert x == -7                 # 9 wraps to -7 in 4-bit signed

        x = avl.Int(-9, width=4)
        assert x == 7                  # -9 wraps to 7 in 4-bit signed

        x = avl.Int(5, width=4)
        y = avl.Int(5, width=4)
        assert x + y == -6             # 5 + 5 = 10 wraps to -6 in 4-bit signed

        self.info("Signed logic and arithmetic operations passed successfully.")

    def test_avl_uint(self):

        self.info("Testing unsigned logic and arithmetic operations...")

        a = avl.Uint(250, width=8)
        b = avl.Uint(10, width=8)

        assert a + b == 4              # 250 + 10 = 260 % 256 = 4
        c = avl.Uint(a, width=8)
        c += b
        assert c == 4                  # 250 + 10 = 260 % 256 = 4

        assert a - b == 240            # 250 - 10 = 240
        assert b - a == 16             # 10 - 250 = -240 % 256 = 16
        c = avl.Uint(b, width=8)
        c -= a
        assert c == 16                # 10 - 250 = -240 % 256 = 16

        assert a * b == 196            # 250 * 10 = 2500 % 256 = 196
        c = avl.Uint(a, width=8)
        c *= b
        assert c == 196               # 250 * 10 = 2500 % 256 = 196

        assert a // b == 25            # 250 // 10 = 25
        c = avl.Uint(a, width=8)
        c //= b
        assert c == 25                # 250 // 10 = 25

        assert a % b == 0              # 250 % 10 = 0
        c = avl.Uint(a, width=8)
        c %= b
        assert c == 0                 # 250 % 10 = 0

        base = avl.Uint(2, width=8)
        exp = avl.Uint(5, width=8)
        assert base ** exp == 32       # 2 ** 5 = 32
        c = avl.Uint(base, width=8)
        c **= exp
        assert c == 32                # 2 ** 5 = 32

        assert b << 2 == 40            # 10 << 2 = 40
        c = avl.Uint(b, width=8)
        c <<= 2
        assert c == 40                # 10 << 2 = 40

        assert a >> 2 == 62            # 250 >> 2 = 62
        c = avl.Uint(a, width=8)
        c >>= 2
        assert c == 62                # 250 >> 2 = 62

        # Comparisons
        assert a > b                   # 250 > 10
        assert not (a < b)
        assert a >= b
        assert not (a <= b)
        assert a != b
        assert a == avl.Uint(250, width=8)

        assert str(a) == "250"         # String representation
        assert hex(a) == "0xfa"        # 250 in hex
        assert isinstance(repr(a), str)

        # === Wrapping Tests ===

        # Literal overflow: 300 % 256 = 44
        assert avl.Uint(300, width=8) == 44

        # Literal underflow: -5 % 256 = 251
        assert avl.Uint(-5, width=8) == 251

        # Add overflow: 200 + 100 = 300 % 256 = 44
        x = avl.Uint(200, width=8)
        y = avl.Uint(100, width=8)
        assert x + y == 44            # 200 + 100 = 300 % 256 = 44

        # Sub underflow: 5 - 10 = -5 % 256 = 251
        x = avl.Uint(5, width=8)
        y = avl.Uint(10, width=8)
        assert x - y == 251           # 5 - 10 = -5 % 256 = 251

        # Multiply overflow: 20 * 20 = 400 % 256 = 144
        x = avl.Uint(20, width=8)
        y = avl.Uint(20, width=8)
        assert x * y == 144           # 400 % 256 = 144

        # Small width test: 4-bit unsigned max = 15
        x = avl.Uint(17, width=4)
        assert x == 1                 # 17 % 16 = 1

        x = avl.Uint(-1, width=4)
        assert x == 15                # -1 % 16 = 15

        x = avl.Uint(8, width=4)
        y = avl.Uint(12, width=4)
        assert x + y == 4             # 8 + 12 = 20 % 16 = 4

        self.info("Unsigned logic and arithmetic operations passed successfully.")

    def test_randomization(self):

        self.info("Testing randomization...")

        # Create a random Logic variable
        rand_var = avl.Int8(0, auto_random=True)

        # Simple randomization
        for _ in range(10):
            rand_var.randomize()
            assert -128 <= rand_var < 128

        # Randomization with hard constraints
        for _ in range(10):
            rand_var.randomize(hard=[lambda x: And(x >=1, x <= 2)])
            assert  rand_var >= 1 and rand_var <= 2

        self.info("Randomization test passed successfully.")

    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.test_avl_int()

        self.test_avl_uint()

        self.test_randomization()

@cocotb.test
async def test(dut):
    _ = example_env("env", None)

