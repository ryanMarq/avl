# Copyright 2024 Apheleia
#
# Description:
# Apheleia phase example


import avl
import avl.templates
import cocotb
from cocotb.triggers import RisingEdge


class adder_item(avl.SequenceItem):
    def __init__(self, name, parent_sequence):
        super().__init__(name, parent_sequence)

        self.a = avl.Uint8(0, fmt=str)
        self.b = avl.Uint8(0, fmt=str)
        self.c = avl.Logic(0, fmt=str, auto_random=False, width=9)

    def randomize(self):
        super().randomize()
        self.c.value = self.a.value + self.b.value


class adder_driver(avl.templates.VanillaDriver):
    async def reset(self):
        self.hdl.valid_in.value = 0
        self.hdl.a.value = 0
        self.hdl.b.value = 0

    async def clear(self):
        await RisingEdge(self.clk)
        await self.reset()

    async def run_phase(self):
        await self.reset()

        await RisingEdge(self.hdl.clk)
        while True:
            item = await self.seq_item_port.blocking_get()

            while True:
                await RisingEdge(self.hdl.clk)
                if self.rst.value == 0:
                    await self.reset()
                else:
                    break

            self.hdl.valid_in.value = 1
            self.hdl.a.value = item.a.value
            self.hdl.b.value = item.b.value
            item.set_event("done")
            cocotb.start_soon(self.clear())


class adder_monitor(avl.templates.VanillaMonitor):
    async def collect_result(self, item):
        await RisingEdge(self.hdl.clk)
        if self.hdl.valid_out.value != 1:
            self.error(f"Expected valid_out to be 1, got {self.hdl.valid_out.value}")

        item.c.value = int(self.hdl.c.value)
        self.item_export.write(item)

    async def run_phase(self):
        while True:
            await RisingEdge(self.clk)

            if self.rst.value == 0:
                continue

            if self.hdl.valid_in.value == 1:
                item = adder_item("item", None)
                item.a.value = int(self.hdl.a.value)
                item.b.value = int(self.hdl.b.value)
                cocotb.start_soon(self.collect_result(item))


@cocotb.test
async def test(dut):
    # Create the environment
    avl.Factory.set_variable("*.hdl", dut)
    avl.Factory.set_variable("*.clk", dut.clk)
    avl.Factory.set_variable("*.rst", dut.rst_n)
    avl.Factory.set_variable("env.cfg.timeout_ns", 100000)
    avl.Factory.set_variable("*.n_items", 1000)
    avl.Factory.set_override_by_type(avl.templates.VanillaDriver, adder_driver)
    avl.Factory.set_override_by_type(avl.templates.VanillaMonitor, adder_monitor)
    avl.Factory.set_override_by_type(avl.SequenceItem, adder_item)

    e = avl.templates.VanillaEnv("env", None)

    await e.start()
