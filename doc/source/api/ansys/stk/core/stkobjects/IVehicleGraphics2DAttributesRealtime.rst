IVehicleGraphics2DAttributesRealtime
====================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime

   IVehicleGraphics2DAttributes
   
   2D Graphics attributes for a vehicle based on real time data state.

.. py:currentmodule:: IVehicleGraphics2DAttributesRealtime

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime.history`
              - Get the historical data, consisting of all data points received from the time of the most current data point back to the last point within the look behind duration.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime.spline`
              - Get the spline between the last point received and the new point.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime.look_ahead`
              - Get the look ahead data, calculated on the basis of the last received data point.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime.drop_out`
              - Get the drop out, i.e. data that is outside the time out gap.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DAttributesRealtime


Property detail
---------------

.. py:property:: history
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime.history
    :type: IVehicleGraphics2DAttributesBasic

    Get the historical data, consisting of all data points received from the time of the most current data point back to the last point within the look behind duration.

.. py:property:: spline
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime.spline
    :type: IVehicleGraphics2DAttributesBasic

    Get the spline between the last point received and the new point.

.. py:property:: look_ahead
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime.look_ahead
    :type: IVehicleGraphics2DAttributesBasic

    Get the look ahead data, calculated on the basis of the last received data point.

.. py:property:: drop_out
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DAttributesRealtime.drop_out
    :type: IVehicleGraphics2DAttributesBasic

    Get the drop out, i.e. data that is outside the time out gap.


