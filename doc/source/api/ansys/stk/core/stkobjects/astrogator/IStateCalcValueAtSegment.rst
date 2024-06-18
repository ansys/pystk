IStateCalcValueAtSegment
========================

.. py:class:: IStateCalcValueAtSegment

   object
   
   Properties for a Value At Segment calculation object.

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


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IStateCalcValueAtSegment


Property detail
---------------

.. py:property:: calc_object_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegment.calc_object_name
    :type: str

    Gets or sets the calculation object.

.. py:property:: other_segment_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegment.other_segment_name
    :type: str

    Gets or sets the segment to be compared against.

.. py:property:: segment_state_to_use
    :canonical: ansys.stk.core.stkobjects.astrogator.IStateCalcValueAtSegment.segment_state_to_use
    :type: "SEGMENT_STATE"

    Gets or sets the segment state to use in the calculation.


