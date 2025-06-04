VehicleDefinition
=================

.. py:class:: ansys.stk.core.stkobjects.VehicleDefinition

   Pass break definition properties.

.. py:currentmodule:: VehicleDefinition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleDefinition.set_break_angle_type`
              - Set the Break Angle type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleDefinition.break_angle_type`
              - Latitude or longitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleDefinition.break_angle`
              - Value of latitude or longitude used for defining pass break.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleDefinition.direction`
              - Descending or ascending.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleDefinition


Property detail
---------------

.. py:property:: break_angle_type
    :canonical: ansys.stk.core.stkobjects.VehicleDefinition.break_angle_type
    :type: VehicleBreakAngleType

    Latitude or longitude.

.. py:property:: break_angle
    :canonical: ansys.stk.core.stkobjects.VehicleDefinition.break_angle
    :type: IVehicleBreakAngle

    Value of latitude or longitude used for defining pass break.

.. py:property:: direction
    :canonical: ansys.stk.core.stkobjects.VehicleDefinition.direction
    :type: VehicleDirection

    Descending or ascending.


Method detail
-------------


.. py:method:: set_break_angle_type(self, break_angle_type: VehicleBreakAngleType) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleDefinition.set_break_angle_type

    Set the Break Angle type.

    :Parameters:

        **break_angle_type** : :obj:`~VehicleBreakAngleType`


    :Returns:

        :obj:`~None`




