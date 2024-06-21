IAttitudeTransitions
====================

.. py:class:: ansys.stk.core.stkobjects.aviator.IAttitudeTransitions

   object
   
   Interface used to access the Attitude Transitions options found in the Basic Acceleration Model of an aircraft.

.. py:currentmodule:: IAttitudeTransitions

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAttitudeTransitions.roll_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAttitudeTransitions.pitch_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IAttitudeTransitions.yaw_rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAttitudeTransitions


Property detail
---------------

.. py:property:: roll_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IAttitudeTransitions.roll_rate
    :type: typing.Any

    Gets or sets the roll rate when the aircraft in a turn.

.. py:property:: pitch_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IAttitudeTransitions.pitch_rate
    :type: typing.Any

    Gets or sets the pitch rate when transitioning between attitude modes.

.. py:property:: yaw_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IAttitudeTransitions.yaw_rate
    :type: typing.Any

    Gets or sets the yaw rate when transitioning between attitude modes.


