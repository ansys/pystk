VehiclePartialPassMeasurement
=============================

.. py:class:: ansys.stk.core.stkobjects.VehiclePartialPassMeasurement

   IntEnum


.. py:currentmodule:: VehiclePartialPassMeasurement

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ANGLE`
              - By Angle: angles are used to measure partial passes.

            * - :py:attr:`~MEAN_ARGUMENT_OF_LATITUDE`
              - By Mean Argument of Latitude: passes are measured as the difference in the mean argument of latitude at the current time and that at the start of the pass break divided by 2 pi (argument of latitude = mean anomaly plus argument of perigee).

            * - :py:attr:`~TIME`
              - By Time: time is used to measure partial passes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePartialPassMeasurement


