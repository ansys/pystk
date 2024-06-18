IVehicleGraphics3DPathTickMarks
===============================

.. py:class:: IVehicleGraphics3DPathTickMarks

   object
   
   Interface for tick marks for 3D trajectory graphics. Tick marks represent milestones at specified intervals along the trajectory in the 3D window.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_tick_data_type`
              - Set the type of tick marks to display.
            * - :py:meth:`~is_tick_data_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_visible`
            * - :py:meth:`~tick_data_type`
            * - :py:meth:`~tick_data_supported_types`
            * - :py:meth:`~tick_data`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DPathTickMarks


Property detail
---------------

.. py:property:: is_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DPathTickMarks.is_visible
    :type: bool

    Opt whether to display tick marks.

.. py:property:: tick_data_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DPathTickMarks.tick_data_type
    :type: "TICK_DATA"

    Get the type of tick marks to display.

.. py:property:: tick_data_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DPathTickMarks.tick_data_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: tick_data
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DPathTickMarks.tick_data
    :type: "IAgVeVOTickData"

    Get the tick mark data.


Method detail
-------------




.. py:method:: set_tick_data_type(self, tickData:"TICK_DATA") -> None

    Set the type of tick marks to display.

    :Parameters:

    **tickData** : :obj:`~"TICK_DATA"`

    :Returns:

        :obj:`~None`

.. py:method:: is_tick_data_type_supported(self, tickData:"TICK_DATA") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **tickData** : :obj:`~"TICK_DATA"`

    :Returns:

        :obj:`~bool`



