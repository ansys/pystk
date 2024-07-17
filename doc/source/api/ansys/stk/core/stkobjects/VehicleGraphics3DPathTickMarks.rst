VehicleGraphics3DPathTickMarks
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks

   Bases: 

   Tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

.. py:currentmodule:: VehicleGraphics3DPathTickMarks

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.set_tick_data_type`
              - Set the type of tick marks to display.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.is_tick_data_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.is_visible`
              - Opt whether to display tick marks.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data_type`
              - Get the type of tick marks to display.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data`
              - Get the tick mark data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DPathTickMarks


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.is_visible
    :type: bool

    Opt whether to display tick marks.

.. py:property:: tick_data_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data_type
    :type: TICK_DATA

    Get the type of tick marks to display.

.. py:property:: tick_data_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: tick_data
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.tick_data
    :type: IVehicleGraphics3DTickData

    Get the tick mark data.


Method detail
-------------




.. py:method:: set_tick_data_type(self, tickData: TICK_DATA) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.set_tick_data_type

    Set the type of tick marks to display.

    :Parameters:

    **tickData** : :obj:`~TICK_DATA`

    :Returns:

        :obj:`~None`

.. py:method:: is_tick_data_type_supported(self, tickData: TICK_DATA) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DPathTickMarks.is_tick_data_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **tickData** : :obj:`~TICK_DATA`

    :Returns:

        :obj:`~bool`



