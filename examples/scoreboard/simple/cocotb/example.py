# Copyright 2024 Apheleia
#
# Description:
# Apheleia scoreboard example


import avl
import cocotb


class example_item(avl.Object):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.value = None


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.sb = avl.Scoreboard("sb", self)
        self.sb.set_verbose(True)

    async def run_phase(self):
        self.raise_objection()

        for i in range(10):
            await cocotb.triggers.Timer(1, unit="ns")
            item = example_item("item" + str(i), None)
            item.value = i
            self.info(f"Item : {item.get_name()}")

            self.sb.before_port.append(item)
            self.sb.after_port.append(item)

        self.drop_objection()


@cocotb.test
async def test(dut):
    e = example_env("env", None)
    await e.start()
