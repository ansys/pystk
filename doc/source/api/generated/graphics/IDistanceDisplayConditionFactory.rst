IDistanceDisplayConditionFactory
================================

.. py:class:: IDistanceDisplayConditionFactory

   object
   
   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the object.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default distance display condition. minimum distance is set to 0 and maximum distance is set to Double.MaxValue. With this interval, an object is always rendered regardless of its distance to the camera.
            * - :py:meth:`~initialize_with_distances`
              - Initialize a distance display condition with the inclusive distance interval [minimumDistance, maximumDistance]...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IDistanceDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IDistanceDisplayCondition"

    Initialize a default distance display condition. minimum distance is set to 0 and maximum distance is set to Double.MaxValue. With this interval, an object is always rendered regardless of its distance to the camera.

    :Returns:

        :obj:`~"IDistanceDisplayCondition"`

.. py:method:: initialize_with_distances(self, minimumDistance:float, maximumDistance:float) -> "IDistanceDisplayCondition"

    Initialize a distance display condition with the inclusive distance interval [minimumDistance, maximumDistance]...

    :Parameters:

    **minimumDistance** : :obj:`~float`
    **maximumDistance** : :obj:`~float`

    :Returns:

        :obj:`~"IDistanceDisplayCondition"`

