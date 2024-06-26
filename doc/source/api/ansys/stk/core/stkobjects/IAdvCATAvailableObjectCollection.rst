IAdvCATAvailableObjectCollection
================================

.. py:class:: ansys.stk.core.stkobjects.IAdvCATAvailableObjectCollection

   object
   
   IAgAdvCATAvailableObjectCollection represents available objects.

.. py:currentmodule:: IAdvCATAvailableObjectCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATAvailableObjectCollection.get_available_object`
              - Return name, date and type times of the interval at a given index.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATAvailableObjectCollection.to_array`
              - Return a two-dimensional array of objects.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAdvCATAvailableObjectCollection.count`
              - Number of items in the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAdvCATAvailableObjectCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IAdvCATAvailableObjectCollection.count
    :type: int

    Number of items in the collection.


Method detail
-------------


.. py:method:: get_available_object(self, index: int) -> typing.Tuple[typing.Any, typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkobjects.IAdvCATAvailableObjectCollection.get_available_object

    Return name, date and type times of the interval at a given index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, typing.Any]`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.IAdvCATAvailableObjectCollection.to_array

    Return a two-dimensional array of objects.

    :Returns:

        :obj:`~list`

