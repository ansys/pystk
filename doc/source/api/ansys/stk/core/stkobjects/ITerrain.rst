ITerrain
========

.. py:class:: ITerrain

   object
   
   IAgTerrain Interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~location`
            * - :py:meth:`~file_type`
            * - :py:meth:`~sw_latitude`
            * - :py:meth:`~sw_longitude`
            * - :py:meth:`~ne_latitude`
            * - :py:meth:`~ne_longitude`
            * - :py:meth:`~resolution`
            * - :py:meth:`~use_terrain`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ITerrain


Property detail
---------------

.. py:property:: location
    :canonical: ansys.stk.core.stkobjects.ITerrain.location
    :type: str

    Location of the terrain contained in the terrain data file.

.. py:property:: file_type
    :canonical: ansys.stk.core.stkobjects.ITerrain.file_type
    :type: TERRAIN_FILE_TYPE

    Type of terrain data file. A member of the AgETerrainFileType enumeration.

.. py:property:: sw_latitude
    :canonical: ansys.stk.core.stkobjects.ITerrain.sw_latitude
    :type: typing.Any

    Latitude of the southwest corner of the terrain contained in the terrain data file. Uses Angle Dimension.

.. py:property:: sw_longitude
    :canonical: ansys.stk.core.stkobjects.ITerrain.sw_longitude
    :type: typing.Any

    Longitude of the southwest corner of the terrain contained in the terrain data file. Uses Angle Dimension.

.. py:property:: ne_latitude
    :canonical: ansys.stk.core.stkobjects.ITerrain.ne_latitude
    :type: typing.Any

    Latitude of the northeast corner of the terrain contained in the terrain data file. Uses Angle Dimension.

.. py:property:: ne_longitude
    :canonical: ansys.stk.core.stkobjects.ITerrain.ne_longitude
    :type: typing.Any

    Latitude of the northeast corner of the terrain contained in the terrain data file. Uses Angle Dimension.

.. py:property:: resolution
    :canonical: ansys.stk.core.stkobjects.ITerrain.resolution
    :type: typing.Any

    Resolution of the terrain data. Uses Angle Dimension.

.. py:property:: use_terrain
    :canonical: ansys.stk.core.stkobjects.ITerrain.use_terrain
    :type: bool

    Whether to use the terrain.


