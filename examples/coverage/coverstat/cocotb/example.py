# Copyright 2024 Apheleia
#
# Description:
# Apheleia coverage example


import random

import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = avl.Int64("a", 0)

        self.cg = avl.Covergroup("cg", self)

        # Add a traditional coverpoint
        self.cp_a = self.cg.add_coverpoint("cp_a", lambda: self.a)
        for i in range(10):
            self.cp_a.add_bin(f"bin[{i}]", i)

        # Add a coverstat
        self.cp_b = self.cg.add_coverpoint("cp_b", lambda: self.a)
        self.cp_b.add_bin("bin", range(0, 10), stats=True)

        for _ in range(10):
            self.a.value = random.randint(2, 8)
            self.cg.sample()

        print(self.cg.report(full=False))
        print(self.cg.report(full=True))


@cocotb.test
async def test(dut):
    example_env("env", None)
