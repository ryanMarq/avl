.. _coverage_report:

AVL Coverage Reports
====================

AVL provides a simple script to generate coverage reports in HTML format. The script
is located in the `bin` directory of the AVL source tree. To generate a coverage report,
you need to run the script with the following command:

.. code-block:: shell

    $ bin/coverage_report.py --path <search path> --output <output_directory>

An index page will be created in the specified output directory, and it will contain links to
all the coverage reports found in the specified path. The script will search for all files
with the `.json` extension in the specified path and its subdirectories. The generated
HTML files will be placed in the specified output directory, and the index page will link to
them.


Merging Coverage Reports
------------------------

Adding the `--merge` option to the command will merge all the coverage reports found in the
specified path and its subdirectories into a single report. The merged report will be
generated in the specified output directory, and the index page will link to it. The
merged report will contain the coverage data from all the individual reports, allowing you
to see the overall coverage of your design.

Merging is performed on a per bin basis. If the cumulative total exceeds the at_least for the bin,
the bin is considered covered. The merged report will show the total coverage for each bin.

The command to generate a merged coverage report is as follows:

.. code-block:: shell

    $ bin/coverage_report.py --path <search path> --output <output_directory> --merge

Ranking Coverage Reports
------------------------

Adding the `--rank` option to the command will rank the coverage reports found in the
specified path and its subdirectories based on their coverage percentage. The ranked
reports will be generated in the specified output directory, and the index page will link to
them. Ranking provides 2 additional reports:

1. A report that shows the list of tests that contributed to the coverage of each bin.
2. A report that applies a score to the value of each test.

The score is calculated as follows:

- (1000 * number of unique bins) + (10 * number of rare bins (i.e. < 10 tests contributed)) + number of total bins

.. code-block:: shell

    $ bin/coverage_report.py --path <search path> --output <output_directory> --rank

The rank and merge options are orthogonal and can be used together.


Index Page
----------

.. image:: /images/avl_coverage_index.png
   :align: center

Report Page
-----------

.. image:: /images/avl_coverage_report.png
   :align: center

Example
-------

.. literalinclude:: ../../../examples/coverage/report/cocotb/example.py
    :language: python
