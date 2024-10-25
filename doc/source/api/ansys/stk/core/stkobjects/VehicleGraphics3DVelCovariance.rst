VehicleGraphics3DVelCovariance
==============================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance

   3D velocity covariance ellipsoids.

.. py:currentmodule:: VehicleGraphics3DVelCovariance

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.set_attributes_type`
              - Set the velocity ellipsoid attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.scale`
              - A scale value for the velocity ellipsoid size. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.attributes_type`
              - Get the velocity ellipsoid attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.attributes_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.attributes`
              - Get the velocity ellipsoid graphics attributes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DVelCovariance


Property detail
---------------

.. py:property:: scale
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.scale
    :type: float

    A scale value for the velocity ellipsoid size. Dimensionless.

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.attributes_type
    :type: VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE

    Get the velocity ellipsoid attributes type.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.attributes
    :type: IVehicleGraphics3DAttributes

    Get the velocity ellipsoid graphics attributes.


Method detail
-------------




.. py:method:: set_attributes_type(self, attributes: VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.set_attributes_type

    Set the velocity ellipsoid attributes type.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE`

    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DVelCovariance.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_3D_ATTRIBUTE_TYPE`

    :Returns:

        :obj:`~bool`



