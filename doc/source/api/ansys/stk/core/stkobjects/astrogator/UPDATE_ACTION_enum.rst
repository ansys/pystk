UPDATE_ACTION
=============

.. py:class:: ansys.stk.core.stkobjects.astrogator.UPDATE_ACTION

   IntEnum


.. py:currentmodule:: UPDATE_ACTION

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~NO_CHANGE`
              - No change in value - leave the current value for this parameter unchanged (ignoring any quantity that may appear in the Value column).

            * - :py:attr:`~ADD_VALUE`
              - Add value - add the quantity entered in the Value column to the current value for this parameter.

            * - :py:attr:`~SUBTRACT_VALUE`
              - Subtract value - subtract the quantity entered in the Value column from the current value for this parameter.

            * - :py:attr:`~SET_TO_NEW_VALUE`
              - Set to new value - replace the current value for this parameter with the quantity entered in the Value column.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import UPDATE_ACTION


