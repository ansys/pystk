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

