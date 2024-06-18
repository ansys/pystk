IMarkerBatchPrimitiveOptionalParameters
=======================================

.. py:class:: IMarkerBatchPrimitiveOptionalParameters

   object
   
   Optional per-marker parameters for marker batch primitive that overrides the marker batch's per-batch parameters...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_textures`
              - Define a collection of textures, one for each marker in the batch.
            * - :py:meth:`~set_sizes`
              - Define a collection of sizes, one for each marker in the batch.
            * - :py:meth:`~set_colors`
              - Define a collection of colors, one for each marker in the batch.
            * - :py:meth:`~set_origins`
              - Define a collection of origins, one for each marker in the batch.
            * - :py:meth:`~set_pixel_offsets`
              - Define a collection of pixel offsets, one for each marker in the batch.
            * - :py:meth:`~set_eye_offsets`
              - Define a collection of eye offsets, one for each marker in the batch.
            * - :py:meth:`~set_rotations`
              - Define a collection of rotation angles, one for each marker in the batch.
            * - :py:meth:`~set_texture_coordinates`
              - Define a collection of texture coordinates, one for each marker in the batch.
            * - :py:meth:`~set_time_interval_display_conditions`
              - Define a collection of time interval display conditions, one for each marker in the batch.
            * - :py:meth:`~set_displays`
              - Define a collection of boolean display flags, one for each marker in the batch.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IMarkerBatchPrimitiveOptionalParameters



Method detail
-------------

.. py:method:: set_textures(self, textures:list) -> None

    Define a collection of textures, one for each marker in the batch.

    :Parameters:

    **textures** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_sizes(self, sizes:list) -> None

    Define a collection of sizes, one for each marker in the batch.

    :Parameters:

    **sizes** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_colors(self, colors:list) -> None

    Define a collection of colors, one for each marker in the batch.

    :Parameters:

    **colors** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_origins(self, origins:list) -> None

    Define a collection of origins, one for each marker in the batch.

    :Parameters:

    **origins** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_pixel_offsets(self, pixelOffsets:list) -> None

    Define a collection of pixel offsets, one for each marker in the batch.

    :Parameters:

    **pixelOffsets** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_eye_offsets(self, eyeOffsets:list) -> None

    Define a collection of eye offsets, one for each marker in the batch.

    :Parameters:

    **eyeOffsets** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_rotations(self, rotationAngles:list) -> None

    Define a collection of rotation angles, one for each marker in the batch.

    :Parameters:

    **rotationAngles** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_texture_coordinates(self, textureCoordinates:list) -> None

    Define a collection of texture coordinates, one for each marker in the batch.

    :Parameters:

    **textureCoordinates** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_time_interval_display_conditions(self, timeIntervals:list) -> None

    Define a collection of time interval display conditions, one for each marker in the batch.

    :Parameters:

    **timeIntervals** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_displays(self, displays:list) -> None

    Define a collection of boolean display flags, one for each marker in the batch.

    :Parameters:

    **displays** : :obj:`~list`

    :Returns:

        :obj:`~None`

