STKDate
=======

.. py:class:: ansys.stk.extensions.data_analysis.dates.STKDate



   Wrapper class associated with STK Date object.

.. py:currentmodule:: STKDate


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.extensions.data_analysis.dates.STKDate.get_epsec`
              - Return the date in Epoch Seconds.
            * - :py:attr:`~ansys.stk.extensions.data_analysis.dates.STKDate.get_utcg`
              - Return the date formatted in UTCG.
            * - :py:attr:`~ansys.stk.extensions.data_analysis.dates.STKDate.format`
              - Return the date formatted as any unit.

Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.dates import STKDate


Method detail
-------------

.. py:method:: get_epsec(self: ~typing.Self) -> ~float
    :canonical: ansys.stk.extensions.data_analysis.dates.STKDate.get_epsec

    Return the date in Epoch Seconds.



    :Parameters:



    :Returns:

        :obj:`~float`
        The date in Epoch Seconds.

.. py:method:: get_utcg(self: ~typing.Self) -> ~str
    :canonical: ansys.stk.extensions.data_analysis.dates.STKDate.get_utcg

    Return the date formatted in UTCG.



    :Parameters:



    :Returns:

        :obj:`~str`
        The date formatted as UTCG.

.. py:method:: format(self: ~typing.Self, unit: ~str) -> ~typing.Any
    :canonical: ansys.stk.extensions.data_analysis.dates.STKDate.format

    Return the date formatted as any unit.



    :Parameters:

        **unit** : :obj:`~str`
        The unit to format the date as.



    :Returns:

        :obj:`~str`
        The formatted date.


