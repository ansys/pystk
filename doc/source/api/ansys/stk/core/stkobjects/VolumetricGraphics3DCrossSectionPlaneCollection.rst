VolumetricGraphics3DCrossSectionPlaneCollection
===============================================

.. py:class:: ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection

   Class defining collection of cross-section planes for volumetric grid.

.. py:currentmodule:: VolumetricGraphics3DCrossSectionPlaneCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.add`
              - Add a new plane to the collection.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.count`
              - Return the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection._new_enum`
              - Return an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VolumetricGraphics3DCrossSectionPlaneCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.count
    :type: int

    Return the number of elements in a collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VolumetricGraphics3DCrossSectionPlane
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~VolumetricGraphics3DCrossSectionPlane`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, plane: str) -> VolumetricGraphics3DCrossSectionPlane
    :canonical: ansys.stk.core.stkobjects.VolumetricGraphics3DCrossSectionPlaneCollection.add

    Add a new plane to the collection.

    :Parameters:

        **plane** : :obj:`~str`


    :Returns:

        :obj:`~VolumetricGraphics3DCrossSectionPlane`

