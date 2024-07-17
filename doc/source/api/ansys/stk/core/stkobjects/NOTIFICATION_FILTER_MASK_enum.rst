NOTIFICATION_FILTER_MASK
========================

.. py:class:: ansys.stk.core.stkobjects.NOTIFICATION_FILTER_MASK

   IntFlag


.. py:currentmodule:: NOTIFICATION_FILTER_MASK

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NO_EVENTS`
              - Disable all events.

            * - :py:attr:`~ANIMATION_EVENTS`
              - Clients are notified upon occurrence of any of the available animation events. Animation events include OnAnimUpdate, OnAnimationRewind, etc.

            * - :py:attr:`~SCENARIO_EVENTS`
              - Clients are notified upon occurrence of any of the available scenario events. Scenario events include OnScenarioNew, OnScenarioLoad, OnScenarioBeforeClose, OnScenarioClose, etc.

            * - :py:attr:`~LOGGING_EVENTS`
              - Clients are notified upon occurrence of OnLogMessage event.

            * - :py:attr:`~OBJECT_EVENTS`
              - Clients are notified upon occurrence of an event affecting the object hierarchy (OnStkObjectAdded, OnStkObjectDeleted and OnStkObjectPreDelete).

            * - :py:attr:`~OBJECT_CHANGED_EVENTS`
              - Clients are notified upon occurrence of OnStkObjectChanged event.

            * - :py:attr:`~PERCENT_COMPLETE_EVENTS`
              - Clients are notified upon occurrence of any of the available percent complete events (OnPercentComplete*).

            * - :py:attr:`~OBJECT_RENAME_EVENTS`
              - Clients are notified upon occurrence of an STK object renaming event.

            * - :py:attr:`~ENABLE_ALL_EVENTS`
              - Enable all events.

            * - :py:attr:`~STK_OBJECT_3D_EDITING_EVENTS`
              - Clients are notified upon occurrence of any of the available object editing events. Object editing events include OnStkObjectStart3dEditing, OnStkObjectStop3dEditing, OnStkObjectApply3dEditing, OnStkObjectCancel3dEditing etc.

            * - :py:attr:`~STK_OBJECT_CUT_COPY_PASTE_EVENTS`
              - Clients are notified upon occurrence of any of the available STK object Cut, Copy and Paste events.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import NOTIFICATION_FILTER_MASK


