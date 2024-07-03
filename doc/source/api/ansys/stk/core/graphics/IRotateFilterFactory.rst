IRotateFilterFactory
====================

.. py:class:: ansys.stk.core.graphics.IRotateFilterFactory

   object
   
   Rotate the source raster clockwise by the specified angle.

.. py:currentmodule:: IRotateFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IRotateFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.IRotateFilterFactory.initialize_with_angle`
              - Initialize a new instance with a counterclockwise rotation angle.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IRotateFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> IRotateFilter
    :canonical: ansys.stk.core.graphics.IRotateFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~IRotateFilter`

.. py:method:: initialize_with_angle(self, rotateAngle: float) -> IRotateFilter
    :canonical: ansys.stk.core.graphics.IRotateFilterFactory.initialize_with_angle

    Initialize a new instance with a counterclockwise rotation angle.

    :Parameters:

    **rotateAngle** : :obj:`~float`

    :Returns:

        :obj:`~IRotateFilter`

