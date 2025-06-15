.. _env:

avl.Env
=======

.. inheritance-diagram:: avl._core.Env
    :parts: 1

The :doc:`avl.Env </modules/avl._core.env>` module is intended to be the top-level environment for the \
testbench and instantiated in the cocotb test.

On top of providing the same functionalities inherited from the :doc:`avl.Component </modules/avl._core.component>` \
class, the :doc:`avl.Env </modules/avl._core.env>` module also provides the following features:

Clocks
------

The clock method provided by AVL wraps the cocotb Clock() method, but defines the clock in terms \
of frequency rather than in terms of period (a much more common way to refer to clocks in specifications).

.. code-block:: python

    await cocotb.start(self.clock(self.dut.clk, freq_mHz=100))

Resets
------

Synchroneous and asynchronous resets, of either polarity, methods are also provided.

Synchroneous resets are defined in terms of clock cycles:

.. code-block:: python

    await cocotb.start(self.sync_reset(self.dut.clk, self.dut.rst, cycles=10, active_high=True))

Asynchronous resets are defined in terms of time:

.. code-block:: python

    await cocotb.start(self.async_reset(self.dut.rst, duration=1000, units='ps', active_high=False))

Timeouts
--------

The timeout method is used to define a timeout for the test. The purpose of the timeout is to kill \
unintentioanlly long tests and indicate failure.

.. code-block:: python

    await cocotb.start(self.timeout(duration=1000, units='ns'))

Tickers
-------

Ticker functions are provided to provide updates on stdout at regular intervals so the user can track \
test progress in batch mode during low activity (such as hibernation).

Multiple tickers can run simultaneously and the message is user defined.

.. code-block:: python

    await cocotb.start(self.ticker(duration=1000, msg='Tempus Fugit', units='ns'))
