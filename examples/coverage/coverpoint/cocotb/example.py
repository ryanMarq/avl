# Copyright 2024 Apheleia
#
# Description:
# Apheleia coverage example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = avl.Int8(0)
        self.b = 0

        self.cg = avl.Covergroup("cg", self)
        self.cp_a = self.cg.add_coverpoint("cp_a", lambda: self.a)
        self.cp_a.add_bin("bin", 1, 2, range(100, 200))

        self.cp_b = self.cg.add_coverpoint("cp_b", lambda: self.b)
        self.cp_b.add_bin("bin", lambda x: x == 10)

        self.cg.sample()

        print(self.cg.report(full=True))

        self.a = 101
        self.b = 10
        self.cg.sample()

        print(self.cg.report(full=True))
        print(self.cg.report())


@cocotb.test
async def test(dut):
    example_env("env", None)
