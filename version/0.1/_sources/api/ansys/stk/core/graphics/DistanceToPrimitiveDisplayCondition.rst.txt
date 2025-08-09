DistanceToPrimitiveDisplayCondition
===================================

.. py:class:: ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition

   Bases: :py:class:`~ansys.stk.core.graphics.IDisplayCondition`

   Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

.. py:currentmodule:: DistanceToPrimitiveDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.primitive`
              - Get or set the primitive associated with this instance.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.minimum_distance`
              - Get or set the minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.minimum_distance_squared`
              - Get the squared minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.maximum_distance`
              - Get or set the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.maximum_distance_squared`
              - Get the squared maximum distance of the inclusive distance interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import DistanceToPrimitiveDisplayCondition


Property detail
---------------

.. py:property:: primitive
    :canonical: ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.primitive
    :type: IPrimitive

    Get or set the primitive associated with this instance.

.. py:property:: minimum_distance
    :canonical: ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.minimum_distance
    :type: float

    Get or set the minimum distance of the inclusive distance interval.

.. py:property:: minimum_distance_squared
    :canonical: ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.minimum_distance_squared
    :type: float

    Get the squared minimum distance of the inclusive distance interval.

.. py:property:: maximum_distance
    :canonical: ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.maximum_distance
    :type: float

    Get or set the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.

.. py:property:: maximum_distance_squared
    :canonical: ansys.stk.core.graphics.DistanceToPrimitiveDisplayCondition.maximum_distance_squared
    :type: float

    Get the squared maximum distance of the inclusive distance interval.


