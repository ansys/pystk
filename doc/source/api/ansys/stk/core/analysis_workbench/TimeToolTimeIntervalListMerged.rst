TimeToolTimeIntervalListMerged
==============================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

.. py:currentmodule:: TimeToolTimeIntervalListMerged

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_list_a`
              - Set the interval list A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_a`
              - Set the interval A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_list_b`
              - Set the interval list B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_b`
              - Set the interval B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.add_interval`
              - Add interval.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.add_interval_list`
              - Add interval list.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval`
              - Set the interval at given index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_list`
              - Set the interval list at given index.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.get_time_component`
              - Get time component at given position.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.get_time_component_size`
              - Get time component list size.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.remove_time_component`
              - Remove time component at given position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.interval_list_or_interval_a`
              - The interval list or interval A.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.interval_list_or_interval_b`
              - The interval list or interval B.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.merge_operation`
              - The merge operation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalListMerged


Property detail
---------------

.. py:property:: interval_list_or_interval_a
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.interval_list_or_interval_a
    :type: IAnalysisWorkbenchComponent

    The interval list or interval A.

.. py:property:: interval_list_or_interval_b
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.interval_list_or_interval_b
    :type: IAnalysisWorkbenchComponent

    The interval list or interval B.

.. py:property:: merge_operation
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.merge_operation
    :type: EventListMergeOperation

    The merge operation.


Method detail
-------------





.. py:method:: set_interval_list_a(self, ref_intervals: ITimeToolTimeIntervalList) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_list_a

    Set the interval list A.

    :Parameters:

        **ref_intervals** : :obj:`~ITimeToolTimeIntervalList`


    :Returns:

        :obj:`~None`

.. py:method:: set_interval_a(self, ref_intervals: ITimeToolTimeInterval) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_a

    Set the interval A.

    :Parameters:

        **ref_intervals** : :obj:`~ITimeToolTimeInterval`


    :Returns:

        :obj:`~None`

.. py:method:: set_interval_list_b(self, ref_intervals: ITimeToolTimeIntervalList) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_list_b

    Set the interval list B.

    :Parameters:

        **ref_intervals** : :obj:`~ITimeToolTimeIntervalList`


    :Returns:

        :obj:`~None`

.. py:method:: set_interval_b(self, ref_intervals: ITimeToolTimeInterval) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_b

    Set the interval B.

    :Parameters:

        **ref_intervals** : :obj:`~ITimeToolTimeInterval`


    :Returns:

        :obj:`~None`

.. py:method:: add_interval(self, ref_intervals: ITimeToolTimeInterval) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.add_interval

    Add interval.

    :Parameters:

        **ref_intervals** : :obj:`~ITimeToolTimeInterval`


    :Returns:

        :obj:`~None`

.. py:method:: add_interval_list(self, ref_intervals: ITimeToolTimeIntervalList) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.add_interval_list

    Add interval list.

    :Parameters:

        **ref_intervals** : :obj:`~ITimeToolTimeIntervalList`


    :Returns:

        :obj:`~None`

.. py:method:: set_interval(self, ref_intervals: ITimeToolTimeInterval, pos: int) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval

    Set the interval at given index.

    :Parameters:

        **ref_intervals** : :obj:`~ITimeToolTimeInterval`

        **pos** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: set_interval_list(self, ref_intervals: ITimeToolTimeIntervalList, pos: int) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.set_interval_list

    Set the interval list at given index.

    :Parameters:

        **ref_intervals** : :obj:`~ITimeToolTimeIntervalList`

        **pos** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: get_time_component(self, pos: int) -> str
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.get_time_component

    Get time component at given position.

    :Parameters:

        **pos** : :obj:`~int`


    :Returns:

        :obj:`~str`

.. py:method:: get_time_component_size(self) -> int
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.get_time_component_size

    Get time component list size.

    :Returns:

        :obj:`~int`

.. py:method:: remove_time_component(self, pos: int) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListMerged.remove_time_component

    Remove time component at given position.

    :Parameters:

        **pos** : :obj:`~int`


    :Returns:

        :obj:`~None`

