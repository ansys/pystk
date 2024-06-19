IAircraftDescent
================

.. py:class:: IAircraftDescent

   object
   
   Interface used to access the descent options for an aircraft in the Aviator catalog.

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
            * - :py:meth:`~get_basic_descent_by_name`
              - Get the basic descent model with the given name.
            * - :py:meth:`~get_advanced_descent_by_name`
              - Get the advanced descent model with the given name.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftDescent



Method detail
-------------

.. py:method:: get_built_in_model(self) -> IAircraftBasicDescentModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftDescent.get_built_in_model

    Get the built-in model.

    :Returns:

        :obj:`~IAircraftBasicDescentModel`

.. py:method:: get_basic_descent_by_name(self, name: str) -> IAircraftBasicDescentModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftDescent.get_basic_descent_by_name

    Get the basic descent model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftBasicDescentModel`

.. py:method:: get_advanced_descent_by_name(self, name: str) -> IAircraftAdvancedDescentModel
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftDescent.get_advanced_descent_by_name

    Get the advanced descent model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IAircraftAdvancedDescentModel`

.. py:method:: get_as_catalog_item(self) -> ICatalogItem
    :canonical: ansys.stk.core.stkobjects.aviator.IAircraftDescent.get_as_catalog_item

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~ICatalogItem`

