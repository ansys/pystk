IDistanceToPrimitiveDisplayCondition
====================================

.. py:class:: IDistanceToPrimitiveDisplayCondition

   object
   
   Define an inclusive distance interval that determines when an object, such as a screen overlay, is rendered based on the distance from the camera to the primitive...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~primitive`
            * - :py:meth:`~minimum_distance`
            * - :py:meth:`~minimum_distance_squared`
            * - :py:meth:`~maximum_distance`
            * - :py:meth:`~maximum_distance_squared`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IDistanceToPrimitiveDisplayCondition


Property detail
---------------

.. py:property:: primitive
    :canonical: ansys.stk.core.graphics.IDistanceToPrimitiveDisplayCondition.primitive
    :type: IAgStkGraphicsPrimitive

    Gets or sets the primitive associated with this instance.

.. py:property:: minimum_distance
    :canonical: ansys.stk.core.graphics.IDistanceToPrimitiveDisplayCondition.minimum_distance
    :type: float

    Gets or sets the minimum distance of the inclusive distance interval.

.. py:property:: minimum_distance_squared
    :canonical: ansys.stk.core.graphics.IDistanceToPrimitiveDisplayCondition.minimum_distance_squared
    :type: float

    Gets the squared minimum distance of the inclusive distance interval.

.. py:property:: maximum_distance
    :canonical: ansys.stk.core.graphics.IDistanceToPrimitiveDisplayCondition.maximum_distance
    :type: float

    Gets or sets the maximum distance of the inclusive distance interval. Use Double.MaxValue to ignore checking the maximum distance.

.. py:property:: maximum_distance_squared
    :canonical: ansys.stk.core.graphics.IDistanceToPrimitiveDisplayCondition.maximum_distance_squared
    :type: float

    Gets the squared maximum distance of the inclusive distance interval.


