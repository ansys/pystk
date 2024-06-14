IUnitPreferencesUnitCollection
==============================

.. py:class:: IUnitPreferencesUnitCollection

   object
   
   Provide access to the Unit collection.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return the specific item in the collection given a unit identifier or an index.
            * - :py:meth:`~get_item_by_index`
              - Retrieve a unit from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve a unit from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IUnitPreferencesUnitCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesUnitCollection.count
    :type: int

    Returns the number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkutil.IUnitPreferencesUnitCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumeration of AgUnitPrefsUnit.


Method detail
-------------

.. py:method:: item(self, indexOrName:typing.Any) -> "IUnitPreferencesUnit"

    Return the specific item in the collection given a unit identifier or an index.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"IUnitPreferencesUnit"`



.. py:method:: get_item_by_index(self, index:int) -> "IUnitPreferencesUnit"

    Retrieve a unit from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IUnitPreferencesUnit"`

.. py:method:: get_item_by_name(self, name:str) -> "IUnitPreferencesUnit"

    Retrieve a unit from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IUnitPreferencesUnit"`

