IVehiclePropagator11ParamDescriptorCollection
=============================================

.. py:class:: IVehiclePropagator11ParamDescriptorCollection

   object
   
   A collection of 11-Parameter files.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Given an index, returns an element in the collection.
            * - :py:meth:`~remove_at`
              - Remove an element from the collection using specified index.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~add`
              - Add a new element to the collection.
            * - :py:meth:`~add_from_array`
              - Add multiple files to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagator11ParamDescriptorCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptorCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagator11ParamDescriptorCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IVehiclePropagator11ParamDescriptor"

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IVehiclePropagator11ParamDescriptor"`


.. py:method:: remove_at(self, index:int) -> None

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, filePath:str) -> "IVehiclePropagator11ParamDescriptor"

    Add a new element to the collection.

    :Parameters:

    **filePath** : :obj:`~str`

    :Returns:

        :obj:`~"IVehiclePropagator11ParamDescriptor"`

.. py:method:: add_from_array(self, arrayOfFiles:list) -> None

    Add multiple files to the collection.

    :Parameters:

    **arrayOfFiles** : :obj:`~list`

    :Returns:

        :obj:`~None`

