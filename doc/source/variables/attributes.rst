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

AVL uses `Tabulate <https://pypi.org/project/tabulate/>`_ to format the string representation of a class. By default the table is formatted using the "grid" format, \
but the user can customize.

However, not all tabulate table format support sub-tables nicely. The following formats are shown in the example below to work nicely and can be set by calling :any:`Object.set_table_fmt`:

+------------------+
| Format           |
+==================+
| grid (default)   |
+------------------+
| fancy_grid       |
+------------------+
| simple_grid      |
+------------------+
| presto           |
+------------------+
| psql             |
+------------------+
| orgtbl           |
+------------------+
| rst              |
+------------------+
| jira             |
+------------------+



.. literalinclude:: ../../../examples/attributes/print/cocotb/example.py
    :language: python

Expected output (grid format):

.. code-block:: none

    +-------------+----------------+
    | name        | env            |
    +-------------+----------------+
    | dec_var     | 100            |
    +-------------+----------------+
    | hex_var     | 0x64           |
    +-------------+----------------+
    | custom_var  | custom_var=100 |
    +-------------+----------------+
    | hex_list    | 0x64           |
    |             | 0xc8           |
    |             | 0x12c          |
    +-------------+----------------+
    | hex_dict    | A: 0x64        |
    |             | B: 0xc8        |
    |             | C: 0x12c       |
    +-------------+----------------+
    | list_list   | -              |
    |             |   0            |
    |             |   1            |
    |             | -              |
    |             |   2            |
    |             |   3            |
    |             | -              |
    |             |   4            |
    |             |   5            |
    +-------------+----------------+
    | simple_dict | A: 1           |
    |             | B: 2           |
    |             | C: 3           |
    +-------------+----------------+
    | list_dict   | X:             |
    |             |   a            |
    |             |   b            |
    |             | Y:             |
    |             |   0            |
    +-------------+----------------+
    | mixed       | -              |
    |             |   dict:        |
    |             |     value1     |
    |             |     value2     |
    |             | -              |
    |             |   list0        |
    |             |   list1        |
    |             |   0b1100100    |
    +-------------+----------------+
    | obj         | +------+-----+ |
    |             | | name | obj | |
    |             | +------+-----+ |
    +-------------+----------------+


Transposing
-----------

Depending on the class contents to may be useful to transpose the table representation of the class. This can be done by setting the `transpose` argument to `True` when calling \
:any:`Object.set_table_fmt`.

Expected output (grid format):

.. code-block:: none

    +------+---------+---------+----------------+----------+----------+-----------+-------------+-----------+-------------+----------------+
    | name | dec_var | hex_var | custom_var     | hex_list | hex_dict | list_list | simple_dict | list_dict | mixed       | obj            |
    +------+---------+---------+----------------+----------+----------+-----------+-------------+-----------+-------------+----------------+
    | env  | 100     | 0x64    | custom_var=100 | 0x64     | A: 0x64  | -         | A: 1        | X:        | -           | +------+-----+ |
    |      |         |         |                | 0xc8     | B: 0xc8  |   0       | B: 2        |   a       |   dict:     | | name | obj | |
    |      |         |         |                | 0x12c    | C: 0x12c |   1       | C: 3        |   b       |     value1  | +------+-----+ |
    |      |         |         |                |          |          | -         |             | Y:        |     value2  |                |
    |      |         |         |                |          |          |   2       |             |   0       | -           |                |
    |      |         |         |                |          |          |   3       |             |           |   list0     |                |
    |      |         |         |                |          |          | -         |             |           |   list1     |                |
    |      |         |         |                |          |          |   4       |             |           |   0b1100100 |                |
    |      |         |         |                |          |          |   5       |             |           |             |                |
    +------+---------+---------+----------------+----------+----------+-----------+-------------+-----------+-------------+----------------+

Recursion
---------

AVL supports recursive printing of classes. This is useful when the class contains nested classes or variables. However, this can lead to very large output, \
so it can be dictated by setting the `recurse` argument to `True` when calling :any:`Object.set_table_fmt`.

Expected output (grid format):

.. code-block:: none

    +------+---------+---------+----------------+----------+----------+-----------+-------------+-----------+-------------+--------------------------------+
    | name | dec_var | hex_var | custom_var     | hex_list | hex_dict | list_list | simple_dict | list_dict | mixed       | obj                            |
    +------+---------+---------+----------------+----------+----------+-----------+-------------+-----------+-------------+--------------------------------+
    | env  | 100     | 0x64    | custom_var=100 | 0x64     | A: 0x64  | -         | A: 1        | X:        | -           | type(Object) at 0x7a13c9fd3440 |
    |      |         |         |                | 0xc8     | B: 0xc8  |   0       | B: 2        |   a       |   dict:     |                                |
    |      |         |         |                | 0x12c    | C: 0x12c |   1       | C: 3        |   b       |     value1  |                                |
    |      |         |         |                |          |          | -         |             | Y:        |     value2  |                                |
    |      |         |         |                |          |          |   2       |             |   0       | -           |                                |
    |      |         |         |                |          |          |   3       |             |           |   list0     |                                |
    |      |         |         |                |          |          | -         |             |           |   list1     |                                |
    |      |         |         |                |          |          |   4       |             |           |   0b1100100 |                                |
    |      |         |         |                |          |          |   5       |             |           |             |                                |
    +------+---------+---------+----------------+----------+----------+-----------+-------------+-----------+-------------+--------------------------------+

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


