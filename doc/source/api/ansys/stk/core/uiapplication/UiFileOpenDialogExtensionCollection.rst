UiFileOpenDialogExtensionCollection
===================================

.. py:class:: ansys.stk.core.uiapplication.UiFileOpenDialogExtensionCollection

   Multiple file open collection.

.. py:currentmodule:: UiFileOpenDialogExtensionCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.UiFileOpenDialogExtensionCollection.item`
              - Get the file at the specified index.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.uiapplication.UiFileOpenDialogExtensionCollection.count`
              - Get the total count of files in the collection.
            * - :py:attr:`~ansys.stk.core.uiapplication.UiFileOpenDialogExtensionCollection._new_enum`
              - Enumerates through the file collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.uiapplication import UiFileOpenDialogExtensionCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.uiapplication.UiFileOpenDialogExtensionCollection.count
    :type: int

    Get the total count of files in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.uiapplication.UiFileOpenDialogExtensionCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the file collection.


Method detail
-------------



.. py:method:: item(self, n_index: int) -> str
    :canonical: ansys.stk.core.uiapplication.UiFileOpenDialogExtensionCollection.item

    Get the file at the specified index.

    :Parameters:

    **n_index** : :obj:`~int`

    :Returns:

        :obj:`~str`

