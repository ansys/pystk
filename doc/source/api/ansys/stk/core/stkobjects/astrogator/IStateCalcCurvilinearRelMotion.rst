IStateCalcCurvilinearRelMotion
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion

   object
   
   Properties for Curvilinear Relative Motion  calculation object.

.. py:currentmodule:: IStateCalcCurvilinearRelMotion

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference_ellipse`
              - Selection of the satellite orbit that is used as the reference ellipse.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.location_source`
              - Selection of the satellite whose location is being reported with respect to the reference ellipse.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference`
              - Get the reference object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.element_type`
              - Choice of osculating or mean elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.sign_convention`
              - Gets or sets the sign of the angle when the relative position has a positive component along the orbit normal.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcCurvilinearRelMotion


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: reference_ellipse
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference_ellipse
    :type: CALC_OBJECT_REFERENCE_ELLIPSE

    Selection of the satellite orbit that is used as the reference ellipse.

.. py:property:: location_source
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.location_source
    :type: CALC_OBJECT_LOCATION_SOURCE

    Selection of the satellite whose location is being reported with respect to the reference ellipse.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.element_type
    :type: CALC_OBJECT_ELEM

    Choice of osculating or mean elements.

.. py:property:: sign_convention
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcCurvilinearRelMotion.sign_convention
    :type: CALC_OBJECT_ANGLE_SIGN

    Gets or sets the sign of the angle when the relative position has a positive component along the orbit normal.


