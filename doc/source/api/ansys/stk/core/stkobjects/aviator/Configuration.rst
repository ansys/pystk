Configuration
=============

.. py:class:: ansys.stk.core.stkobjects.aviator.Configuration

   Class defining the aircraft configuration for an Aviator mission.

.. py:currentmodule:: Configuration

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.set_empty_cg`
              - Set the aircraft's Empty CG position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.paste_configuration`
              - Paste the aircraft's configuration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.get_stations`
              - Get a collection of the aircraft's payload stations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.save`
              - Save.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.empty_weight`
              - Gets or sets the empty weight of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.max_landing_weight`
              - Gets or sets the max landing weight of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.base_drag_index`
              - Gets or sets the base drag index of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.empty_cgx`
              - Get the X value of the aircraft's Empty CG position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.empty_cgy`
              - Get the Y value of the aircraft's Empty CG position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.empty_cgz`
              - Get the Z value of the aircraft's Empty CG position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.total_weight`
              - Get the total weight of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.total_weight_max_fuel`
              - Get the total weight of the aircraft with all fuel tanks full.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.total_drag_index`
              - Get the total drag index of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.total_cgx`
              - Get the X value of the aircraft's Total CG position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.total_cgy`
              - Get the Y value of the aircraft's Total CG position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.total_cgz`
              - Get the Z value of the aircraft's Total CG position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.total_capacity`
              - Get the total fuel capacity of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Configuration.initial_fuel_state`
              - Get the initial fuel state of the aircraft.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import Configuration


Property detail
---------------

.. py:property:: empty_weight
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.empty_weight
    :type: float

    Gets or sets the empty weight of the aircraft.

.. py:property:: max_landing_weight
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.max_landing_weight
    :type: float

    Gets or sets the max landing weight of the aircraft.

.. py:property:: base_drag_index
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.base_drag_index
    :type: float

    Gets or sets the base drag index of the aircraft.

.. py:property:: empty_cgx
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.empty_cgx
    :type: float

    Get the X value of the aircraft's Empty CG position.

.. py:property:: empty_cgy
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.empty_cgy
    :type: float

    Get the Y value of the aircraft's Empty CG position.

.. py:property:: empty_cgz
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.empty_cgz
    :type: float

    Get the Z value of the aircraft's Empty CG position.

.. py:property:: total_weight
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.total_weight
    :type: float

    Get the total weight of the aircraft.

.. py:property:: total_weight_max_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.total_weight_max_fuel
    :type: float

    Get the total weight of the aircraft with all fuel tanks full.

.. py:property:: total_drag_index
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.total_drag_index
    :type: float

    Get the total drag index of the aircraft.

.. py:property:: total_cgx
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.total_cgx
    :type: float

    Get the X value of the aircraft's Total CG position.

.. py:property:: total_cgy
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.total_cgy
    :type: float

    Get the Y value of the aircraft's Total CG position.

.. py:property:: total_cgz
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.total_cgz
    :type: float

    Get the Z value of the aircraft's Total CG position.

.. py:property:: total_capacity
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.total_capacity
    :type: float

    Get the total fuel capacity of the aircraft.

.. py:property:: initial_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.initial_fuel_state
    :type: float

    Get the initial fuel state of the aircraft.


Method detail
-------------










.. py:method:: set_empty_cg(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.set_empty_cg

    Set the aircraft's Empty CG position.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`







.. py:method:: paste_configuration(self, other_configuration: Configuration) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.paste_configuration

    Paste the aircraft's configuration.

    :Parameters:

    **other_configuration** : :obj:`~Configuration`

    :Returns:

        :obj:`~None`

.. py:method:: get_stations(self) -> StationCollection
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.get_stations

    Get a collection of the aircraft's payload stations.

    :Returns:

        :obj:`~StationCollection`



.. py:method:: save(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.Configuration.save

    Save.

    :Returns:

        :obj:`~None`

