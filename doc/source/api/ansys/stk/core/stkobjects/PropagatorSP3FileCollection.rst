PropagatorSP3FileCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.PropagatorSP3FileCollection

   A collection of SP3 files.

.. py:currentmodule:: PropagatorSP3FileCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3FileCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3FileCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3FileCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3FileCollection.add`
              - Load an SP3 file using the specified file path and adds the file to a collection of SP3 files.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3FileCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.PropagatorSP3FileCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PropagatorSP3FileCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3FileCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3FileCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> PropagatorSP3File
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3FileCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~PropagatorSP3File`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3FileCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3FileCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, filePath: str) -> PropagatorSP3File
    :canonical: ansys.stk.core.stkobjects.PropagatorSP3FileCollection.add

    Load an SP3 file using the specified file path and adds the file to a collection of SP3 files.

    :Parameters:

    **filePath** : :obj:`~str`

    :Returns:

        :obj:`~PropagatorSP3File`

