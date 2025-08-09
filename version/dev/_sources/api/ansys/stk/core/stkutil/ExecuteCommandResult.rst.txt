ExecuteCommandResult
====================

.. py:class:: ansys.stk.core.stkutil.ExecuteCommandResult

   Collection of strings returned by the ExecuteCommand.

.. py:currentmodule:: ExecuteCommandResult

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ExecuteCommandResult.item`
              - Get the element at the specified index (0-based).
            * - :py:attr:`~ansys.stk.core.stkutil.ExecuteCommandResult.range`
              - Return the elements within the specified range.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ExecuteCommandResult._new_enum`
              - Return an object that can be used to iterate through all the strings in the collection.
            * - :py:attr:`~ansys.stk.core.stkutil.ExecuteCommandResult.count`
              - Number of elements contained in the collection.
            * - :py:attr:`~ansys.stk.core.stkutil.ExecuteCommandResult.is_succeeded`
              - Indicate whether the object contains valid results.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import ExecuteCommandResult


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkutil.ExecuteCommandResult._new_enum
    :type: EnumeratorProxy

    Return an object that can be used to iterate through all the strings in the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkutil.ExecuteCommandResult.count
    :type: int

    Number of elements contained in the collection.

.. py:property:: is_succeeded
    :canonical: ansys.stk.core.stkutil.ExecuteCommandResult.is_succeeded
    :type: bool

    Indicate whether the object contains valid results.


Method detail
-------------



.. py:method:: item(self, index: int) -> str
    :canonical: ansys.stk.core.stkutil.ExecuteCommandResult.item

    Get the element at the specified index (0-based).

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~str`

.. py:method:: range(self, start_index: int, stop_index: int) -> list
    :canonical: ansys.stk.core.stkutil.ExecuteCommandResult.range

    Return the elements within the specified range.

    :Parameters:

        **start_index** : :obj:`~int`

        **stop_index** : :obj:`~int`


    :Returns:

        :obj:`~list`


