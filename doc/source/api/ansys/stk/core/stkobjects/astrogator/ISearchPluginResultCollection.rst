ISearchPluginResultCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection

   object
   
   Properties for the list of search plugin equality constraints.

.. py:currentmodule:: ISearchPluginResultCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection.get_result_by_paths`
              - Return the result specified by the object/result path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection._NewEnum`
              - Function to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection.count`
              - Size of the collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISearchPluginResultCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection._NewEnum
    :type: EnumeratorProxy

    Function to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection.count
    :type: int

    Size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> ISearchPluginResult
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ISearchPluginResult`



.. py:method:: get_result_by_paths(self, objectPath: str, resultPath: str) -> ISearchPluginResult
    :canonical: ansys.stk.core.stkobjects.astrogator.ISearchPluginResultCollection.get_result_by_paths

    Return the result specified by the object/result path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **resultPath** : :obj:`~str`

    :Returns:

        :obj:`~ISearchPluginResult`

