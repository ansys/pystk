IMissileSimpleProp
==================

.. py:class:: ansys.stk.core.stkobjects.aviator.IMissileSimpleProp

   object
   
   Interface used to access the Simple propulsion options for a missile.

.. py:currentmodule:: IMissileSimpleProp

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileSimpleProp.max_thrust`
              - Gets or sets the maximum thrust of the missile.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileSimpleProp.fuel_flow`
              - Gets or sets the fuel flow at max thrust.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IMissileSimpleProp.no_thrust_when_no_fuel`
              - Opt to have no thrust if the fuel is empty.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IMissileSimpleProp


Property detail
---------------

.. py:property:: max_thrust
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileSimpleProp.max_thrust
    :type: float

    Gets or sets the maximum thrust of the missile.

.. py:property:: fuel_flow
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileSimpleProp.fuel_flow
    :type: float

    Gets or sets the fuel flow at max thrust.

.. py:property:: no_thrust_when_no_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IMissileSimpleProp.no_thrust_when_no_fuel
    :type: bool

    Opt to have no thrust if the fuel is empty.


