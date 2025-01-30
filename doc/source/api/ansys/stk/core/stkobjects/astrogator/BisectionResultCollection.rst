BisectionResultCollection
=========================

.. py:class:: ansys.stk.core.stkobjects.astrogator.BisectionResultCollection

   Bisection result collection.

.. py:currentmodule:: BisectionResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResultCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResultCollection.get_result_by_paths`
              - Return the result specified by the object/result names.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResultCollection._new_enum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.BisectionResultCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import BisectionResultCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResultCollection._new_enum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResultCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> BisectionResult
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~BisectionResult`



.. py:method:: get_result_by_paths(self, object_path: str, result_path: str) -> BisectionResult
    :canonical: ansys.stk.core.stkobjects.astrogator.BisectionResultCollection.get_result_by_paths

    Return the result specified by the object/result names.

    :Parameters:

    **object_path** : :obj:`~str`
    **result_path** : :obj:`~str`

    :Returns:

        :obj:`~BisectionResult`

