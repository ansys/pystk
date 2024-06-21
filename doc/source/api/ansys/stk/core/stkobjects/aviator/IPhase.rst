IPhase
======

.. py:class:: ansys.stk.core.stkobjects.aviator.IPhase

   object
   
   Interface used to access the phase options for a mission.

.. py:currentmodule:: IPhase

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPhase.get_performance_model_by_type`
              - Get the active performance model for the given category type.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPhase.set_default_perf_models`
              - Set the phase to use the default performance models of the aircraft.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPhase.copy_performance_models`
              - Create a copy of the active performance models for the current phase.
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPhase.paste_performance_models`
              - Paste the performance models.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPhase.procedures`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IPhase.name`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IPhase


Property detail
---------------

.. py:property:: procedures
    :canonical: ansys.stk.core.stkobjects.aviator.IPhase.procedures
    :type: IProcedureCollection

    Returns the procedure collection.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.aviator.IPhase.name
    :type: str

    Gets or sets the name of the phase.


Method detail
-------------




.. py:method:: get_performance_model_by_type(self, type: str) -> IPerformanceModelOptions
    :canonical: ansys.stk.core.stkobjects.aviator.IPhase.get_performance_model_by_type

    Get the active performance model for the given category type.

    :Parameters:

    **type** : :obj:`~str`

    :Returns:

        :obj:`~IPerformanceModelOptions`

.. py:method:: set_default_perf_models(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPhase.set_default_perf_models

    Set the phase to use the default performance models of the aircraft.

    :Returns:

        :obj:`~None`

.. py:method:: copy_performance_models(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPhase.copy_performance_models

    Create a copy of the active performance models for the current phase.

    :Returns:

        :obj:`~None`

.. py:method:: paste_performance_models(self) -> None
    :canonical: ansys.stk.core.stkobjects.aviator.IPhase.paste_performance_models

    Paste the performance models.

    :Returns:

        :obj:`~None`

