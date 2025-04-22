Terrain
=======

.. py:class:: ansys.stk.core.stkobjects.Terrain

   Class defining terrain data for a Scenario.

.. py:currentmodule:: Terrain

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Terrain.location`
              - Location of the terrain contained in the terrain data file.
            * - :py:attr:`~ansys.stk.core.stkobjects.Terrain.file_type`
              - Type of terrain data file. A member of the TerrainFileType enumeration.
            * - :py:attr:`~ansys.stk.core.stkobjects.Terrain.southwest_latitude`
              - Latitude of the southwest corner of the terrain contained in the terrain data file. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Terrain.southwest_longitude`
              - Longitude of the southwest corner of the terrain contained in the terrain data file. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Terrain.northeast_latitude`
              - Latitude of the northeast corner of the terrain contained in the terrain data file. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Terrain.northeast_longitude`
              - Latitude of the northeast corner of the terrain contained in the terrain data file. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Terrain.resolution`
              - Resolution of the terrain data. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Terrain.use_terrain`
              - Whether to use the terrain.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Terrain


Property detail
---------------

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.Terrain.location
    :type: str

    Location of the terrain contained in the terrain data file.

.. py:property:: file_type
    :canonical: ansys.stk.core.stkobjects.Terrain.file_type
    :type: TerrainFileType

    Type of terrain data file. A member of the TerrainFileType enumeration.

.. py:property:: southwest_latitude
    :canonical: ansys.stk.core.stkobjects.Terrain.southwest_latitude
    :type: typing.Any

    Latitude of the southwest corner of the terrain contained in the terrain data file. Uses Angle Dimension.

.. py:property:: southwest_longitude
    :canonical: ansys.stk.core.stkobjects.Terrain.southwest_longitude
    :type: typing.Any

    Longitude of the southwest corner of the terrain contained in the terrain data file. Uses Angle Dimension.

.. py:property:: northeast_latitude
    :canonical: ansys.stk.core.stkobjects.Terrain.northeast_latitude
    :type: typing.Any

    Latitude of the northeast corner of the terrain contained in the terrain data file. Uses Angle Dimension.

.. py:property:: northeast_longitude
    :canonical: ansys.stk.core.stkobjects.Terrain.northeast_longitude
    :type: typing.Any

    Latitude of the northeast corner of the terrain contained in the terrain data file. Uses Angle Dimension.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.Terrain.resolution
    :type: typing.Any

    Resolution of the terrain data. Uses Angle Dimension.

.. py:property:: use_terrain
    :canonical: ansys.stk.core.stkobjects.Terrain.use_terrain
    :type: bool

    Whether to use the terrain.


