TimeToolTimeIntervalListFile
============================

.. py:class:: ansys.stk.core.vgt.TimeToolTimeIntervalListFile

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolTimeIntervalList`, :py:class:`~ansys.stk.core.vgt.IComponent`

   Interval list loaded from specified interval file - ASCII file with .int extension. See STK help.

.. py:currentmodule:: TimeToolTimeIntervalListFile

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFile.reload`
              - Reload the interval list file.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFile.get_file_span`
              - Compute the interval list file span.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolTimeIntervalListFile.filename`
              - The path of an external file that contains the time interval list.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolTimeIntervalListFile


Property detail
---------------

.. py:property:: filename
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFile.filename
    :type: str

    The path of an external file that contains the time interval list.


Method detail
-------------



.. py:method:: reload(self) -> None
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFile.reload

    Reload the interval list file.

    :Returns:

        :obj:`~None`

.. py:method:: get_file_span(self) -> TimeToolTimeIntervalResult
    :canonical: ansys.stk.core.vgt.TimeToolTimeIntervalListFile.get_file_span

    Compute the interval list file span.

    :Returns:

        :obj:`~TimeToolTimeIntervalResult`

