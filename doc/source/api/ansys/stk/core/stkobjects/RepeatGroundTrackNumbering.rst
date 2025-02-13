RepeatGroundTrackNumbering
==========================

.. py:class:: ansys.stk.core.stkobjects.RepeatGroundTrackNumbering

   Repeat ground track numbering: The path number in the repeat ground track cycle corresponding to the initial conditions and the number of revolutions in the repeat cycle.

.. py:currentmodule:: RepeatGroundTrackNumbering

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.RepeatGroundTrackNumbering.first_pass_number`
              - Path numbers are incremented concurrently with pass numbers, but are limited to a range of 1 to the number of revolutions in the repeat cycle. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.RepeatGroundTrackNumbering.revolutions_to_repeat`
              - Once the path number reaches the number of revolutions in the repeat cycle, the next path number is 1. Dimensionless.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import RepeatGroundTrackNumbering


Property detail
---------------

.. py:property:: first_pass_number
    :canonical: ansys.stk.core.stkobjects.RepeatGroundTrackNumbering.first_pass_number
    :type: int

    Path numbers are incremented concurrently with pass numbers, but are limited to a range of 1 to the number of revolutions in the repeat cycle. Dimensionless.

.. py:property:: revolutions_to_repeat
    :canonical: ansys.stk.core.stkobjects.RepeatGroundTrackNumbering.revolutions_to_repeat
    :type: int

    Once the path number reaches the number of revolutions in the repeat cycle, the next path number is 1. Dimensionless.


