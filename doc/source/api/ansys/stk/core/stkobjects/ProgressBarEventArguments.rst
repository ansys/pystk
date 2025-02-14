ProgressBarEventArguments
=========================

.. py:class:: ansys.stk.core.stkobjects.ProgressBarEventArguments

   Represents a structure used by the Percent Complete events.

.. py:currentmodule:: ProgressBarEventArguments

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ProgressBarEventArguments.cancel`
              - Cancel a lengthy operation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ProgressBarEventArguments.canceled`
              - Return whether the lengthy operation has been canceled.
            * - :py:attr:`~ansys.stk.core.stkobjects.ProgressBarEventArguments.can_cancel`
              - Return whether the lengthy operation can be canceled.
            * - :py:attr:`~ansys.stk.core.stkobjects.ProgressBarEventArguments.percent_completed`
              - Return the current progress status. The value returned is greater or equal to 0 and less or equal to 100.
            * - :py:attr:`~ansys.stk.core.stkobjects.ProgressBarEventArguments.message`
              - Get a progress message.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ProgressBarEventArguments


Property detail
---------------

.. py:property:: canceled
    :canonical: ansys.stk.core.stkobjects.ProgressBarEventArguments.canceled
    :type: bool

    Return whether the lengthy operation has been canceled.

.. py:property:: can_cancel
    :canonical: ansys.stk.core.stkobjects.ProgressBarEventArguments.can_cancel
    :type: bool

    Return whether the lengthy operation can be canceled.

.. py:property:: percent_completed
    :canonical: ansys.stk.core.stkobjects.ProgressBarEventArguments.percent_completed
    :type: int

    Return the current progress status. The value returned is greater or equal to 0 and less or equal to 100.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.ProgressBarEventArguments.message
    :type: str

    Get a progress message.


Method detail
-------------

.. py:method:: cancel(self) -> None
    :canonical: ansys.stk.core.stkobjects.ProgressBarEventArguments.cancel

    Cancel a lengthy operation.

    :Returns:

        :obj:`~None`





