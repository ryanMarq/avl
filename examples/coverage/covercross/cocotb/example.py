# Copyright 2024 Apheleia
#
# Description:
# Apheleia coverage example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = 0
        self.b = 0

        self.cg = avl.Covergroup("cg", self)

        self.cp_a = self.cg.add_coverpoint("cp_a", lambda: self.a)
        self.cp_a.add_bin("a1", 1)
        self.cp_a.add_bin("a2", 2)
        self.cp_a.add_bin("a3", 3)

        self.cp_b = self.cg.add_coverpoint("cp_b", lambda: self.b)
        self.cp_b.add_bin("b10", 10)
        self.cp_b.add_bin("b20", 20)

        self.cc = self.cg.add_covercross("cc", self.cp_a, self.cp_b)

        self.a = 2
        self.b = 10
        self.cg.sample()

        print(self.cg.report(full=True))
        print(self.cg.report(full=False))


@cocotb.test
async def my_test(dut):
    example_env("env", None)
