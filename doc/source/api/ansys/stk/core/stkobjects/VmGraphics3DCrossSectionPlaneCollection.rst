VmGraphics3DCrossSectionPlaneCollection
=======================================

.. py:class:: ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection

   Bases: 

   Class defining collection of cross-section planes for volumetric grid.

.. py:currentmodule:: VmGraphics3DCrossSectionPlaneCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.remove_at`
              - Remove an element from the collection using specified index.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.add`
              - Add a new plane to the collection.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.count`
              - Returns the number of elements in a collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection._NewEnum`
              - Returns an enumerator that can iterate through the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VmGraphics3DCrossSectionPlaneCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.count
    :type: int

    Returns the number of elements in a collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that can iterate through the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> VmGraphics3DCrossSectionPlane
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~VmGraphics3DCrossSectionPlane`


.. py:method:: remove_at(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.remove_at

    Remove an element from the collection using specified index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: add(self, plane: str) -> VmGraphics3DCrossSectionPlane
    :canonical: ansys.stk.core.stkobjects.VmGraphics3DCrossSectionPlaneCollection.add

    Add a new plane to the collection.

    :Parameters:

    **plane** : :obj:`~str`

    :Returns:

        :obj:`~VmGraphics3DCrossSectionPlane`

