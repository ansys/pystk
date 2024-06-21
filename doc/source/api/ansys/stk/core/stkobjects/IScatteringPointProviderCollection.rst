IScatteringPointProviderCollection
==================================

.. py:class:: ansys.stk.core.stkobjects.IScatteringPointProviderCollection

   object
   
   Represents a collection of scattering point provider elements.

.. py:currentmodule:: IScatteringPointProviderCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollection.item`
              - Given an index, returns the scattering point provider element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollection.remove_at`
              - Remove the scattering point provider element with the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollection.insert_at`
              - Insert a new scattering point provider element at the supplied index, configured with a component with the supplied identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollection.add`
              - Add a new default scattering point provider element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollection.clear`
              - Clear all scattering point provider elements from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IScatteringPointProviderCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IScatteringPointProviderCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollection.count
    :type: int

    Returns the number of scattering point provider elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IScatteringPointProviderCollectionElement
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollection.item

    Given an index, returns the scattering point provider element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScatteringPointProviderCollectionElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollection.remove_at

    Remove the scattering point provider element with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: insert_at(self, index: int) -> IScatteringPointProviderCollectionElement
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollection.insert_at

    Insert a new scattering point provider element at the supplied index, configured with a component with the supplied identifier.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IScatteringPointProviderCollectionElement`

.. py:method:: add(self) -> IScatteringPointProviderCollectionElement
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollection.add

    Add a new default scattering point provider element to the collection.

    :Returns:

        :obj:`~IScatteringPointProviderCollectionElement`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.IScatteringPointProviderCollection.clear

    Clear all scattering point provider elements from the collection.

    :Returns:

        :obj:`~None`

