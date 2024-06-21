IConfiguration
==============

.. py:class:: ansys.stk.core.stkobjects.aviator.IConfiguration

   object
   
   Interface used to change an aircraft's configuration for an Aviator mission.

.. py:currentmodule:: IConfiguration

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.set_empty_cg`
              - Set the aircraft's Empty CG position.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.paste_configuration`
              - Paste the aircraft's configuration.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.get_stations`
              - Get a collection of the aircraft's payload stations.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.save`
              - Save.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.empty_weight`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.max_landing_weight`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.base_drag_index`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.empty_cgx`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.empty_cgy`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.empty_cgz`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.total_weight`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.total_weight_max_fuel`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.total_drag_index`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.total_cgx`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.total_cgy`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.total_cgz`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.total_capacity`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IConfiguration.initial_fuel_state`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IConfiguration


Property detail
---------------

.. py:property:: empty_weight
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.empty_weight
    :type: float

    Gets or sets the empty weight of the aircraft.

.. py:property:: max_landing_weight
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.max_landing_weight
    :type: float

    Gets or sets the max landing weight of the aircraft.

.. py:property:: base_drag_index
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.base_drag_index
    :type: float

    Gets or sets the base drag index of the aircraft.

.. py:property:: empty_cgx
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.empty_cgx
    :type: float

    Get the X value of the aircraft's Empty CG position.

.. py:property:: empty_cgy
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.empty_cgy
    :type: float

    Get the Y value of the aircraft's Empty CG position.

.. py:property:: empty_cgz
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.empty_cgz
    :type: float

    Get the Z value of the aircraft's Empty CG position.

.. py:property:: total_weight
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.total_weight
    :type: float

    Get the total weight of the aircraft.

.. py:property:: total_weight_max_fuel
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.total_weight_max_fuel
    :type: float

    Get the total weight of the aircraft with all fuel tanks full.

.. py:property:: total_drag_index
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.total_drag_index
    :type: float

    Get the total drag index of the aircraft.

.. py:property:: total_cgx
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.total_cgx
    :type: float

    Get the X value of the aircraft's Total CG position.

.. py:property:: total_cgy
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.total_cgy
    :type: float

    Get the Y value of the aircraft's Total CG position.

.. py:property:: total_cgz
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.total_cgz
    :type: float

    Get the Z value of the aircraft's Total CG position.

.. py:property:: total_capacity
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.total_capacity
    :type: float

    Get the total fuel capacity of the aircraft.

.. py:property:: initial_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.initial_fuel_state
    :type: float

    Get the initial fuel state of the aircraft.


Method detail
-------------










.. py:method:: set_empty_cg(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.set_empty_cg

    Set the aircraft's Empty CG position.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`







.. py:method:: paste_configuration(self, otherConfiguration: IConfiguration) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.paste_configuration

    Paste the aircraft's configuration.

    :Parameters:

    **otherConfiguration** : :obj:`~IConfiguration`

    :Returns:

        :obj:`~None`

.. py:method:: get_stations(self) -> IStationCollection
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.get_stations

    Get a collection of the aircraft's payload stations.

    :Returns:

        :obj:`~IStationCollection`



.. py:method:: save(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IConfiguration.save

    Save.

    :Returns:

        :obj:`~None`

