SearchPluginResultCollection
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection

   The list of search plugin equality constraints.

.. py:currentmodule:: SearchPluginResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection.get_result_by_paths`
              - Return the result specified by the object/result path.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection._new_enum`
              - Function to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection.count`
              - Size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SearchPluginResultCollection


Property detail
---------------

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection._new_enum
    :type: EnumeratorProxy

    Function to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection.count
    :type: int

    Size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> SearchPluginResult
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~SearchPluginResult`



.. py:method:: get_result_by_paths(self, object_path: str, result_path: str) -> SearchPluginResult
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

        **object_path** : :obj:`~str`

        **result_path** : :obj:`~str`


    :Returns:

        :obj:`~SearchPluginResult`

