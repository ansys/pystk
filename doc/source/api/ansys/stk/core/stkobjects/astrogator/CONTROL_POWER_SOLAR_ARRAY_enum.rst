CONTROL_POWER_SOLAR_ARRAY
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CONTROL_POWER_SOLAR_ARRAY

   IntEnum


.. py:currentmodule:: CONTROL_POWER_SOLAR_ARRAY

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~C0`
              - The ThermalModel.C0 coefficient.

            * - :py:attr:`~C1`
              - The ThermalModel.C1 coefficient.

            * - :py:attr:`~C2`
              - The ThermalModel.C2 coefficient.

            * - :py:attr:`~C3`
              - The ThermalModel.C3 coefficient.

            * - :py:attr:`~C4`
              - The ThermalModel.C4 coefficient.

            * - :py:attr:`~AREA`
              - The solar array panel area.

            * - :py:attr:`~EFFICIENCY`
              - The array efficiency in producing output power from a collection of cells.

            * - :py:attr:`~CELL_EFFICIENCY`
              - The cell efficiency in producing output power from incident sunlight.

            * - :py:attr:`~CONCENTRATION`
              - The solar array concentration factor.

            * - :py:attr:`~INCLINATION_TO_SUN_LINE`
              - The angle from the panel normal vector to the apparent sun line.

            * - :py:attr:`~PERCENT_DEGRADATION`
              - The percent degradation per year; degradation factor is (1 - x%/yr)timeSinceRefEpoch.

            * - :py:attr:`~EPOCH`
              - The date and time used as a reference epoch for degradation.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CONTROL_POWER_SOLAR_ARRAY


