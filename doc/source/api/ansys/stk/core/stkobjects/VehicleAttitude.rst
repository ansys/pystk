VehicleAttitude
===============

.. py:class:: ansys.stk.core.stkobjects.VehicleAttitude

   IntEnum


.. py:currentmodule:: VehicleAttitude

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unsupported attitude option.

            * - :py:attr:`~REAL_TIME`
              - Real-time: define the vehicle's attitude profile using near-real time attitude data supplied via Connect.

            * - :py:attr:`~STANDARD`
              - Standard: use a basic, targeted or external attitude profile.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleAttitude


