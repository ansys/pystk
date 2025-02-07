StateCalcRelativeAtAOLMaster
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   RelAOLMaster Calc objects.

.. py:currentmodule:: StateCalcRelativeAtAOLMaster

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.central_body_name`
              - Get or set the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.calculation_object_name`
              - Get or set the calculation object of interest.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.direction`
              - Get or set the direction to search for the desired value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.reference_selection`
              - Get or set the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.reference`
              - Get the reference object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcRelativeAtAOLMaster


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.central_body_name
    :type: str

    Get or set the central body of the component.

.. py:property:: calculation_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.calculation_object_name
    :type: str

    Get or set the calculation object of interest.

.. py:property:: direction
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.direction
    :type: CalculationObjectDirection

    Get or set the direction to search for the desired value.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.reference_selection
    :type: CalculationObjectReference

    Get or set the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcRelativeAtAOLMaster.reference
    :type: ILinkToObject

    Get the reference object.


