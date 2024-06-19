IDistanceToPrimitiveDisplayConditionFactory
===========================================

.. py:class:: IDistanceToPrimitiveDisplayConditionFactory

   object
   
   Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default distance to primitive display condition. With this constructor, an object is always rendered regardless of the camera's distance to the primitive.
            * - :py:meth:`~initialize_with_distances`
              - Initialize a distance to primitive display condition with the inclusive distance interval [minimumDistance, maximumDistance]...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IDistanceToPrimitiveDisplayConditionFactory



Method detail
-------------

.. py:method:: initialize(self) -> IDistanceToPrimitiveDisplayCondition
    :canonical: ansys.stk.core.graphics.IDistanceToPrimitiveDisplayConditionFactory.initialize

    Initialize a default distance to primitive display condition. With this constructor, an object is always rendered regardless of the camera's distance to the primitive.

    :Returns:

        :obj:`~IDistanceToPrimitiveDisplayCondition`

.. py:method:: initialize_with_distances(self, primitive: IPrimitive, minimumDistance: float, maximumDistance: float) -> IDistanceToPrimitiveDisplayCondition
    :canonical: ansys.stk.core.graphics.IDistanceToPrimitiveDisplayConditionFactory.initialize_with_distances

    Initialize a distance to primitive display condition with the inclusive distance interval [minimumDistance, maximumDistance]...

    :Parameters:

    **primitive** : :obj:`~IPrimitive`
    **minimumDistance** : :obj:`~float`
    **maximumDistance** : :obj:`~float`

    :Returns:

        :obj:`~IDistanceToPrimitiveDisplayCondition`

