# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb
import numpy as np
from cocotb.triggers import Timer


class example_env(avl.Env):

    def test_avl_fp16(self):
        a = avl.Fp16("a", 2.0)
        b = avl.Fp16("b", 3.0)

        # Arithmetic
        assert a + b == 5.0            # 2.0 + 3.0 = 5.0
        c = avl.Fp16("c", a)
        c += b
        assert c == 5.0                # 2.0 + 3.0 = 5.0

        assert a - b == -1.0           # 2.0 - 3.0 = -1.0
        c = avl.Fp16("c", a)
        c -= b
        assert c == -1.0               # 2.0 - 3.0 = -1.0

        assert a * b == 6.0            # 2.0 * 3.0 = 6.0
        c = avl.Fp16("c", a)
        c *= b
        assert c == 6.0                # 2.0 * 3.0 = 6.0

        assert b / a == 1.5            # 3.0 / 2.0 = 1.5
        c = avl.Fp16("c", b)
        c /= a
        assert c == 1.5                # 3.0 / 2.0 = 1.5

        # Power
        assert a ** 2 == 4.0           # 2.0 ** 2 = 4.0
        c = avl.Fp16("c", a)
        c **= 2
        assert c == 4.0                # 2.0 ** 2 = 4.0

        # Comparisons
        assert a < b                   # 2.0 < 3.0
        assert not (a > b)
        assert a <= b
        assert not (a >= b)
        assert a != b
        assert a == avl.Fp16("a2", 2.0)

        # String
        assert str(a) == "2.0"         # str of float16
        assert isinstance(repr(a), str)

        # === Special values ===

        # Positive infinity
        pos_inf = avl.Fp16("pos_inf", np.inf)
        assert pos_inf > b             # inf > 3.0
        assert str(pos_inf) == "inf"

        # Negative infinity
        neg_inf = avl.Fp16("neg_inf", -np.inf)
        assert neg_inf < b             # -inf < 3.0
        assert str(neg_inf) == "-inf"

        # NaN
        nan = avl.Fp16("nan", np.nan)
        assert nan != nan              # NaN is not equal to anything
        assert not (nan < b)           # Comparisons with NaN are always False
        assert not (nan > b)
        assert not (nan == b)
        assert str(nan) == "nan"

        # Overflow to inf
        large = avl.Fp16("large", 1e5)
        assert large.value == np.inf    # np.float16 overflows at ~65504

        # Underflow to 0
        tiny = avl.Fp16("tiny", 1e-10)
        assert tiny.value == 0.0        # underflow to zero in float16

    def test_avl_fp32(self):
        a = avl.Fp32("a", 2.0)
        b = avl.Fp32("b", 3.0)

        # Arithmetic
        assert a + b == 5.0            # 2.0 + 3.0 = 5.0
        c = avl.Fp32("c", a)
        c += b
        assert c == 5.0                # 2.0 + 3.0 = 5.0

        assert a - b == -1.0           # 2.0 - 3.0 = -1.0
        c = avl.Fp32("c", a)
        c -= b
        assert c == -1.0               # 2.0 - 3.0 = -1.0

        assert a * b == 6.0            # 2.0 * 3.0 = 6.0
        c = avl.Fp32("c", a)
        c *= b
        assert c == 6.0                # 2.0 * 3.0 = 6.0

        assert b / a == 1.5            # 3.0 / 2.0 = 1.5
        c = avl.Fp32("c", b)
        c /= a
        assert c == 1.5                # 3.0 / 2.0 = 1.5

        # Power
        assert a ** 2 == 4.0           # 2.0 ** 2 = 4.0
        c = avl.Fp32("c", a)
        c **= 2
        assert c == 4.0                # 2.0 ** 2 = 4.0

        # Comparisons
        assert a < b
        assert not (a > b)
        assert a <= b
        assert not (a >= b)
        assert a != b
        assert a == avl.Fp32("a2", 2.0)

        # String
        assert str(a) == "2.0"
        assert isinstance(repr(a), str)

        # Special values
        pos_inf = avl.Fp32("pos_inf", np.inf)
        assert pos_inf > b
        assert str(pos_inf) == "inf"

        neg_inf = avl.Fp32("neg_inf", -np.inf)
        assert neg_inf < b
        assert str(neg_inf) == "-inf"

        nan = avl.Fp32("nan", np.nan)
        assert nan != nan
        assert not (nan < b)
        assert not (nan > b)
        assert not (nan == b)
        assert str(nan) == "nan"

        large = avl.Fp32("large", 1e40)
        assert large.value == np.inf

        tiny = avl.Fp32("tiny", 1e-50)
        assert tiny.value == 0.0

    def test_avl_fp64(self):
        a = avl.Fp64("a", 2.0)
        b = avl.Fp64("b", 3.0)

        # Arithmetic
        assert a + b == 5.0
        c = avl.Fp64("c", a)
        c += b
        assert c == 5.0

        assert a - b == -1.0
        c = avl.Fp64("c", a)
        c -= b
        assert c == -1.0

        assert a * b == 6.0
        c = avl.Fp64("c", a)
        c *= b
        assert c == 6.0

        assert b / a == 1.5
        c = avl.Fp64("c", b)
        c /= a
        assert c == 1.5

        # Power
        assert a ** 2 == 4.0
        c = avl.Fp64("c", a)
        c **= 2
        assert c == 4.0

        # Comparisons
        assert a < b
        assert not (a > b)
        assert a <= b
        assert not (a >= b)
        assert a != b
        assert a == avl.Fp64("a2", 2.0)

        # String
        assert str(a) == "2.0"
        assert isinstance(repr(a), str)

        # Special values
        pos_inf = avl.Fp64("pos_inf", np.inf)
        assert pos_inf > b
        assert str(pos_inf) == "inf"

        neg_inf = avl.Fp64("neg_inf", -np.inf)
        assert neg_inf < b
        assert str(neg_inf) == "-inf"

        nan = avl.Fp64("nan", np.nan)
        assert nan != nan
        assert not (nan < b)
        assert not (nan > b)
        assert not (nan == b)
        assert str(nan) == "nan"

        large = avl.Fp64("large", 1e310)
        assert large.value == np.inf

        tiny = avl.Fp64("tiny", 1e-400)
        assert tiny.value == 0.0

    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.test_avl_fp16()

        self.test_avl_fp32()

        self.test_avl_fp64()

        # Variables for testing HDL interaction
        self.fp16 = avl.Fp16("fp16", 0.0)
        self.fp32 = avl.Fp32("fp32", 0.0)
        self.fp64 = avl.Fp64("fp64", 0.0)


@cocotb.test
async def test(dut):
    e = example_env("env", None)

    await Timer(100, units="ns")

    e.fp16 += -0.3
    assert e.fp16 == -0.3
    dut.fp16.value = e.fp16.to_bits()

    e.fp32 += 11.4
    assert e.fp32 == 11.4
    dut.fp32.value = e.fp32.to_bits()

    e.fp64 += 110202.0821
    assert e.fp64 == 110202.0821
    dut.fp64.value = e.fp64.to_bits()

    await Timer(100, units="ns")

    # Read back and check
    fp16 = avl.Fp16("fp16", 0.0)
    fp16.from_bits(dut.fp16.value)
    assert fp16 == e.fp16

    fp32 = avl.Fp32("fp32", 0.0)
    fp32.from_bits(dut.fp32.value)
    assert fp32 == e.fp32

    fp64 = avl.Fp64("fp64", 0.0)
    fp64.from_bits(dut.fp64.value)
    assert fp64 == e.fp64
