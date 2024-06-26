ITextBatchPrimitiveOptionalParameters
=====================================

.. py:class:: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters

   object
   
   Optional per-string and per-batch parameters for text batch primitive...

.. py:currentmodule:: ITextBatchPrimitiveOptionalParameters

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.set_origins`
              - Define a collection of origins, one for each string in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.set_eye_offsets`
              - Define a collection of eye offsets, one for each string in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.set_pixel_offsets`
              - Define a collection of pixel offsets, one for each string in the batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.set_colors`
              - Define a collection of colors, one for each string in the batch.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.origin`
              - Gets or sets the per-batch origin, which is applied to each string in the text batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.eye_offset`
              - Gets or sets the per-batch eye offset, which is applied to each string in the text batch. The array contains the components of the offset arranged in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.pixel_offset`
              - Gets or sets the per-batch pixel offset, which is applied to each string in the text batch. The array contains one x pixel offset followed by one y pixel offset.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.maximum_string_length`
              - Gets or sets the maximum length of each string in the text batch.
            * - :py:attr:`~ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.screen_space_rendering`
              - Gets or sets a flag that informs the CTextBatchPrimitive to use rendering optimized for screen space text.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ITextBatchPrimitiveOptionalParameters


Property detail
---------------

.. py:property:: origin
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.origin
    :type: ORIGIN

    Gets or sets the per-batch origin, which is applied to each string in the text batch.

.. py:property:: eye_offset
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.eye_offset
    :type: list

    Gets or sets the per-batch eye offset, which is applied to each string in the text batch. The array contains the components of the offset arranged in the order x, y, z.

.. py:property:: pixel_offset
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.pixel_offset
    :type: list

    Gets or sets the per-batch pixel offset, which is applied to each string in the text batch. The array contains one x pixel offset followed by one y pixel offset.

.. py:property:: maximum_string_length
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.maximum_string_length
    :type: int

    Gets or sets the maximum length of each string in the text batch.

.. py:property:: screen_space_rendering
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.screen_space_rendering
    :type: bool

    Gets or sets a flag that informs the CTextBatchPrimitive to use rendering optimized for screen space text.


Method detail
-------------









.. py:method:: set_origins(self, origins: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.set_origins

    Define a collection of origins, one for each string in the batch.

    :Parameters:

    **origins** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_eye_offsets(self, eyeOffsets: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.set_eye_offsets

    Define a collection of eye offsets, one for each string in the batch.

    :Parameters:

    **eyeOffsets** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_pixel_offsets(self, pixelOffsets: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.set_pixel_offsets

    Define a collection of pixel offsets, one for each string in the batch.

    :Parameters:

    **pixelOffsets** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: set_colors(self, colors: list) -> None
    :canonical: ansys.stk.core.graphics.ITextBatchPrimitiveOptionalParameters.set_colors

    Define a collection of colors, one for each string in the batch.

    :Parameters:

    **colors** : :obj:`~list`

    :Returns:

        :obj:`~None`



