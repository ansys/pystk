DistanceToGlobeOverlayDisplayCondition
======================================

.. py:class:: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

.. py:currentmodule:: DistanceToGlobeOverlayDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.globe_overlay`
              - Get or set the globe overlay associated with this instance.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.minimum_distance`
              - Get or set the minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.minimum_distance_squared`
              - Get the squared minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.maximum_distance`
              - Get or set the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.maximum_distance_squared`
              - Get the squared maximum distance of the inclusive distance interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import DistanceToGlobeOverlayDisplayCondition


Property detail
---------------

.. py:property:: globe_overlay
    :canonical: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.globe_overlay
    :type: IGlobeOverlay

    Get or set the globe overlay associated with this instance.

.. py:property:: minimum_distance
    :canonical: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.minimum_distance
    :type: float

    Get or set the minimum distance of the inclusive distance interval.

.. py:property:: minimum_distance_squared
    :canonical: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.minimum_distance_squared
    :type: float

    Get the squared minimum distance of the inclusive distance interval.

.. py:property:: maximum_distance
    :canonical: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.maximum_distance
    :type: float

    Get or set the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.

.. py:property:: maximum_distance_squared
    :canonical: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayCondition.maximum_distance_squared
    :type: float

    Get the squared maximum distance of the inclusive distance interval.


