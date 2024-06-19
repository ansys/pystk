IVehicleGraphics3DCovariance
============================

.. py:class:: IVehicleGraphics3DCovariance

   object
   
   Interface for 3D covariance ellipsoids.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_sigma_scale_type`
              - Set the sigma scale type.
            * - :py:meth:`~is_sigma_scale_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:meth:`~set_attributes_type`
              - Set the position ellipsoid attributes type.
            * - :py:meth:`~is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~sigma_scale_type`
            * - :py:meth:`~sigma_scale_supported_types`
            * - :py:meth:`~sigma_scale`
            * - :py:meth:`~attributes_type`
            * - :py:meth:`~attributes_supported_types`
            * - :py:meth:`~attributes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DCovariance


Property detail
---------------

.. py:property:: sigma_scale_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.sigma_scale_type
    :type: VEHICLE_GRAPHICS_3D_SIGMA_SCALE

    Get the sigma scale type.

.. py:property:: sigma_scale_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.sigma_scale_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: sigma_scale
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.sigma_scale
    :type: IAgVeVOSigmaScale

    Get the sigma scale.

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.attributes_type
    :type: VEHICLE_GRAPHICS_3D_ATTRIBUTES

    Get the position ellipsoid attributes type.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.attributes
    :type: IAgVeVOAttributes

    Get the position ellipsoid graphics attributes.


Method detail
-------------


.. py:method:: set_sigma_scale_type(self, sigmaScale: VEHICLE_GRAPHICS_3D_SIGMA_SCALE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.set_sigma_scale_type

    Set the sigma scale type.

    :Parameters:

    **sigmaScale** : :obj:`~VEHICLE_GRAPHICS_3D_SIGMA_SCALE`

    :Returns:

        :obj:`~None`

.. py:method:: is_sigma_scale_type_supported(self, sigmaScale: VEHICLE_GRAPHICS_3D_SIGMA_SCALE) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.is_sigma_scale_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **sigmaScale** : :obj:`~VEHICLE_GRAPHICS_3D_SIGMA_SCALE`

    :Returns:

        :obj:`~bool`




.. py:method:: set_attributes_type(self, attributes: VEHICLE_GRAPHICS_3D_ATTRIBUTES) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.set_attributes_type

    Set the position ellipsoid attributes type.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_3D_ATTRIBUTES`

    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VEHICLE_GRAPHICS_3D_ATTRIBUTES) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariance.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_3D_ATTRIBUTES`

    :Returns:

        :obj:`~bool`



