ScatteringPointProviderCollection
=================================

.. py:class:: ansys.stk.core.stkobjects.ScatteringPointProviderCollection

   Class defining an scattering point provider collection.

.. py:currentmodule:: ScatteringPointProviderCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection.item`
              - Given an index, returns the scattering point provider element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection.remove_at`
              - Remove the scattering point provider element with the specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection.insert_at`
              - Insert a new scattering point provider element at the supplied index, configured with a component with the supplied identifier.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection.add`
              - Add a new default scattering point provider element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection.clear`
              - Clear all scattering point provider elements from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection.count`
              - Return the number of scattering point provider elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ScatteringPointProviderCollection._new_enum`
              - Return an enumerator for the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ScatteringPointProviderCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderCollection.count
    :type: int

    Return the number of scattering point provider elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ScatteringPointProviderCollectionElement
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderCollection.item

    Given an index, returns the scattering point provider element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScatteringPointProviderCollectionElement`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderCollection.remove_at

    Remove the scattering point provider element with the specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: insert_at(self, index: int) -> ScatteringPointProviderCollectionElement
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderCollection.insert_at

    Insert a new scattering point provider element at the supplied index, configured with a component with the supplied identifier.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ScatteringPointProviderCollectionElement`

.. py:method:: add(self) -> ScatteringPointProviderCollectionElement
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderCollection.add

    Add a new default scattering point provider element to the collection.

    :Returns:

        :obj:`~ScatteringPointProviderCollectionElement`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.stkobjects.ScatteringPointProviderCollection.clear

    Clear all scattering point provider elements from the collection.

    :Returns:

        :obj:`~None`

