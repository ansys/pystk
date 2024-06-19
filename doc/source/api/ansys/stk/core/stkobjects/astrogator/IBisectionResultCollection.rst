IBisectionResultCollection
==========================

.. py:class:: IBisectionResultCollection

   object
   
   Bisection result collection.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Allow you to iterate through the collection.
            * - :py:meth:`~get_result_by_paths`
              - Return the result specified by the object/result names.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IBisectionResultCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResultCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResultCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IBisectionResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IBisectionResult`



.. py:method:: get_result_by_paths(self, objectPath: str, resultPath: str) -> IBisectionResult
    :canonical: ansys.stk.core.stkobjects.astrogator.IBisectionResultCollection.get_result_by_paths

    Return the result specified by the object/result names.

    :Parameters:

    **objectPath** : :obj:`~str`
    **resultPath** : :obj:`~str`

    :Returns:

        :obj:`~IBisectionResult`

