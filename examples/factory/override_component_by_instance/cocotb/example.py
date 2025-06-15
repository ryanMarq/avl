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
        self.o = object_A("o", self)


class sub_comp_A(avl.Component):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.error("sub_comp_A should have been overriden by sub_comp_B")


class sub_comp_B(avl.Component):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.info("sub_comp_B successfully overriden sub_comp_A")


class object_A(avl.Object):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.error("object_A should have been overriden by object_B")


class object_B(avl.Object):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.info("object_B successfully overriden object_A")


@cocotb.test
async def test(dut):
    avl.Factory.set_override_by_instance("env.s", sub_comp_B)
    avl.Factory.set_override_by_instance("env.o", object_B)

    e = example_env("env", None)
    await e.start()
