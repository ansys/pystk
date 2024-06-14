IAircraftTakeoff
================

.. py:class:: IAircraftTakeoff

   object
   
   Interface used to access the takeoff options for an aircraft in the Aviator catalog.

.. py:currentmodule:: ansys.stk.core.stkobjects.aviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~get_built_in_model`
              - Get the built-in model.
            * - :py:meth:`~get_basic_takeoff_by_name`
              - Get the basic Takeoff model with the given name.
            * - :py:meth:`~get_advanced_takeoff_by_name`
              - Get the advanced Takeoff model with the given name.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftTakeoff



Method detail
-------------

.. py:method:: get_built_in_model(self) -> "IAircraftBasicTakeoffModel"

    Get the built-in model.

    :Returns:

        :obj:`~"IAircraftBasicTakeoffModel"`

.. py:method:: get_basic_takeoff_by_name(self, name:str) -> "IAircraftBasicTakeoffModel"

    Get the basic Takeoff model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IAircraftBasicTakeoffModel"`

.. py:method:: get_advanced_takeoff_by_name(self, name:str) -> "IAircraftAdvancedTakeoffModel"

    Get the advanced Takeoff model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IAircraftAdvancedTakeoffModel"`

.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

