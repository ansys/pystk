IVehicleGraphics2DAttributesCustom
==================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom

   IVehicleGraphics2DAttributes
   
   Vehicle 2D graphics display based on custom intervals.

.. py:currentmodule:: IVehicleGraphics2DAttributesCustom

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.deconflict`
              - Deconflict the custom intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.default`
              - Get the default attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.intervals`
              - Get the custom intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.preemptive_intervals`
              - Opt whether the hiding of graphics for a given interval affects that interval alone or causes the entire path display for that vehicle to disappear when you animate through the selected interval.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DAttributesCustom


Property detail
---------------

.. py:property:: default
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.default
    :type: IVehicleGraphics2DAttributesBasic

    Get the default attributes.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.intervals
    :type: IVehicleGraphics2DIntervalsCollection

    Get the custom intervals.

.. py:property:: preemptive_intervals
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.preemptive_intervals
    :type: bool

    Opt whether the hiding of graphics for a given interval affects that interval alone or causes the entire path display for that vehicle to disappear when you animate through the selected interval.


Method detail
-------------



.. py:method:: deconflict(self) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.deconflict

    Deconflict the custom intervals.

    :Returns:

        :obj:`~None`



