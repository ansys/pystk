RotateFilterFactory
===================

.. py:class:: ansys.stk.core.graphics.RotateFilterFactory

   Rotate the source raster clockwise by the specified angle.

.. py:currentmodule:: RotateFilterFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.RotateFilterFactory.initialize`
              - Initialize a new instance.
            * - :py:attr:`~ansys.stk.core.graphics.RotateFilterFactory.initialize_with_angle`
              - Initialize a new instance with a counterclockwise rotation angle.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RotateFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> RotateFilter
    :canonical: ansys.stk.core.graphics.RotateFilterFactory.initialize

    Initialize a new instance.

    :Returns:

        :obj:`~RotateFilter`

.. py:method:: initialize_with_angle(self, rotate_angle: float) -> RotateFilter
    :canonical: ansys.stk.core.graphics.RotateFilterFactory.initialize_with_angle

    Initialize a new instance with a counterclockwise rotation angle.

    :Parameters:

    **rotate_angle** : :obj:`~float`

    :Returns:

        :obj:`~RotateFilter`

