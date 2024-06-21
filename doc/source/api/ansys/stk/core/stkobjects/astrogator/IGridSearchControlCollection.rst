IGridSearchControlCollection
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection

   object
   
   Properties for the list of Grid Search control parameters.

.. py:currentmodule:: IGridSearchControlCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection.item`
              - Allow you to iterate through the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection.get_control_by_paths`
              - Return the control specified by the object/control path.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection._NewEnum`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection.count`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IGridSearchControlCollection


Property detail
---------------

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection._NewEnum
    :type: EnumeratorProxy

    Allows you to enumerate through the collection.

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection.count
    :type: int

    Returns the size of the collection.


Method detail
-------------

.. py:method:: item(self, index: int) -> IGridSearchControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection.item

    Allow you to iterate through the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IGridSearchControl`



.. py:method:: get_control_by_paths(self, objectPath: str, controlPath: str) -> IGridSearchControl
    :canonical: ansys.stk.core.stkobjects.astrogator.IGridSearchControlCollection.get_control_by_paths

    Return the control specified by the object/control path.

    :Parameters:

    **objectPath** : :obj:`~str`
    **controlPath** : :obj:`~str`

    :Returns:

        :obj:`~IGridSearchControl`

