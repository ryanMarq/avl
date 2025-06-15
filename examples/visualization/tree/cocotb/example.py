# Copyright 2024 Apheleia
#
# Description:
# Apheleia phase example


import avl
import avl.templates
import cocotb


@cocotb.test
async def test(dut):
    # Create the environment
    avl.Factory.set_variable("*.hdl", dut)
    avl.Factory.set_variable("*.clk", dut.clk)
    avl.Factory.set_variable("*.rst", dut.rst_n)
    avl.Factory.set_variable("env.cfg.n_agent", 2)

    e = avl.templates.VanillaEnv("env", None)

    # Display the hierarchy tree of the environment
    print(avl.Visualization.tree(e))
