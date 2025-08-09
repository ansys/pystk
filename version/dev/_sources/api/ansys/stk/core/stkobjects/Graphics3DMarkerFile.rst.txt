Graphics3DMarkerFile
====================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DMarkerFile

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGraphics3DMarkerData`

   Class defining 3D marker file attributes.

.. py:currentmodule:: Graphics3DMarkerFile

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarkerFile.file_path`
              - Full file path and name to display a 2D image to represent the object at the specified threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarkerFile.filename`
              - Display a 2D image to represent the object at the specified threshold.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarkerFile.is_transparent`
              - Use the color of the upper right pixel of the image as the transparent color if an image file is being used. No pixels of that color in the image are drawn.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DMarkerFile.use_soft_transparency`
              - Whether to use soft transparency.  Soft transparency shows smoother edges for images with a transparency channel.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DMarkerFile


Property detail
---------------

.. py:property:: file_path
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarkerFile.file_path
    :type: str

    Full file path and name to display a 2D image to represent the object at the specified threshold.

.. py:property:: filename
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarkerFile.filename
    :type: str

    Display a 2D image to represent the object at the specified threshold.

.. py:property:: is_transparent
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarkerFile.is_transparent
    :type: bool

    Use the color of the upper right pixel of the image as the transparent color if an image file is being used. No pixels of that color in the image are drawn.

.. py:property:: use_soft_transparency
    :canonical: ansys.stk.core.stkobjects.Graphics3DMarkerFile.use_soft_transparency
    :type: bool

    Whether to use soft transparency.  Soft transparency shows smoother edges for images with a transparency channel.


