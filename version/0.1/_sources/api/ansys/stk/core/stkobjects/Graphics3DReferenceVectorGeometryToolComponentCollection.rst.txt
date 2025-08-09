Graphics3DReferenceVectorGeometryToolComponentCollection
========================================================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection

   Collection of reference vectors, axes, points, planes and angles (3D Graphics, Vector Geometry Tool).

.. py:currentmodule:: Graphics3DReferenceVectorGeometryToolComponentCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.item`
              - Return an element of the collection at the specified position.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.add`
              - Add a VGT component to the collection. The path must refer to a valid VGT component. The method throws an exception if the path is invalid or if the element already exist.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.remove`
              - Remove an element at the specified position from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.remove_all`
              - Remove all elements from the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.remove_by_name`
              - Remove an element from the collection using the element's path. The method does not throw an exception if the element with the specified name is not in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.get_component_by_name`
              - Return an element with the specified name and type. The method throws an exception if the element with the specified name does not exist.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection._new_enum`
              - Enumerates through the vector collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.available_vector_geometry_tool_components`
              - Get a list of available VGT elements that can be added to the collection.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DReferenceVectorGeometryToolComponentCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection._new_enum
    :type: EnumeratorProxy

    Enumerates through the vector collection.

.. py:property:: available_vector_geometry_tool_components
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.available_vector_geometry_tool_components
    :type: list

    Get a list of available VGT elements that can be added to the collection.


Method detail
-------------


.. py:method:: item(self, index: int) -> IGraphics3DReferenceAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.item

    Return an element of the collection at the specified position.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IGraphics3DReferenceAnalysisWorkbenchComponent`


.. py:method:: add(self, type: GeometricElementType, name: str) -> IGraphics3DReferenceAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.add

    Add a VGT component to the collection. The path must refer to a valid VGT component. The method throws an exception if the path is invalid or if the element already exist.

    :Parameters:

        **type** : :obj:`~GeometricElementType`

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IGraphics3DReferenceAnalysisWorkbenchComponent`

.. py:method:: remove(self, index: int) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.remove

    Remove an element at the specified position from the collection.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.remove_all

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_by_name(self, type: GeometricElementType, name: str) -> None
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.remove_by_name

    Remove an element from the collection using the element's path. The method does not throw an exception if the element with the specified name is not in the collection.

    :Parameters:

        **type** : :obj:`~GeometricElementType`

        **name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: get_component_by_name(self, type: GeometricElementType, name: str) -> IGraphics3DReferenceAnalysisWorkbenchComponent
    :canonical: ansys.stk.core.stkobjects.Graphics3DReferenceVectorGeometryToolComponentCollection.get_component_by_name

    Return an element with the specified name and type. The method throws an exception if the element with the specified name does not exist.

    :Parameters:

        **type** : :obj:`~GeometricElementType`

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IGraphics3DReferenceAnalysisWorkbenchComponent`

