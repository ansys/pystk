IStateCalcRelativeInclination
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination

   object
   
   Properties for a Relative Inclination Angle calculation object.

.. py:currentmodule:: IStateCalcRelativeInclination

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.central_body_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.satellite_orbit_normal_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.reference_satellite_orbit_normal_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.reference_selection`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.reference`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcRelativeInclination


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: satellite_orbit_normal_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.satellite_orbit_normal_type
    :type: CALC_OBJECT_ELEM

    Choice of osculating or mean elements for describing the orbit plane.

.. py:property:: reference_satellite_orbit_normal_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.reference_satellite_orbit_normal_type
    :type: CALC_OBJECT_ELEM

    Choice of osculating or mean elements for describing the orbit plane.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelativeInclination.reference
    :type: ILinkToObject

    Get the reference object.


