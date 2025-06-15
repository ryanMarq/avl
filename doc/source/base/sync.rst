.. _sync:

AVL Synchronization and TLM
============================

AVL provides a simple and flexible synchronization mechanism, similar to the UVM TLM.

The mechansim is based on the following classes:

avl_list
----------

.. inheritance-diagram:: avl._core.list
    :parts: 1

The :doc:`avl.List </modules/avl._core.list>` is extended from the `Python List <https://docs.python.org/3/tutorial/datastructures.html>`_ variable \
and as such all methods familiar to Python users are available.

The :doc:`avl.List </modules/avl._core.list>` provides adds the :any:`List.blocking_pop` method and the alias :any:`List.blocking_get` method \
to wait on an item being available in the list.

.. code-block:: python

    async def run_phase(self):
    while True:
        item = await self.seq_item_port.blocking_get()
        self.info(f'New Item: {item}')

avl_fifo
--------

.. inheritance-diagram:: avl._core.fifo
    :parts: 1

The :doc:`avl.Fifo </modules/avl._core.fifo>` is extended from :doc:`avl.List </modules/avl._core.list>` and provides a FIFO queue.

When attempting to append, extend or insert the method will block until there is space in the FIFO.

avl_port
---------

.. inheritance-diagram:: avl._core.port
    :parts: 1

The :doc:`avl.Port </modules/avl._core.port>` is equivalent the the UVM port class, but also serves as the TLM port in sequencers.

Effectively the :doc:`avl.Port </modules/avl._core.port>` provides the one-to-many communication mechanism between components.

