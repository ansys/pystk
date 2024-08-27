Graphics3DOffsetAttach
======================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DOffsetAttach

   Class defining attach points for the attachment of lines to objects.

.. py:currentmodule:: Graphics3DOffsetAttach

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetAttach.enable`
              - Opt whether to attach the line to a specific point on the object. Otherwise, the line is attached to the center of the object.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetAttach.attach_point_name`
              - Name of the attach point.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DOffsetAttach.available_attach_points`
              - Returns available attach points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DOffsetAttach


Property detail
---------------

.. py:property:: enable
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetAttach.enable
    :type: bool

    Opt whether to attach the line to a specific point on the object. Otherwise, the line is attached to the center of the object.

.. py:property:: attach_point_name
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetAttach.attach_point_name
    :type: str

    Name of the attach point.

.. py:property:: available_attach_points
    :canonical: ansys.stk.core.stkobjects.Graphics3DOffsetAttach.available_attach_points
    :type: list

    Returns available attach points.


