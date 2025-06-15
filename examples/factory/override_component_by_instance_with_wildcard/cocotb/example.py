# Copyright 2024 Apheleia
#
# Description:
# Apheleia factory example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.s = sub_comp_A("s", self)


class sub_comp_A(avl.Component):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.error("sub_comp_A should have been overriden by sub_comp_B")


class sub_comp_B(avl.Component):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.info("sub_comp_B successfully overriden sub_comp_A")


@cocotb.test
async def test(dut):
    avl.Factory.set_override_by_instance("*.s", sub_comp_B)
    avl.Factory.set_override_by_instance(
        "env.*", sub_comp_A
    )  # Shouldn't be used as not the closest match

    e = example_env("env", None)
    await e.start()
