ITimeToolIntervalVectorCollection
=================================

.. py:class:: ITimeToolIntervalVectorCollection

   object
   
   A collection of interval collections.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Access an element at the specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolIntervalVectorCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalVectorCollection.count
    :type: int

    Number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalVectorCollection._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index: int) -> ITimeToolIntervalCollection
    :canonical: ansys.stk.core.vgt.ITimeToolIntervalVectorCollection.item

    Access an element at the specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ITimeToolIntervalCollection`


