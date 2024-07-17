SearchPluginControlCollection
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection

   Bases: 

   The list of search plugin control parameters.

.. py:currentmodule:: SearchPluginControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection._NewEnum`
              - Property that allows you to enumerate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.count`
              - Returns the size of the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SearchPluginControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection._NewEnum
    :type: EnumeratorProxy

    Property that allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> SearchPluginControl
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~SearchPluginControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> SearchPluginControl
    :canonical: ansys.stk.core.stkobjects.astrogator.SearchPluginControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~SearchPluginControl`

