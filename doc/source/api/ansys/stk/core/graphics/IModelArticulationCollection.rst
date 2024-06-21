IModelArticulationCollection
============================

.. py:class:: ansys.stk.core.graphics.IModelArticulationCollection

   object
   
   A collection containing a model primitive's available articulations. A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

.. py:currentmodule:: IModelArticulationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IModelArticulationCollection.item`
              - Get the articulation at the given index. The index is zero-based.
            * - :py:attr:`~ansys.stk.core.graphics.IModelArticulationCollection.get_item_by_string`
              - Get an articulation by name.
            * - :py:attr:`~ansys.stk.core.graphics.IModelArticulationCollection.get_by_name`
              - Get an articulation by name.
            * - :py:attr:`~ansys.stk.core.graphics.IModelArticulationCollection.contains`
              - Return true if the collection contains the articulation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IModelArticulationCollection.count`
            * - :py:attr:`~ansys.stk.core.graphics.IModelArticulationCollection._NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IModelArticulationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IModelArticulationCollection.count
    :type: int

    Gets the number of articulations in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IModelArticulationCollection._NewEnum
    :type: EnumeratorProxy

    Returns the enumerator for this collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IModelArticulation
    :canonical: ansys.stk.core.graphics.IModelArticulationCollection.item

    Get the articulation at the given index. The index is zero-based.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IModelArticulation`

.. py:method:: get_item_by_string(self, name: str) -> IModelArticulation
    :canonical: ansys.stk.core.graphics.IModelArticulationCollection.get_item_by_string

    Get an articulation by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IModelArticulation`

.. py:method:: get_by_name(self, name: str) -> IModelArticulation
    :canonical: ansys.stk.core.graphics.IModelArticulationCollection.get_by_name

    Get an articulation by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~IModelArticulation`

.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.graphics.IModelArticulationCollection.contains

    Return true if the collection contains the articulation.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`


