IVehicleGraphics2DAttributesCustom
==================================

.. py:class:: IVehicleGraphics2DAttributesCustom

   IVehicleGraphics2DAttributes
   
   Vehicle 2D graphics display based on custom intervals.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~deconflict`
              - Deconflict the custom intervals.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~default`
            * - :py:meth:`~intervals`
            * - :py:meth:`~preemptive_intervals`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DAttributesCustom


Property detail
---------------

.. py:property:: default
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.default
    :type: IAgVeGfxAttributesBasic

    Get the default attributes.

.. py:property:: intervals
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesCustom.intervals
    :type: IAgVeGfxIntervalsCollection

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



