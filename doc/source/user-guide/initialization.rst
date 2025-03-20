Initialization
##############

This topic explains how to establish a connection and prepare PySTK for usage with STK application interfaces and runnable programs.

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


Initialize with STK Desktop
===========================

This section describes how to use PySTK with STK Desktop. 

The :py:meth:`~ansys.stk.core.stkdesktop.STKDesktop.start_application` and :py:meth:`~ansys.stk.core.stkdesktop.STKDesktop.attach_to_application` methods are available to obtain the :py:class:`~ansys.stk.core.stkdesktop.STKDesktopApplication` class and begin interacting with STK through the :py:mod:`~ansys.stk.core.UiApplication` API. From the application interface, the most common way to begin working with STK is to use the :py:class:`~ansys.stk.core.stkobjects.StkObjectRoot` class, which is accessible as the :py:attr:`~ansys.stk.core.stkdesktop.STKDesktopApplication.root` property of the :py:class:`~ansys.stk.core.stkdesktop.STKDesktopApplication` object.

Start a new STK Desktop instance
--------------------------------

Use the :py:meth:`~ansys.stk.core.stkdesktop.STKDesktop.start_application` method to start a new STK Desktop application session:

.. literalinclude:: /../../tests/doc_snippets_tests/initialization/initialization_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def CreateSTKNewSnippet
  :end-at: root = stk.root
  :dedent:

The :py:meth:`~ansys.stk.core.stkdesktop.STKDesktop.start_application` method has optional arguments to control if the application should be visible, if it should exit when the Python script ends, and to switch to gRPC for communicating with STK Desktop (instead of Windows automation by default).

.. note:: To learn more about gRPC see `https://grpc.io/ <https://grpc.io/>`_

Attach to a running STK Desktop instance
----------------------------------------

Use the :py:meth:`~ansys.stk.core.stkdesktop.STKDesktop.attach_to_application` method to attach to a running STK desktop application:

.. literalinclude:: /../../tests/doc_snippets_tests/initialization/initialization_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def AttachSTKSnippet
  :end-at: root = stk.root
  :dedent:

The :py:meth:`~ansys.stk.core.stkdesktop.STKDesktop.attach_to_application` method has additional arguments to specify the Process ID (PID) if more than one STK application is running, as well as switching to gRPC for communicating with STK Desktop (instead of Windows automation by default).

Initialize with STK Engine
==========================

This section describes how to use PySTK with STK Engine. The STK Engine API is supported on both Windows and Linux, although `some features <https://help.agi.com/stkEngineOnUNIX/Content/stkEngineUX/stkFunctionalityNS.htm>`_ are not supported on Linux. STK Engine runs in-process in your Python script, so unlike STK Desktop, only one instance of engine is possible, which is started using :py:meth:`~ansys.stk.core.stkengine.STKEngine.start_application`, returning the :py:class:`~ansys.stk.core.stkengine.STKEngineApplication` class and giving access to the :py:class:`~ansys.stk.core.stkx.STKXApplication` API. Unlike :py:class:`~ansys.stk.core.stkdesktop.STKDesktopApplication`, the object model root is not a property and a new root object may be obtained from the :py:meth:`~ansys.stk.core.stkengine.STKEngineApplication.new_object_root` method on the :py:class:`~ansys.stk.core.stkengine.STKEngineApplication` object.

Initialize STK Engine with graphics
-----------------------------------

To select this mode, do not specify any argument when calling  :py:meth:`~ansys.stk.core.stkengine.STKEngine.start_application`, as by default the `no_graphics` argument is `False`.

.. literalinclude:: /../../tests/doc_snippets_tests/initialization/initialization_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def StartSTKEngineWithGfxSnippet
  :end-at: root = stk.new_object_root()
  :dedent:

Initialize STK Engine without graphics
--------------------------------------

If your use case consists of using STK Engine as a computational tool and does not require 2D/3D visualization (for instance, if your application is running as a service on a compute node without direct user interaction), skipping graphics mode results in faster load times and a lighter memory footprint. When graphics are not loaded, all 2D and 3D graphics support is skipped, and the code and libraries related to graphics do not get loaded into memory. Graphics cannot be used when running on hardware that does not have hardware or software support for OpenGL or X11 on Linux. It needs to be turned on during initialization and cannot be changed afterwards. The 2D, 3D and Graphics Analysis controls are not available. To avoid loading graphics, pass the `no_graphics=True` argument when initializing STK Engine:

.. literalinclude:: /../../tests/doc_snippets_tests/initialization/initialization_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def StartSTKEngineWithoutGfxSnippet
  :end-at: root = stk.new_object_root()
  :dedent:

The NoGraphics mode also alters the way scenarios are saved and loaded. When an engine application in NoGraphics mode loads a scenario coming from STK Desktop, the 2D and 3D information serialized as part of the scenario is ignored. If that scenario is then saved, all 2D and 3D information is lost. If the scenario is then loaded into STK Desktop, default graphics options are used.


Finish your work with STK Engine
--------------------------------

:py:class:`~ansys.stk.core.stkengine.STKEngineApplication` provides a :py:meth:`~ansys.stk.core.stkengine.STKEngineApplication.shutdown` method that is the recommended way to stop the connection to STK and free up resources. After calling that method, it is no longer valid to start a new engine application in the current process.


Tkinter globe control, map control, and graphics analysis control
-----------------------------------------------------------------
This section describes how to use PySTK with the Tkinter :py:class:`~ansys.stk.core.stkengine.tkcontrols.GlobeControl`, :py:class:`~ansys.stk.core.stkengine.tkcontrols.MapControl`, and :py:class:`~ansys.stk.core.stkengine.tkcontrols.GfxAnalysisControl` classes.

Create a Tkinter window with a map control and a globe control
``````````````````````````````````````````````````````````````

.. literalinclude:: /../../tests/doc_snippets_tests/test_util.py
  :language: py
  :tab-width: 4
  :start-at: from tkinter import Tk, BOTH, YES, LEFT
  :end-at: self.window.update() 
  :dedent:


Initialize STKRuntime
======================

STKRuntime is an executable that serves STK Engine capabilities via gRPC. Use the :py:mod:`~ansys.stk.core.stkruntime` module to start or attach to a running STKRuntime application. Once the :py:class:`ansys.stk.core.stkruntime.STKRuntimeApplication` object is obtained, interact with STK, via :py:class:`~ansys.stk.core.stkobjects.StkObjectRoot` obtained from calling :py:meth:`~ansys.stk.core.stkruntime.STKRuntimeApplication.new_object_root`. Shutting down the remote STKRuntime process is possible by calling :py:meth:`~ansys.stk.core.stkruntime.STKRuntimeApplication.shutdown`, or using the `user_control=False` option when starting the application.

Start a new STKRuntime instance
-------------------------------

STKRuntime may be started on the local machine using :py:meth:`~ansys.stk.core.stkruntime.STKRuntime.start_application`. While STKRuntime offers STK Engine capabilities similar to the STKEngine module, there are a few key differences, including:

- STK Engine runs STK in-process with Python, whereas STKRuntime is out-of-process using gRPC to communicate.
- STKRuntime does not offer visualizations at this time.

.. literalinclude:: /../../tests/doc_snippets_tests/initialization/initialization_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def CreateSTKRuntimeNewSnippet
  :end-at: root = stk.new_object_root()
  :dedent:


The :py:meth:`~ansys.stk.core.stkruntime.STKRuntime.attach_to_application` method has additional arguments to control if the application should exit when the Python script ends, to enable the NoGraphics mode, and to customize the gRPC connection.


Attach to a running STKRuntime instance
---------------------------------------

To attach to a running STKRuntime application via gRPC, you can use :py:meth:`~ansys.stk.core.stkruntime.STKRuntime.attach_to_application`. To shut down the STK Runtime application, :py:meth:`~ansys.stk.core.stkruntime.STKRuntimeApplication.shutdown` must be called.

.. literalinclude:: /../../tests/doc_snippets_tests/initialization/initialization_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def AttachSTKRuntimeSnippet
  :end-at: root = stk.new_object_root()
  :dedent:

If you need to configure the gRPC connection with STKRuntime, the :py:meth:`~ansys.stk.core.stkruntime.STKRuntime.attach_to_application` method provides additional arguments such as the gRPC host, port, and timeout.

