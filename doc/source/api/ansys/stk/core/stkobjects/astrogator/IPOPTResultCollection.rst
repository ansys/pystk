IPOPTResultCollection
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection

   IPOPT result collection.

.. py:currentmodule:: IPOPTResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection.get_result_by_paths`
              - Return the result specified by the object/result names.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection._new_enum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPOPTResultCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection._new_enum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IPOPTResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IPOPTResult`



.. py:method:: get_result_by_paths(self, object_path: str, result_path: str) -> IPOPTResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection.get_result_by_paths

    Return the result specified by the object/result names.

    :Parameters:

    **object_path** : :obj:`~str`
    **result_path** : :obj:`~str`

    :Returns:

        :obj:`~IPOPTResult`

