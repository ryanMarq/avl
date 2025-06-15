# Copyright 2024 Apheleia
#
# Description:
# Apheleia scoreboard example


import random

import avl
import cocotb
from cocotb.triggers import Timer


class example_item(avl.SequenceItem):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.value = 0

    def randomize(self):
        self.value = random.randint(0x0, 0xFF)


class example_sub_sequence(avl.Sequence):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.delay = 0

    async def body(self):
        for i in range(5):
            await Timer(self.delay, "ns")
            item = example_item(f"item_{i}", self)
            await self.start_item(item)
            item.randomize()
            await self.finish_item(item)


class example_sequence(avl.Sequence):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)

    async def body(self):
        for i in range(5):
            delay = random.randint(0, 100)
            seq = example_sub_sequence(f"sub_sequence_{i}", self)
            seq.delay = delay
            await cocotb.start(seq.start())


class example_driver(avl.Driver):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.count = 0

    async def run_phase(self):
        while True:
            item = await self.seq_item_port.blocking_get()
            self.debug(f"Driving from sub_sequence: {item._parent_sequence_.name}")
            item.set_event("done")
            self.count += 1

    async def report_phase(self):
        if self.count != 25:
            self.error(f"Expected 25 items, got {self.count}")
        else:
            self.info("All items driven")


class example_sequencer(avl.Sequencer):
    def __init__(self, name, parent):
        super().__init__(name, parent)


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.driver = example_driver("driver", self)
        self.sequencer = example_sequencer("sequencer", self)

        self.sequencer.seq_item_export.connect(self.driver.seq_item_port)

    async def run_phase(self):
        self.raise_objection()

        seq = example_sequence("sequence", self.sequencer)
        await seq.start()

        await Timer(1000, "ns")

        self.drop_objection()


@cocotb.test
async def test(dut):
    e = example_env("env", None)
    await e.start()
