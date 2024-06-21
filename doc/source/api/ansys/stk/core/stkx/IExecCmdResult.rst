IExecCmdResult
==============

.. py:class:: ansys.stk.core.stkx.IExecCmdResult

   object
   
   Collection of strings returned by the ExecuteCommand.

.. py:currentmodule:: IExecCmdResult

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IExecCmdResult.item`
              - Get the element at the specified index (0-based).
            * - :py:attr:`~ansys.stk.core.stkx.IExecCmdResult.range`
              - Return the elements within the specified range.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkx.IExecCmdResult.count`
            * - :py:attr:`~ansys.stk.core.stkx.IExecCmdResult._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkx.IExecCmdResult.is_succeeded`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkx import IExecCmdResult


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkx.IExecCmdResult.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkx.IExecCmdResult._NewEnum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the strings in the collection.

.. py:property:: is_succeeded
    :canonical: ansys.stk.core.stkx.IExecCmdResult.is_succeeded
    :type: bool

    Indicates whether the object contains valid results.


Method detail
-------------


.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkx.IExecCmdResult.item

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: range(self, startIndex: int, stopIndex: int) -> list
    :canonical: ansys.stk.core.stkx.IExecCmdResult.range

    Return the elements within the specified range.

    :Parameters:

    **startIndex** : :obj:`~int`
    **stopIndex** : :obj:`~int`

    :Returns:

        :obj:`~list`


