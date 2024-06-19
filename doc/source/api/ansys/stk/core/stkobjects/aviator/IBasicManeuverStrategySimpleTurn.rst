IBasicManeuverStrategySimpleTurn
================================

.. py:class:: IBasicManeuverStrategySimpleTurn

   object
   
   Interface used to access options for a Simple Turn Strategy of a Basic Maneuver Procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_frame`
            * - :py:meth:`~turn_angle`
            * - :py:meth:`~turn_radius_factor`
            * - :py:meth:`~compensate_for_coriolis_accel`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IBasicManeuverStrategySimpleTurn


Property detail
---------------

.. py:property:: reference_frame
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySimpleTurn.reference_frame
    :type: BASIC_MANEUVER_REFERENCE_FRAME

    Gets or sets the reference frame for the simple turn.

.. py:property:: turn_angle
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySimpleTurn.turn_angle
    :type: typing.Any

    Gets or sets the turn angle for the simple turn.

.. py:property:: turn_radius_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySimpleTurn.turn_radius_factor
    :type: float

    Gets or sets the turn radius factor for the simple turn.

.. py:property:: compensate_for_coriolis_accel
    :canonical: ansys.stk.core.stkobjects.aviator.IBasicManeuverStrategySimpleTurn.compensate_for_coriolis_accel
    :type: bool

    Gets or sets the option to compensate for the acceleration due to the Coriolis effect.


