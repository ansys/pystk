SensorGraphics3DOffset
======================

.. py:class:: ansys.stk.core.stkobjects.SensorGraphics3DOffset

   Class defining 3D Graphics vertex offset properties of a Sensor.

.. py:currentmodule:: SensorGraphics3DOffset

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.get_axis_offset_value`
              - Get the selected axis offset type.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.set_axis_offset_value`
              - Select the axis offset type.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.inherit_from_parent_obj`
              - Opt whether to use the position offset from the parent object.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.enable_translational`
              - Opt whether to specify the sensor projection starting point position offset in the parent object's body frame in the X, Y and Z directions.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.x`
              - Offset in the X direction. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.y`
              - Offset in the Y direction. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.z`
              - Offset in the Z direction. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.enable_attach_point`
              - Enable the use of an attach point, i.e. the place from which the sensor cone emits. If this feature is not used, the sensor cone origin is the center of the parent model.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.attach_point_name`
              - Name of the attach point.
            * - :py:attr:`~ansys.stk.core.stkobjects.SensorGraphics3DOffset.available_attach_points`
              - Returns available attach points.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SensorGraphics3DOffset


Property detail
---------------

.. py:property:: inherit_from_parent_obj
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.inherit_from_parent_obj
    :type: bool

    Opt whether to use the position offset from the parent object.

.. py:property:: enable_translational
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.enable_translational
    :type: bool

    Opt whether to specify the sensor projection starting point position offset in the parent object's body frame in the X, Y and Z directions.

.. py:property:: x
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.x
    :type: float

    Offset in the X direction. Uses Distance Dimension.

.. py:property:: y
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.y
    :type: float

    Offset in the Y direction. Uses Distance Dimension.

.. py:property:: z
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.z
    :type: float

    Offset in the Z direction. Uses Distance Dimension.

.. py:property:: enable_attach_point
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.enable_attach_point
    :type: bool

    Enable the use of an attach point, i.e. the place from which the sensor cone emits. If this feature is not used, the sensor cone origin is the center of the parent model.

.. py:property:: attach_point_name
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.attach_point_name
    :type: str

    Name of the attach point.

.. py:property:: available_attach_points
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.available_attach_points
    :type: list

    Returns available attach points.


Method detail
-------------











.. py:method:: get_axis_offset_value(self, offsetType: AXIS_OFFSET) -> float
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.get_axis_offset_value

    Get the selected axis offset type.

    :Parameters:

    **offsetType** : :obj:`~AXIS_OFFSET`

    :Returns:

        :obj:`~float`

.. py:method:: set_axis_offset_value(self, offsetType: AXIS_OFFSET, axisOffsetValue: float) -> None
    :canonical: ansys.stk.core.stkobjects.SensorGraphics3DOffset.set_axis_offset_value

    Select the axis offset type.

    :Parameters:

    **offsetType** : :obj:`~AXIS_OFFSET`
    **axisOffsetValue** : :obj:`~float`

    :Returns:

        :obj:`~None`






