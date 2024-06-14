IVehicleDuration
================

.. py:class:: IVehicleDuration

   object
   
   Look ahead and look behind duration options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~look_ahead`
            * - :py:meth:`~look_behind`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleDuration


Property detail
---------------

.. py:property:: look_ahead
    :canonical: ansys.stk.core.stkobjects.IVehicleDuration.look_ahead
    :type: float

    Look ahead duration: STK calculates attitude at a future point in time defined by adding the look ahead duration to the time of the most current data point. Uses Time Dimension. Valid value is between 1.0 and 1000000.0 seconds.

.. py:property:: look_behind
    :canonical: ansys.stk.core.stkobjects.IVehicleDuration.look_behind
    :type: float

    Look behind duration: specifies how long the temporary data points are to be stored by subtracting the look behind duration from the time of the most current data point. Uses Time Dimension.


