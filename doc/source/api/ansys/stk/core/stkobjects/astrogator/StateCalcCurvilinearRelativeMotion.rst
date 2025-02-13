StateCalcCurvilinearRelativeMotion
==================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Curvilinear Relative Motion objects.

.. py:currentmodule:: StateCalcCurvilinearRelativeMotion

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.reference_ellipse`
              - Selection of the satellite orbit that is used as the reference ellipse.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.location_source`
              - Selection of the satellite whose location is being reported with respect to the reference ellipse.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.reference_selection`
              - Get or set the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.reference`
              - Get the reference object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.element_type`
              - Choice of osculating or mean elements.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.sign_convention`
              - Get or set the sign of the angle when the relative position has a positive component along the orbit normal.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcCurvilinearRelativeMotion


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: reference_ellipse
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.reference_ellipse
    :type: CalculationObjectReferenceEllipse

    Selection of the satellite orbit that is used as the reference ellipse.

.. py:property:: location_source
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.location_source
    :type: CalculationObjectLocationSource

    Selection of the satellite whose location is being reported with respect to the reference ellipse.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.reference_selection
    :type: CalculationObjectReference

    Get or set the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.reference
    :type: ILinkToObject

    Get the reference object.

.. py:property:: element_type
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.element_type
    :type: CalculationObjectElement

    Choice of osculating or mean elements.

.. py:property:: sign_convention
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcCurvilinearRelativeMotion.sign_convention
    :type: CalculationObjectAngleSign

    Get or set the sign of the angle when the relative position has a positive component along the orbit normal.


