ExecMultiCmdResult
==================

.. py:class:: ansys.stk.core.stkx.ExecMultiCmdResult

   Collection of objects returned by the ExecuteMultipleCommands.

.. py:currentmodule:: ExecMultiCmdResult

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.ExecMultiCmdResult.item`
              - Get the element at the specified index (0-based).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.ExecMultiCmdResult.count`
              - Number of elements contained in the collection.
            * - :py:attr:`~ansys.stk.core.stkx.ExecMultiCmdResult._NewEnum`
              - Returns an object that can be used to iterate through all the objects in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import ExecMultiCmdResult


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkx.ExecMultiCmdResult.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkx.ExecMultiCmdResult._NewEnum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the objects in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ExecCmdResult
    :canonical: ansys.stk.core.stkx.ExecMultiCmdResult.item

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ExecCmdResult`


