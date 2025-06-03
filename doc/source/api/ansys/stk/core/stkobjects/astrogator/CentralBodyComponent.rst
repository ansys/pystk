CentralBodyComponent
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   Central Body.

.. py:currentmodule:: CentralBodyComponent

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.set_default_gravity_model_by_name`
              - Select a gravity model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_gravity_model`
              - Add a central body gravity model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.remove_gravity_model_by_name`
              - Remove a central body gravity model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.set_default_shape_by_name`
              - Select a central body shape.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_shape`
              - Add a central body shape type from the available types.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.remove_shape_by_name`
              - Remove a central body shape type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.set_default_attitude_by_name`
              - Select a central body attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_attitude`
              - Add a central body attitude type from the available types.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.remove_attitude_by_name`
              - Remove a central body attitude type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.set_default_ephemeris_by_name`
              - Select an ephemeris type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_ephemeris`
              - Add an ephemeris type from the available types.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.remove_ephemeris_by_name`
              - Remove an ephemeris type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.cut_gravity_model_by_name`
              - Copy a gravity model to the clipboard and removes it from the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.copy_gravity_model_by_name`
              - Copy a gravity model to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.paste_gravity_model`
              - Add the gravity model in the clipboard to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_copy_of_gravity_model`
              - Add the gravity model to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.cut_shape_by_name`
              - Copy a central body shape to the clipboard and removes it from the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.copy_shape_by_name`
              - Copy a central body shape to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.paste_shape`
              - Add the central body shape in the clipboard to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_copy_of_shape`
              - Add the central body shape to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.cut_attitude_by_name`
              - Copy a central body attitude definition to the clipboard and removes it from the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.copy_attitude_by_name`
              - Copy a central body attitude definition to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.paste_attitude`
              - Add the central body attitude definition in the clipboard to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_copy_of_attitude`
              - Add the central body attitude definition to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.cut_ephemeris_by_name`
              - Copy a central body ephemeris definition to the clipboard and removes it from the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.copy_ephemeris_by_name`
              - Copy a central body ephemeris definition to the clipboard.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.paste_ephemeris`
              - Add the central body ephemeris definition in the clipboard to the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_copy_of_ephemeris`
              - Add the central body ephemeris definition to the central body.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.gravitational_parameter`
              - Get or set the gravitational parameter to be used. Uses Gravity Parameter Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.parent_name`
              - Get or set the parent of this central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.children`
              - Get the children of this central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_gravity_model_name`
              - Get the gravity model.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_gravity_model_data`
              - Get the gravity model parameters.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_shape_name`
              - Get the shape of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_shape_data`
              - Get the parameters of the central body shape.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_attitude_name`
              - Get the attitude of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_attitude_data`
              - Get the parameters of the central body attitude.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_ephemeris_name`
              - Get the ephemeris of the central body.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_ephemeris_data`
              - Get the parameters of the central body ephemeris.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import CentralBodyComponent


Property detail
---------------

.. py:property:: gravitational_parameter
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.gravitational_parameter
    :type: float

    Get or set the gravitational parameter to be used. Uses Gravity Parameter Dimension.

.. py:property:: parent_name
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.parent_name
    :type: str

    Get or set the parent of this central body.

.. py:property:: children
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.children
    :type: CentralBodyComponentCollection

    Get the children of this central body.

.. py:property:: default_gravity_model_name
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_gravity_model_name
    :type: str

    Get the gravity model.

.. py:property:: default_gravity_model_data
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_gravity_model_data
    :type: CentralBodyComponentGravityModel

    Get the gravity model parameters.

.. py:property:: default_shape_name
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_shape_name
    :type: str

    Get the shape of the central body.

.. py:property:: default_shape_data
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_shape_data
    :type: ICentralBodyComponentShape

    Get the parameters of the central body shape.

.. py:property:: default_attitude_name
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_attitude_name
    :type: str

    Get the attitude of the central body.

.. py:property:: default_attitude_data
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_attitude_data
    :type: ICentralBodyComponentAttitude

    Get the parameters of the central body attitude.

.. py:property:: default_ephemeris_name
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_ephemeris_name
    :type: str

    Get the ephemeris of the central body.

.. py:property:: default_ephemeris_data
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.default_ephemeris_data
    :type: ICentralBodyComponentEphemeris

    Get the parameters of the central body ephemeris.


Method detail
-------------







.. py:method:: set_default_gravity_model_by_name(self, gravity_model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.set_default_gravity_model_by_name

    Select a gravity model.

    :Parameters:

        **gravity_model_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: add_gravity_model(self, gravity_model: CentralBodyGravityModel, unique_name: str) -> CentralBodyComponentGravityModel
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_gravity_model

    Add a central body gravity model type.

    :Parameters:

        **gravity_model** : :obj:`~CentralBodyGravityModel`

        **unique_name** : :obj:`~str`


    :Returns:

        :obj:`~CentralBodyComponentGravityModel`

.. py:method:: remove_gravity_model_by_name(self, gravity_model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.remove_gravity_model_by_name

    Remove a central body gravity model type.

    :Parameters:

        **gravity_model_name** : :obj:`~str`


    :Returns:

        :obj:`~None`



.. py:method:: set_default_shape_by_name(self, shape_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.set_default_shape_by_name

    Select a central body shape.

    :Parameters:

        **shape_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: add_shape(self, shape: CentralBodyShape, unique_name: str) -> ICentralBodyComponentShape
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_shape

    Add a central body shape type from the available types.

    :Parameters:

        **shape** : :obj:`~CentralBodyShape`

        **unique_name** : :obj:`~str`


    :Returns:

        :obj:`~ICentralBodyComponentShape`

.. py:method:: remove_shape_by_name(self, shape_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.remove_shape_by_name

    Remove a central body shape type.

    :Parameters:

        **shape_name** : :obj:`~str`


    :Returns:

        :obj:`~None`



.. py:method:: set_default_attitude_by_name(self, attitude_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.set_default_attitude_by_name

    Select a central body attitude.

    :Parameters:

        **attitude_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: add_attitude(self, attitude: CentralBodyAttitude, unique_name: str) -> ICentralBodyComponentAttitude
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_attitude

    Add a central body attitude type from the available types.

    :Parameters:

        **attitude** : :obj:`~CentralBodyAttitude`

        **unique_name** : :obj:`~str`


    :Returns:

        :obj:`~ICentralBodyComponentAttitude`

.. py:method:: remove_attitude_by_name(self, attitude_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.remove_attitude_by_name

    Remove a central body attitude type.

    :Parameters:

        **attitude_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: set_default_ephemeris_by_name(self, ephemeris_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.set_default_ephemeris_by_name

    Select an ephemeris type.

    :Parameters:

        **ephemeris_name** : :obj:`~str`


    :Returns:

        :obj:`~None`


.. py:method:: add_ephemeris(self, ephemeris: CentralBodyEphemeris, unique_name: str) -> ICentralBodyComponentEphemeris
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_ephemeris

    Add an ephemeris type from the available types.

    :Parameters:

        **ephemeris** : :obj:`~CentralBodyEphemeris`

        **unique_name** : :obj:`~str`


    :Returns:

        :obj:`~ICentralBodyComponentEphemeris`

.. py:method:: remove_ephemeris_by_name(self, ephemeris_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.remove_ephemeris_by_name

    Remove an ephemeris type.

    :Parameters:

        **ephemeris_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: cut_gravity_model_by_name(self, gravity_model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.cut_gravity_model_by_name

    Copy a gravity model to the clipboard and removes it from the central body.

    :Parameters:

        **gravity_model_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: copy_gravity_model_by_name(self, gravity_model_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.copy_gravity_model_by_name

    Copy a gravity model to the clipboard.

    :Parameters:

        **gravity_model_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: paste_gravity_model(self) -> CentralBodyComponentGravityModel
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.paste_gravity_model

    Add the gravity model in the clipboard to the central body.

    :Returns:

        :obj:`~CentralBodyComponentGravityModel`

.. py:method:: add_copy_of_gravity_model(self, gravity_model: CentralBodyComponentGravityModel) -> CentralBodyComponentGravityModel
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_copy_of_gravity_model

    Add the gravity model to the central body.

    :Parameters:

        **gravity_model** : :obj:`~CentralBodyComponentGravityModel`


    :Returns:

        :obj:`~CentralBodyComponentGravityModel`

.. py:method:: cut_shape_by_name(self, shape_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.cut_shape_by_name

    Copy a central body shape to the clipboard and removes it from the central body.

    :Parameters:

        **shape_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: copy_shape_by_name(self, shape_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.copy_shape_by_name

    Copy a central body shape to the clipboard.

    :Parameters:

        **shape_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: paste_shape(self) -> ICentralBodyComponentShape
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.paste_shape

    Add the central body shape in the clipboard to the central body.

    :Returns:

        :obj:`~ICentralBodyComponentShape`

.. py:method:: add_copy_of_shape(self, shape: ICentralBodyComponentShape) -> ICentralBodyComponentShape
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_copy_of_shape

    Add the central body shape to the central body.

    :Parameters:

        **shape** : :obj:`~ICentralBodyComponentShape`


    :Returns:

        :obj:`~ICentralBodyComponentShape`

.. py:method:: cut_attitude_by_name(self, attitude_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.cut_attitude_by_name

    Copy a central body attitude definition to the clipboard and removes it from the central body.

    :Parameters:

        **attitude_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: copy_attitude_by_name(self, attitude_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.copy_attitude_by_name

    Copy a central body attitude definition to the clipboard.

    :Parameters:

        **attitude_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: paste_attitude(self) -> ICentralBodyComponentAttitude
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.paste_attitude

    Add the central body attitude definition in the clipboard to the central body.

    :Returns:

        :obj:`~ICentralBodyComponentAttitude`

.. py:method:: add_copy_of_attitude(self, attitude: ICentralBodyComponentAttitude) -> ICentralBodyComponentAttitude
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_copy_of_attitude

    Add the central body attitude definition to the central body.

    :Parameters:

        **attitude** : :obj:`~ICentralBodyComponentAttitude`


    :Returns:

        :obj:`~ICentralBodyComponentAttitude`

.. py:method:: cut_ephemeris_by_name(self, ephemeris_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.cut_ephemeris_by_name

    Copy a central body ephemeris definition to the clipboard and removes it from the central body.

    :Parameters:

        **ephemeris_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: copy_ephemeris_by_name(self, ephemeris_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.copy_ephemeris_by_name

    Copy a central body ephemeris definition to the clipboard.

    :Parameters:

        **ephemeris_name** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: paste_ephemeris(self) -> ICentralBodyComponentEphemeris
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.paste_ephemeris

    Add the central body ephemeris definition in the clipboard to the central body.

    :Returns:

        :obj:`~ICentralBodyComponentEphemeris`

.. py:method:: add_copy_of_ephemeris(self, ephemeris: ICentralBodyComponentEphemeris) -> ICentralBodyComponentEphemeris
    :canonical: ansys.stk.core.stkobjects.astrogator.CentralBodyComponent.add_copy_of_ephemeris

    Add the central body ephemeris definition to the central body.

    :Parameters:

        **ephemeris** : :obj:`~ICentralBodyComponentEphemeris`


    :Returns:

        :obj:`~ICentralBodyComponentEphemeris`

