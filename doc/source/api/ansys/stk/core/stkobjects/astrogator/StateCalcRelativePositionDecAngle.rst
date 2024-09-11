StateCalcRelativePositionDecAngle
=================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Relative Position Declination Angle objects.

.. py:currentmodule:: StateCalcRelativePositionDecAngle

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.orbit_plane_source`
              - Selection of the satellite that will generate the orbit plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.element_type`
              - Choice of osculating or mean elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.reference`
              - Get the reference object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.relative_position_type`
              - Gets or sets the type of the relative position.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.sign_convention`
              - Gets or sets the sign of the angle when the relative position has a positive component along the orbit normal.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcRelativePositionDecAngle


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: orbit_plane_source
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.orbit_plane_source
    :type: CALCULATION_OBJECT_ORBIT_PLANE_SOURCE

    Selection of the satellite that will generate the orbit plane.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.element_type
    :type: CALCULATION_OBJECT_ELEMENT

    Choice of osculating or mean elements.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.reference_selection
    :type: CALCULATION_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: relative_position_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.relative_position_type
    :type: CALCULATION_OBJECT_RELATIVE_POSITION

    Gets or sets the type of the relative position.

.. py:property:: sign_convention
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativePositionDecAngle.sign_convention
    :type: CALCULATION_OBJECT_ANGLE_SIGN

    Gets or sets the sign of the angle when the relative position has a positive component along the orbit normal.


