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

    async def report_phase(self):
        self.error("report phase - failed")


@cocotb.test
async def test(dut):
    avl.PhaseManager.remove_phase("REPORT")
    e = example_env("env", None)
    await e.start()
