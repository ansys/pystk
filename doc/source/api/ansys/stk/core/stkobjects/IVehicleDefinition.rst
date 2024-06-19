IVehicleDefinition
==================

.. py:class:: IVehicleDefinition

   object
   
   Pass break definition properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_break_angle_type`
              - Set the Break Angle type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~break_angle_type`
            * - :py:meth:`~break_angle`
            * - :py:meth:`~direction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleDefinition


Property detail
---------------

.. py:property:: break_angle_type
    :canonical: ansys.stk.core.stkobjects.IVehicleDefinition.break_angle_type
    :type: VEHICLE_BREAK_ANGLE_TYPE

    Latitude or longitude.

.. py:property:: break_angle
    :canonical: ansys.stk.core.stkobjects.IVehicleDefinition.break_angle
    :type: IAgVeBreakAngle

    Value of latitude or longitude used for defining pass break.

.. py:property:: direction
    :canonical: ansys.stk.core.stkobjects.IVehicleDefinition.direction
    :type: VEHICLE_DIRECTION

    Descending or ascending.


Method detail
-------------


.. py:method:: set_break_angle_type(self, breakAngleType: VEHICLE_BREAK_ANGLE_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleDefinition.set_break_angle_type

    Set the Break Angle type.

    :Parameters:

    **breakAngleType** : :obj:`~VEHICLE_BREAK_ANGLE_TYPE`

    :Returns:

        :obj:`~None`




