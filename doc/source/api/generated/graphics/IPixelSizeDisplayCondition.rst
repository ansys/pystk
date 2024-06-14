IPixelSizeDisplayCondition
==========================

.. py:class:: IPixelSizeDisplayCondition

   object
   
   Define an inclusive interval, in pixels, that determines when an object, such as a primitive, is rendered based on the number of pixels the object's bounding sphere (or in the case of screen overlays, bounding rectangle) covers on the screen...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~minimum_pixel_size`
            * - :py:meth:`~maximum_pixel_size`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPixelSizeDisplayCondition


Property detail
---------------

.. py:property:: minimum_pixel_size
    :canonical: ansys.stk.core.graphics.IPixelSizeDisplayCondition.minimum_pixel_size
    :type: int

    Gets or sets the minimum pixel size of the inclusive distance interval.

.. py:property:: maximum_pixel_size
    :canonical: ansys.stk.core.graphics.IPixelSizeDisplayCondition.maximum_pixel_size
    :type: int

    Gets or sets the maximum pixel size of the inclusive distance interval. Use Int32.MaxValue to ignore checking the maximum distance.


