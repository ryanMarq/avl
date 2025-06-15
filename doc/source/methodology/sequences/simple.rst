.. _simple_sequence:

Simple Sequence
===============

The most basic sequence is to implement the :any:`Sequence.body` method with a series of items to be started and finished.

.. code-block:: python

    async def body(self):
        for i in range(5):
            item = example_item(f'item_{i}', self)
            await self.start_item(item)
            item.randomize()
            await self.finish_item(item)

In the driver the user must simply set the done event to finish the item.

.. code-block:: python

    async def run_phase(self):
        while True:
            item = await self.seq_item_port.blocking_get()
            item.set_event('done')
            item.set_event('response', item, ok=True)


Full Example
------------

.. literalinclude:: ../../../../examples/sequences/simple/cocotb/example.py
    :language: python
