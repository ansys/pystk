Graphics3DDataDisplayCollection
===============================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection

   Collection of 3D Graphics data display text.

.. py:currentmodule:: Graphics3DDataDisplayCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.is_pre_data_required`
              - Determine if the data display needs additional data, such as a comparison object for an RIC report or a set of axes for a vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.add_data_display_requiring_pre_data`
              - Add a data display using additional data, such as a comparison object for an RIC report or a set of axes for a vector.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.available_data`
              - Gets the available data.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DDataDisplayCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.

.. py:property:: available_data
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.available_data
    :type: list

    Gets the available data.


Method detail
-------------


.. py:method:: item(self, index: int) -> Graphics3DDataDisplayElement
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~Graphics3DDataDisplayElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, name: str) -> Graphics3DDataDisplayElement
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.add

    Add a new element to the collection.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~Graphics3DDataDisplayElement`


.. py:method:: is_pre_data_required(self, dataDisplayName: str) -> bool
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.is_pre_data_required

    Determine if the data display needs additional data, such as a comparison object for an RIC report or a set of axes for a vector.

    :Parameters:

    **dataDisplayName** : :obj:`~str`

    :Returns:

        :obj:`~bool`

.. py:method:: add_data_display_requiring_pre_data(self, name: str, preData: str) -> Graphics3DDataDisplayElement
    :canonical: ansys.stk.core.stkobjects.Graphics3DDataDisplayCollection.add_data_display_requiring_pre_data

    Add a data display using additional data, such as a comparison object for an RIC report or a set of axes for a vector.

    :Parameters:

    **name** : :obj:`~str`
    **preData** : :obj:`~str`

    :Returns:

        :obj:`~Graphics3DDataDisplayElement`

