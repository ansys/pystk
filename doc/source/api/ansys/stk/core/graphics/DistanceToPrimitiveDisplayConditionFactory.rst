DistanceToPrimitiveDisplayConditionFactory
==========================================

.. py:class:: ansys.stk.core.graphics.DistanceToPrimitiveDisplayConditionFactory

   Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

.. py:currentmodule:: DistanceToPrimitiveDisplayConditionFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayConditionFactory.initialize`
              - Initialize a default distance to primitive display condition. With this constructor, an object is always rendered regardless of the camera's distance to the primitive.
            * - :py:attr:`~ansys.stk.core.graphics.DistanceToPrimitiveDisplayConditionFactory.initialize_with_distances`
              - Initialize a distance to primitive display condition with the inclusive distance interval [minimumDistance, maximumDistance]...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import DistanceToPrimitiveDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> DistanceToPrimitiveDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceToPrimitiveDisplayConditionFactory.initialize

    Initialize a default distance to primitive display condition. With this constructor, an object is always rendered regardless of the camera's distance to the primitive.

    :Returns:

        :obj:`~DistanceToPrimitiveDisplayCondition`

.. py:method:: initialize_with_distances(self, primitive: IPrimitive, minimum_distance: float, maximum_distance: float) -> DistanceToPrimitiveDisplayCondition
    :canonical: ansys.stk.core.graphics.DistanceToPrimitiveDisplayConditionFactory.initialize_with_distances

    Initialize a distance to primitive display condition with the inclusive distance interval [minimumDistance, maximumDistance]...

    :Parameters:

        **primitive** : :obj:`~IPrimitive`

        **minimum_distance** : :obj:`~float`

        **maximum_distance** : :obj:`~float`


    :Returns:

        :obj:`~DistanceToPrimitiveDisplayCondition`

