BasicManeuverStrategyStraightAhead
==================================

.. py:class:: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategy`

   Class defining the Straight Ahead strategy for a basic maneuver procedure.

.. py:currentmodule:: BasicManeuverStrategyStraightAhead

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead.reference_frame`
              - Get or set the reference frame the aircraft will use to fly straight ahead.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead.compensate_for_coriolis_acceleration`
              - Get or set the option to compensate for the acceleration due to the Coriolis effect.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import BasicManeuverStrategyStraightAhead


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead.reference_frame
    :type: StraightAheadReferenceFrame

    Get or set the reference frame the aircraft will use to fly straight ahead.

.. py:property:: compensate_for_coriolis_acceleration
    :canonical: ansys.stk.core.stkobjects.aviator.BasicManeuverStrategyStraightAhead.compensate_for_coriolis_acceleration
    :type: bool

    Get or set the option to compensate for the acceleration due to the Coriolis effect.


