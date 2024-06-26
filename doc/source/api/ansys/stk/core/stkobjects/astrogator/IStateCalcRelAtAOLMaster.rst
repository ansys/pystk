IStateCalcRelAtAOLMaster
========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster

   object
   
   Properties for a RelativeAtAOL calculation object.

.. py:currentmodule:: IStateCalcRelAtAOLMaster

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.central_body_name`
              - Gets or sets the central body of the component.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.calc_object_name`
              - Gets or sets the calculation object of interest.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.direction`
              - Gets or sets the direction to search for the desired value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.reference_selection`
              - Gets or sets the reference object selection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.reference`
              - Get the reference object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcRelAtAOLMaster


Property detail
---------------

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.central_body_name
    :type: str

    Gets or sets the central body of the component.

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.calc_object_name
    :type: str

    Gets or sets the calculation object of interest.

.. py:property:: direction
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.direction
    :type: CALC_OBJECT_DIRECTION

    Gets or sets the direction to search for the desired value.

.. py:property:: reference_selection
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.reference_selection
    :type: CALC_OBJECT_REFERENCE

    Gets or sets the reference object selection.

.. py:property:: reference
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcRelAtAOLMaster.reference
    :type: ILinkToObject

    Get the reference object.


