VolumetricGraphics3DSpatialCalculationLevelCollection
=====================================================

.. py:class:: ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection

   Class defining collections of defining Spatial Calculation Boundary/Fill Levels for volumetric grid.

.. py:currentmodule:: VolumetricGraphics3DSpatialCalculationLevelCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.add`
              - Add a new level to the collection. When adding a level with duplicate 'Value', it will update 'Color' and 'Translucency' values of the existing level.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VolumetricGraphics3DSpatialCalculationLevelCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, level: int) -> VolumetricGraphics3DSpatialCalculationLevel
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **level** : :obj:`~int`


    :Returns:

        :obj:`~VolumetricGraphics3DSpatialCalculationLevel`


.. py:method:: remove_at(self, level: int) -> None
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **level** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, value: float, color: agcolor.Color, translucency: float) -> VolumetricGraphics3DSpatialCalculationLevel
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DSpatialCalculationLevelCollection.add

    Add a new level to the collection. When adding a level with duplicate 'Value', it will update 'Color' and 'Translucency' values of the existing level.

    :Parameters:

        **value** : :obj:`~float`

        **color** : :obj:`~agcolor.Color`

        **translucency** : :obj:`~float`


    :Returns:

        :obj:`~VolumetricGraphics3DSpatialCalculationLevel`

