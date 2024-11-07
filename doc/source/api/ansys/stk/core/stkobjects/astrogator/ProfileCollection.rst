ProfileCollection
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileCollection

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Profiles of a Target Sequence.

.. py:currentmodule:: ProfileCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.add`
              - Add a profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.remove`
              - Remove an item from the profile collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.remove_all`
              - Remove all profiles from the profile collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.cut`
              - Copy the profile into the clipboard and removes profile from the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.paste`
              - Pastes the profile from the clipboard and inserts into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.insert_copy`
              - Copy the profile and inserts the copy into the list.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.add2`
              - Add a profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.get_item_by_index`
              - Retrieve a profile from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.get_item_by_name`
              - Retrieve a profile from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.count`
              - Returns the size of the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.available_profiles`
              - Returns a list of available profiles.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileCollection.provide_runtime_type_info`
              - Returns the IAgRuntimeTypeInfo interface to access properties at runtime.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.count
    :type: int

    Returns the size of the collection.

.. py:property:: available_profiles
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.available_profiles
    :type: list

    Returns a list of available profiles.

.. py:property:: provide_runtime_type_info
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.provide_runtime_type_info
    :type: IRuntimeTypeInfo

    Returns the IAgRuntimeTypeInfo interface to access properties at runtime.


Method detail
-------------

.. py:method:: add(self, profile_name: str) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.add

    Add a profile.

    :Parameters:

    **profile_name** : :obj:`~str`

    :Returns:

        :obj:`~IProfile`

.. py:method:: item(self, index_or_name: typing.Any) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IProfile`




.. py:method:: remove(self, index_or_profile_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.remove

    Remove an item from the profile collection.

    :Parameters:

    **index_or_profile_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.remove_all

    Remove all profiles from the profile collection.

    :Returns:

        :obj:`~None`


.. py:method:: cut(self, index_or_name: typing.Any) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.cut

    Copy the profile into the clipboard and removes profile from the list.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: paste(self, index_or_name: typing.Any, direction: PROFILE_INSERT_DIRECTION) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.paste

    Pastes the profile from the clipboard and inserts into the list.

    :Parameters:

    **index_or_name** : :obj:`~typing.Any`
    **direction** : :obj:`~PROFILE_INSERT_DIRECTION`

    :Returns:

        :obj:`~IProfile`

.. py:method:: insert_copy(self, profile: IProfile, index_or_name: typing.Any, direction: PROFILE_INSERT_DIRECTION) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.insert_copy

    Copy the profile and inserts the copy into the list.

    :Parameters:

    **profile** : :obj:`~IProfile`
    **index_or_name** : :obj:`~typing.Any`
    **direction** : :obj:`~PROFILE_INSERT_DIRECTION`

    :Returns:

        :obj:`~IProfile`

.. py:method:: add2(self, profile_name: str, index_or_name: typing.Any, direction: PROFILE_INSERT_DIRECTION) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.add2

    Add a profile.

    :Parameters:

    **profile_name** : :obj:`~str`
    **index_or_name** : :obj:`~typing.Any`
    **direction** : :obj:`~PROFILE_INSERT_DIRECTION`

    :Returns:

        :obj:`~IProfile`

.. py:method:: get_item_by_index(self, index: int) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.get_item_by_index

    Retrieve a profile from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IProfile`

.. py:method:: get_item_by_name(self, name: str) -> IProfile
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileCollection.get_item_by_name

    Retrieve a profile from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IProfile`

