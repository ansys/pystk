IWinProjectionPosition
======================

.. py:class:: IWinProjectionPosition

   object
   
   Projected window position detail.

.. py:currentmodule:: ansys.stk.core.stkx

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~x_position`
            * - :py:meth:`~y_position`
            * - :py:meth:`~is_win_projection_position_valid`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IWinProjectionPosition


Property detail
---------------

.. py:property:: x_position
    :canonical: ansys.stk.core.stkx.IWinProjectionPosition.x_position
    :type: float

    Projected window X position.

.. py:property:: y_position
    :canonical: ansys.stk.core.stkx.IWinProjectionPosition.y_position
    :type: float

    Projected window Y position.

.. py:property:: is_win_projection_position_valid
    :canonical: ansys.stk.core.stkx.IWinProjectionPosition.is_win_projection_position_valid
    :type: bool

    Indicates if the returned projected position is valid or not.


