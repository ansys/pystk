What's Included in the API
==========================

The following components are included in the API:

Package
-------

The STK Python API is packaged as a Python wheel file:

   **agi.stk--py3-none-any.whl**

Modules
-------

The following modules are provided:

-  agi.stk.graphics
-  agi.stk.plugins.accessconstraintplugin
-  agi.stk.plugins.attrautomation
-  agi.stk.plugins.commrdrfoundation
-  agi.stk.plugins.crdnplugin
-  agi.stk.plugins.gatorplugin
-  agi.stk.plugins.hpopplugin
-  agi.stk.plugins.propagator
-  agi.stk.plugins.stkplugin
-  agi.stk.plugins.stkradarplugin
-  agi.stk.plugins.utplugin
-  agi.stk.plugins.asplugin
-  agi.stk.plugins.searchplugin
-  agi.stk.stkdesktop
-  agi.stk.stkengine
-  agi.stk.stkengine.tkcontrols
-  agi.stk.stkruntime
-  agi.stk.stkobjects
-  agi.stk.stkobjects.astrogator
-  agi.stk.stkobjects.aviator
-  agi.stk.stkobjects.aviator.matlab
-  agi.stk.stkutil
-  agi.stk.stkx
-  agi.stk.uiapplication
-  agi.stk.uicore
-  agi.stk.vgt
-  agi.stk.utilities.colors
-  agi.stk.utilities.exceptions
-  agi.stk.utilities.comobject

Limitations
-----------

The STK Python API currently has the following limitations:

-  UI plugins are not currently supported.
-  Enabling socket connection by setting the
   IAgSTKXApplication.EnableConnect to True is not currently supported.
   Connect commands may be used through the object model root
   ExecuteCommand method.
-  When using gRPC, GetRawPluginObject (available on
   IAgAccessCnstrPluginMinMax and IAgVePluginPropagator) and
   RawPluginObject (available on IAgScatteringPointProviderPlugin,
   IAgScatterPointModelPlugin, IAgRadarClutterGeometryModelPlugin,
   IAgRadarProbabilityOfDetectionPlugin, IAgRadarClutterMapModelPlugin,
   IAgRadarCrossSectionComputeStrategyPlugin, and
   IAgRadarStcAttenuationPlugin) are not available and will always
   return None.

These limitations will be addressed in future releases of the API.
