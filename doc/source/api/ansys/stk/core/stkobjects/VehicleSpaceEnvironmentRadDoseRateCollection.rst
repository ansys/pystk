VehicleSpaceEnvironmentRadDoseRateCollection
============================================

.. py:class:: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateCollection

   Collection of dose rate elements computed for a shielding thickness.

.. py:currentmodule:: VehicleSpaceEnvironmentRadDoseRateCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleSpaceEnvironmentRadDoseRateCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VehicleSpaceEnvironmentRadDoseRateElement
    :canonical: ansys.stk.core.stkobjects.VehicleSpaceEnvironmentRadDoseRateCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VehicleSpaceEnvironmentRadDoseRateElement`


