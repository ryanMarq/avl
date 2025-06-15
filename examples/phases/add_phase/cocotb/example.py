# Copyright 2024 Apheleia
#
# Description:
# Apheleia phase example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.custom_phase_run = False

    async def custom_phase(self):
        self.custom_phase_run = True

    async def report_phase(self):
        if self.custom_phase_run:
            self.info("Custom phase - ok")
        else:
            self.error("Custom phase - failed")


@cocotb.test
async def test(dut):
    avl.PhaseManager.add_phase("CUSTOM", after=avl.PhaseManager().get_phase("RUN"))
    e = example_env("env", None)
    await e.start()
