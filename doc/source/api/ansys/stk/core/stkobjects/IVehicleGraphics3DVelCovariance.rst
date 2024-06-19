IVehicleGraphics3DVelCovariance
===============================

.. py:class:: IVehicleGraphics3DVelCovariance

   object
   
   Interface for 3D velocity covariance ellipsoids.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_attributes_type`
              - Set the velocity ellipsoid attributes type.
            * - :py:meth:`~is_attributes_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~scale`
            * - :py:meth:`~attributes_type`
            * - :py:meth:`~attributes_supported_types`
            * - :py:meth:`~attributes`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics3DVelCovariance


Property detail
---------------

.. py:property:: scale
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DVelCovariance.scale
    :type: float

    A scale value for the velocity ellipsoid size. Dimensionless.

.. py:property:: attributes_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DVelCovariance.attributes_type
    :type: VEHICLE_GRAPHICS_3D_ATTRIBUTES

    Get the velocity ellipsoid attributes type.

.. py:property:: attributes_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DVelCovariance.attributes_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: attributes
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DVelCovariance.attributes
    :type: IAgVeVOAttributes

    Get the velocity ellipsoid graphics attributes.


Method detail
-------------




.. py:method:: set_attributes_type(self, attributes: VEHICLE_GRAPHICS_3D_ATTRIBUTES) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DVelCovariance.set_attributes_type

    Set the velocity ellipsoid attributes type.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_3D_ATTRIBUTES`

    :Returns:

        :obj:`~None`

.. py:method:: is_attributes_type_supported(self, attributes: VEHICLE_GRAPHICS_3D_ATTRIBUTES) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics3DVelCovariance.is_attributes_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **attributes** : :obj:`~VEHICLE_GRAPHICS_3D_ATTRIBUTES`

    :Returns:

        :obj:`~bool`



