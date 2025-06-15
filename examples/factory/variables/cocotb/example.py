# Copyright 2024 Apheleia
#
# Description:
# Apheleia factory example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = avl.Factory.get_variable(f"{self.get_full_name()}.a", 0)

        if self.a != 100:
            self.error(f"Expected a to be 100, got {self.a}")


@cocotb.test
async def test(dut):
    avl.Factory.set_variable("env.a", 100)

    e = example_env("env", None)
    await e.start()
