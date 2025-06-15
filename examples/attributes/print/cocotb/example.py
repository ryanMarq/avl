# Copyright 2024 Apheleia
#
# Description:
# Apheleia attributes example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        # Python variables
        self.dec_var = 100
        self.hex_var = 100
        self.custom_var = 100
        self.hex_list = [100, 200, 300]
        self.simple_dict = {"A": 1, "B": 2, "C": 3}

        self.set_field_attributes("hex_var", fmt=hex)
        self.set_field_attributes("hex_list", fmt=hex)
        self.set_field_attributes("custom_var", fmt=self.custom_fmt)

    def custom_fmt(self, value):
        return f"custom_var={value}"


@cocotb.test
async def test(dut):
    e = example_env("env", None)
    print(e)

    print("\n\n\n\n")

    e.set_table_fmt("github")
    print(e)
