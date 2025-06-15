Random Constraints
==================

The :doc:`avl.Object </modules/avl._core.object>` module provides user implementable :any:`Object.pre_randomize`, :any:`Object.randomize` and \
:any:`Object.post_randomize` methods.

The most basic form of randomization can be implemented:

.. code-block:: python

    import avl_object

    class MyObject(avl.Object):
        def __init__(self, name, parent=None):
            super().__init__(name)
            self.value = None


        def randomize(self):
            self.value = random.randint(0, 100)
