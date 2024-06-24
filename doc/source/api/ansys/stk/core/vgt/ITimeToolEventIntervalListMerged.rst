ITimeToolEventIntervalListMerged
================================

.. py:class:: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged

   object
   
   Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

.. py:currentmodule:: ITimeToolEventIntervalListMerged

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_list_a`
              - Set the interval list A.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_a`
              - Set the interval A.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_list_b`
              - Set the interval list B.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_b`
              - Set the interval B.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.add_interval`
              - Add interval.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.add_interval_list`
              - Add interval list.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval`
              - Set the interval at given index.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_list`
              - Set the interval list at given index.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.get_time_component`
              - Get time component at given position.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.get_time_component_size`
              - Get time component list size.
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.remove_time_component`
              - Remove time component at given position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.interval_list_or_interval_a`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.interval_list_or_interval_b`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.merge_operation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalListMerged


Property detail
---------------

.. py:property:: interval_list_or_interval_a
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.interval_list_or_interval_a
    :type: IAnalysisWorkbenchComponent

    The interval list or interval A.

.. py:property:: interval_list_or_interval_b
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.interval_list_or_interval_b
    :type: IAnalysisWorkbenchComponent

    The interval list or interval B.

.. py:property:: merge_operation
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.merge_operation
    :type: CRDN_EVENT_LIST_MERGE_OPERATION

    The merge operation.


Method detail
-------------





.. py:method:: set_interval_list_a(self, refIntervals: ITimeToolEventIntervalList) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_list_a

    Set the interval list A.

    :Parameters:

    **refIntervals** : :obj:`~ITimeToolEventIntervalList`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval_a(self, refIntervals: ITimeToolEventInterval) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_a

    Set the interval A.

    :Parameters:

    **refIntervals** : :obj:`~ITimeToolEventInterval`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval_list_b(self, refIntervals: ITimeToolEventIntervalList) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_list_b

    Set the interval list B.

    :Parameters:

    **refIntervals** : :obj:`~ITimeToolEventIntervalList`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval_b(self, refIntervals: ITimeToolEventInterval) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_b

    Set the interval B.

    :Parameters:

    **refIntervals** : :obj:`~ITimeToolEventInterval`

    :Returns:

        :obj:`~None`

.. py:method:: add_interval(self, refIntervals: ITimeToolEventInterval) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.add_interval

    Add interval.

    :Parameters:

    **refIntervals** : :obj:`~ITimeToolEventInterval`

    :Returns:

        :obj:`~None`

.. py:method:: add_interval_list(self, refIntervals: ITimeToolEventIntervalList) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.add_interval_list

    Add interval list.

    :Parameters:

    **refIntervals** : :obj:`~ITimeToolEventIntervalList`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval(self, refIntervals: ITimeToolEventInterval, pos: int) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval

    Set the interval at given index.

    :Parameters:

    **refIntervals** : :obj:`~ITimeToolEventInterval`
    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval_list(self, refIntervals: ITimeToolEventIntervalList, pos: int) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.set_interval_list

    Set the interval list at given index.

    :Parameters:

    **refIntervals** : :obj:`~ITimeToolEventIntervalList`
    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: get_time_component(self, pos: int) -> str
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.get_time_component

    Get time component at given position.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~str`

.. py:method:: get_time_component_size(self) -> int
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.get_time_component_size

    Get time component list size.

    :Returns:

        :obj:`~int`

.. py:method:: remove_time_component(self, pos: int) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.remove_time_component

    Remove time component at given position.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

