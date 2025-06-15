.. _scoreboard_indexed:


avl.IndexedScoreboard
======================

.. inheritance-diagram:: avl._core.scoreboard_indexed
    :parts: 1

Indexed scoreboards for interfaces or buses where the data may be out of order within the bus, but is actually \
constructed from multiple in-order streams. This applies to any threaded interface such as AXI or PCIe.

The indexed scoreboard automatically constructs multiple in-order scoreboards and compares the items in the correct order.

The user must simply implement the :any:`IndexedScoreboard.get_index` and call the :any:`IndexedScoreboard.set_indices` to define\
the individual streams and assign the item to the correct instance.

.. image:: /images/avl_scoreboard_indexed.png
   :align: center

Example
-------

.. literalinclude:: ../../../examples/scoreboard/indexed/cocotb/example.py
    :language: python


