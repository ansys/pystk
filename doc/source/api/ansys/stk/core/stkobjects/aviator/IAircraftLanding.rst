IAircraftLanding
================

.. py:class:: IAircraftLanding

   object
   
   Interface used to access the landing options for an aircraft in the Aviator catalog.

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
            * - :py:meth:`~get_basic_landing_by_name`
              - Get the basic Landing model with the given name.
            * - :py:meth:`~get_advanced_landing_by_name`
              - Get the advanced Landing model with the given name.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftLanding



Method detail
-------------

.. py:method:: get_built_in_model(self) -> IAircraftBasicLandingModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftLanding.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~IAircraftBasicLandingModel`

.. py:method:: get_basic_landing_by_name(self, name: str) -> IAircraftBasicLandingModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftLanding.get_basic_landing_by_name

    Get the basic Landing model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftBasicLandingModel`

.. py:method:: get_advanced_landing_by_name(self, name: str) -> IAircraftAdvancedLandingModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftLanding.get_advanced_landing_by_name

    Get the advanced Landing model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftAdvancedLandingModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftLanding.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

