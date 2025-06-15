# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb


class example_env(avl.Env):

    async def blocking_push_test(self, f : avl.Fifo) -> None:
        t = cocotb.start_soon(self.blocking_push(f, 10, 42))
        await self.delayed_pop(f, 10, 42)
        await t
        assert(len(f) == 4)

    async def blocking_push(self, f : avl.Fifo, d : int, v : int) -> int:
        await f.blocking_push(v)
        assert(cocotb.utils.get_sim_time(units="ns") == d)

    async def delayed_pop(self, f : avl.Fifo, d : int, v : int) -> None:
        await cocotb.triggers.Timer(d, "ns")

        r = f.pop(0)
        assert(r == 0)

    def __init__(self, name, parent):
        super().__init__(name, parent)

        # Start with empty list
        f = avl.Fifo(4)
        assert(len(f) == 0)

        # Check push
        for i in range(10):
            f.append(i)
        assert(len(f) == 4)

        # Check pop
        for i in range(4):
            assert(f.pop(0) == i)

        # Check empty
        assert(not f)

        # Check init
        f = avl.Fifo(8, 0, 1, 2)
        assert(len(f) == 3)

        # Check extend
        f.extend([3, 4, 5])
        assert(len(f) == 6)

        # Check clear
        f.clear()
        assert(len(f) == 0 and not f)

        # Check insert - should raise NotImplementedError
        f = avl.Fifo(4, 0, 1, 2, 3)
        try:
            f.insert(0, 42)
        except NotImplementedError:
            pass
        assert(len(f) == 4)

        # Check remove - should raise NotImplementedError
        try:
            f.remove(2)
        except NotImplementedError:
            pass
        assert(len(f) == 4)



    async def run_phase(self):
        self.raise_objection()

        f = avl.Fifo(4, 0, 1, 2, 3) # Initialize to full
        await self.blocking_push_test(f)

        self.drop_objection()

@cocotb.test
async def test(dut):
    e = example_env("env", None)
    await e.start()
