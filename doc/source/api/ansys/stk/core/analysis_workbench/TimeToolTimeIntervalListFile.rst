TimeToolTimeIntervalListFile
============================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFile

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

.. py:currentmodule:: TimeToolTimeIntervalListFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFile.get_file_span`
              - Compute the interval list file span.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFile.reload`
              - Reload the interval list file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFile.filename`
              - The path of an external file that contains the time interval list.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolTimeIntervalListFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFile.filename
    :type: str

    The path of an external file that contains the time interval list.


Method detail
-------------



.. py:method:: get_file_span(self) -> TimeToolTimeIntervalResult
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFile.get_file_span

    Compute the interval list file span.

    :Returns:

        :obj:`~TimeToolTimeIntervalResult`

.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolTimeIntervalListFile.reload

    Reload the interval list file.

    :Returns:

        :obj:`~None`

