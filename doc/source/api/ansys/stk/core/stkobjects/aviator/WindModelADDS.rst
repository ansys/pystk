WindModelADDS
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.WindModelADDS

   Class defining a wind model using the NOAA ADDS service for a mission.

.. py:currentmodule:: WindModelADDS

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.add_current_forecast`
              - Add the current forecast from the ADDS service.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.name`
              - Gets or sets the name of the wind model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.blend_time`
              - Gets or sets the blend time to transition from the previous wind model if one exists.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.message_interpolation_type`
              - Gets or sets the message interpolation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.message_extrapolation_type`
              - Gets or sets the message extrapolation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.missing_message_type`
              - Gets or sets the missing message type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.interpolation_blend_time`
              - Gets or sets the blend time to transition from the previous wind condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.messages`
              - Get the messages from the current forecast.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import WindModelADDS


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.name
    :type: str

    Gets or sets the name of the wind model.

.. py:property:: blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.blend_time
    :type: float

    Gets or sets the blend time to transition from the previous wind model if one exists.

.. py:property:: message_interpolation_type
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.message_interpolation_type
    :type: ADDSMessageInterpolationType

    Gets or sets the message interpolation type.

.. py:property:: message_extrapolation_type
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.message_extrapolation_type
    :type: ADDSMessageExtrapolationType

    Gets or sets the message extrapolation type.

.. py:property:: missing_message_type
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.missing_message_type
    :type: ADDSMissingMessageType

    Gets or sets the missing message type.

.. py:property:: interpolation_blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.interpolation_blend_time
    :type: float

    Gets or sets the blend time to transition from the previous wind condition.

.. py:property:: messages
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.messages
    :type: ADDSMessageCollection

    Get the messages from the current forecast.


Method detail
-------------













.. py:method:: add_current_forecast(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.add_current_forecast

    Add the current forecast from the ADDS service.

    :Returns:

        :obj:`~str`


