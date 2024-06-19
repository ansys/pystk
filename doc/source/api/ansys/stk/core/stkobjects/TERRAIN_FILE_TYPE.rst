TERRAIN_FILE_TYPE
=================

.. py:class:: TERRAIN_FILE_TYPE

   IntEnum


.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~USGSDEM`
              - U.S. Geological Survey Digital Elevation Model. Moderate resolution.

            * - :py:attr:`~GTOPO30`
              - GTOPO30 global digital elevation model with horizontal grid spacing of 30 arc seconds. Use this for STK World terrain.

            * - :py:attr:`~NIMANGA_TERRAIN_DIRECTION`
              - NGA Digital Terrain Elevation Data (DTED).

            * - :py:attr:`~MOLA_TERRAIN`
              - Mars Orbiter Laser Altimeter (MOLA)terrain data.

            * - :py:attr:`~GEODAS_GRID_DATA`
              - GEODAS (GEOphysical DAta System), an interactive database management system developed by the National Geophysical Data Center (NGDC) for use in the assimilation, storage and retrieval of geophysical data.

            * - :py:attr:`~MUSE_RASTER_FILE`
              - MUSE Raster File: NGA elevation data that has been converted using the MUSE software raster importer. MUSE terrain files contain position information.

            * - :py:attr:`~NIMANGADTED_LEVEL0`
              - NIM0 NIMA/NGA DTED Level 0 (.dto).

            * - :py:attr:`~NIMANGADTED_LEVEL1`
              - NIM1 NIMA/NGA DTED Level 1 (.dt1).

            * - :py:attr:`~NIMANGADTED_LEVEL2`
              - NIM2 NIMA/NGA DTED Level 2 (.dt2).

            * - :py:attr:`~NIMANGADTED_LEVEL3`
              - NIM3 NIMA/NGA DTED Level 3 (.dt3).

            * - :py:attr:`~NIMANGADTED_LEVEL4`
              - NIM4  NIMA/NGA DTED Level 4 (.dt4).

            * - :py:attr:`~NIMANGADTED_LEVEL5`
              - NIM5 NIMA/NGA DTED Level 5 (.dt5).

            * - :py:attr:`~ARC_INFO_BIN_GRID_FILE`
              - Arc/Info Binary Grid Files (.adf).

            * - :py:attr:`~ARC_INFO_BIN_GRID_MSL_FILE`
              - Arc/Info Binary Grid - MSL (.adf).

            * - :py:attr:`~PDTT_TERRAIN_FILE`
              - AGI Terrain File (.pdtt).

            * - :py:attr:`~AGI_WORLD_TERRAIN`
              - AGI World Terrain File (.hdr).

            * - :py:attr:`~TIFFMSL_TERRAIN_FILE`
              - Tagged Image File Format - MSL (.tif).

            * - :py:attr:`~TIFF_TERRAIN_FILE`
              - Tagged Image File Format (.tif).

            * - :py:attr:`~ARC_INFO_GRID_DEPTH_MSL_FILE`
              - ArcInfo Grid Depth MSL (.adf).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TERRAIN_FILE_TYPE


