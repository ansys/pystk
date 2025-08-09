DataProviderResultIntervalCollection
====================================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultIntervalCollection

   Represents a collection of intervals returned by the data providers.

.. py:currentmodule:: DataProviderResultIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultIntervalCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultIntervalCollection.count`
              - Return a number of elements in collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultIntervalCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderResultIntervalCollection.count
    :type: int

    Return a number of elements in collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.DataProviderResultIntervalCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> DataProviderResultInterval
    :canonical: ansys.stk.core.stkobjects.DataProviderResultIntervalCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~DataProviderResultInterval`


