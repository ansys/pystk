VehicleGraphics3DVelocityCovariance
===================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance

   3D velocity covariance ellipsoids.

.. py:currentmodule:: VehicleGraphics3DVelocityCovariance

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.set_attributes_type`
              - Set the velocity ellipsoid attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.scale`
              - A scale value for the velocity ellipsoid size. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes_type`
              - Get the velocity ellipsoid attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes`
              - Get the velocity ellipsoid graphics attributes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DVelocityCovariance


Property detail
---------------

.. py:property:: scale
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.scale
    :type: float

    A scale value for the velocity ellipsoid size. Dimensionless.

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes_type
    :type: VehicleGraphics3DAttributeType

    Get the velocity ellipsoid attributes type.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.attributes
    :type: IVehicleGraphics3DAttributes

    Get the velocity ellipsoid graphics attributes.


Method detail
-------------




.. py:method:: set_attributes_type(self, attributes: VehicleGraphics3DAttributeType) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.set_attributes_type

    Set the velocity ellipsoid attributes type.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics3DAttributeType`


    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VehicleGraphics3DAttributeType) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelocityCovariance.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics3DAttributeType`


    :Returns:

        :obj:`~bool`



