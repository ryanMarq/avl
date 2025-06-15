# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb
from z3 import And, Implies, Or


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = avl.Logic("a", 0, width=8, fmt=hex)
        self.b = avl.Logic("b", 0, width=8, fmt=hex)

        self.add_constraint("c_0", lambda x: Or(x == 0, x == 100), self.a)
        self.add_constraint("c_1", lambda x: And(x >= 5, x <= 100), self.b)
        self.add_constraint("c_2", lambda x, y: Implies(x == 0, y == 10), self.a, self.b)


@cocotb.test
async def test(dut):
    e = example_env("env", None)
    for _ in range(100):
        e.randomize()
        assert e.a == 0 or e.a == 100
        assert e.b >= 5 and e.b <= 100
        assert e.b == 10 if e.a == 0 else True
