.. _sequence:

avl.Sequence
============

.. inheritance-diagram:: avl._core.sequence
    :parts: 1


Sequences provide the mechanism to develop re-usable sequences of transactions that can be used to drive the DUT.

In general the structure of sequences has been preserved from UVM without the unnecessary complexity and \
hierarchy.

Sequences are stated and follow the same path as UVM. Users can implement callbacks at the :any:`Sequence.pre_start` and :any:`Sequence.post_start` \
stage as well as the :any:`Sequence.pre_body` and :any:`Sequence.post_body` stage.

By default all pre and post stages are empty.

As with UVM the :any:`Sequence.body` method should be overridden to implement the sequence.

.. note::

    The complexity of sequence ids, parent sequences and root sequences have all been removed. If the user wants to keep a \
    count of the sequence items or create relationships between sequences this is all easily possible using the standard \
    Pythonic way.

    Sequences can start other sequences just like any other :doc:`avl.Object </modules/avl._core.object>`.


.. graphviz::

   digraph flowchart {
        A [label="Start"];
        B [label="Pre-Start"];
        C [label="Pre-Body"];
        D [label="Body"];
        E [label="Post-Body"];
        F [label="Post-Start"];

        A -> B;
        B -> C;
        C -> D;
        D -> E;
        E -> F;
   }

Within the sequence items are stated and finished, just as in UVM. :any:`Sequence.pre_do` and :any:`Sequence.post_do` callbacks are implemented in the same way as UVM.

Starting an item:

.. graphviz::

   digraph flowchart {
        A [label="Start Item"];
        B [label="Wait For Grant"];
        C [label="Pre-Do"];

        A -> B;
        B -> B [label="Waiting"];
        B -> C [label="Granted"];
   }

Finishing an item:

.. graphviz::

   digraph flowchart {
        A [label="Finish Item"];
        B [label="Mid-Do"];
        C [label="Send Request"];
        D [label="Wait for Done"];
        E [label="Post-Do"];

        A -> B;
        B -> C;
        C -> D;
        D -> D [label="Waiting"];
        D -> E [label="Done"];

   }

Examples
--------

.. toctree::
   :maxdepth: 1
   :caption: Examples:

   simple
   with_response
   lock
