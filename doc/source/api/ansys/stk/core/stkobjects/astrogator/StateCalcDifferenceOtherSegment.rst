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
              - Get or set the calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.other_segment_name`
              - Get or set the segment to be compared against.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.segment_state_to_use`
              - Get or set the segment state to use in the calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.difference_order`
              - Get or set the order of the difference calculation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcDifferenceOtherSegment


Property detail
---------------

.. py:property:: calculation_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.calculation_object_name
    :type: str

    Get or set the calculation object.

.. py:property:: other_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.other_segment_name
    :type: str

    Get or set the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.segment_state_to_use
    :type: SegmentState

    Get or set the segment state to use in the calculation.

.. py:property:: difference_order
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceOtherSegment.difference_order
    :type: SegmentDifferenceOrder

    Get or set the order of the difference calculation.


