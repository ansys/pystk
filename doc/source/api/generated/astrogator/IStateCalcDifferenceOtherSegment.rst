IStateCalcDifferenceOtherSegment
================================

.. py:class:: IStateCalcDifferenceOtherSegment

   object
   
   Properties for a Difference Across Segments calculation object.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~calc_object_name`
            * - :py:meth:`~other_segment_name`
            * - :py:meth:`~segment_state_to_use`
            * - :py:meth:`~difference_order`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcDifferenceOtherSegment


Property detail
---------------

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceOtherSegment.calc_object_name
    :type: str

    Gets or sets the calculation object.

.. py:property:: other_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceOtherSegment.other_segment_name
    :type: str

    Gets or sets the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceOtherSegment.segment_state_to_use
    :type: "SEGMENT_STATE"

    Gets or sets the segment state to use in the calculation.

.. py:property:: difference_order
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceOtherSegment.difference_order
    :type: "SEGMENT_DIFFERENCE_ORDER"

    Gets or sets the order of the difference calculation.


