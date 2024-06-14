IModelPrimitiveFactory
======================

.. py:class:: IModelPrimitiveFactory

   object
   
   The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a default model primitive.
            * - :py:meth:`~initialize_with_string_uri`
              - For convenience. Initializes a model primitive with the specified file path.
            * - :py:meth:`~initialize_with_string_uri_and_up_axis`
              - For convenience. Initializes a model primitive with the specified file path and up axis.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IModelPrimitiveFactory



Method detail
-------------

.. py:method:: initialize(self) -> "IModelPrimitive"

    Initialize a default model primitive.

    :Returns:

        :obj:`~"IModelPrimitive"`

.. py:method:: initialize_with_string_uri(self, uri:str) -> "IModelPrimitive"

    For convenience. Initializes a model primitive with the specified file path.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~"IModelPrimitive"`

.. py:method:: initialize_with_string_uri_and_up_axis(self, uri:str, upAxis:"MODEL_UP_AXIS") -> "IModelPrimitive"

    For convenience. Initializes a model primitive with the specified file path and up axis.

    :Parameters:

    **uri** : :obj:`~str`
    **upAxis** : :obj:`~"MODEL_UP_AXIS"`

    :Returns:

        :obj:`~"IModelPrimitive"`

