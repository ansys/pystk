StateCalcValueAtSegmentOtherSat
===============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   ValueAtSegmentOtherSat Calc objects.

.. py:currentmodule:: StateCalcValueAtSegmentOtherSat

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.calculation_object_name`
              - Get or set the calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.other_segment_name`
              - Get or set the segment to be compared against.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.segment_state_to_use`
              - Get or set the segment state to use in the calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.reference_satellite`
              - Get the Astrogator satellite on which the segment to be compared exists.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcValueAtSegmentOtherSat


Property detail
---------------

.. py:property:: calculation_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.calculation_object_name
    :type: str

    Get or set the calculation object.

.. py:property:: other_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.other_segment_name
    :type: str

    Get or set the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.segment_state_to_use
    :type: SegmentState

    Get or set the segment state to use in the calculation.

.. py:property:: reference_satellite
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcValueAtSegmentOtherSat.reference_satellite
    :type: ILinkToObject

    Get the Astrogator satellite on which the segment to be compared exists.


