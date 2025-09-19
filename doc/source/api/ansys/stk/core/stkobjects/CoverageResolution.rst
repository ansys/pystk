CoverageResolution
==================

.. py:class:: ansys.stk.core.stkobjects.CoverageResolution

   IntEnum


.. py:currentmodule:: CoverageResolution

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~RESOLUTION_AREA`
              - Define the location of grid coordinates by using the specified area to determine a latitude/longitude spacing scheme at the equator.

            * - :py:attr:`~RESOLUTION_DISTANCE`
              - Define the location of the grid coordinates by using the specified distance to determine a latitude/longitude spacing scheme at the equator.

            * - :py:attr:`~RESOLUTION_LATITUDE_LONGITUDE`
              - Determine the location of grid coordinates by applying a user-specified value at the equator. STK stretches grid points in longitude at higher or lower latitudes in an attempt to preserve the area of the grid point.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageResolution


