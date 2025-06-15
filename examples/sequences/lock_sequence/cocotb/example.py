# Copyright 2024 Apheleia
#
# Description:
# Apheleia scoreboard example


import random

import avl
import cocotb
from cocotb.triggers import Combine, Timer


class example_item(avl.SequenceItem):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.value = 0

    def randomize(self):
        self.value = random.randint(0x0, 0xFF)


class example_sequence_without_lock(avl.Sequence):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.delay = 0

    async def body(self):
        for i in range(10):
            await Timer(self.delay, "ns")
            item = example_item(f"item_{i}", self)
            await self.start_item(item)
            item.value = 100
            await self.finish_item(item)


class example_sequence_with_lock(avl.Sequence):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.delay = 0

    async def body(self):
        for i in range(10):
            await Timer(self.delay, "ns")
            item = example_item(f"item_{i}", self)
            await self.start_item(item)
            item.value = i
            await self.finish_item(item)

            if i == 1:
                await self.get_sequencer().lock(self)
            elif i == 8:
                self.get_sequencer().unlock(self)


class example_driver(avl.Driver):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.count = 0

    async def run_phase(self):
        while True:
            item = await self.seq_item_port.blocking_get()
            self.info(f"Driving from sequence: {item._parent_sequence_.name} {item.value}")
            item.set_event("done")
            self.count += 1

    async def report_phase(self):
        if self.count != 20:
            self.error(f"Expected 20 items, got {self.count}")
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

        seq0 = example_sequence_without_lock("sequence_without_lock", self.sequencer)
        seq0.delay = 10
        t0 = await cocotb.start(seq0.start())
        seq1 = example_sequence_with_lock("sequence_with_lock", self.sequencer)
        seq1.delay = 20
        t1 = await cocotb.start(seq1.start())

        await Combine(t0, t1)
        self.drop_objection()


@cocotb.test
async def test(dut):
    e = example_env("env", None)
    await e.start()
