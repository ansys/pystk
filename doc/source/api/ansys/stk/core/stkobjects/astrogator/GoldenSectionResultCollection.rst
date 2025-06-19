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

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection._new_enum`
              - Allow you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.count`
              - Return the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import GoldenSectionResultCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection._new_enum
    :type: EnumeratorProxy

    Allow you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.count
    :type: int

    Return the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> GoldenSectionResult
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~GoldenSectionResult`



.. py:method:: get_result_by_paths(self, object_path: str, result_path: str) -> GoldenSectionResult
    :canonical: ansys.stk.core.stkobjects.astrogator.GoldenSectionResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

        **object_path** : :obj:`~str`

        **result_path** : :obj:`~str`


    :Returns:

        :obj:`~GoldenSectionResult`

