# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.b = avl.Bool("b", False)


@cocotb.test
async def test(dut):
    e = example_env("env", None)

    # Direct allocation - must use .value to avoid trampling the class
    e.b.value = False
    assert not e.b

    # Increment
    e.b += 1
    assert e.b

    # Random
    for _ in range(10):
        e.b.randomize()
        assert e.b in [True, False]
