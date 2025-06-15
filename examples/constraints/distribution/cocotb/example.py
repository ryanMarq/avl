# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import random

import avl
import cocotb
import matplotlib.pyplot as plt
import numpy as np


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        self.a = avl.Logic("a", 0, width=8, fmt=hex)
        self.a.add_constraint(
            "d_0", lambda x: x == random.choices([0, 1, 2, 3], k=1, weights=[1, 2, 4, 8])[0]
        )

        self.b = avl.Logic("b", 0, width=32, fmt=hex)
        self.b.add_constraint("d_1", lambda x: x == int(np.random.normal(100, 3)))


@cocotb.test
async def test(dut):
    a = {}
    for i in range(4):
        a[i] = 0

    b = {}
    for i in range(200):
        b[i] = 0

    e = example_env("env", None)
    for _ in range(100):
        e.randomize()
        a[e.a.value] += 1
        b[e.b.value] += 1

    plt.figure(1)
    plt.bar(a.keys(), a.values())
    plt.savefig("a.png")

    plt.figure(2)
    plt.bar(b.keys(), b.values())
    plt.savefig("b.png")
