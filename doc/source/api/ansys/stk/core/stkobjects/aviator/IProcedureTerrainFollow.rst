IProcedureTerrainFollow
=======================

.. py:class:: IProcedureTerrainFollow

   object
   
   Interface used to access the options for a terrain following procedure.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~altitude_agl`
            * - :py:meth:`~navigation_options`
            * - :py:meth:`~terrain_following_airspeed_options`
            * - :py:meth:`~reduce_turn_radii`
            * - :py:meth:`~turn_factor`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureTerrainFollow


Property detail
---------------

.. py:property:: altitude_agl
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTerrainFollow.altitude_agl
    :type: float

    Gets or sets the altitude above ground level the aircraft will fly.

.. py:property:: navigation_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTerrainFollow.navigation_options
    :type: "IAgAvtrNavigationOptions"

    Get the navigation options.

.. py:property:: terrain_following_airspeed_options
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTerrainFollow.terrain_following_airspeed_options
    :type: "IAgAvtrCruiseAirspeedOptions"

    Get the terrain following airspeed options.

.. py:property:: reduce_turn_radii
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTerrainFollow.reduce_turn_radii
    :type: bool

    Option to use the minimum speed to compute the turn radius.

.. py:property:: turn_factor
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureTerrainFollow.turn_factor
    :type: float

    Gets or sets the maximum turn radius factor.


Method detail
-------------









.. py:method:: get_as_procedure(self) -> "IProcedure"

    Get the procedure interface.

    :Returns:

        :obj:`~"IProcedure"`

