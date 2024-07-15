DistanceToGlobeOverlayDisplayConditionFactory
=============================================

.. py:class:: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory

   Bases: 

   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to the globe overlay...

.. py:currentmodule:: DistanceToGlobeOverlayDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory.initialize`
              - Initialize a default distance to globe overlay display condition. With this constructor, an object is always rendered regardless of the camera's distance to the globe overlay.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory.initialize_with_distances`
              - Initialize a distance display condition with the globe overlay and the inclusive distance interval [minimumDistance, maximumDistance]...



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import DistanceToGlobeOverlayDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> DistanceToGlobeOverlayDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory.initialize

    Initialize a default distance to globe overlay display condition. With this constructor, an object is always rendered regardless of the camera's distance to the globe overlay.

    :Returns:

        :obj:`~DistanceToGlobeOverlayDisplayCondition`

.. py:method:: initialize_with_distances(self, globeOverlay: IGlobeOverlay, minimumDistance: float, maximumDistance: float) -> DistanceToGlobeOverlayDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceToGlobeOverlayDisplayConditionFactory.initialize_with_distances

    Initialize a distance display condition with the globe overlay and the inclusive distance interval [minimumDistance, maximumDistance]...

    :Parameters:

    **globeOverlay** : :obj:`~IGlobeOverlay`
    **minimumDistance** : :obj:`~float`
    **maximumDistance** : :obj:`~float`

    :Returns:

        :obj:`~DistanceToGlobeOverlayDisplayCondition`

