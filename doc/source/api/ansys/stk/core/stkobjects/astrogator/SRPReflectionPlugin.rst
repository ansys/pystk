SRPReflectionPlugin
===================

.. py:class:: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IComponentInfo`, :py:class:`~ansys.stk.core.stkobjects.astrogator.ICloneable`

   SRP Reflection Plugin.

.. py:currentmodule:: SRPReflectionPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.plugin_identifier`
              - Get or set the plugin name.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.plugin_config`
              - Get the properties of the selected plugin.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.atmos_altitude`
              - Get or set the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.shadow_model`
              - Get or set the shadow model type.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.sun_position`
              - Get or set the sun position computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.eclipsing_bodies`
              - Other eclipsing bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.include_boundary_mitigation`
              - True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.use_sun_central_body_file_values`
              - True if solar values should come from the Sun.cb file.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.solar_radius`
              - Get the solar radius value to use in eclipse calculations.  Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import SRPReflectionPlugin


Property detail
---------------

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.plugin_identifier
    :type: str

    Get or set the plugin name.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.plugin_config
    :type: PluginProperties

    Get the properties of the selected plugin.

.. py:property:: atmos_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.atmos_altitude
    :type: float

    Get or set the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.

.. py:property:: shadow_model
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.shadow_model
    :type: ShadowModel

    Get or set the shadow model type.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.sun_position
    :type: SunPosition

    Get or set the sun position computation.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.eclipsing_bodies
    :type: CentralBodyComponentCollection

    Other eclipsing bodies.

.. py:property:: include_boundary_mitigation
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.include_boundary_mitigation
    :type: bool

    True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.

.. py:property:: use_sun_central_body_file_values
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.use_sun_central_body_file_values
    :type: bool

    True if solar values should come from the Sun.cb file.

.. py:property:: solar_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.SRPReflectionPlugin.solar_radius
    :type: float

    Get the solar radius value to use in eclipse calculations.  Uses Distance Dimension.


