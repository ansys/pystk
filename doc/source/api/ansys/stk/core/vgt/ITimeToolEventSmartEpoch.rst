ITimeToolEventSmartEpoch
========================

.. py:class:: ITimeToolEventSmartEpoch

   object
   
   A smart epoch.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_explicit_time`
              - Set explicit time instant and the smart epoch's state to Explicit.
            * - :py:meth:`~set_implicit_time`
              - Set the reference event and the smart epoch's state to Implicit.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~time_instant`
            * - :py:meth:`~reference_event`
            * - :py:meth:`~state`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ITimeToolEventSmartEpoch


Property detail
---------------

.. py:property:: time_instant
    :canonical: ansys.stk.core.vgt.ITimeToolEventSmartEpoch.time_instant
    :type: typing.Any

    Represents the time instant if the state is set to explicit.

.. py:property:: reference_event
    :canonical: ansys.stk.core.vgt.ITimeToolEventSmartEpoch.reference_event
    :type: IAgCrdnEvent

    A reference event object used to compute time instant if the state is set to implicit.

.. py:property:: state
    :canonical: ansys.stk.core.vgt.ITimeToolEventSmartEpoch.state
    :type: CRDN_SMART_EPOCH_STATE

    State of the event.


Method detail
-------------





.. py:method:: set_explicit_time(self, epoch: typing.Any) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventSmartEpoch.set_explicit_time

    Set explicit time instant and the smart epoch's state to Explicit.

    :Parameters:

    **epoch** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: set_implicit_time(self, eventEpoch: ITimeToolEvent) -> None
    :canonical: ansys.stk.core.vgt.ITimeToolEventSmartEpoch.set_implicit_time

    Set the reference event and the smart epoch's state to Implicit.

    :Parameters:

    **eventEpoch** : :obj:`~ITimeToolEvent`

    :Returns:

        :obj:`~None`

