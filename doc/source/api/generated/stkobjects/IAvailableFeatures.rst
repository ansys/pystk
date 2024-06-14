IAvailableFeatures
==================

.. py:class:: IAvailableFeatures

   object
   
   Define methods to inquiry available and supported features, object types, etc.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~is_propagator_type_available`
              - Return true if the specified propagator is available.
            * - :py:meth:`~is_object_type_available`
              - Return true if the specified STK object type is available.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAvailableFeatures



Method detail
-------------

.. py:method:: is_propagator_type_available(self, propagatorType:"VEHICLE_PROPAGATOR_TYPE") -> bool

    Return true if the specified propagator is available.

    :Parameters:

    **propagatorType** : :obj:`~"VEHICLE_PROPAGATOR_TYPE"`

    :Returns:

        :obj:`~bool`

.. py:method:: is_object_type_available(self, objectType:"STK_OBJECT_TYPE") -> bool

    Return true if the specified STK object type is available.

    :Parameters:

    **objectType** : :obj:`~"STK_OBJECT_TYPE"`

    :Returns:

        :obj:`~bool`

