IGraphics3DModelTransformationCollection
========================================

.. py:class:: IGraphics3DModelTransformationCollection

   object
   
   IAgVOModelTransCollection Interface. A collection of available transformations in the model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return a model transformation by name or at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~name`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGraphics3DModelTransformationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelTransformationCollection.count
    :type: int

    Returns a number of elements in the collection.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelTransformationCollection._NewEnum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelTransformationCollection.name
    :type: str

    Name of the Model Transformation.


Method detail
-------------


.. py:method:: item(self, index: int) -> IGraphics3DModelTransformation
    :canonical: ansys.stk.core.stkobjects.IGraphics3DModelTransformationCollection.item

    Return a model transformation by name or at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~IGraphics3DModelTransformation`



