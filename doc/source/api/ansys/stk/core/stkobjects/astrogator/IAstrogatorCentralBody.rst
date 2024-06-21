IAstrogatorCentralBody
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody

   object
   
   General properties for a central body.

.. py:currentmodule:: IAstrogatorCentralBody

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.set_default_gravity_model_by_name`
              - Select a gravity model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_gravity_model`
              - Add a central body gravity model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.remove_gravity_model_by_name`
              - Remove a central body gravity model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.set_default_shape_by_name`
              - Select a central body shape.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_shape`
              - Add a central body shape type from the available types.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.remove_shape_by_name`
              - Remove a central body shape type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.set_default_attitude_by_name`
              - Select a central body attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_attitude`
              - Add a central body attitude type from the available types.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.remove_attitude_by_name`
              - Remove a central body attitude type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.set_default_ephemeris_by_name`
              - Select an ephemeris type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_ephemeris`
              - Add an ephemeris type from the available types.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.remove_ephemeris_by_name`
              - Remove an ephemeris type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.cut_gravity_model_by_name`
              - Copy a gravity model to the clipboard and removes it from the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.copy_gravity_model_by_name`
              - Copy a gravity model to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.paste_gravity_model`
              - Add the gravity model in the clipboard to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_copy_of_gravity_model`
              - Add the gravity model to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.cut_shape_by_name`
              - Copy a central body shape to the clipboard and removes it from the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.copy_shape_by_name`
              - Copy a central body shape to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.paste_shape`
              - Add the central body shape in the clipboard to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_copy_of_shape`
              - Add the central body shape to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.cut_attitude_by_name`
              - Copy a central body attitude definition to the clipboard and removes it from the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.copy_attitude_by_name`
              - Copy a central body attitude definition to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.paste_attitude`
              - Add the central body attitude definition in the clipboard to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_copy_of_attitude`
              - Add the central body attitude definition to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.cut_ephemeris_by_name`
              - Copy a central body ephemeris definition to the clipboard and removes it from the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.copy_ephemeris_by_name`
              - Copy a central body ephemeris definition to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.paste_ephemeris`
              - Add the central body ephemeris definition in the clipboard to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_copy_of_ephemeris`
              - Add the central body ephemeris definition to the central body.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.gravitational_param`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.parent_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.children`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_gravity_model_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_gravity_model_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_shape_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_shape_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_attitude_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_attitude_data`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_ephemeris_name`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_ephemeris_data`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IAstrogatorCentralBody


Property detail
---------------

.. py:property:: gravitational_param
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.gravitational_param
    :type: float

    Gets or sets the gravitational parameter to be used. Uses Gravity Parameter Dimension.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.parent_name
    :type: str

    Gets or sets the parent of this central body.

.. py:property:: children
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.children
    :type: ICentralBodyCollection

    Get the children of this central body.

.. py:property:: default_gravity_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_gravity_model_name
    :type: str

    Get the gravity model.

.. py:property:: default_gravity_model_data
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_gravity_model_data
    :type: ICentralBodyGravityModel

    Get the gravity model parameters.

.. py:property:: default_shape_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_shape_name
    :type: str

    Get the shape of the central body.

.. py:property:: default_shape_data
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_shape_data
    :type: ICentralBodyShape

    Get the parameters of the central body shape.

.. py:property:: default_attitude_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_attitude_name
    :type: str

    Get the attitude of the central body.

.. py:property:: default_attitude_data
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_attitude_data
    :type: ICentralBodyAttitude

    Get the parameters of the central body attitude.

.. py:property:: default_ephemeris_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_ephemeris_name
    :type: str

    Get the ephemeris of the central body.

.. py:property:: default_ephemeris_data
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.default_ephemeris_data
    :type: ICentralBodyEphemeris

    Get the parameters of the central body ephemeris.


Method detail
-------------







.. py:method:: set_default_gravity_model_by_name(self, gravityModelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.set_default_gravity_model_by_name

    Select a gravity model.

    :Parameters:

    **gravityModelName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: add_gravity_model(self, eGravityModel: CENTRAL_BODY_GRAVITY_MODEL, uniqueName: str) -> ICentralBodyGravityModel
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_gravity_model

    Add a central body gravity model type.

    :Parameters:

    **eGravityModel** : :obj:`~CENTRAL_BODY_GRAVITY_MODEL`
    **uniqueName** : :obj:`~str`

    :Returns:

        :obj:`~ICentralBodyGravityModel`

.. py:method:: remove_gravity_model_by_name(self, gravityModelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.remove_gravity_model_by_name

    Remove a central body gravity model type.

    :Parameters:

    **gravityModelName** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_default_shape_by_name(self, shapeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.set_default_shape_by_name

    Select a central body shape.

    :Parameters:

    **shapeName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_shape(self, eShape: CENTRAL_BODY_SHAPE, uniqueName: str) -> ICentralBodyShape
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_shape

    Add a central body shape type from the available types.

    :Parameters:

    **eShape** : :obj:`~CENTRAL_BODY_SHAPE`
    **uniqueName** : :obj:`~str`

    :Returns:

        :obj:`~ICentralBodyShape`

.. py:method:: remove_shape_by_name(self, shapeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.remove_shape_by_name

    Remove a central body shape type.

    :Parameters:

    **shapeName** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: set_default_attitude_by_name(self, attitudeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.set_default_attitude_by_name

    Select a central body attitude.

    :Parameters:

    **attitudeName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: add_attitude(self, eAttitude: CENTRAL_BODY_ATTITUDE, uniqueName: str) -> ICentralBodyAttitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_attitude

    Add a central body attitude type from the available types.

    :Parameters:

    **eAttitude** : :obj:`~CENTRAL_BODY_ATTITUDE`
    **uniqueName** : :obj:`~str`

    :Returns:

        :obj:`~ICentralBodyAttitude`

.. py:method:: remove_attitude_by_name(self, attitudeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.remove_attitude_by_name

    Remove a central body attitude type.

    :Parameters:

    **attitudeName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: set_default_ephemeris_by_name(self, ephemerisName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.set_default_ephemeris_by_name

    Select an ephemeris type.

    :Parameters:

    **ephemerisName** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: add_ephemeris(self, eEphemeris: CENTRAL_BODY_EPHEMERIS, uniqueName: str) -> ICentralBodyEphemeris
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_ephemeris

    Add an ephemeris type from the available types.

    :Parameters:

    **eEphemeris** : :obj:`~CENTRAL_BODY_EPHEMERIS`
    **uniqueName** : :obj:`~str`

    :Returns:

        :obj:`~ICentralBodyEphemeris`

.. py:method:: remove_ephemeris_by_name(self, ephemerisName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.remove_ephemeris_by_name

    Remove an ephemeris type.

    :Parameters:

    **ephemerisName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: cut_gravity_model_by_name(self, gravityModelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.cut_gravity_model_by_name

    Copy a gravity model to the clipboard and removes it from the central body.

    :Parameters:

    **gravityModelName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_gravity_model_by_name(self, gravityModelName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.copy_gravity_model_by_name

    Copy a gravity model to the clipboard.

    :Parameters:

    **gravityModelName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: paste_gravity_model(self) -> ICentralBodyGravityModel
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.paste_gravity_model

    Add the gravity model in the clipboard to the central body.

    :Returns:

        :obj:`~ICentralBodyGravityModel`

.. py:method:: add_copy_of_gravity_model(self, gravityModel: ICentralBodyGravityModel) -> ICentralBodyGravityModel
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_copy_of_gravity_model

    Add the gravity model to the central body.

    :Parameters:

    **gravityModel** : :obj:`~ICentralBodyGravityModel`

    :Returns:

        :obj:`~ICentralBodyGravityModel`

.. py:method:: cut_shape_by_name(self, shapeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.cut_shape_by_name

    Copy a central body shape to the clipboard and removes it from the central body.

    :Parameters:

    **shapeName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_shape_by_name(self, shapeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.copy_shape_by_name

    Copy a central body shape to the clipboard.

    :Parameters:

    **shapeName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: paste_shape(self) -> ICentralBodyShape
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.paste_shape

    Add the central body shape in the clipboard to the central body.

    :Returns:

        :obj:`~ICentralBodyShape`

.. py:method:: add_copy_of_shape(self, shape: ICentralBodyShape) -> ICentralBodyShape
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_copy_of_shape

    Add the central body shape to the central body.

    :Parameters:

    **shape** : :obj:`~ICentralBodyShape`

    :Returns:

        :obj:`~ICentralBodyShape`

.. py:method:: cut_attitude_by_name(self, attitudeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.cut_attitude_by_name

    Copy a central body attitude definition to the clipboard and removes it from the central body.

    :Parameters:

    **attitudeName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_attitude_by_name(self, attitudeName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.copy_attitude_by_name

    Copy a central body attitude definition to the clipboard.

    :Parameters:

    **attitudeName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: paste_attitude(self) -> ICentralBodyAttitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.paste_attitude

    Add the central body attitude definition in the clipboard to the central body.

    :Returns:

        :obj:`~ICentralBodyAttitude`

.. py:method:: add_copy_of_attitude(self, attitude: ICentralBodyAttitude) -> ICentralBodyAttitude
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_copy_of_attitude

    Add the central body attitude definition to the central body.

    :Parameters:

    **attitude** : :obj:`~ICentralBodyAttitude`

    :Returns:

        :obj:`~ICentralBodyAttitude`

.. py:method:: cut_ephemeris_by_name(self, ephemerisName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.cut_ephemeris_by_name

    Copy a central body ephemeris definition to the clipboard and removes it from the central body.

    :Parameters:

    **ephemerisName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: copy_ephemeris_by_name(self, ephemerisName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.copy_ephemeris_by_name

    Copy a central body ephemeris definition to the clipboard.

    :Parameters:

    **ephemerisName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: paste_ephemeris(self) -> ICentralBodyEphemeris
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.paste_ephemeris

    Add the central body ephemeris definition in the clipboard to the central body.

    :Returns:

        :obj:`~ICentralBodyEphemeris`

.. py:method:: add_copy_of_ephemeris(self, ephemeris: ICentralBodyEphemeris) -> ICentralBodyEphemeris
    :canonical: ansys.stk.core.stkobjects.astrogator.IAstrogatorCentralBody.add_copy_of_ephemeris

    Add the central body ephemeris definition to the central body.

    :Parameters:

    **ephemeris** : :obj:`~ICentralBodyEphemeris`

    :Returns:

        :obj:`~ICentralBodyEphemeris`

