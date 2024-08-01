MissilePropulsion
=================

.. py:class:: ansys.stk.core.stkobjects.aviator.MissilePropulsion

   Bases: 

   Class defining the propulsion options for a missile.

.. py:currentmodule:: MissilePropulsion

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissilePropulsion.propulsion_strategy`
              - Gets or sets the propulsion strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_simple`
              - Get the interface for a simple propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_external`
              - Get the interface for an external file propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_ramjet`
              - Get the interface for an Ramjet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_turbojet`
              - Get the interface for an Turbojet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_rocket`
              - Get the interface for an Rocket propulsion strategy.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import MissilePropulsion


Property detail
---------------

.. py:property:: propulsion_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.MissilePropulsion.propulsion_strategy
    :type: MISSILE_PROPULSION_STRATEGY

    Gets or sets the propulsion strategy type.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_simple
    :type: IMissileSimplePropulsion

    Get the interface for a simple propulsion strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_external
    :type: IMissileExternalPropulsion

    Get the interface for an external file propulsion strategy.

.. py:property:: mode_as_ramjet
    :canonical: ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_ramjet
    :type: IMissileRamjetPropulsion

    Get the interface for an Ramjet propulsion strategy.

.. py:property:: mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_turbojet
    :type: IMissileTurbojetPropulsion

    Get the interface for an Turbojet propulsion strategy.

.. py:property:: mode_as_rocket
    :canonical: ansys.stk.core.stkobjects.aviator.MissilePropulsion.mode_as_rocket
    :type: IMissileRocketPropulsion

    Get the interface for an Rocket propulsion strategy.


