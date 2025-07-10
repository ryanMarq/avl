# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.e1 = avl.Enum("e1", "A", {"A": 0, "B": 1, "C": 2}, width=4)
        self.e2 = avl.Enum("e2", value="B", values={"A" : 127, "B" : -128})


@cocotb.test
async def test(dut):
    e = example_env("env", None)

    # Direct allocation - must use .value to avoid trampling the class
    e.e1.value = e.e1.B
    assert e.e1 == e.e1.B

    # Increment
    e.e1 += 1
    assert e.e1== e.e1.C

    # Random
    for _ in range(10):
        e.e1.randomize()
        assert e.e1 in e.e1.values.values()

    # Enum Width
    assert e.e1.width == 4
    assert e.e2.width == 8

    

