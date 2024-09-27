StateCalcDifferenceAcrossSegmentsOtherSatellite
===============================================

.. py:class:: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   DifferenceAcrossSegmentsOtherSat Calc objects.

.. py:currentmodule:: StateCalcDifferenceAcrossSegmentsOtherSatellite

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.calculation_object_name`
              - Gets or sets the calculation object.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.other_segment_name`
              - Gets or sets the segment to be compared against.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.segment_state_to_use`
              - Gets or sets the segment state to use in the calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.difference_order`
              - Gets or sets the order of the difference calculation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.reference_satellite`
              - Get the Astrogator satellite on which the segment to be compared exists.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import StateCalcDifferenceAcrossSegmentsOtherSatellite


Property detail
---------------

.. py:property:: calculation_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.calculation_object_name
    :type: str

    Gets or sets the calculation object.

.. py:property:: other_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.other_segment_name
    :type: str

    Gets or sets the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.segment_state_to_use
    :type: SEGMENT_STATE

    Gets or sets the segment state to use in the calculation.

.. py:property:: difference_order
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.difference_order
    :type: SEGMENT_DIFFERENCE_ORDER

    Gets or sets the order of the difference calculation.

.. py:property:: reference_satellite
    :canonical: ansys.stk.core.stkobjects.astrogator.StateCalcDifferenceAcrossSegmentsOtherSatellite.reference_satellite
    :type: ILinkToObject

    Get the Astrogator satellite on which the segment to be compared exists.


