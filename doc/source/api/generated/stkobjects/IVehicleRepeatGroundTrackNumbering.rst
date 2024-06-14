IVehicleRepeatGroundTrackNumbering
==================================

.. py:class:: IVehicleRepeatGroundTrackNumbering

   object
   
   Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~first_path_num`
            * - :py:meth:`~revs_to_repeat`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleRepeatGroundTrackNumbering


Property detail
---------------

.. py:property:: first_path_num
    :canonical: ansys.stk.core.stkobjects.IVehicleRepeatGroundTrackNumbering.first_path_num
    :type: int

    Path numbers are incremented concurrently with pass numbers, but are limited to a range of 1 to the number of revolutions in the repeat cycle. Dimensionless.

.. py:property:: revs_to_repeat
    :canonical: ansys.stk.core.stkobjects.IVehicleRepeatGroundTrackNumbering.revs_to_repeat
    :type: int

    Once the path number reaches the number of revolutions in the repeat cycle, the next path number is 1. Dimensionless.


