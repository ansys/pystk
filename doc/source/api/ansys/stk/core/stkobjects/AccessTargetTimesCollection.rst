AccessTargetTimesCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.AccessTargetTimesCollection

   Collection of access times.

.. py:currentmodule:: AccessTargetTimesCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTargetTimesCollection.item`
              - Return target times scheme by name or at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTargetTimesCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.AccessTargetTimesCollection._NewEnum`
              - Enumerates the elements in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AccessTargetTimesCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.AccessTargetTimesCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.AccessTargetTimesCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> AccessTargetTime
    :canonical: ansys.stk.core.stkobjects.AccessTargetTimesCollection.item

    Return target times scheme by name or at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~AccessTargetTime`


