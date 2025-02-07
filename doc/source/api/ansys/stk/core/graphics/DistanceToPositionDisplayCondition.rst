DistanceToPositionDisplayCondition
==================================

.. py:class:: ansys.stk.core.graphics.DistanceToPositionDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

.. py:currentmodule:: DistanceToPositionDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayCondition.minimum_distance`
              - Get or set the minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayCondition.minimum_distance_squared`
              - Get the squared minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayCondition.maximum_distance`
              - Get or set the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayCondition.maximum_distance_squared`
              - Get the squared maximum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayCondition.position`
              - Get or set the position used to compute the distance from the camera. The array contains the components of the position arranged in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayCondition.reference_frame`
              - Get or set the reference frame that position is defined in.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import DistanceToPositionDisplayCondition


Property detail
---------------

.. py:property:: minimum_distance
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayCondition.minimum_distance
    :type: float

    Get or set the minimum distance of the inclusive distance interval.

.. py:property:: minimum_distance_squared
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayCondition.minimum_distance_squared
    :type: float

    Get the squared minimum distance of the inclusive distance interval.

.. py:property:: maximum_distance
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayCondition.maximum_distance
    :type: float

    Get or set the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.

.. py:property:: maximum_distance_squared
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayCondition.maximum_distance_squared
    :type: float

    Get the squared maximum distance of the inclusive distance interval.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayCondition.position
    :type: list

    Get or set the position used to compute the distance from the camera. The array contains the components of the position arranged in the order x, y, z.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayCondition.reference_frame
    :type: IVectorGeometryToolSystem

    Get or set the reference frame that position is defined in.


