IAccessTimeCollection
=====================

.. py:class:: IAccessTimeCollection

   object
   
   IAgAccessTimeCollection Interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return target times scheme by name or at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAccessTimeCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAccessTimeCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IAccessTimeCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IAccessTime
    :canonical: ansys.stk.core.stkobjects.IAccessTimeCollection.item

    Return target times scheme by name or at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IAccessTime`


