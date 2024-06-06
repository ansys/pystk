What's New in the STK Python API
================================

STK Python API 12.8
-------------------

To see general API updates like classes, interfaces or enumerations that
were added, changed, deprecated or removed in this release, see the
`What's New pages <..\releasenotes.htm>`__.

-  The Python API now offers a remotable option using gRPC. Options have
   been added to the agi.stk12.stkdesktop module for communicating with
   STK Desktop via gRPC, and the agi.stk12.stkruntime module has been
   added to interact with STKRuntime using gRPC.

STK Python API 12.7
-------------------

To see general API updates like classes, interfaces or enumerations that
were added, changed, deprecated or removed in this release, see the
`What's New pages <..\releasenotes.htm>`__.

-  Error handling in the IAgAttrBuilder interface was improved to check
   for null and empty strings

STK Python API 12.6
-------------------

To see general API updates like classes, interfaces or enumerations that
were added, changed, deprecated or removed in this release, see the
`What's New pages <..\releasenotes.htm>`__.

-  The following native Python plugin points have been added to STK:

   -  Ephemeris File Reader Plugin
   -  Search Plugin

-  The following new modules have been added to support the plugin
   points:

   -  agi.stk12.plugins.asplugin
   -  agi.stk12.plugins.searchplugin

-  The IAgDrDataSetCollection Python interface has been enhanced with
   the `ToNumpyArray and
   ToPandasDataFrame <pythonProgrammingGuide.htm#DataAnalysis>`__
   methods.

STK Python API 12.5
-------------------

To see general API updates like classes, interfaces or enumerations that
were added, changed, deprecated or removed in this release, see the
`What's New pages <..\releasenotes.htm>`__.

-  The following native Python plugin points have been added to STK:

   -  Density Model
   -  Drag Model
   -  EOM Function
   -  HPOP Force Model
   -  Light Reflection
   -  VGT Axes
   -  VGT Point
   -  VGT Vector
   -  Attitude Control
   -  Engine Model
   -  Radar Clutter Geometry
   -  Radar Clutter Map
   -  Radar RCS

-  The following new modules have been added to support the plugin
   points:

   -  agi.stk12.plugins.commrdrfoundation
   -  agi.stk12.plugins.stkradarplugin
   -  agi.stk12.plugins.gatorplugin
   -  agi.stk12.plugins.propagator
   -  agi.stk12.plugins.hpopplugin

STK Python API 12.4
-------------------

-  Native Python plugin points have been added to STK for Access
   Constraints and VGT Calc Scalar plugins.
-  The following new modules have been added to support the plugin
   points:

   -  agi.stk12.plugins.accessconstraintplugin
   -  agi.stk12.plugins.attrautomation
   -  agi.stk12.plugins.crdnplugin
   -  agi.stk12.plugins.stkplugin
   -  agi.stk12.plugins.utplugin

STK Python API 12.3
-------------------

No classes, interfaces or enumerations were added, changed, deprecated
or removed in this version.

STK Python API 12.2
-------------------

-  `Events are now supported. <pythonProgrammingGuide.htm#Events>`__
-  `agi.stk12.stkengine.tkcontrols module adds access to Globe, Map, and
   Gfx controls. <pythonProgrammingGuide.htm#TkinterContols>`__
-  `(Advanced Topic) Added helper methods for marshalling STK objects
   between Python
   threads. <pythonProgrammingGuide.htm#ThreadMarshalling>`__

STK Python API 12.1
-------------------

This is initial release of the STK Python API. Below is an overview of
its features:

-  No dependency on comtypes or win32com libraries.
-  IDE autocomplete (e.g. Intellisense) support for developers.
-  STK Object Model Enumerations are now class types.
-  agi.stk12.stkengine and agi.stk12.stkdesktop modules simplify how to
   initialize STK.
-  agi.stk12.utilities.colors module simplify colors in python for STK.
-  agi.stk12.utilities.exceptions module to provide better exception
   information in python for STK.
-  Cross-platform support (Windows and Linux).
