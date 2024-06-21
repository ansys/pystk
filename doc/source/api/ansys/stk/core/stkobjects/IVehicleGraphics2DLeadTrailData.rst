IVehicleGraphics2DLeadTrailData
===============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData

   object
   
   2D Graphics pass properties: lead/trail for ground tracks.

.. py:currentmodule:: IVehicleGraphics2DLeadTrailData

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.set_lead_data_type`
              - Lead data type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.is_lead_data_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.set_trail_data_type`
              - Trail data type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.is_trail_data_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.set_trail_same_as_lead`
              - Set the trailing display option (and value, if applicable) to be the same as for the leading portion.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.lead_data_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.lead_data_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.lead_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.trail_data_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.trail_data_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.trail_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.has_lead_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.has_trail_data`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DLeadTrailData


Property detail
---------------

.. py:property:: lead_data_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.lead_data_type
    :type: LEAD_TRAIL_DATA

    Lead data type.

.. py:property:: lead_data_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.lead_data_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: lead_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.lead_data
    :type: IVehicleLeadTrailData

    Lead data.

.. py:property:: trail_data_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.trail_data_type
    :type: LEAD_TRAIL_DATA

    Trail data type.

.. py:property:: trail_data_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.trail_data_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: trail_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.trail_data
    :type: IVehicleLeadTrailData

    Trail data.

.. py:property:: has_lead_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.has_lead_data
    :type: bool

    Determine whether the leading display option has value data.

.. py:property:: has_trail_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.has_trail_data
    :type: bool

    Determine whether the trailing display option has value data.


Method detail
-------------


.. py:method:: set_lead_data_type(self, leadData: LEAD_TRAIL_DATA) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.set_lead_data_type

    Lead data type.

    :Parameters:

    **leadData** : :obj:`~LEAD_TRAIL_DATA`

    :Returns:

        :obj:`~None`

.. py:method:: is_lead_data_type_supported(self, leadData: LEAD_TRAIL_DATA) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.is_lead_data_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **leadData** : :obj:`~LEAD_TRAIL_DATA`

    :Returns:

        :obj:`~bool`




.. py:method:: set_trail_data_type(self, trailData: LEAD_TRAIL_DATA) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.set_trail_data_type

    Trail data type.

    :Parameters:

    **trailData** : :obj:`~LEAD_TRAIL_DATA`

    :Returns:

        :obj:`~None`

.. py:method:: is_trail_data_type_supported(self, trailData: LEAD_TRAIL_DATA) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.is_trail_data_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **trailData** : :obj:`~LEAD_TRAIL_DATA`

    :Returns:

        :obj:`~bool`





.. py:method:: set_trail_same_as_lead(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DLeadTrailData.set_trail_same_as_lead

    Set the trailing display option (and value, if applicable) to be the same as for the leading portion.

    :Returns:

        :obj:`~None`

