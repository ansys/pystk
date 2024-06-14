IAircraftClimb
==============

.. py:class:: IAircraftClimb

   object
   
   Interface used to access the climb options for an aircraft in the Aviator catalog.

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
            * - :py:meth:`~get_basic_climb_by_name`
              - Get the basic climb model with the given name.
            * - :py:meth:`~get_advanced_climb_by_name`
              - Get the advanced climb model with the given name.
            * - :py:meth:`~get_as_catalog_item`
              - Get the catalog item interface for this object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IAircraftClimb



Method detail
-------------

.. py:method:: get_built_in_model(self) -> "IAircraftBasicClimbModel"

    Get the built-in model.

    :Returns:

        :obj:`~"IAircraftBasicClimbModel"`

.. py:method:: get_basic_climb_by_name(self, name:str) -> "IAircraftBasicClimbModel"

    Get the basic climb model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IAircraftBasicClimbModel"`

.. py:method:: get_advanced_climb_by_name(self, name:str) -> "IAircraftAdvancedClimbModel"

    Get the advanced climb model with the given name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IAircraftAdvancedClimbModel"`

.. py:method:: get_as_catalog_item(self) -> "ICatalogItem"

    Get the catalog item interface for this object.

    :Returns:

        :obj:`~"ICatalogItem"`

