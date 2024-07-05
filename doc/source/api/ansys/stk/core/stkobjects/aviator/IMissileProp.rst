IMissileProp
============

.. py:class:: ansys.stk.core.stkobjects.aviator.IMissileProp

   object
   
   Interface used to access the Propulsion options for a missile.

.. py:currentmodule:: IMissileProp

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileProp.prop_strategy`
              - Gets or sets the propulsion strategy type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_simple`
              - Get the interface for a simple propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_external`
              - Get the interface for an external file propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_ramjet`
              - Get the interface for an Ramjet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_turbojet`
              - Get the interface for an Turbojet propulsion strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_rocket`
              - Get the interface for an Rocket propulsion strategy.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileProp


Property detail
---------------

.. py:property:: prop_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.prop_strategy
    :type: MISSILE_PROP_STRATEGY

    Gets or sets the propulsion strategy type.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_simple
    :type: IMissileSimpleProp

    Get the interface for a simple propulsion strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_external
    :type: IMissileExternalProp

    Get the interface for an external file propulsion strategy.

.. py:property:: mode_as_ramjet
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_ramjet
    :type: IMissileRamjetProp

    Get the interface for an Ramjet propulsion strategy.

.. py:property:: mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_turbojet
    :type: IMissileTurbojetProp

    Get the interface for an Turbojet propulsion strategy.

.. py:property:: mode_as_rocket
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_rocket
    :type: IMissileRocketProp

    Get the interface for an Rocket propulsion strategy.


