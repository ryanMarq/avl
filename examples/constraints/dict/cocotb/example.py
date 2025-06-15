# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import random

import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = {
            "a0": avl.Logic("a[a0]", 0, width=32, fmt=hex),
            "a1": avl.Logic("a[a1]", 0, width=32, fmt=hex),
        }
        self.add_constraint("c_0", lambda x: x == random.randint(0, 100), self.a["a0"])
        self.add_constraint("c_1", lambda x, y: x == y + 1, self.a["a1"], self.a["a0"])


@cocotb.test
async def test(dut):
    e = example_env("env", None)
    for _ in range(10):
        e.randomize()
        assert e.a["a0"] >= 0 and e.a["a0"] <= 100
        assert e.a["a1"] == e.a["a0"] + 1
