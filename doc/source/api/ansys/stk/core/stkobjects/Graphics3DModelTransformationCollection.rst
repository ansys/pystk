Graphics3DModelTransformationCollection
=======================================

.. py:class:: ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection

   Collection of available transformations in a model.

.. py:currentmodule:: Graphics3DModelTransformationCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection.item`
              - Return a model transformation by name or at a specified position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection.count`
              - Return a number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection._new_enum`
              - Enumerates the elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection.name`
              - Name of the Model Transformation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Graphics3DModelTransformationCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection.count
    :type: int

    Return a number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection._new_enum
    :type: EnumeratorProxy

    Enumerates the elements in the collection.

.. py:property:: name
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection.name
    :type: str

    Name of the Model Transformation.


Method detail
-------------


.. py:method:: item(self, index: int) -> Graphics3DModelTransformation
    :canonical: ansys.stk.core.stkobjects.Graphics3DModelTransformationCollection.item

    Return a model transformation by name or at a specified position.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~Graphics3DModelTransformation`



