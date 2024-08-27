PctCmpltEventArgs
=================

.. py:class:: ansys.stk.core.stkobjects.PctCmpltEventArgs

   Represents a structure used by the Percent Complete events.

.. py:currentmodule:: PctCmpltEventArgs

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PctCmpltEventArgs.cancel`
              - Cancel a lengthy operation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PctCmpltEventArgs.canceled`
              - Returns whether the lengthy operation has been canceled.
            * - :py:attr:`~ansys.stk.core.stkobjects.PctCmpltEventArgs.can_cancel`
              - Returns whether the lengthy operation can be canceled.
            * - :py:attr:`~ansys.stk.core.stkobjects.PctCmpltEventArgs.percent_completed`
              - Returns the current progress status. The value returned is greater or equal to 0 and less or equal to 100.
            * - :py:attr:`~ansys.stk.core.stkobjects.PctCmpltEventArgs.message`
              - Gets a progress message.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PctCmpltEventArgs


Property detail
---------------

.. py:property:: canceled
    :canonical: ansys.stk.core.stkobjects.PctCmpltEventArgs.canceled
    :type: bool

    Returns whether the lengthy operation has been canceled.

.. py:property:: can_cancel
    :canonical: ansys.stk.core.stkobjects.PctCmpltEventArgs.can_cancel
    :type: bool

    Returns whether the lengthy operation can be canceled.

.. py:property:: percent_completed
    :canonical: ansys.stk.core.stkobjects.PctCmpltEventArgs.percent_completed
    :type: int

    Returns the current progress status. The value returned is greater or equal to 0 and less or equal to 100.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.PctCmpltEventArgs.message
    :type: str

    Gets a progress message.


Method detail
-------------

.. py:method:: cancel(self) -> None
    :canonical: ansys.stk.core.stkobjects.PctCmpltEventArgs.cancel

    Cancel a lengthy operation.

    :Returns:

        :obj:`~None`





