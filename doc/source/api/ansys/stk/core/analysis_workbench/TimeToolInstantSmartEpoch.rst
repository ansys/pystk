TimeToolInstantSmartEpoch
=========================

.. py:class:: ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ITimeToolInstant`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A smart epoch.

.. py:currentmodule:: TimeToolInstantSmartEpoch

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.set_explicit_time`
              - Set explicit time instant and the smart epoch's state to Explicit.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.set_implicit_time`
              - Set the reference event and the smart epoch's state to Implicit.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.time_instant`
              - Represents the time instant if the state is set to explicit.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.reference_epoch`
              - A reference event object used to compute time instant if the state is set to implicit.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.state`
              - State of the event.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import TimeToolInstantSmartEpoch


Property detail
---------------

.. py:property:: time_instant
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.time_instant
    :type: typing.Any

    Represents the time instant if the state is set to explicit.

.. py:property:: reference_epoch
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.reference_epoch
    :type: ITimeToolInstant

    A reference event object used to compute time instant if the state is set to implicit.

.. py:property:: state
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.state
    :type: SmartEpochState

    State of the event.


Method detail
-------------





.. py:method:: set_explicit_time(self, epoch: typing.Any) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.set_explicit_time

    Set explicit time instant and the smart epoch's state to Explicit.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~None`

.. py:method:: set_implicit_time(self, event_epoch: ITimeToolInstant) -> None
    :canonical: ansys.stk.core.analysis_workbench.TimeToolInstantSmartEpoch.set_implicit_time

    Set the reference event and the smart epoch's state to Implicit.

    :Parameters:

        **event_epoch** : :obj:`~ITimeToolInstant`


    :Returns:

        :obj:`~None`

