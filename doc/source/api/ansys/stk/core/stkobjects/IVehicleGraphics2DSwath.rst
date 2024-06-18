IVehicleGraphics2DSwath
=======================

.. py:class:: IVehicleGraphics2DSwath

   object
   
   Vehicle swath interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_elevation_type`
              - Set the elevation type.
            * - :py:meth:`~is_elevation_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~elevation_type`
            * - :py:meth:`~elevation_supported_types`
            * - :py:meth:`~elevation`
            * - :py:meth:`~options`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleGraphics2DSwath


Property detail
---------------

.. py:property:: elevation_type
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation_type
    :type: "VEHICLE_GRAPHICS_2D_ELEVATION"

    Ground elevation, swath half width or vehicle half angle.

.. py:property:: elevation_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: elevation
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.elevation
    :type: "IAgVeGfxElevation"

    Get the elevation value.

.. py:property:: options
    :canonical: ansys.stk.core.stkobjects.IVehicleGraphics2DSwath.options
    :type: "VEHICLE_GRAPHICS_2D_OPTIONS"

    Options for swath display.


Method detail
-------------


.. py:method:: set_elevation_type(self, elevation:"VEHICLE_GRAPHICS_2D_ELEVATION") -> None

    Set the elevation type.

    :Parameters:

    **elevation** : :obj:`~"VEHICLE_GRAPHICS_2D_ELEVATION"`

    :Returns:

        :obj:`~None`

.. py:method:: is_elevation_type_supported(self, elevation:"VEHICLE_GRAPHICS_2D_ELEVATION") -> bool

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **elevation** : :obj:`~"VEHICLE_GRAPHICS_2D_ELEVATION"`

    :Returns:

        :obj:`~bool`





