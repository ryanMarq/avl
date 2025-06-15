.. _variable_attributes:

Variable Attributes
===================

AVL provides similar functionality to the UVM field macros, without the unnecessary verbosity.

The is also avoids the long running arguments over whether the user should use the macros or not.

Only the most common attributes are supported, and the user is encouraged to use the Pythonic way of setting attributes.

- Automatic inclusion in class comparison
- Custom string formatting

Attributes can be:

- Set  :any:`Object.set_field_attributes`

- Retrieved :any:`Object.get_field_attributes`

- Cleared :any:`Object.remove_field_attributes`

.. note::

    AVL implements no additional functionality to support copying.

    If a user wishes to copy a class or variable the should follow the well understood `Python copy <https://docs.python.org/3/library/copy.html>`_ library.

Naming Conventions
------------------
To keep things simple, all variables beginning with an underscore ("_") are considered private and should not be accessed directly. Equally \
all private variables are excluded from all in-built support functions

This rule has been applied to all AVL base classes.


Printing / String Formatting
----------------------------

When using :doc:`avl.Var </modules/avl._core.var>` variables, the user can set the string formatting of the variable as part of the class constructor.

For regualar Python variables the default string representation is used, unless a specific string format it registered.

By default all non-private class variables are included in the string representation of an :doc:`avl.Object </modules/avl._core.object>` class.

AVL uses `Tabulate <https://pypi.org/project/tabulate/>`_ to format the string representation of a class. By default the table is formatted using the "outline" format, \
but the user can customise.

.. literalinclude:: ../../../examples/attributes/print/cocotb/example.py
    :language: python

Expected output:

.. code-block:: none

    +--------------+----------------+
    | Field        | Value          |
    +==============+================+
    | name         | env            |
    | dec_var      | 100            |
    | hex_var      | 0x64           |
    | custom_var   | custom_var=100 |
    | hex_list:    |                |
    | [0]          | 0x64           |
    | [1]          | 0xc8           |
    | [2]          | 0x12c          |
    | simple_dict: |                |
    | [A]          | 1              |
    | [B]          | 2              |
    | [C]          | 3              |
    +--------------+----------------+





    | Field        | Value          |
    |--------------|----------------|
    | name         | env            |
    | dec_var      | 100            |
    | hex_var      | 0x64           |
    | custom_var   | custom_var=100 |
    | hex_list:    |                |
    | [0]          | 0x64           |
    | [1]          | 0xc8           |
    | [2]          | 0x12c          |
    | simple_dict: |                |
    | [A]          | 1              |
    | [B]          | 2              |
    | [C]          | 3              |


Comparison
----------

By default all non-private class variables are included in the comparison of two :doc:`avl.Object </modules/avl._core.object>` classes.

In addition a bi-directional comparison is optionally performed (on by default). This ensures that all fields in both classes are compared i.e. if a field is missing from either class \
the comparison will fail.

.. literalinclude:: ../../../examples/attributes/compare/cocotb/example.py

Expected output:

.. code-block:: none

     0.00ns INFO     cocotb.regression                  running test (1/1)
      0.0ns INFO     None                               Field "name" comparison passed (a == a)
      0.0ns INFO     None                               Field "var_b" comparison passed (1 == 1)
      0.0ns INFO     None                               Field "name" comparison passed (a == a)
      0.0ns INFO     None                               Field "var_b" comparison passed (1 == 1)
     0.00ns INFO     cocotb.regression                  test passed


