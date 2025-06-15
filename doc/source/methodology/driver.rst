.. _driver:

avl.Driver
============

.. inheritance-diagram:: avl._core.driver
    :parts: 1


Drivers provide the same purpose as in UVM, driving the sequence item to the DUT.

Unlike UVM the interaction with HDL is not limited to virtual interfaces. The user can implement the driver to interact with the DUT in any way they see fit.

Connecting the driver to HDL is best done using the factory.

.. code-block:: python

    self.hdl = avl.Factory.get_variable(f"{self.get_full_name()}.hdl", None)
