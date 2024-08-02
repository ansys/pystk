SpatialAnalysisToolVolumeCalcGroup
==================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup

   Access or create VGT volume calc associated with an object or a central body.

.. py:currentmodule:: SpatialAnalysisToolVolumeCalcGroup

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.remove`
              - Remove a specified element.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.item`
              - Return an element by name or at a specified position.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.get_item_by_index`
              - Retrieve a volume calculation from the collection by index.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.get_item_by_name`
              - Retrieve a volume calculation from the collection by name.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.context`
              - Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.count`
              - Returns a number of elements in the group.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.factory`
              - Returns a factory object used to create volume calc components.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup._NewEnum`
              - Returns a COM enumerator.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeCalcGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.context
    :type: IAnalysisWorkbenchContext

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.factory
    :type: SpatialAnalysisToolVolumeCalcFactory

    Returns a factory object used to create volume calc components.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, eventName: str) -> None
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.remove

    Remove a specified element.

    :Parameters:

    **eventName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.contains

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName: typing.Any) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.item

    Return an element by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`


.. py:method:: get_item_by_index(self, index: int) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.get_item_by_index

    Retrieve a volume calculation from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

.. py:method:: get_item_by_name(self, name: str) -> ISpatialAnalysisToolVolumeCalc
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcGroup.get_item_by_name

    Retrieve a volume calculation from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ISpatialAnalysisToolVolumeCalc`

