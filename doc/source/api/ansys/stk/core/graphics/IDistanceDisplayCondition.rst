IDistanceDisplayCondition
=========================

.. py:class:: ansys.stk.core.graphics.IDistanceDisplayCondition

   object
   
   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

.. py:currentmodule:: IDistanceDisplayCondition

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IDistanceDisplayCondition.minimum_distance`
              - Gets or sets the minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceDisplayCondition.maximum_distance`
              - Gets or sets the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceDisplayCondition.minimum_distance_squared`
              - Gets the squared minimum distance of the inclusive distance interval.
            * - :py:attr:`~ansys.stk.core.graphics.IDistanceDisplayCondition.maximum_distance_squared`
              - Gets the squared maximum distance of the inclusive distance interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IDistanceDisplayCondition


Property detail
---------------

.. py:property:: minimum_distance
    :canonical: ansys.stk.core.graphics.IDistanceDisplayCondition.minimum_distance
    :type: float

    Gets or sets the minimum distance of the inclusive distance interval.

.. py:property:: maximum_distance
    :canonical: ansys.stk.core.graphics.IDistanceDisplayCondition.maximum_distance
    :type: float

    Gets or sets the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.

.. py:property:: minimum_distance_squared
    :canonical: ansys.stk.core.graphics.IDistanceDisplayCondition.minimum_distance_squared
    :type: float

    Gets the squared minimum distance of the inclusive distance interval.

.. py:property:: maximum_distance_squared
    :canonical: ansys.stk.core.graphics.IDistanceDisplayCondition.maximum_distance_squared
    :type: float

    Gets the squared maximum distance of the inclusive distance interval.


