# Copyright 2024 Apheleia
#
# Description:
# Apheleia phase example


import avl
import cocotb


class example_env(avl.Env):
    def __init__(self, name, parent):
        super().__init__(name, parent)

        subjects = [
            "The cat",
            "A robot",
            "My neighbor",
            "An astronaut",
            "The teacher",
            "A dragon",
            "The dog",
            "A hacker",
            "A wizard",
            "The artist",
        ]
        verbs = [
            "eats",
            "builds",
            "paints",
            "jumps over",
            "writes",
            "discovers",
            "destroys",
            "fixes",
            "draws",
            "invents",
        ]
        objects = [
            "a sandwich",
            "a spaceship",
            "a masterpiece",
            "the fence",
            "a story",
            "a secret",
            "the city",
            "a computer",
            "a map",
            "a spell",
        ]

        for i in range(10):
            sentence = f"{subjects[i]} {verbs[i]} {objects[i]}."
            self.info(sentence)

        self.info("Now open avl_log.txt to see the log file created by avl_log.")


@cocotb.test
async def test(dut):
    # Create a text based logfile
    avl.Log.set_logfile("avl_log.txt")

    e = example_env("env", None)
    await e.start()
