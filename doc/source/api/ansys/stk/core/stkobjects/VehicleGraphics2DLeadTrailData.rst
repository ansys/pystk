VehicleGraphics2DLeadTrailData
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData

   2D Graphics pass properties: lead/trail for ground tracks.

.. py:currentmodule:: VehicleGraphics2DLeadTrailData

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.set_lead_data_type`
              - Lead data type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.is_lead_data_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.set_trail_data_type`
              - Trail data type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.is_trail_data_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.set_trail_same_as_lead`
              - Set the trailing display option (and value, if applicable) to be the same as for the leading portion.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.lead_data_type`
              - Lead data type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.lead_data_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.lead_data`
              - Lead data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.trail_data_type`
              - Trail data type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.trail_data_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.trail_data`
              - Trail data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.has_lead_data`
              - Determine whether the leading display option has value data.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.has_trail_data`
              - Determine whether the trailing display option has value data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DLeadTrailData


Property detail
---------------

.. py:property:: lead_data_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.lead_data_type
    :type: LeadTrailData

    Lead data type.

.. py:property:: lead_data_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.lead_data_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: lead_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.lead_data
    :type: IVehicleLeadTrailData

    Lead data.

.. py:property:: trail_data_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.trail_data_type
    :type: LeadTrailData

    Trail data type.

.. py:property:: trail_data_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.trail_data_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: trail_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.trail_data
    :type: IVehicleLeadTrailData

    Trail data.

.. py:property:: has_lead_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.has_lead_data
    :type: bool

    Determine whether the leading display option has value data.

.. py:property:: has_trail_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.has_trail_data
    :type: bool

    Determine whether the trailing display option has value data.


Method detail
-------------


.. py:method:: set_lead_data_type(self, lead_data: LeadTrailData) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.set_lead_data_type

    Lead data type.

    :Parameters:

        **lead_data** : :obj:`~LeadTrailData`


    :Returns:

        :obj:`~None`

.. py:method:: is_lead_data_type_supported(self, lead_data: LeadTrailData) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.is_lead_data_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **lead_data** : :obj:`~LeadTrailData`


    :Returns:

        :obj:`~bool`




.. py:method:: set_trail_data_type(self, trail_data: LeadTrailData) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.set_trail_data_type

    Trail data type.

    :Parameters:

        **trail_data** : :obj:`~LeadTrailData`


    :Returns:

        :obj:`~None`

.. py:method:: is_trail_data_type_supported(self, trail_data: LeadTrailData) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.is_trail_data_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **trail_data** : :obj:`~LeadTrailData`


    :Returns:

        :obj:`~bool`





.. py:method:: set_trail_same_as_lead(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DLeadTrailData.set_trail_same_as_lead

    Set the trailing display option (and value, if applicable) to be the same as for the leading portion.

    :Returns:

        :obj:`~None`

