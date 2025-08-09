ModelPrimitive
==============

.. py:class:: ansys.stk.core.graphics.ModelPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

.. py:currentmodule:: ModelPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitive.load_with_string_uri`
              - For convenience. Loads a `COLLADA <https://www.khronos.org/collada/>`_ (DAE) or AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) model using a file path.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitive.load_with_string_uri_and_up_axis`
              - For convenience. Loads a `COLLADA <https://www.khronos.org/collada/>`_ (DAE) or AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) model using a file path.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitive.set_position_cartographic`
              - For convenience. Sets the cartographic position of the model. This also sets position.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitive.uri_as_string`
              - Get the URI of the file used to load the file.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitive.scale`
              - Get or set the linear scale used to increase or decrease the size of the rendered model.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitive.position`
              - Get or set the position of the model. The position is defined in the model's reference frame. The array contains the components of the position in the order x, y, z.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitive.orientation`
              - Get or set the model's orientation. The quaternion is a rotation from the model's local axes to the axes of the model's reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.ModelPrimitive.articulations`
              - Get the model's articulations. Articulations identify geometry and contain transformations for manipulating that geometry.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ModelPrimitive


Property detail
---------------

.. py:property:: uri_as_string
    :canonical: ansys.stk.core.graphics.ModelPrimitive.uri_as_string
    :type: str

    Get the URI of the file used to load the file.

.. py:property:: scale
    :canonical: ansys.stk.core.graphics.ModelPrimitive.scale
    :type: float

    Get or set the linear scale used to increase or decrease the size of the rendered model.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.ModelPrimitive.position
    :type: list

    Get or set the position of the model. The position is defined in the model's reference frame. The array contains the components of the position in the order x, y, z.

.. py:property:: orientation
    :canonical: ansys.stk.core.graphics.ModelPrimitive.orientation
    :type: IOrientation

    Get or set the model's orientation. The quaternion is a rotation from the model's local axes to the axes of the model's reference frame.

.. py:property:: articulations
    :canonical: ansys.stk.core.graphics.ModelPrimitive.articulations
    :type: ModelArticulationCollection

    Get the model's articulations. Articulations identify geometry and contain transformations for manipulating that geometry.


Method detail
-------------









.. py:method:: load_with_string_uri(self, uri: str) -> None
    :canonical: ansys.stk.core.graphics.ModelPrimitive.load_with_string_uri

    For convenience. Loads a `COLLADA <https://www.khronos.org/collada/>`_ (DAE) or AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) model using a file path.

    :Parameters:

        **uri** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: load_with_string_uri_and_up_axis(self, uri: str, up_axis: ModelUpAxis) -> None
    :canonical: ansys.stk.core.graphics.ModelPrimitive.load_with_string_uri_and_up_axis

    For convenience. Loads a `COLLADA <https://www.khronos.org/collada/>`_ (DAE) or AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) model using a file path.

    :Parameters:

        **uri** : :obj:`~str`

        **up_axis** : :obj:`~ModelUpAxis`


    :Returns:

        :obj:`~None`

.. py:method:: set_position_cartographic(self, central_body: str, position: list) -> None
    :canonical: ansys.stk.core.graphics.ModelPrimitive.set_position_cartographic

    For convenience. Sets the cartographic position of the model. This also sets position.

    :Parameters:

        **central_body** : :obj:`~str`

        **position** : :obj:`~list`


    :Returns:

        :obj:`~None`

