IMissionControlSequenceSegment
==============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment

   object
   
   General properties for segments.

.. py:currentmodule:: IMissionControlSequenceSegment

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.get_result_value`
              - Return a result value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.run`
              - Run the segment in individual segment mode.  See IAgVADriverMCS.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.type`
              - Returns the type of segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.properties`
              - Returns the properties of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.initial_state`
              - Get the initial state of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.final_state`
              - Get the final state of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.results`
              - Get the results of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.exec_summary`
              - Get the segment summary report.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMissionControlSequenceSegment


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.type
    :type: SEGMENT_TYPE

    Returns the type of segment.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.properties
    :type: IMissionControlSequenceSegmentProperties

    Returns the properties of the segment.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.initial_state
    :type: IState

    Get the initial state of the segment.

.. py:property:: final_state
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.final_state
    :type: IState

    Get the final state of the segment.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.results
    :type: ICalcObjectCollection

    Get the results of the segment.

.. py:property:: exec_summary
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.exec_summary
    :type: IDataProviderResult

    Get the segment summary report.


Method detail
-------------





.. py:method:: get_result_value(self, resultName: str) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.get_result_value

    Return a result value.

    :Parameters:

    **resultName** : :obj:`~str`

    :Returns:

        :obj:`~typing.Any`

.. py:method:: run(self) -> State
    :canonical: ansys.stk.core.stkobjects.astrogator.IMissionControlSequenceSegment.run

    Run the segment in individual segment mode.  See IAgVADriverMCS.

    :Returns:

        :obj:`~State`



