VehicleGraphics3DCovariancePointingContour
==========================================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour

   Covariance pointing contours.

.. py:currentmodule:: VehicleGraphics3DCovariancePointingContour

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.set_sigma_scale_type`
              - Set the sigma scale type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.is_sigma_scale_type_supported`
              - Get a value indicating whether the specified type can be used.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.set_attributes_type`
              - Set the graphics attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.sigma_scale_type`
              - Opt whether to size the contour indirectly by specifying a probability or directly by specifying a scale.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.sigma_scale_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.sigma_scale`
              - Get the sigma scale.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.attributes_type`
              - Get the graphics attributes type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.attributes_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.attributes`
              - Get the graphics attributes.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.show_cone`
              - Opt whether to display a cone connecting the center of the current object with the contour.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.size`
              - Get the size of the contour.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.to_object`
              - Get the 'To object' for covariance pointing.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics3DCovariancePointingContour


Property detail
---------------

.. py:property:: sigma_scale_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.sigma_scale_type
    :type: VehicleGraphics3DSigmaScale

    Opt whether to size the contour indirectly by specifying a probability or directly by specifying a scale.

.. py:property:: sigma_scale_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.sigma_scale_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: sigma_scale
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.sigma_scale
    :type: IVehicleGraphics3DSigmaScale

    Get the sigma scale.

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.attributes_type
    :type: VehicleGraphics3DAttributeType

    Get the graphics attributes type.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.attributes_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.attributes
    :type: IVehicleGraphics3DAttributes

    Get the graphics attributes.

.. py:property:: show_cone
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.show_cone
    :type: bool

    Opt whether to display a cone connecting the center of the current object with the contour.

.. py:property:: size
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.size
    :type: VehicleGraphics3DSize

    Get the size of the contour.

.. py:property:: to_object
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.to_object
    :type: LinkToObject

    Get the 'To object' for covariance pointing.


Method detail
-------------


.. py:method:: set_sigma_scale_type(self, sigma_scale: VehicleGraphics3DSigmaScale) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.set_sigma_scale_type

    Set the sigma scale type.

    :Parameters:

        **sigma_scale** : :obj:`~VehicleGraphics3DSigmaScale`


    :Returns:

        :obj:`~None`

.. py:method:: is_sigma_scale_type_supported(self, sigma_scale: VehicleGraphics3DSigmaScale) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.is_sigma_scale_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **sigma_scale** : :obj:`~VehicleGraphics3DSigmaScale`


    :Returns:

        :obj:`~bool`




.. py:method:: set_attributes_type(self, attributes: VehicleGraphics3DAttributeType) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.set_attributes_type

    Set the graphics attributes type.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics3DAttributeType`


    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VehicleGraphics3DAttributeType) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics3DCovariancePointingContour.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **attributes** : :obj:`~VehicleGraphics3DAttributeType`


    :Returns:

        :obj:`~bool`







