IPOPTResultCollection
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection

   Bases: 

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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IPOPTResultCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection._NewEnum
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



.. py:method:: get_result_by_paths(self, objectPath: str, resultPath: str) -> IPOPTResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IPOPTResultCollection.get_result_by_paths

    Return the result specified by the object/result names.

    :Parameters:

    **objectPath** : :obj:`~str`
    **resultPath** : :obj:`~str`

    :Returns:

        :obj:`~IPOPTResult`

