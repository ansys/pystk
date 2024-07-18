ModelArticulation
=================

.. py:class:: ansys.stk.core.graphics.ModelArticulation

   Bases: 

   A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

.. py:currentmodule:: ModelArticulation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulation.item`
              - Get the transformation at the given index. The index is zero-based.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulation.get_item_by_string`
              - Get a transformation by name.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulation.get_by_name`
              - Get a transformation by name.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulation.contains`
              - Return true if the collection contains the transformation.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulation.name`
              - Gets the name of the articulation.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulation.count`
              - Gets the number of transformations in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulation._NewEnum`
              - Returns the enumerator for this collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ModelArticulation


Property detail
---------------

.. py:property:: name
    :canonical: ansys.stk.core.graphics.ModelArticulation.name
    :type: str

    Gets the name of the articulation.

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ModelArticulation.count
    :type: int

    Gets the number of transformations in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.ModelArticulation._NewEnum
    :type: EnumeratorProxy

    Returns the enumerator for this collection.


Method detail
-------------



.. py:method:: item(self, index: int) -> ModelTransformation
    :canonical: ansys.stk.core.graphics.ModelArticulation.item

    Get the transformation at the given index. The index is zero-based.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~ModelTransformation`

.. py:method:: get_item_by_string(self, name: str) -> ModelTransformation
    :canonical: ansys.stk.core.graphics.ModelArticulation.get_item_by_string

    Get a transformation by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ModelTransformation`

.. py:method:: get_by_name(self, name: str) -> ModelTransformation
    :canonical: ansys.stk.core.graphics.ModelArticulation.get_by_name

    Get a transformation by name.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~ModelTransformation`

.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.graphics.ModelArticulation.contains

    Return true if the collection contains the transformation.

    :Parameters:

    **name** : :obj:`~str`

    :Returns:

        :obj:`~bool`


