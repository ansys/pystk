IContrastFilterFactory
======================

.. py:class:: ansys.stk.core.graphics.IContrastFilterFactory

   object
   
   Adjusts the contrast of the source raster. The adjustment to contrast is a value between -1 and 1, corresponding to least contrast to most contrast.

.. py:currentmodule:: IContrastFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IContrastFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.IContrastFilterFactory.initialize_with_adjustment`
              - Initialize a new instance with the adjustment to contrast.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IContrastFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IContrastFilter
    :canonical: ansys.stk.core.graphics.IContrastFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IContrastFilter`

.. py:method:: initialize_with_adjustment(self, adjustment: float) -> IContrastFilter
    :canonical: ansys.stk.core.graphics.IContrastFilterFactory.initialize_with_adjustment

    Initialize a new instance with the adjustment to contrast.

    :Parameters:

    **adjustment** : :obj:`~float`

    :Returns:

        :obj:`~IContrastFilter`

