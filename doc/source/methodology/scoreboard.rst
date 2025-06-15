.. _scoreboards:

AVL Scoreboards
===============

Scoreboards provide an essential part of verification environments, but error prone and often \
lack basic functionality.

AVL provides 2 simple scoreboard implementations that are simple to extend and catch the most common \
errors.

1. Ensuring a minimum number of items are compared. This avoids the common use-case where a scoreboard has been forgotten to be connected to the DUT.

2. Ensuring that all items have been compared. This avoids the common use-case where items are left in the scoreboard un-compared at the end of the simulation.

The AVL scoreboards are connected using a pair of lists (:doc:`avl.List </modules/avl._core.list>`).

When both ports contain items, the scoreboard will pop from the list using the :any:`List.blocking_pop` method and call \
a bi-directional :any:`Object.compare`.

.. toctree::
    :maxdepth: 1

    scoreboard_simple
    scoreboard_indexed
