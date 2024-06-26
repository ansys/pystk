IDistanceToPositionDisplayCondition
===================================

.. py:class:: ansys.stk.core.graphics.IDistanceToPositionDisplayCondition

   object
   
   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

.. py:currentmodule:: IDistanceToPositionDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.minimum_distance`
              - Gets or sets the minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.minimum_distance_squared`
              - Gets the squared minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.maximum_distance`
              - Gets or sets the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.maximum_distance_squared`
              - Gets the squared maximum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.position`
              - Gets or sets the position used to compute the distance from the camera. The array contains the components of the position arranged in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.reference_frame`
              - Gets or sets the reference frame that position is defined in.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IDistanceToPositionDisplayCondition


Property detail
---------------

.. py:property:: minimum_distance
    :canonical: ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.minimum_distance
    :type: float

    Gets or sets the minimum distance of the inclusive distance interval.

.. py:property:: minimum_distance_squared
    :canonical: ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.minimum_distance_squared
    :type: float

    Gets the squared minimum distance of the inclusive distance interval.

.. py:property:: maximum_distance
    :canonical: ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.maximum_distance
    :type: float

    Gets or sets the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.

.. py:property:: maximum_distance_squared
    :canonical: ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.maximum_distance_squared
    :type: float

    Gets the squared maximum distance of the inclusive distance interval.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.position
    :type: list

    Gets or sets the position used to compute the distance from the camera. The array contains the components of the position arranged in the order x, y, z.

.. py:property:: reference_frame
    :canonical: ansys.stk.core.graphics.IDistanceToPositionDisplayCondition.reference_frame
    :type: IVectorGeometryToolSystem

    Gets or sets the reference frame that position is defined in.


