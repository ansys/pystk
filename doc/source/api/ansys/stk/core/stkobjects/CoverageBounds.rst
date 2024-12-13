CoverageBounds
==============

.. py:class:: ansys.stk.core.stkobjects.CoverageBounds

   IntEnum


.. py:currentmodule:: CoverageBounds

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~CUSTOM_REGIONS`
              - Create a grid within regions specified by a combination of user-selected area targets, region list files (.rl) and/or ArcView shapefiles (.shp).

            * - :py:attr:`~GLOBAL`
              - Create a grid that covers the entire globe.

            * - :py:attr:`~LATITUDE`
              - Create a grid between the user-specified Minimum and Maximum Latitude boundaries.

            * - :py:attr:`~LATITUDE_LINE`
              - Create a set of points along a single latitude line.

            * - :py:attr:`~LONGITUDE_LINE`
              - Create a set of points along a single meridian.

            * - :py:attr:`~CUSTOM_BOUNDARY`
              - Custom boundary coverage.

            * - :py:attr:`~LATITUDE_LONGITUDE_REGION`
              - Create a lat-lon region between the user-specified Minimum and Maximum Latitude/Longitude boundaries.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import CoverageBounds


