StateCalcSolarInPlaneAngle
==========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Solar In Plane Angle objects.

.. py:currentmodule:: StateCalcSolarInPlaneAngle

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.orbit_plane_source`
              - Selection of the satellite that will generate the orbit plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.element_type`
              - Choice of osculating or mean elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.reference`
              - Get the reference object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.sun_position`
              - Gets or sets the type of the Sun location.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.counter_clockwise_rotation`
              - Sets sign of the angle for counterclockwise rotation about orbit normal.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.reference_direction`
              - Direction that establishes the zero value when projected into the orbit plane.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcSolarInPlaneAngle


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: orbit_plane_source
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.orbit_plane_source
    :type: CalculationObjectOrbitPlaneSource

    Selection of the satellite that will generate the orbit plane.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.element_type
    :type: CalculationObjectElement

    Choice of osculating or mean elements.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.reference_selection
    :type: CalculationObjectReference

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.sun_position
    :type: CalculationObjectSunPosition

    Gets or sets the type of the Sun location.

.. py:property:: counter_clockwise_rotation
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.counter_clockwise_rotation
    :type: CalculationObjectAngleSign

    Sets sign of the angle for counterclockwise rotation about orbit normal.

.. py:property:: reference_direction
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcSolarInPlaneAngle.reference_direction
    :type: CalculationObjectReferenceDirection

    Direction that establishes the zero value when projected into the orbit plane.


