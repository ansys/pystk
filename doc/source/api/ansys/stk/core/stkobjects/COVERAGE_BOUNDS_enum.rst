COVERAGE_BOUNDS
===============

.. py:class:: ansys.stk.core.stkobjects.COVERAGE_BOUNDS

   IntEnum


.. py:currentmodule:: COVERAGE_BOUNDS

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~BOUNDS_CUSTOM_REGIONS`
              - Create a grid within regions specified by a combination of user-selected area targets, region list files (.rl) and/or ArcView shapefiles (.shp).

            * - :py:attr:`~BOUNDS_GLOBAL`
              - Create a grid that covers the entire globe.

            * - :py:attr:`~BOUNDS_LAT`
              - Create a grid between the user-specified Minimum and Maximum Latitude boundaries.

            * - :py:attr:`~BOUNDS_LAT_LINE`
              - Create a set of points along a single latitude line.

            * - :py:attr:`~BOUNDS_LON_LINE`
              - Create a set of points along a single meridian.

            * - :py:attr:`~BOUNDS_CUSTOM_BOUNDARY`
              - Custom boundary coverage.

            * - :py:attr:`~BOUNDS_LAT_LON_REGION`
              - Create a lat-lon region between the user-specified Minimum and Maximum Latitude/Longitude boundaries.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import COVERAGE_BOUNDS


