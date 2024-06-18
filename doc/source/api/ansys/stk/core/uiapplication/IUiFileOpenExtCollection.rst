IUiFileOpenExtCollection
========================

.. py:class:: IUiFileOpenExtCollection

   object
   
   Multiple file open collection.

.. py:currentmodule:: ansys.stk.core.uiapplication

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the file at the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import IUiFileOpenExtCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.uiapplication.IUiFileOpenExtCollection.count
    :type: int

    Gets the total count of files in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.uiapplication.IUiFileOpenExtCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the file collection.


Method detail
-------------



.. py:method:: item(self, nIndex:int) -> str

    Get the file at the specified index.

    :Parameters:

    **nIndex** : :obj:`~int`

    :Returns:

        :obj:`~str`

