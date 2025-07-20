.. _trace:

AVL Trace
=================

.. inheritance-diagram:: avl._core.trace
    :parts: 0

Overview
--------

ACL provides a trace mechanism to help debug a stream of transactions sent over a port. \

This mechanism can use used however the user sees helpful, but is primarily intended to be used in conjunction with the \
a :doc:`avl.Monitor </modules/avl._core.monitor>` component which observes and packages transactions from the HDL.\

The mechanism is super simple and generate a `Comma-Separated Values (csv) file <https://en.wikipedia.org/wiki/Comma-separated_values/>`_ \
with one row per transaction.

The columns can be define in the trace file configuration, however if left None one column will be created for each public item attribute.

In addition 2 columns "_timestamp_" and "_path_" are automatically added to the trace file indicating the time the object was received by the trace component,\
and the path to the object in the AVL tree.

Tools
-----

AVL provides a simple tool to read, merge, sort and query the trace files to make debug simple.

.. code-block:: bash

    usage: avl-trace-analysis [-h] --tracefile TRACEFILE [TRACEFILE ...] [--query QUERY] [--sort SORT] [--output OUTPUT] [--debug]

    Analyze and visualize AVL trace data

    options:
      -h, --help            show this help message and exit
      --tracefile TRACEFILE [TRACEFILE ...]
                            Trace file(s) to analyze.
      --query QUERY         Query to filter trace data.
      --sort SORT           Column to sort by.
      --output OUTPUT       Output HTML file name.
      --debug               Enable debug mode for detailed output.


For simple searching and ordering the output can be sent stdout as a markdown table:

.. code-block:: bash

    avl-trace-analysis --tracefile env.trace0.csv env.trace1.csv --sort data --query "data >= 98"
    +---------------+------------+---------+--------+
    |   _timestamp_ | _path_     | name    |   data |
    +===============+============+=========+========+
    |           420 | env.trace0 | item_41 |     98 |
    +---------------+------------+---------+--------+
    |           440 | env.trace0 | item_43 |     98 |
    +---------------+------------+---------+--------+
    |           440 | env.trace1 | item_43 |     98 |
    +---------------+------------+---------+--------+
    |           420 | env.trace1 | item_41 |     98 |
    +---------------+------------+---------+--------+
    |           960 | env.trace0 | item_95 |    100 |
    +---------------+------------+---------+--------+
    |           170 | env.trace0 | item_16 |    100 |
    +---------------+------------+---------+--------+
    |           170 | env.trace1 | item_16 |    100 |
    +---------------+------------+---------+--------+
    |           960 | env.trace1 | item_95 |    100 |
    +---------------+------------+---------+--------+


When more complex analysis is required, or the amount of data is large the --output option can be used to generate an HTML file with \
the results. This file can be opened in a web browser and provides a simple interface to filter, sort and search the data.

Example
-------

.. literalinclude:: ../../../examples/trace/simple/cocotb/example.py
    :language: python

T
