.. _variable_structs:

Structs
=======

AVL provides a generic structs wrapper.

The main reason for including a struct wrapper is `Verilator <https://www.veripool.org/wiki/verilator>`_ flattens all \
structs into a single variable. This means that the user must manually manage the offsets of each field in the struct. \
This is error prone, difficult to debug and maintain.

Commercial simulators usually provide PLI/VPI access to individual fields in structs, but the :doc:`avl.Struct </modules/avl._core.struct>` \
can still be useful to ensure a test-bench works across all simulators.

The variables declared in the struct must be variations of the :doc:`avl.Var </modules/avl._core.var>` class, \
as these classes have understanding of the width and therefore can be used to pack and unpack the struct.

The declaration order of variables matches those of the Verilog struct syntax.

Example
-------

.. literalinclude:: ../../../examples/struct/cocotb/example.py
    :language: python
