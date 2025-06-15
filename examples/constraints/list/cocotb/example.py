# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb
from z3 import If


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = [avl.Logic(f"a[{i}]", i, width=32, fmt=hex) for i in range(4)]
        for i in range(0, len(self.a)):
            self.add_constraint(
                f"c_{i}", lambda i, x, y: x == If(i == 0, 100, y + 1), i, self.a[i], self.a[i - 1]
            )


@cocotb.test
async def test(dut):
    e = example_env("env", None)
    for _ in range(10):
        e.randomize()
        assert e.a[0] == 100
        assert e.a[1] == e.a[0] + 1
        assert e.a[2] == e.a[1] + 1
        assert e.a[3] == e.a[2] + 1
