STKDateFactory
==============

.. py:class:: ansys.stk.extensions.data_analysis.dates.STKDateFactory



   Factory class to create STKDate objects.

.. py:currentmodule:: STKDateFactory


Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.extensions.data_analysis.dates.STKDateFactory.new_date`
              - Create a new STKDate object.

Import detail
-------------

.. code-block:: python

    from ansys.stk.extensions.data_analysis.dates import STKDateFactory


Method detail
-------------

.. py:method:: new_date(self: ~typing.Self, value: ~str, unit: ~str = 'UTCG') -> ~STKDate
    :canonical: ansys.stk.extensions.data_analysis.dates.STKDateFactory.new_date

    Create a new STKDate object.



    :Parameters:

        **value** : :obj:`~str`
        String containing date to be parsed.

        **unit** : :obj:`~str`
        String representing the unit the date is in (the default is UTCG).



    :Returns:

        :obj:`~ansys.stk.extensions.data_analysis.dates.STKDate`
        The `STKDate` object.


