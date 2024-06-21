IDistanceToGlobeOverlayDisplayCondition
=======================================

.. py:class:: ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition

   object
   
   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

.. py:currentmodule:: IDistanceToGlobeOverlayDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.globe_overlay`
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.minimum_distance`
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.minimum_distance_squared`
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.maximum_distance`
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.maximum_distance_squared`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IDistanceToGlobeOverlayDisplayCondition


Property detail
---------------

.. py:property:: globe_overlay
    :canonical: ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.globe_overlay
    :type: IGlobeOverlay

    Gets or sets the globe overlay associated with this instance.

.. py:property:: minimum_distance
    :canonical: ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.minimum_distance
    :type: float

    Gets or sets the minimum distance of the inclusive distance interval.

.. py:property:: minimum_distance_squared
    :canonical: ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.minimum_distance_squared
    :type: float

    Gets the squared minimum distance of the inclusive distance interval.

.. py:property:: maximum_distance
    :canonical: ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.maximum_distance
    :type: float

    Gets or sets the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.

.. py:property:: maximum_distance_squared
    :canonical: ansys.stk.core.graphics.IDistanceToGlobeOverlayDisplayCondition.maximum_distance_squared
    :type: float

    Gets the squared maximum distance of the inclusive distance interval.


