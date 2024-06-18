IExecCmdResult
==============

.. py:class:: IExecCmdResult

   object
   
   Collection of strings returned by the ExecuteCommand.

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
            * - :py:meth:`~range`
              - Return the elements within the specified range.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~is_succeeded`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IExecCmdResult


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.IExecCmdResult.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkutil.IExecCmdResult._NewEnum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the strings in the collection.

.. py:property:: is_succeeded
    :canonical: ansys.stk.core.stkutil.IExecCmdResult.is_succeeded
    :type: bool

    Indicates whether the object contains valid results.


Method detail
-------------


.. py:method:: item(self, index:int) -> str

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~str`


.. py:method:: range(self, startIndex:int, stopIndex:int) -> list

    Return the elements within the specified range.

    :Parameters:

    **startIndex** : :obj:`~int`
    **stopIndex** : :obj:`~int`

    :Returns:

        :obj:`~list`


