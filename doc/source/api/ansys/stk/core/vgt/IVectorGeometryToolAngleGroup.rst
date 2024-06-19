IVectorGeometryToolAngleGroup
=============================

.. py:class:: IVectorGeometryToolAngleGroup

   object
   
   Access or create VGT angles associated with an object or a central body.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove`
              - Remove a specified Angle.
            * - :py:meth:`~contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:meth:`~item`
              - Return an angle by name or at a specified position.
            * - :py:meth:`~get_item_by_index`
              - Retrieve an angle from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve an angle from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~context`
            * - :py:meth:`~count`
            * - :py:meth:`~factory`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAngleGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup.context
    :type: IAgCrdnContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup.factory
    :type: IAgCrdnAngleFactory

    Returns a Factory object used to create custom angles.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, angleName: str) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup.remove

    Remove a specified Angle.

    :Parameters:

    **angleName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup.item

    Return an angle by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`


.. py:method:: get_item_by_index(self, index: int) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup.get_item_by_index

    Retrieve an angle from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`

.. py:method:: get_item_by_name(self, name: str) -> IVectorGeometryToolAngle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAngleGroup.get_item_by_name

    Retrieve an angle from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IVectorGeometryToolAngle`

