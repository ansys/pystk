StateCalcRelativePositionInPlaneAngle
=====================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Relative Position Declination Angle objects.

.. py:currentmodule:: StateCalcRelativePositionInPlaneAngle

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.counter_clockwise_rotation`
              - Set sign of the angle for counterclockwise rotation about orbit normal.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.element_type`
              - Choice of osculating or mean elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.orbit_plane_source`
              - Selection of the satellite that will generate the orbit plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.reference`
              - Get the reference object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.reference_direction`
              - Direction that establishes the zero value when projected into the orbit plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.reference_selection`
              - Get or set the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.relative_position_type`
              - Get or set the type of the relative position.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcRelativePositionInPlaneAngle


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: counter_clockwise_rotation
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.counter_clockwise_rotation
    :type: CalculationObjectAngleSign

    Set sign of the angle for counterclockwise rotation about orbit normal.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.element_type
    :type: CalculationObjectElement

    Choice of osculating or mean elements.

.. py:property:: orbit_plane_source
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.orbit_plane_source
    :type: CalculationObjectOrbitPlaneSource

    Selection of the satellite that will generate the orbit plane.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: reference_direction
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.reference_direction
    :type: CalculationObjectReferenceDirection

    Direction that establishes the zero value when projected into the orbit plane.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.reference_selection
    :type: CalculationObjectReference

    Get or set the reference object selection.

.. py:property:: relative_position_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionInPlaneAngle.relative_position_type
    :type: CalculationObjectRelativePosition

    Get or set the type of the relative position.


