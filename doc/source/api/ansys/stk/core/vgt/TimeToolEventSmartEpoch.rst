TimeToolEventSmartEpoch
=======================

.. py:class:: ansys.stk.core.vgt.TimeToolEventSmartEpoch

   Bases: :py:class:`~ansys.stk.core.vgt.ITimeToolEvent`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A smart epoch.

.. py:currentmodule:: TimeToolEventSmartEpoch

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventSmartEpoch.set_explicit_time`
              - Set explicit time instant and the smart epoch's state to Explicit.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventSmartEpoch.set_implicit_time`
              - Set the reference event and the smart epoch's state to Implicit.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventSmartEpoch.time_instant`
              - Represents the time instant if the state is set to explicit.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventSmartEpoch.reference_event`
              - A reference event object used to compute time instant if the state is set to implicit.
            * - :py:attr:`~ansys.stk.core.vgt.TimeToolEventSmartEpoch.state`
              - State of the event.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import TimeToolEventSmartEpoch


Property detail
---------------

.. py:property:: time_instant
    :canonical: ansys.stk.core.vgt.TimeToolEventSmartEpoch.time_instant
    :type: typing.Any

    Represents the time instant if the state is set to explicit.

.. py:property:: reference_event
    :canonical: ansys.stk.core.vgt.TimeToolEventSmartEpoch.reference_event
    :type: ITimeToolEvent

    A reference event object used to compute time instant if the state is set to implicit.

.. py:property:: state
    :canonical: ansys.stk.core.vgt.TimeToolEventSmartEpoch.state
    :type: CRDN_SMART_EPOCH_STATE

    State of the event.


Method detail
-------------





.. py:method:: set_explicit_time(self, epoch: typing.Any) -> None
    :canonical: ansys.stk.core.vgt.TimeToolEventSmartEpoch.set_explicit_time

    Set explicit time instant and the smart epoch's state to Explicit.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_implicit_time(self, eventEpoch: ITimeToolEvent) -> None
    :canonical: ansys.stk.core.vgt.TimeToolEventSmartEpoch.set_implicit_time

    Set the reference event and the smart epoch's state to Implicit.

    :Parameters:

    **eventEpoch** : :obj:`~ITimeToolEvent`

    :Returns:

        :obj:`~None`

