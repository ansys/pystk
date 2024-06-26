IVehicleAttitudeSlewFixedTime
=============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleAttitudeSlewFixedTime

   IVehicleAttitudeSlewBase
   
   Fixed Time slew.

.. py:currentmodule:: IVehicleAttitudeSlewFixedTime

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeSlewFixedTime.slew_time`
              - Gets or sets the time required to change attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeSlewFixedTime.match_angular_velocity`
              - Indicates whether to take account of the angular velocity (slope) at the beginning and the end of the slew.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeSlewFixedTime


Property detail
---------------

.. py:property:: slew_time
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewFixedTime.slew_time
    :type: float

    Gets or sets the time required to change attitude.

.. py:property:: match_angular_velocity
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeSlewFixedTime.match_angular_velocity
    :type: bool

    Indicates whether to take account of the angular velocity (slope) at the beginning and the end of the slew.


