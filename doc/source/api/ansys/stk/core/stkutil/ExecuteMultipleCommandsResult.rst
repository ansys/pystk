ExecuteMultipleCommandsResult
=============================

.. py:class:: ansys.stk.core.stkutil.ExecuteMultipleCommandsResult

   Collection of objects returned by the ExecuteMultipleCommands.

.. py:currentmodule:: ExecuteMultipleCommandsResult

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ExecuteMultipleCommandsResult.item`
              - Get the element at the specified index (0-based).

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ExecuteMultipleCommandsResult.count`
              - Number of elements contained in the collection.
            * - :py:attr:`~ansys.stk.core.stkutil.ExecuteMultipleCommandsResult._new_enum`
              - Returns an object that can be used to iterate through all the objects in the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import ExecuteMultipleCommandsResult


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.ExecuteMultipleCommandsResult.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkutil.ExecuteMultipleCommandsResult._new_enum
    :type: EnumeratorProxy

    Returns an object that can be used to iterate through all the objects in the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ExecuteCommandResult
    :canonical: ansys.stk.core.stkutil.ExecuteMultipleCommandsResult.item

    Get the element at the specified index (0-based).

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ExecuteCommandResult`


