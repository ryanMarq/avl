# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb


class a(avl.Object):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.var_a = 0
        self.var_b = 1
        self.set_field_attributes("var_a", compare=False)


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a0 = a("a", self)
        self.a1 = a("a", self)
        self.a1.var_a = 1  # Should generate an error if not for attribute

        assert self.a0.compare(self.a1, verbose=True)


@cocotb.test
async def test(dut):
    example_env("env", None)
