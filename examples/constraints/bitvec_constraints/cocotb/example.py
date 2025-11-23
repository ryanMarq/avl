# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb
from z3 import Extract


class Item(avl.Object):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = avl.Logic(0, width=32)

        self.add_constraint("object_bitmask",
            lambda a: Extract(7, 0, a) == 0b0000_0110,
            self.a)
        



@cocotb.test
async def test(dut):

    # Object Constraint Test
    item = Item("item", None)
    item.randomize()

    # Avl should have randomized the item, not used
    # the simplest case (a == 6). This assertion may fail 1 in 16777216
    # times.
    assert item.a != 6 


    # Var Constraint Test
    b = avl.Logic(0, width=32)
    b.add_constraint("var_bitmask",
        lambda b: Extract(5, 3, b) == 0b101)
    b.randomize()

    # This assertion may fail 1 in 536870912 times
    assert b != 0b101 << 3