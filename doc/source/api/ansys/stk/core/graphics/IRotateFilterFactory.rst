IRotateFilterFactory
====================

.. py:class:: IRotateFilterFactory

   object
   
   Rotate the source raster clockwise by the specified angle.

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
            * - :py:meth:`~initialize_with_angle`
              - Initialize a new instance with a counterclockwise rotation angle.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IRotateFilterFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IRotateFilter"

    Initialize a new instance.

    :Returns:

        :obj:`~"IRotateFilter"`

.. py:method:: initialize_with_angle(self, rotateAngle:float) -> "IRotateFilter"

    Initialize a new instance with a counterclockwise rotation angle.

    :Parameters:

    **rotateAngle** : :obj:`~float`

    :Returns:

        :obj:`~"IRotateFilter"`

