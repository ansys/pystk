IMissileProp
============

.. py:class:: IMissileProp

   object
   
   Interface used to access the Propulsion options for a missile.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~prop_strategy`
            * - :py:meth:`~mode_as_simple`
            * - :py:meth:`~mode_as_external`
            * - :py:meth:`~mode_as_ramjet`
            * - :py:meth:`~mode_as_turbojet`
            * - :py:meth:`~mode_as_rocket`


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
    :type: IAgAvtrMissileSimpleProp

    Get the interface for a simple propulsion strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_external
    :type: IAgAvtrMissileExternalProp

    Get the interface for an external file propulsion strategy.

.. py:property:: mode_as_ramjet
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_ramjet
    :type: IAgAvtrMissileRamjetProp

    Get the interface for an Ramjet propulsion strategy.

.. py:property:: mode_as_turbojet
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_turbojet
    :type: IAgAvtrMissileTurbojetProp

    Get the interface for an Turbojet propulsion strategy.

.. py:property:: mode_as_rocket
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileProp.mode_as_rocket
    :type: IAgAvtrMissileRocketProp

    Get the interface for an Rocket propulsion strategy.


