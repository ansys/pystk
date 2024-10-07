AircraftLanding
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftLanding

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the aircraft landing category of an Aviator aircraft.

.. py:currentmodule:: AircraftLanding

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftLanding.get_built_in_model`
              - Get the built-in model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftLanding.get_basic_landing_by_name`
              - Get the basic Landing model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftLanding.get_advanced_landing_by_name`
              - Get the advanced Landing model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftLanding.get_as_catalog_item`
              - Get the catalog item interface for this object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftLanding



Method detail
-------------

.. py:method:: get_built_in_model(self) -> AircraftBasicLandingModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftLanding.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~AircraftBasicLandingModel`

.. py:method:: get_basic_landing_by_name(self, name: str) -> AircraftBasicLandingModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftLanding.get_basic_landing_by_name

    Get the basic Landing model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftBasicLandingModel`

.. py:method:: get_advanced_landing_by_name(self, name: str) -> AircraftAdvancedLandingModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftLanding.get_advanced_landing_by_name

    Get the advanced Landing model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~AircraftAdvancedLandingModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftLanding.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

