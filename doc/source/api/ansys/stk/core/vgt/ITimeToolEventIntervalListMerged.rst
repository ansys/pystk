ITimeToolEventIntervalListMerged
================================

.. py:class:: ITimeToolEventIntervalListMerged

   object
   
   Interval list created by merging two constituent interval lists using specified logical operation. It is possible to select either interval list or interval types for either or both constituents.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_interval_list_a`
              - Set the interval list A.
            * - :py:meth:`~set_interval_a`
              - Set the interval A.
            * - :py:meth:`~set_interval_list_b`
              - Set the interval list B.
            * - :py:meth:`~set_interval_b`
              - Set the interval B.
            * - :py:meth:`~add_interval`
              - Add interval.
            * - :py:meth:`~add_interval_list`
              - Add interval list.
            * - :py:meth:`~set_interval`
              - Set the interval at given index.
            * - :py:meth:`~set_interval_list`
              - Set the interval list at given index.
            * - :py:meth:`~get_time_component`
              - Get time component at given position.
            * - :py:meth:`~get_time_component_size`
              - Get time component list size.
            * - :py:meth:`~remove_time_component`
              - Remove time component at given position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~interval_list_or_interval_a`
            * - :py:meth:`~interval_list_or_interval_b`
            * - :py:meth:`~merge_operation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventIntervalListMerged


Property detail
---------------

.. py:property:: interval_list_or_interval_a
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.interval_list_or_interval_a
    :type: "IAgCrdn"

    The interval list or interval A.

.. py:property:: interval_list_or_interval_b
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.interval_list_or_interval_b
    :type: "IAgCrdn"

    The interval list or interval B.

.. py:property:: merge_operation
    :canonical: ansys.stk.core.vgt.ITimeToolEventIntervalListMerged.merge_operation
    :type: "CRDN_EVENT_LIST_MERGE_OPERATION"

    The merge operation.


Method detail
-------------





.. py:method:: set_interval_list_a(self, refIntervals:"ITimeToolEventIntervalList") -> None

    Set the interval list A.

    :Parameters:

    **refIntervals** : :obj:`~"ITimeToolEventIntervalList"`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval_a(self, refIntervals:"ITimeToolEventInterval") -> None

    Set the interval A.

    :Parameters:

    **refIntervals** : :obj:`~"ITimeToolEventInterval"`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval_list_b(self, refIntervals:"ITimeToolEventIntervalList") -> None

    Set the interval list B.

    :Parameters:

    **refIntervals** : :obj:`~"ITimeToolEventIntervalList"`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval_b(self, refIntervals:"ITimeToolEventInterval") -> None

    Set the interval B.

    :Parameters:

    **refIntervals** : :obj:`~"ITimeToolEventInterval"`

    :Returns:

        :obj:`~None`

.. py:method:: add_interval(self, refIntervals:"ITimeToolEventInterval") -> None

    Add interval.

    :Parameters:

    **refIntervals** : :obj:`~"ITimeToolEventInterval"`

    :Returns:

        :obj:`~None`

.. py:method:: add_interval_list(self, refIntervals:"ITimeToolEventIntervalList") -> None

    Add interval list.

    :Parameters:

    **refIntervals** : :obj:`~"ITimeToolEventIntervalList"`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval(self, refIntervals:"ITimeToolEventInterval", pos:int) -> None

    Set the interval at given index.

    :Parameters:

    **refIntervals** : :obj:`~"ITimeToolEventInterval"`
    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: set_interval_list(self, refIntervals:"ITimeToolEventIntervalList", pos:int) -> None

    Set the interval list at given index.

    :Parameters:

    **refIntervals** : :obj:`~"ITimeToolEventIntervalList"`
    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: get_time_component(self, pos:int) -> str

    Get time component at given position.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~str`

.. py:method:: get_time_component_size(self) -> int

    Get time component list size.

    :Returns:

        :obj:`~int`

.. py:method:: remove_time_component(self, pos:int) -> None

    Remove time component at given position.

    :Parameters:

    **pos** : :obj:`~int`

    :Returns:

        :obj:`~None`

