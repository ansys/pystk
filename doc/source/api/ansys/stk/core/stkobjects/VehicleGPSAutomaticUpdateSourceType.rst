VehicleGPSAutomaticUpdateSourceType
===================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGPSAutomaticUpdateSourceType

   IntEnum


.. py:currentmodule:: VehicleGPSAutomaticUpdateSourceType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported TLE source.

            * - :py:attr:`~ONLINE`
              - Auto update the GPS propagator with GPS elements from an online source (AGI server).

            * - :py:attr:`~FILE`
              - Auto update the GPS propagator with GPS elements from file.

            * - :py:attr:`~NONE`
              - Manually specify the almanac with GPS elements.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGPSAutomaticUpdateSourceType


