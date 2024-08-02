Graphics3DReferenceAnalysisWorkbenchCollection
==============================================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection

   Collection of reference vectors, axes, points, planes and angles (3D Graphics, Vector Geometry Tool).

.. py:currentmodule:: Graphics3DReferenceAnalysisWorkbenchCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.item`
              - Return an element of the collection at the specified position.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.add`
              - Add a VGT component to the collection. The path must refer to a valid VGT component. The method throws an exception if the path is invalid or if the element already exist.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.remove`
              - Remove an element at the specified position from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.remove_by_name`
              - Remove an element from the collection using the element's path. The method does not throw an exception if the element with the specified name is not in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.get_crdn_by_name`
              - Return an element with the specified name and type. The method throws an exception if the element with the specified name does not exist.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.count`
              - Returns a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection._NewEnum`
              - Enumerates through the vector collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.available_crdns`
              - Get a list of available VGT elements that can be added to the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DReferenceAnalysisWorkbenchCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the vector collection.

.. py:property:: available_crdns
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.available_crdns
    :type: list

    Get a list of available VGT elements that can be added to the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IGraphics3DReferenceAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.item

    Return an element of the collection at the specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IGraphics3DReferenceAnalysisWorkbenchComponent`


.. py:method:: add(self, type: GEOMETRIC_ELEM_TYPE, name: str) -> IGraphics3DReferenceAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.add

    Add a VGT component to the collection. The path must refer to a valid VGT component. The method throws an exception if the path is invalid or if the element already exist.

    :Parameters:

    **type** : :obj:`~GEOMETRIC_ELEM_TYPE`
    **name** : :obj:`~str`

    :Returns:

        :obj:`~IGraphics3DReferenceAnalysisWorkbenchComponent`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.remove

    Remove an element at the specified position from the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_by_name(self, type: GEOMETRIC_ELEM_TYPE, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.remove_by_name

    Remove an element from the collection using the element's path. The method does not throw an exception if the element with the specified name is not in the collection.

    :Parameters:

    **type** : :obj:`~GEOMETRIC_ELEM_TYPE`
    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: get_crdn_by_name(self, type: GEOMETRIC_ELEM_TYPE, name: str) -> IGraphics3DReferenceAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceAnalysisWorkbenchCollection.get_crdn_by_name

    Return an element with the specified name and type. The method throws an exception if the element with the specified name does not exist.

    :Parameters:

    **type** : :obj:`~GEOMETRIC_ELEM_TYPE`
    **name** : :obj:`~str`

    :Returns:

        :obj:`~IGraphics3DReferenceAnalysisWorkbenchComponent`

