IVehicleSpaceEnvironmentRadDoseRateCollection
=============================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateCollection

   object
   
   The collection holds dose rate elements computed for each shielding thickness.

.. py:currentmodule:: IVehicleSpaceEnvironmentRadDoseRateCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleSpaceEnvironmentRadDoseRateCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IVehicleSpaceEnvironmentRadDoseRateElement
    :canonical: ansys.stk.core.stkobjects.IVehicleSpaceEnvironmentRadDoseRateCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVehicleSpaceEnvironmentRadDoseRateElement`


