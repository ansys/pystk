AvailableFeatures
=================

.. py:class:: ansys.stk.core.stkobjects.AvailableFeatures

   Bases: 

   Class is used to check the availability of the features such as Astrogator, etc.

.. py:currentmodule:: AvailableFeatures

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AvailableFeatures.is_propagator_type_available`
              - Return true if the specified propagator is available.
            * - :py:attr:`~ansys.stk.core.stkobjects.AvailableFeatures.is_object_type_available`
              - Return true if the specified STK object type is available.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AvailableFeatures



Method detail
-------------

.. py:method:: is_propagator_type_available(self, propagatorType: VEHICLE_PROPAGATOR_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.AvailableFeatures.is_propagator_type_available

    Return true if the specified propagator is available.

    :Parameters:

    **propagatorType** : :obj:`~VEHICLE_PROPAGATOR_TYPE`

    :Returns:

        :obj:`~bool`

.. py:method:: is_object_type_available(self, objectType: STK_OBJECT_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.AvailableFeatures.is_object_type_available

    Return true if the specified STK object type is available.

    :Parameters:

    **objectType** : :obj:`~STK_OBJECT_TYPE`

    :Returns:

        :obj:`~bool`

