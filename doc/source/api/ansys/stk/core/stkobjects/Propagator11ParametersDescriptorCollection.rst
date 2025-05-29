Propagator11ParametersDescriptorCollection
==========================================

.. py:class:: ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection

   A collection of 11-Parameter files.

.. py:currentmodule:: Propagator11ParametersDescriptorCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.add_from_array`
              - Add multiple files to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Propagator11ParametersDescriptorCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> Propagator11ParametersDescriptor
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~Propagator11ParametersDescriptor`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, file_path: str) -> Propagator11ParametersDescriptor
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.add

    Add a new element to the collection.

    :Parameters:

        **file_path** : :obj:`~str`


    :Returns:

        :obj:`~Propagator11ParametersDescriptor`

.. py:method:: add_from_array(self, array_of_files: list) -> None
    :canonical: ansys.stk.core.stkobjects.Propagator11ParametersDescriptorCollection.add_from_array

    Add multiple files to the collection.

    :Parameters:

        **array_of_files** : :obj:`~list`


    :Returns:

        :obj:`~None`

