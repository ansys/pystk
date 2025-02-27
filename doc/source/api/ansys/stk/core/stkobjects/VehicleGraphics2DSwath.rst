VehicleGraphics2DSwath
======================

.. py:class:: ansys.stk.core.stkobjects.VehicleGraphics2DSwath

   Vehicle swath.

.. py:currentmodule:: VehicleGraphics2DSwath

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DSwath.set_elevation_type`
              - Set the elevation type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DSwath.is_elevation_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DSwath.elevation_type`
              - Ground elevation, swath half width or vehicle half angle.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DSwath.elevation_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DSwath.elevation`
              - Get the elevation value.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleGraphics2DSwath.options`
              - Options for swath display.



Examples
--------

Set 2D Swath

.. code-block:: python

    # Satellitesatellite: Satellite object
    # Set swath in the 2D properties
    swath = satellite.graphics.swath
    swath.set_elevation_type(VehicleGraphics2DElevation.ELEVATION_GROUND_ELEVATION)
    swath.elevation.angle = 30  # deg
    satellite.graphics.swath.options = VehicleGraphics2DOptionType.OPTIONS_EDGE_LIMITS


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleGraphics2DSwath


Property detail
---------------

.. py:property:: elevation_type
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DSwath.elevation_type
    :type: VehicleGraphics2DElevation

    Ground elevation, swath half width or vehicle half angle.

.. py:property:: elevation_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DSwath.elevation_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: elevation
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DSwath.elevation
    :type: IVehicleGraphics2DElevation

    Get the elevation value.

.. py:property:: options
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DSwath.options
    :type: VehicleGraphics2DOptionType

    Options for swath display.


Method detail
-------------


.. py:method:: set_elevation_type(self, elevation: VehicleGraphics2DElevation) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DSwath.set_elevation_type

    Set the elevation type.

    :Parameters:

    **elevation** : :obj:`~VehicleGraphics2DElevation`

    :Returns:

        :obj:`~None`

.. py:method:: is_elevation_type_supported(self, elevation: VehicleGraphics2DElevation) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleGraphics2DSwath.is_elevation_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **elevation** : :obj:`~VehicleGraphics2DElevation`

    :Returns:

        :obj:`~bool`





