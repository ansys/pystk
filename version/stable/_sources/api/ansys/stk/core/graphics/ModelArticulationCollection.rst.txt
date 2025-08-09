ModelArticulationCollection
===========================

.. py:class:: ansys.stk.core.graphics.ModelArticulationCollection

   A collection containing a model primitive's available articulations. A model articulation identifies geometry on the model and is a collection of transformations that can be applied to that geometry.

.. py:currentmodule:: ModelArticulationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulationCollection.item`
              - Get the articulation at the given index. The index is zero-based.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulationCollection.get_item_by_string`
              - Get an articulation by name.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulationCollection.get_by_name`
              - Get an articulation by name.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulationCollection.contains`
              - Return true if the collection contains the articulation.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulationCollection.count`
              - Get the number of articulations in the collection.
            * - :py:attr:`~ansys.stk.core.graphics.ModelArticulationCollection._new_enum`
              - Return the enumerator for this collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ModelArticulationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.ModelArticulationCollection.count
    :type: int

    Get the number of articulations in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.ModelArticulationCollection._new_enum
    :type: EnumeratorProxy

    Return the enumerator for this collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> ModelArticulation
    :canonical: ansys.stk.core.graphics.ModelArticulationCollection.item

    Get the articulation at the given index. The index is zero-based.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~ModelArticulation`

.. py:method:: get_item_by_string(self, name: str) -> ModelArticulation
    :canonical: ansys.stk.core.graphics.ModelArticulationCollection.get_item_by_string

    Get an articulation by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ModelArticulation`

.. py:method:: get_by_name(self, name: str) -> ModelArticulation
    :canonical: ansys.stk.core.graphics.ModelArticulationCollection.get_by_name

    Get an articulation by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~ModelArticulation`

.. py:method:: contains(self, name: str) -> bool
    :canonical: ansys.stk.core.graphics.ModelArticulationCollection.contains

    Return true if the collection contains the articulation.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~bool`


