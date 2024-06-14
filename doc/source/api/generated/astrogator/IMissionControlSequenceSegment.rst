IMissionControlSequenceSegment
==============================

.. py:class:: IMissionControlSequenceSegment

   object
   
   General properties for segments.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_result_value`
              - Return a result value.
            * - :py:meth:`~run`
              - Run the segment in individual segment mode.  See IAgVADriverMCS.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~type`
            * - :py:meth:`~properties`
            * - :py:meth:`~initial_state`
            * - :py:meth:`~final_state`
            * - :py:meth:`~results`
            * - :py:meth:`~exec_summary`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceSegment


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.type
    :type: "SEGMENT_TYPE"

    Returns the type of segment.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.properties
    :type: "IAgVAMCSSegmentProperties"

    Returns the properties of the segment.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.initial_state
    :type: "IAgVAState"

    Get the initial state of the segment.

.. py:property:: final_state
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.final_state
    :type: "IAgVAState"

    Get the final state of the segment.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.results
    :type: "IAgVACalcObjectCollection"

    Get the results of the segment.

.. py:property:: exec_summary
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.exec_summary
    :type: "IAgDrResult"

    Get the segment summary report.


Method detail
-------------





.. py:method:: get_result_value(self, resultName:str) -> typing.Any

    Return a result value.

    :Parameters:

    **resultName** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: run(self) -> "IState"

    Run the segment in individual segment mode.  See IAgVADriverMCS.

    :Returns:

        :obj:`~"IState"`



