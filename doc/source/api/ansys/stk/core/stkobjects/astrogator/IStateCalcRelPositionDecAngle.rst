IStateCalcRelPositionDecAngle
=============================

.. py:class:: IStateCalcRelPositionDecAngle

   object
   
   Properties for a Relative Position Declination Angle calculation object.

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
            * - :py:meth:`~sign_convention`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcRelPositionDecAngle


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionDecAngle.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: orbit_plane_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionDecAngle.orbit_plane_source
    :type: CALC_OBJECT_ORBIT_PLANE_SOURCE

    Selection of the satellite that will generate the orbit plane.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionDecAngle.element_type
    :type: CALC_OBJECT_ELEM

    Choice of osculating or mean elements.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionDecAngle.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionDecAngle.reference
    :type: IAgLinkToObject

    Get the reference object.

.. py:property:: relative_position_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionDecAngle.relative_position_type
    :type: CALC_OBJECT_RELATIVE_POSITION

    Gets or sets the type of the relative position.

.. py:property:: sign_convention
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelPositionDecAngle.sign_convention
    :type: CALC_OBJECT_ANGLE_SIGN

    Gets or sets the sign of the angle when the relative position has a positive component along the orbit normal.


