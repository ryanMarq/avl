.. _base:

AVL Base classes
================

AVL base classes follow the same basic format as `UVM <https://accellera.org/community/uvm>`_ base classes. \
However, the variables and methods have not been religiously copied from the UVM source.

avl_object
----------

.. inheritance-diagram:: avl._core.object
    :parts: 1

The avl_object class is the base class for all classes in the library. \
It provides the following features:

- :ref:`Factory <factory>`

- :ref:`Logging <logging>`

  - :ref:`Variable formatting <variable_attributes>`

- :ref:`Comparision <variable_attributes>`

- :ref:`Randomization and constraints <constraints>`

Unlike UVM avl_objects always require a parent, however this can be None.

By always providing a parent, the factory is easier to use and quicker.

avl_component
-------------

.. inheritance-diagram:: avl._core.component
    :parts: 1

The avl_component class extends avl_object and provides the following features:

- Hierachy

- :ref:`Phasing and Objections <phases>`
