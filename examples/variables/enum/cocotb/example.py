# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.e = avl.Enum("e", "A", {"A": 0, "B": 1, "C": 2})


@cocotb.test
async def test(dut):
    e = example_env("env", None)

    # Direct allocation - must use .value to avoid trampling the class
    e.e.value = e.e.B
    assert e.e == e.e.B

    # Increment
    e.e += 1
    assert e.e == e.e.C

    # Random
    for _ in range(10):
        e.e.randomize()
        assert e.e in e.e.values.values()
