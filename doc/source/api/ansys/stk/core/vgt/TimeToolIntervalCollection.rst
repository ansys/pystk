TimeToolIntervalCollection
==========================

.. py:class:: ansys.stk.core.vgt.TimeToolIntervalCollection

   Represents a collection of intervals.

.. py:currentmodule:: TimeToolIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolIntervalCollection.item`
              - Return an interval at a specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolIntervalCollection.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolIntervalCollection._new_enum`
              - Returns a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.vgt.TimeToolIntervalCollection.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.vgt.TimeToolIntervalCollection._new_enum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index: int) -> TimeToolInterval
    :canonical: ansys.stk.core.vgt.TimeToolIntervalCollection.item

    Return an interval at a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~TimeToolInterval`


