IWindModelADDS
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.IWindModelADDS

   object
   
   Interface used to access the options for a NOAA ADDS wind model.

.. py:currentmodule:: IWindModelADDS

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelADDS.add_current_forecast`
              - Add the current forecast from the ADDS service.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelADDS.name`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelADDS.blend_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelADDS.msg_interpolation_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelADDS.msg_extrapolation_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelADDS.missing_msg_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelADDS.interp_blend_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IWindModelADDS.messages`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IWindModelADDS


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelADDS.name
    :type: str

    Gets or sets the name of the wind model.

.. py:property:: blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelADDS.blend_time
    :type: float

    Gets or sets the blend time to transition from the previous wind model if one exists.

.. py:property:: msg_interpolation_type
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelADDS.msg_interpolation_type
    :type: ADDS_MSG_INTERP_TYPE

    Gets or sets the message interpolation type.

.. py:property:: msg_extrapolation_type
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelADDS.msg_extrapolation_type
    :type: ADDS_MSG_EXTRAP_TYPE

    Gets or sets the message extrapolation type.

.. py:property:: missing_msg_type
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelADDS.missing_msg_type
    :type: ADDS_MISSING_MSG_TYPE

    Gets or sets the missing message type.

.. py:property:: interp_blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelADDS.interp_blend_time
    :type: float

    Gets or sets the blend time to transition from the previous wind condition.

.. py:property:: messages
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelADDS.messages
    :type: IADDSMessageCollection

    Get the messages from the current forecast.


Method detail
-------------













.. py:method:: add_current_forecast(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.IWindModelADDS.add_current_forecast

    Add the current forecast from the ADDS service.

    :Returns:

        :obj:`~str`


