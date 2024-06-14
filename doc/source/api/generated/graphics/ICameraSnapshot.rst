ICameraSnapshot
===============

.. py:class:: ICameraSnapshot

   object
   
   Takes snapshots of the 3D window.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~save_to_file`
              - Save a snapshot of the 3D window to the filename with the specified format.
            * - :py:meth:`~save_to_file_with_width_and_dpi`
              - Save a snapshot of the 3D window to the filename with the specified format at high resolution...
            * - :py:meth:`~save_to_clipboard`
              - Save a single frame of the 3D window to the clipboard.
            * - :py:meth:`~save_to_raster`
              - Save a snapshot of the 3D window to a raster.
            * - :py:meth:`~save_to_texture`
              - Save a snapshot of the 3D window to a texture 2d.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ICameraSnapshot



Method detail
-------------

.. py:method:: save_to_file(self, filename:str, cameraSnapshotFormat:"CAMERA_SNAPSHOT_FILE_FORMAT") -> None

    Save a snapshot of the 3D window to the filename with the specified format.

    :Parameters:

    **filename** : :obj:`~str`
    **cameraSnapshotFormat** : :obj:`~"CAMERA_SNAPSHOT_FILE_FORMAT"`

    :Returns:

        :obj:`~None`

.. py:method:: save_to_file_with_width_and_dpi(self, filename:str, cameraSnapshotFormat:"CAMERA_SNAPSHOT_FILE_FORMAT", widthInInches:float, dotsPerInch:float) -> None

    Save a snapshot of the 3D window to the filename with the specified format at high resolution...

    :Parameters:

    **filename** : :obj:`~str`
    **cameraSnapshotFormat** : :obj:`~"CAMERA_SNAPSHOT_FILE_FORMAT"`
    **widthInInches** : :obj:`~float`
    **dotsPerInch** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: save_to_clipboard(self) -> None

    Save a single frame of the 3D window to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: save_to_raster(self) -> "IRaster"

    Save a snapshot of the 3D window to a raster.

    :Returns:

        :obj:`~"IRaster"`

.. py:method:: save_to_texture(self) -> "IRendererTexture2D"

    Save a snapshot of the 3D window to a texture 2d.

    :Returns:

        :obj:`~"IRendererTexture2D"`

