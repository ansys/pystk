IModelArticulation
==================

.. py:class:: IModelArticulation

   object
   
   A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Get the transformation at the given index. The index is zero-based.
            * - :py:meth:`~get_item_by_string`
              - Get a transformation by name.
            * - :py:meth:`~get_by_name`
              - Get a transformation by name.
            * - :py:meth:`~contains`
              - Return true if the collection contains the transformation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~name`
            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IModelArticulation


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.graphics.IModelArticulation.name
    :type: str

    Gets the name of the articulation.

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IModelArticulation.count
    :type: int

    Gets the number of transformations in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IModelArticulation._NewEnum
    :type: EnumeratorProxy

    Returns the enumerator for this collection.


Method detail
-------------



.. py:method:: item(self, index:int) -> "IModelTransformation"

    Get the transformation at the given index. The index is zero-based.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IModelTransformation"`

.. py:method:: get_item_by_string(self, name:str) -> "IModelTransformation"

    Get a transformation by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IModelTransformation"`

.. py:method:: get_by_name(self, name:str) -> "IModelTransformation"

    Get a transformation by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IModelTransformation"`

.. py:method:: contains(self, name:str) -> bool

    Return true if the collection contains the transformation.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`


