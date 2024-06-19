IBrightnessFilterFactory
========================

.. py:class:: IBrightnessFilterFactory

   object
   
   Adjusts the brightness of the source raster's color bands. The adjustment to brightness is a value between -1 and 1, corresponding to least bright to most bright.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a new instance.
            * - :py:meth:`~initialize_with_adjustment`
              - Initialize a new instance with the adjustment to brightness.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IBrightnessFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IBrightnessFilter
    :canonical: ansys.stk.core.graphics.IBrightnessFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IBrightnessFilter`

.. py:method:: initialize_with_adjustment(self, adjustment: float) -> IBrightnessFilter
    :canonical: ansys.stk.core.graphics.IBrightnessFilterFactory.initialize_with_adjustment

    Initialize a new instance with the adjustment to brightness.

    :Parameters:

    **adjustment** : :obj:`~float`

    :Returns:

        :obj:`~IBrightnessFilter`

