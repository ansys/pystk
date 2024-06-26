IStateCalcSolarBetaAngle
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle

   object
   
   Properties for a Solar Beta Angle calculation object.

.. py:currentmodule:: IStateCalcSolarBetaAngle

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.orbit_plane_source`
              - Selection of the satellite that will generate the orbit plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.element_type`
              - Choice of osculating or mean elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.reference`
              - Get the reference object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.sun_position`
              - Gets or sets the type of the Sun location.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.sign_convention`
              - Gets or sets the sign of the angle when the relative position has a positive component along the orbit normal.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcSolarBetaAngle


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: orbit_plane_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.orbit_plane_source
    :type: CALC_OBJECT_ORBIT_PLANE_SOURCE

    Selection of the satellite that will generate the orbit plane.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.element_type
    :type: CALC_OBJECT_ELEM

    Choice of osculating or mean elements.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.sun_position
    :type: CALC_OBJECT_SUN_POSITION

    Gets or sets the type of the Sun location.

.. py:property:: sign_convention
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcSolarBetaAngle.sign_convention
    :type: CALC_OBJECT_ANGLE_SIGN

    Gets or sets the sign of the angle when the relative position has a positive component along the orbit normal.


