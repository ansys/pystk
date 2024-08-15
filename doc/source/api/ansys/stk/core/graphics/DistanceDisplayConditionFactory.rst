DistanceDisplayConditionFactory
===============================

.. py:class:: ansys.stk.core.graphics.DistanceDisplayConditionFactory

   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

.. py:currentmodule:: DistanceDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.DistanceDisplayConditionFactory.initialize`
              - Initialize a default distance display condition. minimum distance is set to 0 and maximum distance is set to Double.MaxValue. With this interval, an object is always rendered regardless of its distance to the camera.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceDisplayConditionFactory.initialize_with_distances`
              - Initialize a distance display condition with the inclusive distance interval [minimumDistance, maximumDistance]...



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import DistanceDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> DistanceDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceDisplayConditionFactory.initialize

    Initialize a default distance display condition. minimum distance is set to 0 and maximum distance is set to Double.MaxValue. With this interval, an object is always rendered regardless of its distance to the camera.

    :Returns:

        :obj:`~DistanceDisplayCondition`

.. py:method:: initialize_with_distances(self, minimumDistance: float, maximumDistance: float) -> DistanceDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceDisplayConditionFactory.initialize_with_distances

    Initialize a distance display condition with the inclusive distance interval [minimumDistance, maximumDistance]...

    :Parameters:

    **minimumDistance** : :obj:`~float`
    **maximumDistance** : :obj:`~float`

    :Returns:

        :obj:`~DistanceDisplayCondition`

