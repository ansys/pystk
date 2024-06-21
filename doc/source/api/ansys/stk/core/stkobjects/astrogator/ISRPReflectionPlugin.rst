ISRPReflectionPlugin
====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin

   object
   
   Properties for the plugin SRP Refelction.

.. py:currentmodule:: ISRPReflectionPlugin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.plugin_identifier`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.plugin_config`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.atmos_altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.shadow_model`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.sun_position`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.eclipsing_bodies`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.include_boundary_mitigation`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.use_sun_central_body_file_values`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.solar_radius`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ISRPReflectionPlugin


Property detail
---------------

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.plugin_identifier
    :type: str

    Gets or sets the plugin name.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.plugin_config
    :type: IPluginProperties

    Get the properties of the selected plugin.

.. py:property:: atmos_altitude
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.atmos_altitude
    :type: float

    Gets or sets the atmospheric altitude for eclipse. A simple model to account for some measure of attenuation that simply increases the shape of the Earth by the defined altitude height, often taken to be 23 km. Uses Distance Dimension.

.. py:property:: shadow_model
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.shadow_model
    :type: SHADOW_MODEL

    Gets or sets the shadow model type.

.. py:property:: sun_position
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.sun_position
    :type: SUN_POSITION

    Gets or sets the sun position computation.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.eclipsing_bodies
    :type: ICentralBodyCollection

    Other eclipsing bodies.

.. py:property:: include_boundary_mitigation
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.include_boundary_mitigation
    :type: bool

    True if shadow boundary mitigation should be performed; the state of the satellite after crossing a shadow boundary will be corrected for errors possibly caused by the sudden change in SRP which occurred during the integration step.

.. py:property:: use_sun_central_body_file_values
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.use_sun_central_body_file_values
    :type: bool

    True if solar values should come from the Sun.cb file.

.. py:property:: solar_radius
    :canonical: ansys.stk.core.stkobjects.astrogator.ISRPReflectionPlugin.solar_radius
    :type: float

    Get the solar radius value to use in eclipse calculations.  Uses Distance Dimension.


