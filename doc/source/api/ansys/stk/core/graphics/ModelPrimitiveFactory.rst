ModelPrimitiveFactory
=====================

.. py:class:: ansys.stk.core.graphics.ModelPrimitiveFactory

   The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

.. py:currentmodule:: ModelPrimitiveFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

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

.. py:method:: initialize_with_string_uri_and_up_axis(self, uri: str, up_axis: MODEL_UP_AXIS) -> ModelPrimitive
    :canonical: ansys.stk.core.graphics.ModelPrimitiveFactory.initialize_with_string_uri_and_up_axis

    For convenience. Initializes a model primitive with the specified file path and up axis.

    :Parameters:

    **uri** : :obj:`~str`
    **up_axis** : :obj:`~MODEL_UP_AXIS`

    :Returns:

        :obj:`~ModelPrimitive`

