.. _phases:

AVL Phases
===========

.. inheritance-diagram:: avl._core.phase
    :parts: 0

Overview
--------

The AVL phases are a simplified version of the UVM phases. \
The phases are used to control the flow of the testbench and the DUT. \
The phases are implemented as a class with a number of methods that can be overridden by the user.

By default fewer phases are implemented than in UVM. \
This is to allow the user to implement only the phases they need. But equally users can reduce the number of phases \
if they wish.

avl_phase
---------

The :doc:`avl.Phase </modules/avl._core.phase>` class is the base class provides phase abstraction and \
objection mechanisms.

Unlike UVM all phases in AVL can consume time, but do not have too. If no objections are raise the phase will \
complete immediately.

The default phases are:

- RUN

- REPORT

avl.PhaseManager
-----------------

The :doc:`avl.PhaseManager </modules/avl._core.phase_manager>` is a singleton class that manages the phases.

It provides the mechanisms to add and remove phases from the phase list as well as managing the transition \
between phases.

Examples
--------

Adding Phases
~~~~~~~~~~~~~

.. literalinclude:: ../../../examples/phases/add_phase/cocotb/example.py
    :language: python

Removing Phases
~~~~~~~~~~~~~~~

.. literalinclude:: ../../../examples/phases/remove_phase/cocotb/example.py
    :language: python

UVM Phases
~~~~~~~~~~

.. literalinclude:: ../../../examples/adder/uvm_style/cocotb/example.py
