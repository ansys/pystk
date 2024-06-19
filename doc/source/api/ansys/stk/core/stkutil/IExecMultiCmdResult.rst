IExecMultiCmdResult
===================

.. py:class:: IExecMultiCmdResult

   object
   
   Collection of objects returned by the ExecuteMultipleCommands.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the element at the specified index (0-based).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IExecMultiCmdResult


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.IExecMultiCmdResult.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkutil.IExecMultiCmdResult._NewEnum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the objects in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IExecCmdResult
    :canonical: ansys.stk.core.stkutil.IExecMultiCmdResult.item

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IExecCmdResult`


