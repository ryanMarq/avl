.. _visualization:

AVL Visualization
=================

.. inheritance-diagram:: avl._core.visualization
    :parts: 0

Overview
--------

In order to help debug and understand the hierarchy of the AVL components, AVL provides a \
visualization module that can be used to generate a graphical representation of the \
component hierarchy.

Two types of visualizations are provided:

- Class Hierarchy Tree provided by `anytree library <https://anytree.readthedocs.io/en/latest/>`_

- Class Hierarchy Diagram provided by `graphviz library <https://graphviz.gitlab.io/>`_

Tree Visualization
------------------

.. literalinclude:: ../../../examples/visualization/tree/cocotb/example.py
    :language: python

The output looks like this:

.. code-block:: text

    env
    ├── cfg
    ├── agent0
    │   ├── cfg
    │   ├── sqr
    │   │   └── seq_item_export
    │   ├── drv
    │   ├── mon
    │   │   └── item_export
    │   ├── model
    │   │   └── item_export
    │   └── sb
    └── agent1
        ├── cfg
        ├── sqr
        │   └── seq_item_export
        ├── drv
        ├── mon
        │   └── item_export
        ├── model
        │   └── item_export
        └── sb

Diagram Visualization
---------------------

.. literalinclude:: ../../../examples/visualization/diagram/cocotb/example.py
    :language: python

The output looks like this:

.. image:: /images/visualization.png
   :align: center
