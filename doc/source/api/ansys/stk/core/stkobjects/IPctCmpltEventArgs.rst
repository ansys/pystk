IPctCmpltEventArgs
==================

.. py:class:: IPctCmpltEventArgs

   object
   
   Represents a structure used by the Percent Complete events.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~cancel`
              - Cancel a lengthy operation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~canceled`
            * - :py:meth:`~can_cancel`
            * - :py:meth:`~percent_completed`
            * - :py:meth:`~message`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IPctCmpltEventArgs


Property detail
---------------

.. py:property:: canceled
    :canonical: ansys.stk.core.stkobjects.IPctCmpltEventArgs.canceled
    :type: bool

    Returns whether the lengthy operation has been canceled.

.. py:property:: can_cancel
    :canonical: ansys.stk.core.stkobjects.IPctCmpltEventArgs.can_cancel
    :type: bool

    Returns whether the lengthy operation can be canceled.

.. py:property:: percent_completed
    :canonical: ansys.stk.core.stkobjects.IPctCmpltEventArgs.percent_completed
    :type: int

    Returns the current progress status. The value returned is greater or equal to 0 and less or equal to 100.

.. py:property:: message
    :canonical: ansys.stk.core.stkobjects.IPctCmpltEventArgs.message
    :type: str

    Gets a progress message.


Method detail
-------------

.. py:method:: cancel(self) -> None
    :canonical: ansys.stk.core.stkobjects.IPctCmpltEventArgs.cancel

    Cancel a lengthy operation.

    :Returns:

        :obj:`~None`





