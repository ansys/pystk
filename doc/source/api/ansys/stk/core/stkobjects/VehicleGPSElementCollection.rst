VehicleGPSElementCollection
===========================

.. py:class:: ansys.stk.core.stkobjects.VehicleGPSElementCollection

   A collection of GPS elements.

.. py:currentmodule:: VehicleGPSElementCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGPSElementCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGPSElementCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGPSElementCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGPSElementCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleGPSElementCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VehicleGPSElementCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleGPSElement
    :canonical: ansys.stk.core.stkobjects.VehicleGPSElementCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleGPSElement`


