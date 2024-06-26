IProfileCollection
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileCollection

   object
   
   Properties for a list of target sequence profiles.

.. py:currentmodule:: IProfileCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.add`
              - Add a profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.remove`
              - Remove an item from the profile collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.remove_all`
              - Remove all profiles from the profile collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.cut`
              - Copy the profile into the clipboard and removes profile from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.paste`
              - Pastes the profile from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.insert_copy`
              - Copy the profile and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.add2`
              - Add a profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.get_item_by_index`
              - Retrieve a profile from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.get_item_by_name`
              - Retrieve a profile from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.available_profiles`
              - Returns a list of available profiles.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileCollection.provide_runtime_type_info`
              - Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: available_profiles
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.available_profiles
    :type: list

    Returns a list of available profiles.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: add(self, profileName: str) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.add

    Add a profile.

    :Parameters:

    **profileName** : :obj:`~str`

    :Returns:

        :obj:`~IProfile`

.. py:method:: item(self, indexOrName: typing.Any) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IProfile`




.. py:method:: remove(self, indexOrProfileName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.remove

    Remove an item from the profile collection.

    :Parameters:

    **indexOrProfileName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.remove_all

    Remove all profiles from the profile collection.

    :Returns:

        :obj:`~None`


.. py:method:: cut(self, indexOrName: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.cut

    Copy the profile into the clipboard and removes profile from the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self, indexOrName: typing.Any, direction: PROFILE_INSERT_DIRECTION) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.paste

    Pastes the profile from the clipboard and inserts into the list.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`
    **direction** : :obj:`~PROFILE_INSERT_DIRECTION`

    :Returns:

        :obj:`~IProfile`

.. py:method:: insert_copy(self, profile: IProfile, indexOrName: typing.Any, direction: PROFILE_INSERT_DIRECTION) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.insert_copy

    Copy the profile and inserts the copy into the list.

    :Parameters:

    **profile** : :obj:`~IProfile`
    **indexOrName** : :obj:`~typing.Any`
    **direction** : :obj:`~PROFILE_INSERT_DIRECTION`

    :Returns:

        :obj:`~IProfile`

.. py:method:: add2(self, profileName: str, indexOrName: typing.Any, direction: PROFILE_INSERT_DIRECTION) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.add2

    Add a profile.

    :Parameters:

    **profileName** : :obj:`~str`
    **indexOrName** : :obj:`~typing.Any`
    **direction** : :obj:`~PROFILE_INSERT_DIRECTION`

    :Returns:

        :obj:`~IProfile`

.. py:method:: get_item_by_index(self, index: int) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.get_item_by_index

    Retrieve a profile from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IProfile`

.. py:method:: get_item_by_name(self, name: str) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileCollection.get_item_by_name

    Retrieve a profile from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IProfile`

