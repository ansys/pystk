Phase
=====

.. py:class:: ansys.stk.core.stkobjects.aviator.Phase

   Class defining a phase in an Aviator mission.

.. py:currentmodule:: Phase

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Phase.get_performance_model_by_type`
              - Get the active performance model for the given category type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Phase.set_default_performance_models`
              - Set the phase to use the default performance models of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Phase.copy_performance_models`
              - Create a copy of the active performance models for the current phase.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Phase.paste_performance_models`
              - Paste the performance models.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Phase.procedures`
              - Return the procedure collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.Phase.name`
              - Get or set the name of the phase.



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


Add a new phase and use the same performance models as the first phase

.. code-block:: python

    # PhaseCollection phases: Phase Collection object
    # Add a new phase at the end of the mission
    newPhase = phases.add()
    # Rename the phase
    newPhase.name = "New Phase"
    # Copy the performance models from the first phase and paste it to the new phase
    phases[0].copy_performance_models()
    newPhase.paste_performance_models()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import Phase


Property detail
---------------

.. py:property:: procedures
    :canonical: ansys.stk.core.stkobjects.aviator.Phase.procedures
    :type: ProcedureCollection

    Return the procedure collection.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.Phase.name
    :type: str

    Get or set the name of the phase.


Method detail
-------------




.. py:method:: get_performance_model_by_type(self, type: str) -> PerformanceModelOptions
    :canonical: ansys.stk.core.stkobjects.aviator.Phase.get_performance_model_by_type

    Get the active performance model for the given category type.

    :Parameters:

        **type** : :obj:`~str`


    :Returns:

        :obj:`~PerformanceModelOptions`

.. py:method:: set_default_performance_models(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.Phase.set_default_performance_models

    Set the phase to use the default performance models of the aircraft.

    :Returns:

        :obj:`~None`

.. py:method:: copy_performance_models(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.Phase.copy_performance_models

    Create a copy of the active performance models for the current phase.

    :Returns:

        :obj:`~None`

.. py:method:: paste_performance_models(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.Phase.paste_performance_models

    Paste the performance models.

    :Returns:

        :obj:`~None`

