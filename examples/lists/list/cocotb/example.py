# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb


class example_env(avl.Env):

    async def blocking_pop_test(self, lst : avl.List) -> None:
        cocotb.start_soon(self.delayed_push(lst, 10, 42))
        r = await self.blocking(lst)

        assert(r == 42)
        assert(cocotb.utils.get_sim_time(units="ns") == 10)

    async def blocking(self, lst : avl.List) -> int:
        return await  lst.blocking_pop()

    async def delayed_push(self, lst : avl.List, d, v) -> None:
        await cocotb.triggers.Timer(d, "ns")
        lst.append(v)

    def __init__(self, name, parent):
        super().__init__(name, parent)

        # Start with empty list
        lst = avl.List()
        assert(len(lst) == 0)

        # Check push
        for i in range(10):
            lst.append(i)
        assert(len(lst) == 10)

        # Check pop
        for i in range(10):
            assert(lst.pop(0) == i)

        # Check empty
        assert(not lst)

        # Check init
        lst = avl.List(0, 1, 2)
        assert(len(lst) == 3)

        # Check extend
        lst.extend([3, 4, 5])
        assert(len(lst) == 6)

        # Check insert
        lst.insert(0, -1)
        assert(lst[0] == -1)

        # Check remove
        lst.remove(3)
        assert(len(lst) == 6 and lst[4] == 4)

        # Check clear
        lst.clear()
        assert(len(lst) == 0 and not lst)

    async def run_phase(self):
        self.raise_objection()

        lst = avl.List()
        await self.blocking_pop_test(lst)

        self.drop_objection()

@cocotb.test
async def test(dut):
    e = example_env("env", None)
    await e.start()
