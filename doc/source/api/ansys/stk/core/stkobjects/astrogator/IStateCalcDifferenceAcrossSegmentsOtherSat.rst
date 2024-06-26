IStateCalcDifferenceAcrossSegmentsOtherSat
==========================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat

   object
   
   Properties for a Difference Across Segments Across Satellites calculation object.

.. py:currentmodule:: IStateCalcDifferenceAcrossSegmentsOtherSat

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.calc_object_name`
              - Gets or sets the calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.other_segment_name`
              - Gets or sets the segment to be compared against.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.segment_state_to_use`
              - Gets or sets the segment state to use in the calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.difference_order`
              - Gets or sets the order of the difference calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.reference_sat`
              - Get the Astrogator satellite on which the segment to be compared exists.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcDifferenceAcrossSegmentsOtherSat


Property detail
---------------

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.calc_object_name
    :type: str

    Gets or sets the calculation object.

.. py:property:: other_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.other_segment_name
    :type: str

    Gets or sets the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.segment_state_to_use
    :type: SEGMENT_STATE

    Gets or sets the segment state to use in the calculation.

.. py:property:: difference_order
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.difference_order
    :type: SEGMENT_DIFFERENCE_ORDER

    Gets or sets the order of the difference calculation.

.. py:property:: reference_sat
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcDifferenceAcrossSegmentsOtherSat.reference_sat
    :type: ILinkToObject

    Get the Astrogator satellite on which the segment to be compared exists.


