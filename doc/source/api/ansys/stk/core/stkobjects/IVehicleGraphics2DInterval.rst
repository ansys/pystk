IVehicleGraphics2DInterval
==========================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DInterval

   object
   
   2D Graphics display based on custom intervals.

.. py:currentmodule:: IVehicleGraphics2DInterval

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DInterval.graphics_2d_attributes`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DInterval.start_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DInterval.stop_time`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DInterval


Property detail
---------------

.. py:property:: graphics_2d_attributes
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DInterval.graphics_2d_attributes
    :type: IVehicleGraphics2DAttributesBasic

    Get the 2D Graphics attributes for the interval.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DInterval.start_time
    :type: typing.Any

    Gets or sets the start time of the custom interval. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DInterval.stop_time
    :type: typing.Any

    Gets or sets the stop time of the custom interval. Uses DateFormat Dimension.


