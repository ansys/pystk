DistanceToPositionDisplayConditionFactory
=========================================

.. py:class:: ansys.stk.core.graphics.DistanceToPositionDisplayConditionFactory

   Bases: 

   Define an inclusive distance interval that determines when an object, such as a primitive, is rendered based on the distance from the camera to a position defined in the given reference frame.

.. py:currentmodule:: DistanceToPositionDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayConditionFactory.initialize`
              - Initialize a default distance to position display condition. With this constructor, an object is always rendered regardless of the camera's distance to the position.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayConditionFactory.initialize_with_distances`
              - Initialize a distance display condition with the inclusive distance interval [minimumDistance, maximumDistance]...
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPositionDisplayConditionFactory.initialize_with_reference_frame_and_distances`
              - Initialize a distance display condition with the inclusive distance interval [minimumDistance, maximumDistance]...



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import DistanceToPositionDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> DistanceToPositionDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayConditionFactory.initialize

    Initialize a default distance to position display condition. With this constructor, an object is always rendered regardless of the camera's distance to the position.

    :Returns:

        :obj:`~DistanceToPositionDisplayCondition`

.. py:method:: initialize_with_distances(self, position: list, minimumDistance: float, maximumDistance: float) -> DistanceToPositionDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayConditionFactory.initialize_with_distances

    Initialize a distance display condition with the inclusive distance interval [minimumDistance, maximumDistance]...

    :Parameters:

    **position** : :obj:`~list`
    **minimumDistance** : :obj:`~float`
    **maximumDistance** : :obj:`~float`

    :Returns:

        :obj:`~DistanceToPositionDisplayCondition`

.. py:method:: initialize_with_reference_frame_and_distances(self, referenceFrame: IVectorGeometryToolSystem, position: list, minimumDistance: float, maximumDistance: float) -> DistanceToPositionDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceToPositionDisplayConditionFactory.initialize_with_reference_frame_and_distances

    Initialize a distance display condition with the inclusive distance interval [minimumDistance, maximumDistance]...

    :Parameters:

    **referenceFrame** : :obj:`~IVectorGeometryToolSystem`
    **position** : :obj:`~list`
    **minimumDistance** : :obj:`~float`
    **maximumDistance** : :obj:`~float`

    :Returns:

        :obj:`~DistanceToPositionDisplayCondition`

