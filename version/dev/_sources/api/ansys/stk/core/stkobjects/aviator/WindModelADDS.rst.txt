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

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.blend_time`
              - Get or set the blend time to transition from the previous wind model if one exists.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.interpolation_blend_time`
              - Get or set the blend time to transition from the previous wind condition.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.message_extrapolation_type`
              - Get or set the message extrapolation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.message_interpolation_type`
              - Get or set the message interpolation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.messages`
              - Get the messages from the current forecast.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.missing_message_type`
              - Get or set the missing message type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.WindModelADDS.name`
              - Get or set the name of the wind model.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import WindModelADDS


Property detail
---------------

.. py:property:: blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.blend_time
    :type: float

    Get or set the blend time to transition from the previous wind model if one exists.

.. py:property:: interpolation_blend_time
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.interpolation_blend_time
    :type: float

    Get or set the blend time to transition from the previous wind condition.

.. py:property:: message_extrapolation_type
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.message_extrapolation_type
    :type: ADDSMessageExtrapolationType

    Get or set the message extrapolation type.

.. py:property:: message_interpolation_type
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.message_interpolation_type
    :type: ADDSMessageInterpolationType

    Get or set the message interpolation type.

.. py:property:: messages
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.messages
    :type: ADDSMessageCollection

    Get the messages from the current forecast.

.. py:property:: missing_message_type
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.missing_message_type
    :type: ADDSMissingMessageType

    Get or set the missing message type.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.name
    :type: str

    Get or set the name of the wind model.


Method detail
-------------

.. py:method:: add_current_forecast(self) -> str
    :canonical: ansys.stk.core.stkobjects.aviator.WindModelADDS.add_current_forecast

    Add the current forecast from the ADDS service.

    :Returns:

        :obj:`~str`














