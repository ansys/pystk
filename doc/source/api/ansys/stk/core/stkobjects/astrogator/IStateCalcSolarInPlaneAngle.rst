IStateCalcSolarInPlaneAngle
===========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle

   object
   
   Properties for a Solar In Plane Angle calculation object.

.. py:currentmodule:: IStateCalcSolarInPlaneAngle

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.orbit_plane_source`
              - Selection of the satellite that will generate the orbit plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.element_type`
              - Choice of osculating or mean elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.reference`
              - Get the reference object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.sun_position`
              - Gets or sets the type of the Sun location.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.counter_clockwise_rotation`
              - Sets sign of the angle for counterclockwise rotation about orbit normal.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.reference_direction`
              - Direction that establishes the zero value when projected into the orbit plane.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcSolarInPlaneAngle


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: orbit_plane_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.orbit_plane_source
    :type: CALC_OBJECT_ORBIT_PLANE_SOURCE

    Selection of the satellite that will generate the orbit plane.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.element_type
    :type: CALC_OBJECT_ELEM

    Choice of osculating or mean elements.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.sun_position
    :type: CALC_OBJECT_SUN_POSITION

    Gets or sets the type of the Sun location.

.. py:property:: counter_clockwise_rotation
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.counter_clockwise_rotation
    :type: CALC_OBJECT_ANGLE_SIGN

    Sets sign of the angle for counterclockwise rotation about orbit normal.

.. py:property:: reference_direction
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarInPlaneAngle.reference_direction
    :type: CALC_OBJECT_REFERENCE_DIRECTION

    Direction that establishes the zero value when projected into the orbit plane.


