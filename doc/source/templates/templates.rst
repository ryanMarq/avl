.. _templates:

AVL Templates
=============

One of the biggest obstacles with UVM is the sheer amount of code required to construct simple \
testbenches.

Using templates, AVL aims to reduce this overhead without enforcing a specific structure, or methodology \
on the user.

By default AVL provides a :doc:`avl.Templates.vanilla </modules/avl.templates._vanilla>` template for an environment, containing a configurable number of agents and a scoreboard. \
Each of the agents can be configured to be active or passive.

By overriding variables and types using the factory a testbench can be created with minimal effort and code.

Example
-------

The provided adder example shows how simple it is to extend a template to create a testbench.

.. literalinclude:: ../../../examples/adder/template/cocotb/example.py
    :language: python
