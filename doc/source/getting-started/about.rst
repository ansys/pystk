About
#####

PySTK is the next generation Python API for Ansys Systems Toolkit (STK). Its
main advantages and features include:

- **Remote API using gRPC**: In addition to traditional OLE communication
  with STK, the STK Python API has optional gRPC communication for
  out-of-process or remote interaction with STK.

- **Better namings:** API objects no longer have prefixes in their
  class names and methods. This improves readability, making your code easy to
  read and to maintain.

- **PyAnsys compliance:** the API integrates with the rest of the `PyAnsys`_,
  allowing users to connect STK with other Ansys products.

What's Included in the API
==========================

The following components are included in the API:

Package
-------

The STK Python API is packaged as a Python wheel file:

   **ansys_stk_core-0.1.dev0-py3-none-any.whl**

Modules
-------

The following modules are provided:

-  agi.stk.graphics
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

These limitations will be addressed in future releases of the PySTK.
