.. _logging:

AVL Logging
============

AVL logging sits on top of the `cocotb logging <https://docs.cocotb.org/en/stable/writing_testbenches.html#logging>`_ system.

However, it provides a few additional features:

- It's implemented in a singleton class so you can create groups that are shared across processes.

- It allows for a range of commonly used human and machine readable file formats to be generated.

The choice of file format is dictated by the file extension of the log file.

Supported file formats are:

- `csv <https://docs.python.org/3/library/csv.html>`_

- `json <https://docs.python.org/3/library/json.html>`_

- `yaml / yml <https://pyyaml.org/wiki/PyYAMLDocumentation>`_

- `md (markdown) <https://python-markdown.github.io/>`_

- `rst (restructured text) <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_

- txt (A Simply formatted table with headers is generated)

`cocotb logging <https://docs.cocotb.org/en/stable/writing_testbenches.html#logging>`_ is used to log messages to the console.


.. literalinclude:: ../../../examples/logging/simple/cocotb/example.py
