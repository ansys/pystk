ITimeToolTimeIntervalList
=========================

.. py:class:: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList

   An ordered list of time intervals.

.. py:currentmodule:: ITimeToolTimeIntervalList

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.find_intervals`
              - Return computed interval list that can be empty.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.occurred`
              - Determine if specified time falls within computed interval list.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.type`
              - Return the type of interval list.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.labels`
              - Get the label descriptions associated with the interval list.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.descriptions`
              - Get the labels associated with the interval list.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import ITimeToolTimeIntervalList


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.type
    :type: EventIntervalListType

    Return the type of interval list.

.. py:property:: labels
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.labels
    :type: list

    Get the label descriptions associated with the interval list.

.. py:property:: descriptions
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.descriptions
    :type: list

    Get the labels associated with the interval list.


Method detail
-------------




.. py:method:: find_intervals(self) -> TimeToolIntervalListResult
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.find_intervals

    Return computed interval list that can be empty.

    :Returns:

        :obj:`~TimeToolIntervalListResult`

.. py:method:: occurred(self, epoch: typing.Any) -> bool
    :canonical: ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList.occurred

    Determine if specified time falls within computed interval list.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~bool`

