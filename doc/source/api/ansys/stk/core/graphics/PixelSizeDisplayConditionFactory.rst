PixelSizeDisplayConditionFactory
================================

.. py:class:: ansys.stk.core.graphics.PixelSizeDisplayConditionFactory

   Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

.. py:currentmodule:: PixelSizeDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PixelSizeDisplayConditionFactory.initialize`
              - Initialize a default pixel size display condition. minimum pixel size is set to 0 and maximum pixel size is set to Int32.MaxValue. With this interval, an object is always rendered regardless of how many pixels its bounding sphere or rectangle covers.
            * - :py:attr:`~ansys.stk.core.graphics.PixelSizeDisplayConditionFactory.initialize_with_pixel_sizes`
              - Initialize a pixel size display condition with the inclusive interval [minimumPixelSize, maximumPixelSize]...



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PixelSizeDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> PixelSizeDisplayCondition
    :canonical: ansys.stk.core.graphics.PixelSizeDisplayConditionFactory.initialize

    Initialize a default pixel size display condition. minimum pixel size is set to 0 and maximum pixel size is set to Int32.MaxValue. With this interval, an object is always rendered regardless of how many pixels its bounding sphere or rectangle covers.

    :Returns:

        :obj:`~PixelSizeDisplayCondition`

.. py:method:: initialize_with_pixel_sizes(self, minimumPixelSize: int, maximumPixelSize: int) -> PixelSizeDisplayCondition
    :canonical: ansys.stk.core.graphics.PixelSizeDisplayConditionFactory.initialize_with_pixel_sizes

    Initialize a pixel size display condition with the inclusive interval [minimumPixelSize, maximumPixelSize]...

    :Parameters:

    **minimumPixelSize** : :obj:`~int`
    **maximumPixelSize** : :obj:`~int`

    :Returns:

        :obj:`~PixelSizeDisplayCondition`

