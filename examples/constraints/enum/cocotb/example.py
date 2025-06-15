# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb
from z3 import Or


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.e = avl.Enum("e", "A", {"A": 0, "B": 1, "C": 2})
        self.add_constraint("c_0", lambda x: Or(x == self.e.B, x == self.e.C), self.e)


@cocotb.test
async def test(dut):
    e = example_env("env", None)
    for _ in range(10):
        e.randomize()
        assert e.e != e.e.A
