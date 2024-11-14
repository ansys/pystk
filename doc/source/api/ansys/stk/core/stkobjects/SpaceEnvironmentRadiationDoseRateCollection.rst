SpaceEnvironmentRadiationDoseRateCollection
===========================================

.. py:class:: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection

   Collection of dose rate elements computed for a shielding thickness.

.. py:currentmodule:: SpaceEnvironmentRadiationDoseRateCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection.item`
              - Given an index, returns an element in the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection._new_enum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import SpaceEnvironmentRadiationDoseRateCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> SpaceEnvironmentRadiationDoseRateElement
    :canonical: ansys.stk.core.stkobjects.SpaceEnvironmentRadiationDoseRateCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~SpaceEnvironmentRadiationDoseRateElement`


