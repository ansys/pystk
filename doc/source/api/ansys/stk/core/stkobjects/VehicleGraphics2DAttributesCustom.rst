VehicleGraphics2DAttributesCustom
=================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributes`, :py:class:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesDisplayState`

   Vehicle 2D graphics display based on custom intervals.

.. py:currentmodule:: VehicleGraphics2DAttributesCustom

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom.deconflict`
              - Deconflict the custom intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom.default`
              - Get the default attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom.intervals`
              - Get the custom intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom.preemptive_intervals`
              - Opt whether the hiding of graphics for a given interval affects that interval alone or causes the entire path display for that vehicle to disappear when you animate through the selected interval.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DAttributesCustom


Property detail
---------------

.. py:property:: default
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom.default
    :type: IVehicleGraphics2DAttributesBasic

    Get the default attributes.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom.intervals
    :type: IVehicleGraphics2DIntervalsCollection

    Get the custom intervals.

.. py:property:: preemptive_intervals
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom.preemptive_intervals
    :type: bool

    Opt whether the hiding of graphics for a given interval affects that interval alone or causes the entire path display for that vehicle to disappear when you animate through the selected interval.


Method detail
-------------



.. py:method:: deconflict(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DAttributesCustom.deconflict

    Deconflict the custom intervals.

    :Returns:

        :obj:`~None`



