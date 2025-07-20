# Copyright 2024 Apheleia
#
# Description:
# Apheleia trace example


import random

import avl
import cocotb
from cocotb.triggers import Timer


class example_item(avl.SequenceItem):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.data = 0

class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.port = avl.Port('port', self)
        self.trace0= avl.Trace('trace0', self)
        self.port.connect(self.trace0.item_port)

        self.trace1= avl.Trace('trace1', self)
        self.port.connect(self.trace1.item_port)

        self.dut = None


    async def run_phase(self):
        """
        Run phase for the example environment.
        This method is called to start the environment's operation.
        """
        self.raise_objection()
        for i in range(100):
            await Timer(10, units='ns')
            item = example_item(f"item_{i}", self)
            item.data = random.randint(0, 100)

            self.port.write(item)
            self.dut.data.value = item.data
        self.drop_objection()

@cocotb.test
async def test(dut):
    # Create a text based logfile
    avl.Log.set_logfile("avl_log.txt")

    e = example_env("env", None)
    e.dut = dut
    await e.start()
