.. _sequence_item:

avl.SequenceItem
=================

.. inheritance-diagram:: avl._core.sequence_item
    :parts: 1

The :doc:`avl.SequenceItem </modules/avl._core.sequence_item>` is the base class for all sequence items and \
extends :doc:`avl.Transaction </modules/avl._core.transaction>`.

Unlike UVM synchronization is encapsulated in the transaction and not the components. This avoids the \
complexity of having to track and re-associate to a specific item.


The :doc:`avl.SequenceItem, </modules/avl._core.sequence_item>` adds the "done" and "response" events to :doc:`avl.Transaction </modules/avl._core.transaction>` and handles the \
association with the :doc:`avl.Sequencer </modules/avl._core.sequencer>`.
