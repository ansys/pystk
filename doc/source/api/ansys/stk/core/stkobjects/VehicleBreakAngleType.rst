VehicleBreakAngleType
=====================

.. py:class:: ansys.stk.core.stkobjects.VehicleBreakAngleType

   IntEnum


.. py:currentmodule:: VehicleBreakAngleType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Represents a type of break angle not supported by the Object Model.

            * - :py:attr:`~BY_LATITUDE`
              - Latitude: the Latitude crossing at which a new pass begins. Recommended for non-equatorial orbits. A latitude of 0 deg for an inclined orbit coincides with the ascending or descending node.

            * - :py:attr:`~BY_LONGITUDE`
              - Longitude: the Longitude crossing at which a new pass will begin. Not suitable for polar orbits.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleBreakAngleType


