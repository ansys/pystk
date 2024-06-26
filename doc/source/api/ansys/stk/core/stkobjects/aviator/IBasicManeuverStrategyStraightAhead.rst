IBasicManeuverStrategyStraightAhead
===================================

.. py:class:: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStraightAhead

   object
   
   Interface used to access options for a Straight Ahead Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: IBasicManeuverStrategyStraightAhead

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStraightAhead.reference_frame`
              - Gets or sets the reference frame the aircraft will use to fly straight ahead.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStraightAhead.compensate_for_coriolis_accel`
              - Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategyStraightAhead


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStraightAhead.reference_frame
    :type: STRAIGHT_AHEAD_REFERENCE_FRAME

    Gets or sets the reference frame the aircraft will use to fly straight ahead.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategyStraightAhead.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


