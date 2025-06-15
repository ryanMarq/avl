.. _with_response_sequence:

Sequence With Response
======================

AVL simplifies the request / response handshake by using the event mechanism built into the :doc:`avl.SequenceItem </modules/avl._core.sequence_item>` class.

The user can associate any callback function to the response and, optionally, wait for the response to be triggered.

This means responses can return out of order without the user having to construct a complex state machine to handle the responses.

.. code-block:: python

    class example_sequence(avl.Sequence):
        def __init__(self, name, parent=None):
            super().__init__(name, parent)

        def response_cb(self, item, ok=False):
            if ok:
                self.info(f'Item {item.name} ok')
            else:
                self.error(f'Item {item.name} not ok')

        async def body(self):
            for i in range(5):
                item = example_item(f'item_{i}', self)
                item.add_event('response', self.response_cb)

                await self.start_item(item)
                item.randomize()
                await self.finish_item(item)

                await item.wait_on_event('response')

The implementation in the driver is equally simple.

.. code-block:: python

    class example_driver(avl.Driver):
        def __init__(self, name, parent):
            super().__init__(name, parent)

        async def run_phase(self):
            while True:
                item = await self.seq_item_port.blocking_get()
                item.set_event('done')
                item.set_event('response', item, ok=True)

Full Example
------------

.. literalinclude:: ../../../../examples/sequences/with_response/cocotb/example.py
    :language: python
