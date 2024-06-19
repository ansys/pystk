IVehicleGraphics3DCovariancePointingContour
===========================================

.. py:class:: IVehicleGraphics3DCovariancePointingContour

   object
   
   Interface for covariance pointing contours.

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
              - Set the graphics attributes type.
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
            * - :py:meth:`~is_cone_visible`
            * - :py:meth:`~size`
            * - :py:meth:`~to_object`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DCovariancePointingContour


Property detail
---------------

.. py:property:: sigma_scale_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.sigma_scale_type
    :type: VEHICLE_GRAPHICS_3D_SIGMA_SCALE

    Opt whether to size the contour indirectly by specifying a probability or directly by specifying a scale.

.. py:property:: sigma_scale_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.sigma_scale_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: sigma_scale
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.sigma_scale
    :type: IAgVeVOSigmaScale

    Get the sigma scale.

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.attributes_type
    :type: VEHICLE_GRAPHICS_3D_ATTRIBUTES

    Get the graphics attributes type.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.attributes
    :type: IAgVeVOAttributes

    Get the graphics attributes.

.. py:property:: is_cone_visible
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.is_cone_visible
    :type: bool

    Opt whether to display a cone connecting the center of the current object with the contour.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.size
    :type: IAgVeVOSize

    Get the size of the contour.

.. py:property:: to_object
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.to_object
    :type: IAgLinkToObject

    Get the 'To object' for covariance pointing.


Method detail
-------------


.. py:method:: set_sigma_scale_type(self, sigmaScale: VEHICLE_GRAPHICS_3D_SIGMA_SCALE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.set_sigma_scale_type

    Set the sigma scale type.

    :Parameters:

    **sigmaScale** : :obj:`~VEHICLE_GRAPHICS_3D_SIGMA_SCALE`

    :Returns:

        :obj:`~None`

.. py:method:: is_sigma_scale_type_supported(self, sigmaScale: VEHICLE_GRAPHICS_3D_SIGMA_SCALE) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.is_sigma_scale_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **sigmaScale** : :obj:`~VEHICLE_GRAPHICS_3D_SIGMA_SCALE`

    :Returns:

        :obj:`~bool`




.. py:method:: set_attributes_type(self, attributes: VEHICLE_GRAPHICS_3D_ATTRIBUTES) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.set_attributes_type

    Set the graphics attributes type.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_3D_ATTRIBUTES`

    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VEHICLE_GRAPHICS_3D_ATTRIBUTES) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DCovariancePointingContour.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_3D_ATTRIBUTES`

    :Returns:

        :obj:`~bool`







