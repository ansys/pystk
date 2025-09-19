PerformanceModelOptions
=======================

.. py:class:: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions

   Class defining the options for the active performance model in a phase.

.. py:currentmodule:: PerformanceModelOptions

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.copy_from_catalog`
              - Create a copy of the performance model in the catalog with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.create_new`
              - Create a new performance model of the given type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.delete`
              - Delete the performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.link_to_catalog`
              - Link to the performance model in the catalog with the given name.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.rename`
              - Rename the performance model.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.is_linked_to_catalog`
              - Get whether the performance model is linked to the catalog.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.name`
              - Get the name of the performance model.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.properties`
              - Get the properties of the performance model.



Examples
--------

Configure the performance models to be used in the phase

.. code-block:: python

    # Phase phase: Phase object
    # Get the acceleration performance model used for the current phase
    acceleration = phase.get_performance_model_by_type("Acceleration")
    # Check if it is linked to the catalog
    isLinkedToCatalog = acceleration.is_linked_to_catalog
    # Use the performance model in the catalog named "Built-In Model"
    acceleration.link_to_catalog("Built-In Model")

    # Get the VTOL performance model
    vtol = phase.get_performance_model_by_type("VTOL")
    # Create a new vtol model of type AGI VTOL Model. Note that this new model does not exist in the catalog and only exists in the phase.
    vtol.create_new("AGI VTOL Model")
    # Rename the performance model
    vtol.rename("Temporary VTOL Model")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import PerformanceModelOptions


Property detail
---------------

.. py:property:: is_linked_to_catalog
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.is_linked_to_catalog
    :type: bool

    Get whether the performance model is linked to the catalog.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.name
    :type: str

    Get the name of the performance model.

.. py:property:: properties
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.properties
    :type: IPerformanceModel

    Get the properties of the performance model.


Method detail
-------------

.. py:method:: copy_from_catalog(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.copy_from_catalog

    Create a copy of the performance model in the catalog with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: create_new(self, type: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.create_new

    Create a new performance model of the given type.

    :Parameters:

        **type** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: delete(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.delete

    Delete the performance model.

    :Returns:

        :obj:`~None`


.. py:method:: link_to_catalog(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.link_to_catalog

    Link to the performance model in the catalog with the given name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`



.. py:method:: rename(self, type: str) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.PerformanceModelOptions.rename

    Rename the performance model.

    :Parameters:

        **type** : :obj:`~str`


    :Returns:

        :obj:`~None`

