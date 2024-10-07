VehiclePropagator11ParamDescriptorCollection
============================================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection

   A collection of 11-Parameter files.

.. py:currentmodule:: VehiclePropagator11ParamDescriptorCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.add`
              - Add a new element to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.add_from_array`
              - Add multiple files to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagator11ParamDescriptorCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehiclePropagator11ParamDescriptor
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehiclePropagator11ParamDescriptor`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, filePath: str) -> VehiclePropagator11ParamDescriptor
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.add

    Add a new element to the collection.

    :Parameters:

    **filePath** : :obj:`~str`

    :Returns:

        :obj:`~VehiclePropagator11ParamDescriptor`

.. py:method:: add_from_array(self, arrayOfFiles: list) -> None
    :canonical: ansys.stk.core.stkobjects.VehiclePropagator11ParamDescriptorCollection.add_from_array

    Add multiple files to the collection.

    :Parameters:

    **arrayOfFiles** : :obj:`~list`

    :Returns:

        :obj:`~None`

