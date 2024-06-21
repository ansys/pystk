ISensorTargetCollection
=======================

.. py:class:: ansys.stk.core.stkobjects.ISensorTargetCollection

   object
   
   IAgSnTargetCollection Interface. A collection of targets.

.. py:currentmodule:: ISensorTargetCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection.item`
              - Given an index, returns an IAgSnTarget interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection.add`
              - Add a target.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection.remove`
              - Remove a target given an index.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection.remove_target`
              - Remove a target given the target's name.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection.remove_all`
              - Remove all targets in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection.add_object`
              - Add a target to the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection.remove_object`
              - Remove a target from the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection.count`
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorTargetCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorTargetCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection.count
    :type: int

    The number of items in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> ISensorTarget
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection.item

    Given an index, returns an IAgSnTarget interface.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ISensorTarget`

.. py:method:: add(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection.add

    Add a target.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection.remove

    Remove a target given an index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_target(self, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection.remove_target

    Remove a target given the target's name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection.remove_all

    Remove all targets in the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add_object(self, pObject: IStkObject) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection.add_object

    Add a target to the collection.

    :Parameters:

    **pObject** : :obj:`~IStkObject`

    :Returns:

        :obj:`~None`

.. py:method:: remove_object(self, pObject: IStkObject) -> None
    :canonical: ansys.stk.core.stkobjects.ISensorTargetCollection.remove_object

    Remove a target from the collection.

    :Parameters:

    **pObject** : :obj:`~IStkObject`

    :Returns:

        :obj:`~None`

