UiFileOpenExtCollection
=======================

.. py:class:: ansys.stk.core.uiapplication.UiFileOpenExtCollection

   Bases: 

   Multiple file open collection.

.. py:currentmodule:: UiFileOpenExtCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.UiFileOpenExtCollection.item`
              - Get the file at the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.UiFileOpenExtCollection.count`
              - Gets the total count of files in the collection.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiFileOpenExtCollection._NewEnum`
              - Enumerates through the file collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import UiFileOpenExtCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.uiapplication.UiFileOpenExtCollection.count
    :type: int

    Gets the total count of files in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.uiapplication.UiFileOpenExtCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the file collection.


Method detail
-------------



.. py:method:: item(self, nIndex: int) -> str
    :canonical: ansys.stk.core.uiapplication.UiFileOpenExtCollection.item

    Get the file at the specified index.

    :Parameters:

    **nIndex** : :obj:`~int`

    :Returns:

        :obj:`~str`

