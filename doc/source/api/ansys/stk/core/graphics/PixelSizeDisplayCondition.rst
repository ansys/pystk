PixelSizeDisplayCondition
=========================

.. py:class:: ansys.stk.core.graphics.PixelSizeDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

.. py:currentmodule:: PixelSizeDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PixelSizeDisplayCondition.minimum_pixel_size`
              - Gets or sets the minimum pixel size of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.PixelSizeDisplayCondition.maximum_pixel_size`
              - Gets or sets the maximum pixel size of the inclusive distance interval. Use Int32.MaxValue to ignore checking the maximum distance.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PixelSizeDisplayCondition


Property detail
---------------

.. py:property:: minimum_pixel_size
    :canonical: ansys.stk.core.graphics.PixelSizeDisplayCondition.minimum_pixel_size
    :type: int

    Gets or sets the minimum pixel size of the inclusive distance interval.

.. py:property:: maximum_pixel_size
    :canonical: ansys.stk.core.graphics.PixelSizeDisplayCondition.maximum_pixel_size
    :type: int

    Gets or sets the maximum pixel size of the inclusive distance interval. Use Int32.MaxValue to ignore checking the maximum distance.


