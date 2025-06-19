AircraftDescent
===============

.. py:class:: ansys.stk.core.stkobjects.aviator.AircraftDescent

   Bases: :py:class:`~ansys.stk.core.stkobjects.aviator.ICatalogItem`

   Class defining the aircraft descent category of an Aviator aircraft.

.. py:currentmodule:: AircraftDescent

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftDescent.get_built_in_model`
              - Get the built-in model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftDescent.get_basic_descent_by_name`
              - Get the basic descent model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftDescent.get_advanced_descent_by_name`
              - Get the advanced descent model with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.AircraftDescent.get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import AircraftDescent



Method detail
-------------

.. py:method:: get_built_in_model(self) -> AircraftBasicDescentModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftDescent.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~AircraftBasicDescentModel`

.. py:method:: get_basic_descent_by_name(self, name: str) -> AircraftBasicDescentModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftDescent.get_basic_descent_by_name

    Get the basic descent model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftBasicDescentModel`

.. py:method:: get_advanced_descent_by_name(self, name: str) -> AircraftAdvancedDescentModel
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftDescent.get_advanced_descent_by_name

    Get the advanced descent model with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~AircraftAdvancedDescentModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.AircraftDescent.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

