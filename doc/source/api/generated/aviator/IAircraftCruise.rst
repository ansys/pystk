IAircraftCruise
===============

.. py:class:: IAircraftCruise

   object
   
   Interface used to access the cruise options for an aircraft in the Aviator catalog.

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
            * - :py:meth:`~get_basic_cruise_by_name`
              - Get the basic cruise model with the given name.
            * - :py:meth:`~get_advanced_cruise_by_name`
              - Get the advanced cruise model with the given name.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftCruise



Method detail
-------------

.. py:method:: get_built_in_model(self) -> "IAircraftBasicCruiseModel"

    Get the built-in model.

    :Returns:

        :obj:`~"IAircraftBasicCruiseModel"`

.. py:method:: get_basic_cruise_by_name(self, name:str) -> "IAircraftBasicCruiseModel"

    Get the basic cruise model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IAircraftBasicCruiseModel"`

.. py:method:: get_advanced_cruise_by_name(self, name:str) -> "IAircraftAdvancedCruiseModel"

    Get the advanced cruise model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IAircraftAdvancedCruiseModel"`

.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

