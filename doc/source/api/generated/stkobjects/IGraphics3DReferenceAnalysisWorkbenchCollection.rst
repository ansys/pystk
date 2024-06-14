IGraphics3DReferenceAnalysisWorkbenchCollection
===============================================

.. py:class:: IGraphics3DReferenceAnalysisWorkbenchCollection

   object
   
   Manages the collection of elements that are used to visualize the Vector Geometry Tool components in 3D.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return an element of the collection at the specified position.
            * - :py:meth:`~add`
              - Add a VGT component to the collection. The path must refer to a valid VGT component. The method throws an exception if the path is invalid or if the element already exist.
            * - :py:meth:`~remove`
              - Remove an element at the specified position from the collection.
            * - :py:meth:`~remove_all`
              - Remove all elements from the collection.
            * - :py:meth:`~remove_by_name`
              - Remove an element from the collection using the element's path. The method does not throw an exception if the element with the specified name is not in the collection.
            * - :py:meth:`~get_crdn_by_name`
              - Return an element with the specified name and type. The method throws an exception if the element with the specified name does not exist.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~available_crdns`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DReferenceAnalysisWorkbenchCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates through the vector collection.

.. py:property:: available_crdns
    :canonical: ansys.stk.core.stkobjects.IGraphics3DReferenceAnalysisWorkbenchCollection.available_crdns
    :type: list

    Get a list of available VGT elements that can be added to the collection.


Method detail
-------------


.. py:method:: item(self, index:int) -> "IGraphics3DReferenceAnalysisWorkbenchComponent"

    Return an element of the collection at the specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IGraphics3DReferenceAnalysisWorkbenchComponent"`


.. py:method:: add(self, type:"GEOMETRIC_ELEM_TYPE", name:str) -> "IGraphics3DReferenceAnalysisWorkbenchComponent"

    Add a VGT component to the collection. The path must refer to a valid VGT component. The method throws an exception if the path is invalid or if the element already exist.

    :Parameters:

    **type** : :obj:`~"GEOMETRIC_ELEM_TYPE"`
    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IGraphics3DReferenceAnalysisWorkbenchComponent"`

.. py:method:: remove(self, index:int) -> None

    Remove an element at the specified position from the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_all(self) -> None

    Remove all elements from the collection.

    :Returns:

        :obj:`~None`

.. py:method:: remove_by_name(self, type:"GEOMETRIC_ELEM_TYPE", name:str) -> None

    Remove an element from the collection using the element's path. The method does not throw an exception if the element with the specified name is not in the collection.

    :Parameters:

    **type** : :obj:`~"GEOMETRIC_ELEM_TYPE"`
    **name** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: get_crdn_by_name(self, type:"GEOMETRIC_ELEM_TYPE", name:str) -> "IGraphics3DReferenceAnalysisWorkbenchComponent"

    Return an element with the specified name and type. The method throws an exception if the element with the specified name does not exist.

    :Parameters:

    **type** : :obj:`~"GEOMETRIC_ELEM_TYPE"`
    **name** : :obj:`~str`

    :Returns:

        :obj:`~"IGraphics3DReferenceAnalysisWorkbenchComponent"`

