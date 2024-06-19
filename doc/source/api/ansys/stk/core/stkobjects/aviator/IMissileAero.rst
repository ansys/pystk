IMissileAero
============

.. py:class:: IMissileAero

   object
   
   Interface used to access the aerodynamics options for a missile.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~aero_strategy`
            * - :py:meth:`~mode_as_simple`
            * - :py:meth:`~mode_as_external`
            * - :py:meth:`~mode_as_advanced`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileAero


Property detail
---------------

.. py:property:: aero_strategy
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAero.aero_strategy
    :type: MISSILE_AERO_STRATEGY

    Gets or sets the aerodynamic strategy type.

.. py:property:: mode_as_simple
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAero.mode_as_simple
    :type: IAgAvtrMissileSimpleAero

    Get the interface for a simple aerodynamics strategy.

.. py:property:: mode_as_external
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAero.mode_as_external
    :type: IAgAvtrMissileExternalAero

    Get the interface for an external file aerodynamics strategy.

.. py:property:: mode_as_advanced
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileAero.mode_as_advanced
    :type: IAgAvtrMissileAdvancedAero

    Get the interface for an advanced aerodynamics strategy.


