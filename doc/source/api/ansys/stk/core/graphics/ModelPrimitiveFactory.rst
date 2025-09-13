ModelPrimitiveFactory
=====================

.. py:class:: ansys.stk.core.graphics.ModelPrimitiveFactory

   The model primitive loads and renders `glTF 2.0 <https://www.khronos.org/gltf/>`_ (.gltf, .glb), `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models/>`_ (MDL) models.

.. py:currentmodule:: ModelPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitiveFactory.allow_collada_models`
              - Support for loading COLLADA 3D model format has been officially removed. This method will allow users to continue loading COLLADA models for a short period of time.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitiveFactory.initialize`
              - Initialize a default model primitive.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitiveFactory.initialize_with_string_uri`
              - For convenience. Initializes a model primitive with the specified file path.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitiveFactory.initialize_with_string_uri_and_up_axis`
              - For convenience. Initializes a model primitive with the specified file path and up axis.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ModelPrimitiveFactory



Method detail
-------------

.. py:method:: allow_collada_models(self, allow: bool) -> None
    :canonical: ansys.stk.core.graphics.ModelPrimitiveFactory.allow_collada_models

    Support for loading COLLADA 3D model format has been officially removed. This method will allow users to continue loading COLLADA models for a short period of time.

    :Parameters:

        **allow** : :obj:`~bool`


    :Returns:

        :obj:`~None`

.. py:method:: initialize(self) -> ModelPrimitive
    :canonical: ansys.stk.core.graphics.ModelPrimitiveFactory.initialize

    Initialize a default model primitive.

    :Returns:

        :obj:`~ModelPrimitive`

.. py:method:: initialize_with_string_uri(self, uri: str) -> ModelPrimitive
    :canonical: ansys.stk.core.graphics.ModelPrimitiveFactory.initialize_with_string_uri

    For convenience. Initializes a model primitive with the specified file path.

    :Parameters:

        **uri** : :obj:`~str`


    :Returns:

        :obj:`~ModelPrimitive`

.. py:method:: initialize_with_string_uri_and_up_axis(self, uri: str, up_axis: ModelUpAxis) -> ModelPrimitive
    :canonical: ansys.stk.core.graphics.ModelPrimitiveFactory.initialize_with_string_uri_and_up_axis

    For convenience. Initializes a model primitive with the specified file path and up axis.

    :Parameters:

        **uri** : :obj:`~str`

        **up_axis** : :obj:`~ModelUpAxis`


    :Returns:

        :obj:`~ModelPrimitive`

