CameraSnapshot
==============

.. py:class:: ansys.stk.core.graphics.CameraSnapshot

   Takes snapshots of the 3D window.

.. py:currentmodule:: CameraSnapshot

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.CameraSnapshot.save_to_file`
              - Save a snapshot of the 3D window to the filename with the specified format.
            * - :py:attr:`~ansys.stk.core.graphics.CameraSnapshot.save_to_file_with_width_and_dpi`
              - Save a snapshot of the 3D window to the filename with the specified format at high resolution...
            * - :py:attr:`~ansys.stk.core.graphics.CameraSnapshot.save_to_clipboard`
              - Save a single frame of the 3D window to the clipboard.
            * - :py:attr:`~ansys.stk.core.graphics.CameraSnapshot.save_to_raster`
              - Save a snapshot of the 3D window to a raster.
            * - :py:attr:`~ansys.stk.core.graphics.CameraSnapshot.save_to_texture`
              - Save a snapshot of the 3D window to a texture 2d.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import CameraSnapshot



Method detail
-------------

.. py:method:: save_to_file(self, filename: str, cameraSnapshotFormat: CAMERA_SNAPSHOT_FILE_FORMAT) -> None
    :canonical: ansys.stk.core.graphics.CameraSnapshot.save_to_file

    Save a snapshot of the 3D window to the filename with the specified format.

    :Parameters:

    **filename** : :obj:`~str`
    **cameraSnapshotFormat** : :obj:`~CAMERA_SNAPSHOT_FILE_FORMAT`

    :Returns:

        :obj:`~None`

.. py:method:: save_to_file_with_width_and_dpi(self, filename: str, cameraSnapshotFormat: CAMERA_SNAPSHOT_FILE_FORMAT, widthInInches: float, dotsPerInch: float) -> None
    :canonical: ansys.stk.core.graphics.CameraSnapshot.save_to_file_with_width_and_dpi

    Save a snapshot of the 3D window to the filename with the specified format at high resolution...

    :Parameters:

    **filename** : :obj:`~str`
    **cameraSnapshotFormat** : :obj:`~CAMERA_SNAPSHOT_FILE_FORMAT`
    **widthInInches** : :obj:`~float`
    **dotsPerInch** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: save_to_clipboard(self) -> None
    :canonical: ansys.stk.core.graphics.CameraSnapshot.save_to_clipboard

    Save a single frame of the 3D window to the clipboard.

    :Returns:

        :obj:`~None`

.. py:method:: save_to_raster(self) -> IRaster
    :canonical: ansys.stk.core.graphics.CameraSnapshot.save_to_raster

    Save a snapshot of the 3D window to a raster.

    :Returns:

        :obj:`~IRaster`

.. py:method:: save_to_texture(self) -> RendererTexture2D
    :canonical: ansys.stk.core.graphics.CameraSnapshot.save_to_texture

    Save a snapshot of the 3D window to a texture 2d.

    :Returns:

        :obj:`~RendererTexture2D`

