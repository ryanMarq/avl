.. _coverage:

AVL Coverage
============

.. inheritance-diagram:: avl._core.coverage
    :parts: 1

Overview
--------

AVL provides functional coverage, similar to the featured provided in SystemVerilog.

- :doc:`avl.Covergroup </modules/avl._core.covergroup>` - The covergroup class provides a way to define coverage points in a class.

- :doc:`avl.Coverpoint </modules/avl._core.coverpoint>` - The coverpoint class provides a way to define coverage points in a class.

- :doc:`avl.Covercross </modules/avl._core.covercross>` - The covercross class provides a way to define cross coverage in a class.

Unlike SystemVerilog, AVL coverage is implemented in classes, not native data types. This allows for more flexibility \
and control over the coverage model.

For example, coverage bins can be defined by a variable. This variable can be set by the factory, allowing for easy \
coverage model changes at runtime.

Equally, coverage bins are added via function calls. Therefore the used can used inspection, loops or any other software construct \
to add coverage bins.

Bins
----

A bin can be defined by 3 definitions:

- Value - The sampled values matches any one of the given values (stored as a list)

- Range - The sampled value is within the given range (stored as a python range)

- Lambda Function: The lambda function returns True (stored as a lambda function)

Bins can be marked as illegal. This bins assert when a matching value is sampled.

Unlike SystemVerilog, bins are never ignored. As bins can be systematically added and removed, the user can \
ignore a bin by removing it from the coverage model.

Statistics
----------

AVL adds a significant enhancement to SystemVerilog coverage, allowing the user to collect statistics to :doc:`avl.Coverbin </modules/avl._core.coverbin>`.

When enabled, the rolling min, max, mean, variance and standard deviation of the sampled values is stored. \
`Welford's Algorithm <https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance>`_ is used to minimize the footprint.

The use of statistics allows users to collect more information than just that a bin has been satisfied. Data such as performance, \
latency, statistical distribution and other metrics can be collected.

Reports
-------

When :doc:`Covergroups </modules/avl._core.covergroup>` are added they are automatically registered with the global :doc:`avl.Coverage </modules/avl._core.coverage>` \
container.

On exit, all coverage is converted to a `pandas dataframe <pttps://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html>`_ \
and exported to a .json file.

This allows the user to easily merge, format and export coverage using the rich set of tools provided by the `pandas library <https://pandas.pydata.org/>`_.

Examples
--------

.. literalinclude:: ../../../examples/coverage/coverpoint/cocotb/example.py
    :language: python

.. literalinclude:: ../../../examples/coverage/covercross/cocotb/example.py
    :language: python

.. literalinclude:: ../../../examples/coverage/coverstat/cocotb/example.py
    :language: python
