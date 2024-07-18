Graphics3DOffsetLabel
=====================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DOffsetLabel

   Bases: 

   Class defining the offset of the position of an object label in the 3D Graphics window.

.. py:currentmodule:: Graphics3DOffsetLabel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetLabel.enable`
              - Offset the position of an object label in the 3D Graphics window.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetLabel.x`
              - X value of the offset, where positive and negative values move the label to the right and left, respectively. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetLabel.y`
              - The Y value of the offset, where positive and negative values move the label up and down, respectively. Dimension depends on context.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetLabel.z`
              - The Z value of the offset, used only when the offset frame is Cartesian, where positive and negative values move the label out of and into the screen, respectively. Uses SmallDistanceUnit Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetLabel.offset_frame`
              - The frame used in computing the offset. A member of the AgEOffsetFrameType enumeration.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DOffsetLabel


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetLabel.enable
    :type: bool

    Offset the position of an object label in the 3D Graphics window.

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetLabel.x
    :type: float

    X value of the offset, where positive and negative values move the label to the right and left, respectively. Dimension depends on context.

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetLabel.y
    :type: float

    The Y value of the offset, where positive and negative values move the label up and down, respectively. Dimension depends on context.

.. py:property:: z
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetLabel.z
    :type: float

    The Z value of the offset, used only when the offset frame is Cartesian, where positive and negative values move the label out of and into the screen, respectively. Uses SmallDistanceUnit Dimension.

.. py:property:: offset_frame
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetLabel.offset_frame
    :type: OFFSET_FRAME_TYPE

    The frame used in computing the offset. A member of the AgEOffsetFrameType enumeration.


