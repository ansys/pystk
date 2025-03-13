Initialization
##############
This topic explains how to perform the necessary steps to establish a connection with and prepare PySTK for usage with STK application interfaces and runnable programs.

Configurations
==============

To get started, determine the configuration that you want to use:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - **Configuration**
      - **Available options**
    * - Windows
      - STK Desktop, STK Engine, STK Engine NoGraphics, STKRuntime
    * - Linux
      - STK Engine, STK Engine NoGraphics, STKRuntime
    * - Jupyter Notebook with 3D and 2D widgets
      - STK Engine


Initialize PySTK with STK Desktop
===================================

This section describes how to use PySTK with STK Desktop. The :py:method:`ansys.stk.core.stkdesktop.STKDesktop.start_application` and :py:method`ansys.stk.core.stkdesktop.STKDesktop.attach_to_application` methods are available to obtain the :py:class:`ansys.stk.core.stkdesktop.STKDesktopApplication` class and begin interacting with STK through the AgUiApplication API. From the application interface, the most common way to begin working with STK is to use the :py:class:`ansys.stk.core.stkobjects.StkObjectRoot` class, which is accessible as the Root property of the :py:class:`ansys.stk.core.stkdesktop.STKDesktopApplication` object.

Start a new STK Desktop instance
--------------------------------

Use the STKDesktop.StartApplication method to start a new STK application session. The StartApplication method has optional arguments as a convenience to set commonly used properties:

*INSERT TABLE*
Argument | Description

.. literalinclude:: /../../tests/doc_snippets_tests/initialization/initialization_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def CreateSTKNewSnippet
  :end-at: stk.shutdown()
  :dedent:


Attach to a running STK instance
--------------------------------

Use the :py:method:`ansys.stk.core.stkdesktop.STKDesktop.attach_to_application` method to attach to a running STK desktop application. The AttachToApplication method has additional arguments to specify the Process ID (PID) if more than one STK application is running:

*INSERT TABLE*
Argument | Description



Initialize STKEngine NoGraphics
================================

If your use case consists of using STK Engine as a computational tool and does not require 2D/3D visualization (for instance, if your application is running as a service on a compute node without direct user interaction), using the `no_graphics=True` option results in faster load times and a lighter memory footprint. When that option is turned on, all 2D and 3D graphics support is skipped, and the code and libraries related to graphics do not get loaded into memory. This option must be set to true when running on hardware that does not have hardware or software support for OpenGL or X11 on Linux. It needs to be turned on during initialization and cannot be changed afterwards. The 2D, 3D and Graphics Analysis controls are obviously not available. To select this mode, set the `no_graphics` property to true after creating the STK X application object and before performing any other operation with STK Engine:

Initialize with PySTK
---------------------

from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=True)

The `no_graphics=True` mode also alters the way scenarios are saved and loaded. When an engine application sets `no_graphics=True`, it loads a scenario coming from STK Desktop, the 2D and 3D information serialized as part of the scenario is ignored. If that scenario is then saved, all 2D and 3D information is lost. If the scenario is then loaded into STK Desktop, default graphics options are used.


Initialize STK Engine
=====================

This section describes how to use PySTK with STK Engine. The STK Engine API is supported on both Windows and Linux, although AGI has not implemented some features, such as events. STK Engine runs in-process in your Python script, so unlike STK Desktop, only one instance of engine is possible, which is started using :py:method:`ansys.stk.core.stkengine.STKEngine.start_application`, returning the :py:class`ansys.stk.core.stk.engine.STKEngineApplication` class and giving access to the :py:class:`ansys.stk.core.stkx.STKXApplication` API. Unlike :py:class:`ansys.stk.core.stkdesktop.STKDesktopApplication`, the object model root is not a property and a new root object may be obtained from the :py:method:`ansys.stk.core.stkengine.STKEngine.new_object_root` method on the :py:class:`ansys.stk.core.stkengine.STKEngineApplication` object.

Start STK Engine
----------------
*INSERT PYTHON EXAMPLE FOR STARTING A NEW INSTANCE OF STK ENGINE USING PySTK*

Finish your work with STK Engine
--------------------------------
STKEngineApplication provides a ShutDown method that is the recommended way to stop the connection to STK and free up resources. After calling ShutDown, it is no longer valid to start a new engine application in the current process.


Tkinter GlobeControl, MapControl, and GfxAnalysisControl
--------------------------------------------------------
This section describes how to use PySTK with the Tkinter GlobeControl, MapControl, and GfxAnalysisControl classes.

Create a Tkinter window with a globe control
````````````````````````````````````````````
*INSERT PYTHON EXAMPLE*


Initialize STKRuntime
======================

:py:class:`ansys.stk.core.stkruntime.STKRuntime` is an executable that serves STK Engine capabilities via gRPC. Use the :py:class:`ansys.stk.core.stkruntime.STKRuntime` to start or attach to a running STK instance. Once the :py:class:`ansys.stk.core.stkruntime.STKRuntimeApplication` object is obtained, interact with STK, via :py:class:`ansys.stk.core.stkobjects.StkObjectRoot` obtained from calling the :py:method:`ansys.stk.core.stkruntime.STKRuntimeApplication.new_object_root` method. Shutting down the remote process is possible by calling :py:method`anys.stk.core.stkruntime.STKRuntimeApplication.shutdown`, or using the `user_control=False` option when starting the application.

Start a new STKRuntime instance
-------------------------------

STKRuntime may be started on the local machine using STKRuntime.StartApplication(). While STKRuntime offers STK Engine capabilities similar to the STKEngine module, there are a few key differences, including:

- STK Engine runs STK in-process with Python, whereas STKRuntime is out-of-process using gRPC to communicate.
- STKRuntime does not offer visualizations at this time.

*INSERT TABLE*
Options | Description


Attach to a running STKRuntime instance
---------------------------------------

To attach to a running STKRuntime application via gRPC, you can use STKRuntime.AttachToApplication(). To shut down the STK Runtime application, STKRuntimeApplication.ShutDown() must be called.

*INSERT TABLE*
Options | Description

*INSERT STKRUNTIME PYTHON EXAMPLE*