StateCalcDifferenceOtherSegment
===============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   DifferenceOtherSegment Calc objects.

.. py:currentmodule:: StateCalcDifferenceOtherSegment

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.calculation_object_name`
              - Gets or sets the calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.other_segment_name`
              - Gets or sets the segment to be compared against.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.segment_state_to_use`
              - Gets or sets the segment state to use in the calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.difference_order`
              - Gets or sets the order of the difference calculation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcDifferenceOtherSegment


Property detail
---------------

.. py:property:: calculation_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.calculation_object_name
    :type: str

    Gets or sets the calculation object.

.. py:property:: other_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.other_segment_name
    :type: str

    Gets or sets the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.segment_state_to_use
    :type: SegmentState

    Gets or sets the segment state to use in the calculation.

.. py:property:: difference_order
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.difference_order
    :type: SegmentDifferenceOrder

    Gets or sets the order of the difference calculation.


