.. _factory:

AVL Factory
===========

.. inheritance-diagram:: avl._core.factory
    :parts: 1

Overview
--------

The AVL factory provides the same functionality as the UVM factory without the complexity \
of the class::type_id::create() syntax as the factory is native to the :doc:`avl.Object </modules/avl._core.object>` class.

All classes that exend the :doc:`avl.Object </modules/avl._core.object>` class can be overridden by the factory. \

Override by Type
----------------
.. literalinclude:: ../../../examples/factory/override_component_by_type/cocotb/example.py
    :language: python

Override by Instance
--------------------

There is no override by name in AVL. Instead, the factory can be used to override by instance. As wildcards \
(see below) are supported names can always be found.

.. literalinclude:: ../../../examples/factory/override_component_by_instance/cocotb/example.py
    :language: python

Wildcards are also supported. These are implemented using the Python `fnmatch <https://docs.python.org/3/library/fnmatch.html>`_ module. \
If multiple matches are found, the most specific match is used :any:`Factory.specificity`.

.. literalinclude:: ../../../examples/factory/override_component_by_instance_with_wildcard/cocotb/example.py
    :language: python

Variables
---------

Similar to the UVM config_db / resource_db variables can be set and retrieved from the factory. \
No copying is done automatically, classes are passed by reference and literals by value. \

This means :doc:`avl.Var </modules/avl._core.var>` objects can be easily shared, as can cocotb hdl handles.

The same wildcards as for the override by instance are supported :any:`Factory.specificity`. \

.. literalinclude:: ../../../examples/factory/variables/cocotb/example.py
