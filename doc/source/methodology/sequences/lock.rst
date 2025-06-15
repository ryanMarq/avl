.. _locking_sequence:

Locking Sequence
================

The :doc:`avl.Sequencer </modules/avl._core.sequencer>` provides :any:`Sequencer.lock` and :any:`Sequencer.lock` methods \
to allow the user to lock the sequencer and prevent other sequences from running.

The sequence will wait until it can acquire lock.

.. code-block:: python

    async def body(self):
        await self.get_sequencer().lock(self)
        for i in range(10):
            await Timer(self.delay, 'ns')
            item = example_item(f'item_{i}', self)
            await self.start_item(item)
            item.randomize()
            await self.finish_item(item)
        self.get_sequencer().unlock(self)


Full Example
------------

.. literalinclude:: ../../../../examples/sequences/lock_sequence/cocotb/example.py
    :language: python
