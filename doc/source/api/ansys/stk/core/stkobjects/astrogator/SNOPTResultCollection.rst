SNOPTResultCollection
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection

   Bases: 

   SNOPT result collection.

.. py:currentmodule:: SNOPTResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection.get_result_by_paths`
              - Return the result specified by the object/result names.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SNOPTResultCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> SNOPTResult
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~SNOPTResult`



.. py:method:: get_result_by_paths(self, objectPath: str, resultPath: str) -> SNOPTResult
    :canonical: ansys.stk.core.stkobjects.astrogator.SNOPTResultCollection.get_result_by_paths

    Return the result specified by the object/result names.

    :Parameters:

    **objectPath** : :obj:`~str`
    **resultPath** : :obj:`~str`

    :Returns:

        :obj:`~SNOPTResult`

