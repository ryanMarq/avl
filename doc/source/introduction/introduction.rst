Welcome to AVL's Documentation
==============================

What is AVL?
------------

**AVL** is the Apheleia Verification Library.

AVL has been developed by experienced, industry professional verification engineers to provide a methodology \
and library of base classes for developing functional verification environments in `Python <https://www.python.org/downloads/>`_.

Why Use AVL?
------------

`UVM <https://accellera.org/community/uvm>`_ has been the industry standard for developing verification environments \
for many years. However, UVM is written in SystemVerilog and requires a SystemVerilog simulator to run. \
UVM has provided much of the methodology and best practices for developing verification environments, but has not evolved \
to add the usability and flexibility that modern software development practices have brought to the software industry.

`cocotb <https://docs.cocotb.org/en/stable/>`_ brings the power of Python, including the rich family of well maintained libraries \
to the verification engineer. However, cocotb is a co-simulation environment and does not provide the same level of methodology \
and best practices that UVM has provided.

AVL is built upon the `cocotb <https://docs.cocotb.org/en/stable/>`_ framework and provides a set of base classes \
that provide the `HDL <https://en.wikipedia.org/wiki/Hardware_description_language>`_ constructs, and methodologies that are \
familiar to the verification engineer whist focusing on the flexibility and usability that Python provides.

So AVL implements UVM in Python?
--------------------------------

No. The aim of AVL is not to replicate UVM in Python. The aim of AVL is to provide a set of base classes that \
provide the constructs and methodologies that are familiar to the verification engineer, but in a Pythonic way. \
AVL is not a direct translation of UVM into Python, but rather a re-imagining of the verification environment in Python.

Familiar `UVM constructs <https://uvm-docs-online.readthedocs.io/en/latest/_static/uvm-1.0p1/docs/html/index.html>`_ such as \
Sequences, Drivers and Monitors have been maintained in AVL, but do not rigidly follow the UVM methodology.

Where appropriate AVL has taken inspiration from UVM, but has not been constrained by the limitations of SystemVerilog \
and deliberately simplified, modified or enhanced constructs to provide a simpler, and more usable implementation.

AVL follows the cocotb framework to benefit from it's vendor independence and HDL integration, but looks to add \
`HDL data types <https://www.chipverify.com/systemverilog/systemverilog-datatypes>`_ and features such as \
random constraints that are essential for developing large scale, maintainable verification environments.

Who is AVL Aimed At?
--------------------

AVL is aimed at a range of verification engineers, from novices to seasoned industry experts who are looking to develop \
verification environments more efficiently and effectively.

Although the open-source, AVL is not solely intended for small scale, or hobby projects. By sitting on top of cocotb, with its \
integration to Verilator, AVL can develop whole project scale verification environments that run on a single laptop. But equally, \
by providing the advanced features usually reserved for high-end, paid simulators, AVL can be used to develop verification environments \
to met the demands of large scale, high-end semiconductor projects.

By taking advantage of Python's rich library of tools and the flexibility of the cocotb framework, AVL aims to provide \
a more modern, flexible and usable verification environment that can be used by a wide range of engineers.

By removing the testbench and test code from the traditional event driven UVM environment, AVL removes almost all compilation \
time from the verification process. This allows the engineer to develop and run tests in a fraction of the time it would take \
using a traditional UVM environment, without limiting the scale and re-use required for large scale verification environments.




