IMCSSegment
===========

.. py:class:: ansys.stk.core.stkobjects.astrogator.IMCSSegment

   General properties for segments.

.. py:currentmodule:: IMCSSegment

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment.get_result_value`
              - Return a result value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment.run`
              - Run the segment in individual segment mode.  See MCSDriver.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment.type`
              - Return the type of segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment.properties`
              - Return the properties of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment.initial_state`
              - Get the initial state of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment.final_state`
              - Get the final state of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment.results`
              - Get the results of the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IMCSSegment.segment_summary`
              - Get the segment summary report.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IMCSSegment


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSegment.type
    :type: SegmentType

    Return the type of segment.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSegment.properties
    :type: MCSSegmentProperties

    Return the properties of the segment.

.. py:property:: initial_state
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSegment.initial_state
    :type: State

    Get the initial state of the segment.

.. py:property:: final_state
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSegment.final_state
    :type: State

    Get the final state of the segment.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSegment.results
    :type: CalculationObjectCollection

    Get the results of the segment.

.. py:property:: segment_summary
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSegment.segment_summary
    :type: IDataProviderResult

    Get the segment summary report.


Method detail
-------------





.. py:method:: get_result_value(self, result_name: str) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSegment.get_result_value

    Return a result value.

    :Parameters:

        **result_name** : :obj:`~str`


    :Returns:

        :obj:`~typing.Any`

.. py:method:: run(self) -> State
    :canonical: ansys.stk.core.stkobjects.astrogator.IMCSSegment.run

    Run the segment in individual segment mode.  See MCSDriver.

    :Returns:

        :obj:`~State`



