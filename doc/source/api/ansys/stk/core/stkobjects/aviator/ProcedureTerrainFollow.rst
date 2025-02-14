ProcedureTerrainFollow
======================

.. py:class:: ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.IProcedure`

   Class defining a terrain following procedure.

.. py:currentmodule:: ProcedureTerrainFollow

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.altitude_agl`
              - Get or set the altitude above ground level the aircraft will fly.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.navigation_options`
              - Get the navigation options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.terrain_following_airspeed_options`
              - Get the terrain following airspeed options.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.reduce_turn_radii`
              - Option to use the minimum speed to compute the turn radius.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.turn_factor`
              - Get or set the maximum turn radius factor.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import ProcedureTerrainFollow


Property detail
---------------

.. py:property:: altitude_agl
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.altitude_agl
    :type: float

    Get or set the altitude above ground level the aircraft will fly.

.. py:property:: navigation_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.navigation_options
    :type: NavigationOptions

    Get the navigation options.

.. py:property:: terrain_following_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.terrain_following_airspeed_options
    :type: CruiseAirspeedOptions

    Get the terrain following airspeed options.

.. py:property:: reduce_turn_radii
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.reduce_turn_radii
    :type: bool

    Option to use the minimum speed to compute the turn radius.

.. py:property:: turn_factor
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.turn_factor
    :type: float

    Get or set the maximum turn radius factor.


Method detail
-------------









.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.ProcedureTerrainFollow.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`

