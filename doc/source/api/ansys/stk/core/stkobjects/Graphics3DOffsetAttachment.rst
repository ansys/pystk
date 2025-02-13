Graphics3DOffsetAttachment
==========================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DOffsetAttachment

   Class defining attach points for the attachment of lines to objects.

.. py:currentmodule:: Graphics3DOffsetAttachment

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetAttachment.enable`
              - Opt whether to attach the line to a specific point on the object. Otherwise, the line is attached to the center of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetAttachment.attachment_point_name`
              - Name of the attach point.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetAttachment.available_attachment_points`
              - Return available attach points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DOffsetAttachment


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetAttachment.enable
    :type: bool

    Opt whether to attach the line to a specific point on the object. Otherwise, the line is attached to the center of the object.

.. py:property:: attachment_point_name
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetAttachment.attachment_point_name
    :type: str

    Name of the attach point.

.. py:property:: available_attachment_points
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetAttachment.available_attachment_points
    :type: list

    Return available attach points.


