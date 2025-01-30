VehicleGraphics3DLeadTrailData
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData

   AgLvVOTrajectory2 Class.

.. py:currentmodule:: VehicleGraphics3DLeadTrailData

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.set_lead_data_type`
              - Set the display option for the leading portion of the vehicle's tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.set_trail_data_type`
              - Set the display option for the trailng portion of the vehicle's tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.is_data_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.set_trail_same_as_lead`
              - Set the trailing display option (and value, if applicable) to be the same as for the leading portion.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.lead_data_type`
              - Get display option for the leading portion of the vehicle's tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.trail_data_type`
              - Get display option for the trailing portion of the vehicle's tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.lead_data`
              - Get the display value (time or percent) for the leading portion of the vehicle's tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.trail_data`
              - Get the display value (time or percent) for the trailing portion of the vehicle's tracks.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.has_lead_data`
              - Determine whether the leading display option has value data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.has_trail_data`
              - Determine whether the trailing display option has value data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.supported_data_types`
              - Returns an array of valid choices.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DLeadTrailData


Property detail
---------------

.. py:property:: lead_data_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.lead_data_type
    :type: LeadTrailData

    Get display option for the leading portion of the vehicle's tracks.

.. py:property:: trail_data_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.trail_data_type
    :type: LeadTrailData

    Get display option for the trailing portion of the vehicle's tracks.

.. py:property:: lead_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.lead_data
    :type: IVehicleLeadTrailData

    Get the display value (time or percent) for the leading portion of the vehicle's tracks.

.. py:property:: trail_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.trail_data
    :type: IVehicleLeadTrailData

    Get the display value (time or percent) for the trailing portion of the vehicle's tracks.

.. py:property:: has_lead_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.has_lead_data
    :type: bool

    Determine whether the leading display option has value data.

.. py:property:: has_trail_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.has_trail_data
    :type: bool

    Determine whether the trailing display option has value data.

.. py:property:: supported_data_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.supported_data_types
    :type: list

    Returns an array of valid choices.


Method detail
-------------



.. py:method:: set_lead_data_type(self, lead_data: LeadTrailData) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.set_lead_data_type

    Set the display option for the leading portion of the vehicle's tracks.

    :Parameters:

    **lead_data** : :obj:`~LeadTrailData`

    :Returns:

        :obj:`~None`

.. py:method:: set_trail_data_type(self, trail_data: LeadTrailData) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.set_trail_data_type

    Set the display option for the trailng portion of the vehicle's tracks.

    :Parameters:

    **trail_data** : :obj:`~LeadTrailData`

    :Returns:

        :obj:`~None`





.. py:method:: is_data_type_supported(self, data: LeadTrailData) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.is_data_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **data** : :obj:`~LeadTrailData`

    :Returns:

        :obj:`~bool`


.. py:method:: set_trail_same_as_lead(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DLeadTrailData.set_trail_same_as_lead

    Set the trailing display option (and value, if applicable) to be the same as for the leading portion.

    :Returns:

        :obj:`~None`

