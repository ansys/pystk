IStateCalcRelPositionInPlaneAngle
=================================

.. py:class:: IStateCalcRelPositionInPlaneAngle

   object
   
   Properties for a Relative Position In Plane Angle calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_name`
            * - :py:meth:`~orbit_plane_source`
            * - :py:meth:`~element_type`
            * - :py:meth:`~reference_selection`
            * - :py:meth:`~reference`
            * - :py:meth:`~relative_position_type`
            * - :py:meth:`~counter_clockwise_rotation`
            * - :py:meth:`~reference_direction`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcRelPositionInPlaneAngle


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: orbit_plane_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle.orbit_plane_source
    :type: CALC_OBJECT_ORBIT_PLANE_SOURCE

    Selection of the satellite that will generate the orbit plane.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle.element_type
    :type: CALC_OBJECT_ELEM

    Choice of osculating or mean elements.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle.reference
    :type: IAgLinkToObject

    Get the reference object.

.. py:property:: relative_position_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle.relative_position_type
    :type: CALC_OBJECT_RELATIVE_POSITION

    Gets or sets the type of the relative position.

.. py:property:: counter_clockwise_rotation
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle.counter_clockwise_rotation
    :type: CALC_OBJECT_ANGLE_SIGN

    Sets sign of the angle for counterclockwise rotation about orbit normal.

.. py:property:: reference_direction
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionInPlaneAngle.reference_direction
    :type: CALC_OBJECT_REFERENCE_DIRECTION

    Direction that establishes the zero value when projected into the orbit plane.


