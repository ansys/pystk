ISpatialAnalysisToolVolumeGroup
===============================

.. py:class:: ISpatialAnalysisToolVolumeGroup

   object
   
   Access or create spatial conditions associated with a volume grid.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~remove`
              - Remove a specified element.
            * - :py:meth:`~contains`
              - Search for a an element with a given name. Returns false if the specified element does not exist.
            * - :py:meth:`~item`
              - Return an element by name or at a specified position.
            * - :py:meth:`~get_item_by_index`
              - Retrieve an volume from the collection by index.
            * - :py:meth:`~get_item_by_name`
              - Retrieve volume from the collection by name.

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

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeGroup


Property detail
---------------

.. py:property:: context
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGroup.context
    :type: "IAgCrdnContext"

    Returns a context object. The context can be used to find out which central body or STK object this instance is associated with.

.. py:property:: count
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGroup.count
    :type: int

    Returns a number of elements in the group.

.. py:property:: factory
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGroup.factory
    :type: "IAgCrdnVolumeFactory"

    Returns a factory object used to create spatial condition components.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeGroup._NewEnum
    :type: EnumeratorProxy

    Returns a COM enumerator.


Method detail
-------------

.. py:method:: remove(self, eventName:str) -> None

    Remove a specified element.

    :Parameters:

    **eventName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: contains(self, name:str) -> bool

    Search for a an element with a given name. Returns false if the specified element does not exist.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: item(self, indexOrName:typing.Any) -> "ISpatialAnalysisToolVolume"

    Return an element by name or at a specified position.

    :Parameters:

    **indexOrName** : :obj:`~typing.Any`

    :Returns:

        :obj:`~"ISpatialAnalysisToolVolume"`


.. py:method:: get_item_by_index(self, index:int) -> "ISpatialAnalysisToolVolume"

    Retrieve an volume from the collection by index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"ISpatialAnalysisToolVolume"`

.. py:method:: get_item_by_name(self, name:str) -> "ISpatialAnalysisToolVolume"

    Retrieve volume from the collection by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"ISpatialAnalysisToolVolume"`

