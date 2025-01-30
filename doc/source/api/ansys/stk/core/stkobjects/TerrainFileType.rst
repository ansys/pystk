TerrainFileType
===============

.. py:class:: ansys.stk.core.stkobjects.TerrainFileType

   IntEnum


.. py:currentmodule:: TerrainFileType

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~USGS_DEM`
              - U.S. Geological Survey Digital Elevation Model. Moderate resolution.

            * - :py:attr:`~GTOPO30`
              - GTOPO30 global digital elevation model with horizontal grid spacing of 30 arc seconds. Use this for STK World terrain.

            * - :py:attr:`~NIMA_NGA_TERRAIN_DIRECTORY`
              - NGA Digital Terrain Elevation Data (DTED).

            * - :py:attr:`~MOLA_TERRAIN`
              - Mars Orbiter Laser Altimeter (MOLA)terrain data.

            * - :py:attr:`~GEODAS_GRID_DATA`
              - GEODAS (GEOphysical DAta System), an interactive database management system developed by the National Geophysical Data Center (NGDC) for use in the assimilation, storage and retrieval of geophysical data.

            * - :py:attr:`~MUSE_RASTER_FILE`
              - MUSE Raster File: NGA elevation data that has been converted using the MUSE software raster importer. MUSE terrain files contain position information.

            * - :py:attr:`~NIM0_NIMA_NGA_DTED_LEVEL_0`
              - NIM0 NIMA/NGA DTED Level 0 (.dto).

            * - :py:attr:`~NIM1_NIMA_NGA_DTED_LEVEL_1`
              - NIM1 NIMA/NGA DTED Level 1 (.dt1).

            * - :py:attr:`~NIM2_NIMA_NGA_DTED_LEVEL_2`
              - NIM2 NIMA/NGA DTED Level 2 (.dt2).

            * - :py:attr:`~NIM3_NIMA_NGA_DTED_LEVEL_3`
              - NIM3 NIMA/NGA DTED Level 3 (.dt3).

            * - :py:attr:`~NIM4_NIMA_NGA_DTED_LEVEL_4`
              - NIM4  NIMA/NGA DTED Level 4 (.dt4).

            * - :py:attr:`~NIM5_NIMA_NGA_DTED_LEVEL_5`
              - NIM5 NIMA/NGA DTED Level 5 (.dt5).

            * - :py:attr:`~ARC_INFO_BINARY_GRID`
              - Arc/Info Binary Grid Files (.adf).

            * - :py:attr:`~ARC_INFO_BINARY_GRID_MEAN_SEA_LEVEL`
              - Arc/Info Binary Grid - MSL (.adf).

            * - :py:attr:`~PDTT`
              - AGI Terrain File (.pdtt).

            * - :py:attr:`~AGI_WORLD_TERRAIN`
              - AGI World Terrain File (.hdr).

            * - :py:attr:`~TIFF_TERRAIN_FILE_IN_MEAN_SEA_LEVEL`
              - Tagged Image File Format - MSL (.tif).

            * - :py:attr:`~TIFF_TERRAIN_FILE`
              - Tagged Image File Format (.tif).

            * - :py:attr:`~ARC_INFO_GRID_DEPTH_MEAN_SEA_LEVEL`
              - ArcInfo Grid Depth MSL (.adf).


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import TerrainFileType


