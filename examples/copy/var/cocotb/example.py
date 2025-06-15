# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import copy

import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        # First simple example showing avl_var behaves as int
        x = 0
        y = copy.copy(x)
        y = 1
        assert(x == 0 and y == 1)

        z = copy.deepcopy(x)
        z = 2
        assert(x == 0 and z == 2)

        x = avl.Int("x", 0)
        y = copy.copy(x)
        y.value = 1
        assert(x.value == 0 and y.value == 1)

        z = copy.deepcopy(x)
        z.value = 2
        assert(x.value == 0 and z.value == 2)

        # Show randomization doesn't bleed after copy
        x = avl.Int("x", 0, auto_random=True)
        y = copy.copy(x)
        z = copy.deepcopy(x)

        x.randomize(hard=[lambda value: value == 100])
        y.randomize(hard=[lambda value: value == 200])
        z.randomize(hard=[lambda value: value == 300])
        assert(x.value == 100 and y.value == 200 and z.value == 300)

        # Show constraints are copied
        x = avl.Int("x", 0, auto_random=True)
        x.add_constraint("c", lambda value: value == 10)
        y = copy.copy(x)
        z = copy.deepcopy(x)
        x.randomize()
        y.randomize()
        z.randomize()
        assert(x.value == 10 and y.value == 10 and z.value == 10)

        # Change constraint and show it doesn't bleed
        x.add_constraint("c", lambda value: value == 20)
        x.randomize()
        y.randomize()
        z.randomize()
        assert(x.value == 20 and y.value == 10 and z.value == 10)

        # Show it works with float
        x = avl.Float("x", 0.0, auto_random=True)
        y = copy.copy(x)
        z = copy.deepcopy(x)
        x.randomize(hard=[lambda value: value == 1.0])
        y.randomize(hard=[lambda value: value == 2.0])
        z.randomize(hard=[lambda value: value == 3.0])
        assert(x.value == 1.0 and y.value == 2.0 and z.value == 3.0)

@cocotb.test
async def test(dut):
    example_env("env", None)
