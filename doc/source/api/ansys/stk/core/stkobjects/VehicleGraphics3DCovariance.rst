VehicleGraphics3DCovariance
===========================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance

   3D position covariance ellipsoids.

.. py:currentmodule:: VehicleGraphics3DCovariance

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.set_sigma_scale_type`
              - Set the sigma scale type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.is_sigma_scale_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.set_attributes_type`
              - Set the position ellipsoid attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.sigma_scale_type`
              - Get the sigma scale type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.sigma_scale_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.sigma_scale`
              - Get the sigma scale.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.attributes_type`
              - Get the position ellipsoid attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.attributes_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.attributes`
              - Get the position ellipsoid graphics attributes.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DCovariance


Property detail
---------------

.. py:property:: sigma_scale_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.sigma_scale_type
    :type: VehicleGraphics3DSigmaScale

    Get the sigma scale type.

.. py:property:: sigma_scale_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.sigma_scale_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: sigma_scale
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.sigma_scale
    :type: IVehicleGraphics3DSigmaScale

    Get the sigma scale.

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.attributes_type
    :type: VehicleGraphics3DAttributeType

    Get the position ellipsoid attributes type.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.attributes_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.attributes
    :type: IVehicleGraphics3DAttributes

    Get the position ellipsoid graphics attributes.


Method detail
-------------


.. py:method:: set_sigma_scale_type(self, sigma_scale: VehicleGraphics3DSigmaScale) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.set_sigma_scale_type

    Set the sigma scale type.

    :Parameters:

        **sigma_scale** : :obj:`~VehicleGraphics3DSigmaScale`


    :Returns:

        :obj:`~None`

.. py:method:: is_sigma_scale_type_supported(self, sigma_scale: VehicleGraphics3DSigmaScale) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.is_sigma_scale_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **sigma_scale** : :obj:`~VehicleGraphics3DSigmaScale`


    :Returns:

        :obj:`~bool`




.. py:method:: set_attributes_type(self, attributes: VehicleGraphics3DAttributeType) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.set_attributes_type

    Set the position ellipsoid attributes type.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics3DAttributeType`


    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VehicleGraphics3DAttributeType) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariance.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics3DAttributeType`


    :Returns:

        :obj:`~bool`



