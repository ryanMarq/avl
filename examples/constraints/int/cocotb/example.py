# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb
from z3 import *


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = avl.Uint8(0, fmt=hex)
        self.add_constraint("c_0", lambda x: x != 0, self.a)

        self.b = avl.Int32(0, fmt=str)
        self.add_constraint("c_1", lambda x: And(x > -2, x < 10), self.b)

@cocotb.test
async def test(dut):
    e = example_env("env", None)
    for _ in range(100):
        e.randomize()
        assert e.a != 0
        assert e.b > -2 and e.b < 10
