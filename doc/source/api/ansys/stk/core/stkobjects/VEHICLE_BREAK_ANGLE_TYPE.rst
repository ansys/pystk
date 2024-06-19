VEHICLE_BREAK_ANGLE_TYPE
========================

.. py:class:: VEHICLE_BREAK_ANGLE_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BREAK_ANGLE_TYPE_UNKNOWN`
              - Represents a type of break angle not supported by the Object Model.

            * - :py:attr:`~BREAK_BY_LATITUDE`
              - Latitude: the Latitude crossing at which a new pass begins. Recommended for non-equatorial orbits. A latitude of 0 deg for an inclined orbit coincides with the ascending or descending node.

            * - :py:attr:`~BREAK_BY_LONGITUDE`
              - Longitude: the Longitude crossing at which a new pass will begin. Not suitable for polar orbits.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VEHICLE_BREAK_ANGLE_TYPE


