StateCalcRelativeInclination
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Relative Inclination Angle objects.

.. py:currentmodule:: StateCalcRelativeInclination

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.satellite_orbit_normal_type`
              - Choice of osculating or mean elements for describing the orbit plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.reference_satellite_orbit_normal_type`
              - Choice of osculating or mean elements for describing the orbit plane.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.reference`
              - Get the reference object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcRelativeInclination


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: satellite_orbit_normal_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.satellite_orbit_normal_type
    :type: CALCULATION_OBJECT_ELEMENT

    Choice of osculating or mean elements for describing the orbit plane.

.. py:property:: reference_satellite_orbit_normal_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.reference_satellite_orbit_normal_type
    :type: CALCULATION_OBJECT_ELEMENT

    Choice of osculating or mean elements for describing the orbit plane.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.reference_selection
    :type: CALCULATION_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeInclination.reference
    :type: ILinkToObject

    Get the reference object.


