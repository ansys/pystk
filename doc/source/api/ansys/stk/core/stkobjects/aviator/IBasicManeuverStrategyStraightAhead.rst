IBasicManeuverStrategyStraightAhead
===================================

.. py:class:: IBasicManeuverStrategyStraightAhead

   object
   
   Interface used to access options for a Straight Ahead Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_frame`
            * - :py:meth:`~compensate_for_coriolis_accel`


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


