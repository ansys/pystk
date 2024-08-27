GoldenSectionResultCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection

   Properties for the list of Golden Section result parameters.

.. py:currentmodule:: GoldenSectionResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.get_result_by_paths`
              - Return the result specified by the object/result path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection._NewEnum`
              - Allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GoldenSectionResultCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> GoldenSectionResult
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~GoldenSectionResult`



.. py:method:: get_result_by_paths(self, objectPath: str, resultPath: str) -> GoldenSectionResult
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **resultPath** : :obj:`~str`

    :Returns:

        :obj:`~GoldenSectionResult`

