IModelPrimitive
===============

.. py:class:: ansys.stk.core.graphics.IModelPrimitive

   object
   
   The model primitive loads and renders `COLLADA <https://www.khronos.org/collada/>`_ (DAE) and AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) models.

.. py:currentmodule:: IModelPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IModelPrimitive.load_with_string_uri`
              - For convenience. Loads a `COLLADA <https://www.khronos.org/collada/>`_ (DAE) or AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) model using a file path.
            * - :py:attr:`~ansys.stk.core.graphics.IModelPrimitive.load_with_string_uri_and_up_axis`
              - For convenience. Loads a `COLLADA <https://www.khronos.org/collada/>`_ (DAE) or AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) model using a file path.
            * - :py:attr:`~ansys.stk.core.graphics.IModelPrimitive.set_position_cartographic`
              - For convenience. Sets the cartographic position of the model. This also sets position.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IModelPrimitive.uri_as_string`
            * - :py:attr:`~ansys.stk.core.graphics.IModelPrimitive.scale`
            * - :py:attr:`~ansys.stk.core.graphics.IModelPrimitive.position`
            * - :py:attr:`~ansys.stk.core.graphics.IModelPrimitive.orientation`
            * - :py:attr:`~ansys.stk.core.graphics.IModelPrimitive.articulations`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IModelPrimitive


Property detail
---------------

.. py:property:: uri_as_string
    :canonical: ansys.stk.core.graphics.IModelPrimitive.uri_as_string
    :type: str

    Gets the URI of the file used to load the file.

.. py:property:: scale
    :canonical: ansys.stk.core.graphics.IModelPrimitive.scale
    :type: float

    Gets or sets the linear scale used to increase or decrease the size of the rendered model.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.IModelPrimitive.position
    :type: list

    Gets or sets the position of the model. The position is defined in the model's reference frame. The array contains the components of the position in the order x, y, z.

.. py:property:: orientation
    :canonical: ansys.stk.core.graphics.IModelPrimitive.orientation
    :type: IOrientation

    Gets or sets the model's orientation. The quaternion is a rotation from the model's local axes to the axes of the model's reference frame.

.. py:property:: articulations
    :canonical: ansys.stk.core.graphics.IModelPrimitive.articulations
    :type: IModelArticulationCollection

    Gets the model's articulations. Articulations identify geometry and contain transformations for manipulating that geometry.


Method detail
-------------









.. py:method:: load_with_string_uri(self, uri: str) -> None
    :canonical: ansys.stk.core.graphics.IModelPrimitive.load_with_string_uri

    For convenience. Loads a `COLLADA <https://www.khronos.org/collada/>`_ (DAE) or AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) model using a file path.

    :Parameters:

    **uri** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_with_string_uri_and_up_axis(self, uri: str, upAxis: MODEL_UP_AXIS) -> None
    :canonical: ansys.stk.core.graphics.IModelPrimitive.load_with_string_uri_and_up_axis

    For convenience. Loads a `COLLADA <https://www.khronos.org/collada/>`_ (DAE) or AGI `MDL <https://support.agi.com/3d-models>`_ (MDL) model using a file path.

    :Parameters:

    **uri** : :obj:`~str`
    **upAxis** : :obj:`~MODEL_UP_AXIS`

    :Returns:

        :obj:`~None`

.. py:method:: set_position_cartographic(self, centralBody: str, position: list) -> None
    :canonical: ansys.stk.core.graphics.IModelPrimitive.set_position_cartographic

    For convenience. Sets the cartographic position of the model. This also sets position.

    :Parameters:

    **centralBody** : :obj:`~str`
    **position** : :obj:`~list`

    :Returns:

        :obj:`~None`

