TimeToolIntervalVectorCollection
================================

.. py:class:: ansys.stk.core.vgt.TimeToolIntervalVectorCollection

   A collection of interval collections.

.. py:currentmodule:: TimeToolIntervalVectorCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolIntervalVectorCollection.item`
              - Access an element at the specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolIntervalVectorCollection.count`
              - Number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolIntervalVectorCollection._new_enum`
              - Returns a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolIntervalVectorCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.vgt.TimeToolIntervalVectorCollection.count
    :type: int

    Number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.vgt.TimeToolIntervalVectorCollection._new_enum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------


.. py:method:: item(self, index: int) -> TimeToolIntervalCollection
    :canonical: ansys.stk.core.vgt.TimeToolIntervalVectorCollection.item

    Access an element at the specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~TimeToolIntervalCollection`


