ITimeToolIntervalCollection
===========================

.. py:class:: ansys.stk.core.vgt.ITimeToolIntervalCollection

   object
   
   The interface represents a collection of intervals.

.. py:currentmodule:: ITimeToolIntervalCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolIntervalCollection.item`
              - Return an interval at a specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolIntervalCollection.count`
            * - :py:attr:`~ansys.stk.core.vgt.ITimeToolIntervalCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolIntervalCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalCollection.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalCollection._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index: int) -> ITimeToolInterval
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalCollection.item

    Return an interval at a specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ITimeToolInterval`


