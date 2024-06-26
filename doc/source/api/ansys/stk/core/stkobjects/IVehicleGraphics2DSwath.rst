IVehicleGraphics2DSwath
=======================

.. py:class:: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath

   object
   
   Vehicle swath interface.

.. py:currentmodule:: IVehicleGraphics2DSwath

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.set_elevation_type`
              - Set the elevation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.is_elevation_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation_type`
              - Ground elevation, swath half width or vehicle half angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation`
              - Get the elevation value.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.options`
              - Options for swath display.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DSwath


Property detail
---------------

.. py:property:: elevation_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation_type
    :type: VEHICLE_GRAPHICS_2D_ELEVATION

    Ground elevation, swath half width or vehicle half angle.

.. py:property:: elevation_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: elevation
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation
    :type: IVehicleGraphics2DElevation

    Get the elevation value.

.. py:property:: options
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.options
    :type: VEHICLE_GRAPHICS_2D_OPTIONS

    Options for swath display.


Method detail
-------------


.. py:method:: set_elevation_type(self, elevation: VEHICLE_GRAPHICS_2D_ELEVATION) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.set_elevation_type

    Set the elevation type.

    :Parameters:

    **elevation** : :obj:`~VEHICLE_GRAPHICS_2D_ELEVATION`

    :Returns:

        :obj:`~None`

.. py:method:: is_elevation_type_supported(self, elevation: VEHICLE_GRAPHICS_2D_ELEVATION) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.is_elevation_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **elevation** : :obj:`~VEHICLE_GRAPHICS_2D_ELEVATION`

    :Returns:

        :obj:`~bool`





