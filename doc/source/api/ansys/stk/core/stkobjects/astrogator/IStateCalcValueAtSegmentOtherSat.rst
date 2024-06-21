IStateCalcValueAtSegmentOtherSat
================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat

   object
   
   Properties for a Value At Segment Across Satellites calculation object.

.. py:currentmodule:: IStateCalcValueAtSegmentOtherSat

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat.calc_object_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat.other_segment_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat.segment_state_to_use`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat.reference_sat`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcValueAtSegmentOtherSat


Property detail
---------------

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat.calc_object_name
    :type: str

    Gets or sets the calculation object.

.. py:property:: other_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat.other_segment_name
    :type: str

    Gets or sets the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat.segment_state_to_use
    :type: SEGMENT_STATE

    Gets or sets the segment state to use in the calculation.

.. py:property:: reference_sat
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegmentOtherSat.reference_sat
    :type: ILinkToObject

    Get the Astrogator satellite on which the segment to be compared exists.


