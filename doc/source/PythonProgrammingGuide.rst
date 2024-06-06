Programmer’s Guide
==================

Obtaining Help
--------------

Via STK Programming documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The STK Python API help documents the method/property definitions with
syntax using the Python
`typing <https://docs.python.org/3/library/typing.html>`__ module. The
following example method and property from the
`IAgStkObjectRoot <../DocX/STKObjects~IAgStkObjectRoot.html>`__
interface show this syntax.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------------------------------------------+
   | ``def GetObjectFromPath(self, ObjectPath:str) -> "IAgStkObject":``    |
   | ``@property``                                                         |
   | ``def CurrentScenario(self) -> "IAgStkObject":``                      |
   +-----------------------------------------------------------------------+

These examples show that interface methods and properties are methods
called on an object ("self"). Input argument names (e.g., "ObjectPath")
are shown for methods along with the type of the argument (in this
example, Python str type). The return type is shown after the "->"
operator and STK Object Model types (e.g., "IAgStkObject") are shown in
quotes to help IDEs resolve the type names. The Python API programmer
may call these methods and properties on an IAgStkObjectRoot object in
the expected way. In the following example, an IAgStkObjectRoot object
named "root" has already been created.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------------------------------------------+
   | ``my_object = root.GetObjectFromPath('My Object Path')``              |
   | ``my_scenario = root.CurrentScenario``                                |
   +-----------------------------------------------------------------------+

Within interactive Python
~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the Python help function to display the documentation of
modules, functions, classes, keywords etc. Below is an example printing
the help for the class returned by the object model root current
scenario property.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------------------------------------------+
   | ``# Start new instance of STK Engine using the new API``              |
   | ``from agi.stk.stkengine import STKEngine``                           |
   | ``from agi.stk.stkobjects import *``                                  |
   | ``stk = STKEngine                                                     |
   | .StartApplication(noGraphics=False) # optionally, noGraphics = True`` |
   | ``# Get the IAgStkObjectRoot interface``                              |
   | ``root = stk.NewObjectRoot()``                                        |
   | ``# Create a new scenario``                                           |
   | ``root.NewScenario('HelpDemo')``                                      |
   | ``# Output the d                                                      |
   | ocumentation for the class returned by the CurrentScenario property`` |
   | ``print(help(root.CurrentScenario))``                                 |
   +-----------------------------------------------------------------------+

This produces the following output:

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------------------------------------------+
   | ``Help on AgScenario in module agi.stk.stkobjects object:``           |
   | ``                                                                    |
   | class AgScenario(IAgScenario, IAgStkObject, IAgLifetimeInformation)`` |
   | ``| Class defining the Scenario object.``                             |
   | ``|``                                                                 |
   | ``| Method resolution order:``                                        |
   | ``| AgScenario``                                                      |
   | ``| IAgScenario``                                                     |
   | ``| IAgStkObject``                                                    |
   | ``| IAgLifetimeInformation``                                          |
   | ``| builtins.object``                                                 |
   | ``|``                                                                 |
   | ``| Methods defined here:``                                           |
   | ``|``                                                                 |
   | ``| __init__(self, sourceObject=None)``                               |
   | ``| Initialize self. See help(type(self)) for accurate signature.``   |
   | ``|``                                                                 |
   | ``| ---                                                               |
   | -------------------------------------------------------------------`` |
   | ``| Methods inherited from IAgScenario:``                             |
   | ``|``                                                                 |
   | ``| GetAccessBetweenObje                                              |
   | ctsByPath(self, objectPath1:str, objectPath2:str) -> 'IAgStkAccess'`` |
   | ``| Returns the                                                       |
   |  access object currently associated with the two STK objects specifie |
   | d using their paths. The paths can be fully-qualified or truncated.`` |
   | ``|``                                                                 |
   | ``| GetExistingAccesses(self) -> list``                               |
   | ``| Returns an array of existing accesses in t                        |
   | he current scenario. The result is a two-dimensional array of triplet |
   | s where each triplet contains the paths of two objects participating  |
   | in the access and a flag indicating whether the access is computed.`` |
   | ``|``                                                                 |
   | ``| SetDirty(self) -> None``                                          |
   | ``| Sets the flag indicating the scenario has been modified.``        |
   | ``|``                                                                 |
   | ``| SetTimePeriod(self, startTime:Any, stopTime:Any) -> None``        |
   | ``-- More --``                                                        |
   +-----------------------------------------------------------------------+

Module Mapping
--------------

The following table provides the corresponding library for each Python
module.

+----------------------------------+----------------------------------+
| library                          | Module                           |
+==================================+==================================+
| `STK Graphics                    | agi.stk.graphics                 |
| Primitives <../                  |                                  |
| DocX/AgSTKGraphicsLib_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Access Constraint           | agi.st                           |
| Plugin <../DocX/AgA              | k.plugins.accessconstraintplugin |
| ccessConstraintPlugin_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Attribute                   | agi.stk.plugins.attrautomation   |
| Automation <../                  |                                  |
| DocX/AgAttrAutomation_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Communications and Radar    | a                                |
| foundation <../Doc               | gi.stk.plugins.commrdrfoundation |
| X/AgCommRdrFoundation_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Coordinate(VGT)             | agi.stk.plugins.crdnplugin       |
| plugins                          |                                  |
| <../DocX/AgCrdnPlugin_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Astrogator                  | agi.stk.plugins.gatorplugin      |
| plugin <                         |                                  |
| ../DocX/AgGatorPlugin_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK HPOP                        | agi.stk.plugins.hpopplugin       |
| plugins <.                       |                                  |
| ./DocX/AgAsHpopPlugin_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Propagator                  | agi.stk.plugins.propagator       |
| plugins <../DocX                 |                                  |
| /AgPropagatorWrappers_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK                             | agi.stk.plugins.stkplugin        |
| plugin                           |                                  |
|  <../DocX/AgStkPlugin_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Radar                       | agi.stk.plugins.stkradarplugin   |
| plugin                           |                                  |
| s <../DocX/AgStkRadar_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Utilities                   | agi.stk.plugins.utplugin         |
| plugi                            |                                  |
| n <../DocX/AgUtPlugin_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Astro                       | agi.stk.plugins.asplugin         |
| plugin                           |                                  |
| s <../DocX/AgAsPlugin_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Search                      | agi.stk.plugins.searchplugin     |
| plu                              |                                  |
| gin <../DocX/AgSearch_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK                             | agi.stk.stkobjects               |
| Object                           |                                  |
| s <../DocX/STKObjects_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK                             | agi.stk.stkobjects.aviator       |
| Aviator                          |                                  |
| <../DocX/AgStkAvtrLib_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Aviator                     | a                                |
| MATLAB <../Do                    | gi.stk.stkobjects.aviator.matlab |
| cX/AgStkAvtrMATLABLib_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK                             | agi.stk.stkutil                  |
| Util <../DocX/STKUtil_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK                             | agi.stk.stkx                     |
| X <../DocX/STKXLib_P.html>`__    |                                  |
+----------------------------------+----------------------------------+
| `STK UI                          | agi.stk.uiapplication            |
| Application <../Do               |                                  |
| cX/AgUiApplicationLib_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK UI                          | agi.stk.uicore                   |
| Core                             |                                  |
|  <../DocX/AgUiCoreLib_P.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `STK Vector Geometry             | agi.stk.vgt                      |
| Tool                             |                                  |
|  <../DocX/AgSTKVgtLib_P.html>`__ |                                  |
+----------------------------------+----------------------------------+

.. container::

   .. rubric:: STK Desktop
      :name: stk-desktop

   This section describes how to use the API with STK Desktop. The
   STKDesktop.StartApplication and STKDesktop.AttachToApplication
   methods are available to obtain the STKDesktopApplication class and
   begin interacting with STK through the the
   `AgUiApplication <../DocX/AgUiApplicationLib_P.html>`__ API. From the
   application interface, the most common way to begin working with STK
   is to use the
   `IAgStkObjectRoot <../DocX/STKObjects~IAgStkObjectRoot.html>`__
   interface, which is accessible as the Root property of the
   STKDesktopApplication object.

   .. rubric:: Starting a new STK Desktop instance
      :name: starting-a-new-stk-desktop-instance

   Use the STKDesktop.StartApplication method to start a new STK
   application session. The StartApplication method has optional
   arguments as a convenience to set commonly used properties:

   +----------------------------------+----------------------------------+
   | Argument                         | Description                      |
   +----------------------------------+----------------------------------+
   | set visible=True                 | Start STK in visible mode        |
   +----------------------------------+----------------------------------+
   | set userControl=True             | Keeps STK open after finishing a |
   |                                  | Python script                    |
   +----------------------------------+----------------------------------+
   | grpc_server (bool,               | Specify True to start STK on the |
   | default=False)                   | current machine with the gRPC    |
   |                                  | server active and connect to it  |
   |                                  | using gRPC                       |
   +----------------------------------+----------------------------------+
   | grpc_host (string, default =     | A valid DNS host name for the    |
   | "0.0.0.0")                       | STK gRPC server                  |
   +----------------------------------+----------------------------------+
   | grpc_port (init, default=40704)  | A valid TCP port for the STK     |
   |                                  | gRPC server                      |
   +----------------------------------+----------------------------------+

   .. container:: LanguageSpecific
      :name: Example_Python

      +-----------------------------------+-----------------------------------+
      | [Python - STK API]                |                                   |
      +===================================+===================================+
      | .. container:: LanguageSpecific   |                                   |
      |    :name: Code_Python             |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      |                                   |                                   |
      |  | ``# Start new instanc        | |                                   |
      |                                   |                                   |
      |  | e of STK using the new API`` | |                                   |
      |                                   |                                   |
      |  | ``from agi.stk.st            | |                                   |
      |                                   |                                   |
      |  | kdesktop import STKDesktop`` | |                                   |
      |                                   |                                   |
      |  | ``from a                     | |                                   |
      |                                   |                                   |
      |  | gi.stk.stkobjects import *`` | |                                   |
      |                                   |                                   |
      |  | ``stk = STKDesktop.StartAppl | |                                   |
      |                                   |                                   |
      |  | ication(visible=True) #using | |                                   |
      |                                   |                                   |
      |  |  optional visible argument`` | |                                   |
      |                                   |                                   |
      |  | ``# Get the                  | |                                   |
      |                                   |                                   |
      |  | IAgStkObjectRoot interface`` | |                                   |
      |                                   |                                   |
      |  | ``root = stk.Root``          | |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      +-----------------------------------+-----------------------------------+

   .. rubric:: Attaching to a running instance of STK Desktop
      :name: attaching-to-a-running-instance-of-stk-desktop

   Use the STKDesktop.AttachToApplication method to attach to a running
   STK desktop application. The AttachToApplication method has
   additional arguments to specify the Process ID (pid) if more than one
   STK application is running:

   +----------------------------------+----------------------------------+
   | Argument                         | Description                      |
   +----------------------------------+----------------------------------+
   | pid (int, default = None)        | The process ID for the STK       |
   |                                  | Desktop instance to attach to.   |
   |                                  | Not applicable if gRPC is used.  |
   +----------------------------------+----------------------------------+
   | grpc_server (bool, default =     | Specify True to attach to a      |
   | False)                           | running STK gRPC server.         |
   +----------------------------------+----------------------------------+
   | grpc_host (string, default =     | A valid DNS host name for the    |
   | "localhost")                     | STK gRPC server. "localhost"     |
   |                                  | connects to the local server.    |
   +----------------------------------+----------------------------------+
   | grpc_port (init, default =       | A valid TCP port for the STK     |
   | 40704)                           | gRPC server.                     |
   +----------------------------------+----------------------------------+

   .. container:: LanguageSpecific
      :name: Example_Python

      +-----------------------------------+-----------------------------------+
      | [Python - STK API]                |                                   |
      +===================================+===================================+
      | .. container:: LanguageSpecific   |                                   |
      |    :name: Code_Python             |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      |                                   |                                   |
      |  | ``# G                        | |                                   |
      |                                   |                                   |
      |  | et reference to running STK  | |                                   |
      |                                   |                                   |
      |  | instance using the new API`` | |                                   |
      |                                   |                                   |
      |  | ``from agi.stk.st            | |                                   |
      |                                   |                                   |
      |  | kdesktop import STKDesktop`` | |                                   |
      |                                   |                                   |
      |  | ``from a                     | |                                   |
      |                                   |                                   |
      |  | gi.stk.stkobjects import *`` | |                                   |
      |                                   |                                   |
      |  | ``stk = STKDes               | |                                   |
      |                                   |                                   |
      |  | ktop.AttachToApplication()`` | |                                   |
      |                                   |                                   |
      |  | ``# Get the                  | |                                   |
      |                                   |                                   |
      |  | IAgStkObjectRoot interface`` | |                                   |
      |                                   |                                   |
      |  | ``root = stk.Root``          | |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      +-----------------------------------+-----------------------------------+

   .. rubric:: Finishing your work with STK Desktop
      :name: finishing-your-work-with-stk-desktop

   STKDesktopApplication provides a ShutDown method that is the
   recommended way to terminate the connection to STK and free up
   resources. Set the UserControl property on STKDesktopApplication or
   when calling StartApplication to set the application behavior after
   the call to ShutDown.

   .. container:: LanguageSpecific
      :name: Example_Python

      +-----------------------------------+-----------------------------------+
      | [Python - STK API]                |                                   |
      +===================================+===================================+
      | .. container:: LanguageSpecific   |                                   |
      |    :name: Code_Python             |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      |                                   |                                   |
      |  | ``# G                        | |                                   |
      |                                   |                                   |
      |  | et reference to running STK  | |                                   |
      |                                   |                                   |
      |  | instance using the new API`` | |                                   |
      |                                   |                                   |
      |  | ``from agi.stk.st            | |                                   |
      |                                   |                                   |
      |  | kdesktop import STKDesktop`` | |                                   |
      |                                   |                                   |
      |  | ``from a                     | |                                   |
      |                                   |                                   |
      |  | gi.stk.stkobjects import *`` | |                                   |
      |                                   |                                   |
      |  | ``stk = STKDesktop.StartAppl | |                                   |
      |                                   |                                   |
      |  | ication(userControl=False)`` | |                                   |
      |                                   |                                   |
      |  | ``# Do work...``             | |                                   |
      |                                   |                                   |
      |  | ``stk.ShutDown()``           | |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      +-----------------------------------+-----------------------------------+

   .. rubric:: Advanced topic: marshalling across threads
      :name: advanced-topic-marshalling-across-threads

   STKDesktop.CreateThreadMarshaller (stk_object_to_marshal) was added
   in STK 12.2.0 to assist with marshalling STK objects between Python
   threads. Because the STK Object model is not inherently thread-safe,
   this helper is needed to safely execute commands from two or more
   threads.

   As this is an advanced feature, and only experienced users should
   implement it, and then only when necessary.

   When using this feature, you are responsible for properly
   synchronizing across threads. An example application of this (shown
   below) would be to marshal IAgStkObjectRoot to a new thread and call
   NewScenario, so that the Python application main thread is not
   blocked while the scenario is created.

   STKDesktop.CreateThreadMarshaller returns
   agi.stk.stkdesktop.ThreadMarshaller, which has the methods
   InitializeThread, ReleaseThread, and GetMarshalledToCurrentThread.
   InitializeThread must be called on the destination thread before the
   marshalled object can be used.

   GetMarshalledToCurrentThread is called to return a copy of the
   marshalled object that may be used on the current thread.
   ReleaseThread must be called before the destination thread exits.

   Each ThreadMarshaller may be used only once; the same
   ThreadMarshaller may not be passed to two or more threads.

   .. container:: LanguageSpecific
      :name: Example_Python

      +-----------------------------------+-----------------------------------+
      | [Python - STK API]                |                                   |
      +===================================+===================================+
      | .. container:: LanguageSpecific   |                                   |
      |    :name: Code_Python             |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      |                                   |                                   |
      |  | ``import threading``         | |                                   |
      |                                   |                                   |
      |  | ``from agi.stk.st            | |                                   |
      |                                   |                                   |
      |  | kdesktop import STKDesktop`` | |                                   |
      |                                   |                                   |
      |  | ``def asynchronous_new       | |                                   |
      |                                   |                                   |
      |  | _scenario(rootMarshaller):`` | |                                   |
      |                                   |                                   |
      |  | ``rootMar                    | |                                   |
      |                                   |                                   |
      |  | shaller.InitializeThread()`` | |                                   |
      |                                   |                                   |
      |  | ``root = rootMarshaller.GetM | |                                   |
      |                                   |                                   |
      |  | arshalledToCurrentThread()`` | |                                   |
      |                                   |                                   |
      |  | ``print(f'Creating           | |                                   |
      |                                   |                                   |
      |  |  a new scenario from thread  | |                                   |
      |                                   |                                   |
      |  | {threading.get_ident()}.')`` | |                                   |
      |                                   |                                   |
      |  | ``root                       | |                                   |
      |                                   |                                   |
      |  | .NewScenario('MyScenario')`` | |                                   |
      |                                   |                                   |
      |  | ``root                       | |                                   |
      |                                   |                                   |
      |  | Marshaller.ReleaseThread()`` | |                                   |
      |                                   |                                   |
      |  | ``if __name__=='__main__':`` | |                                   |
      |                                   |                                   |
      |  | ``print                      | |                                   |
      |                                   |                                   |
      |  | (f'Starting STK from thread  | |                                   |
      |                                   |                                   |
      |  | {threading.get_ident()}.')`` | |                                   |
      |                                   |                                   |
      |  | ``stk = STKDes               | |                                   |
      |                                   |                                   |
      |  | ktop.StartApplication(visibl | |                                   |
      |                                   |                                   |
      |  | e=True, userControl=False)`` | |                                   |
      |                                   |                                   |
      |  | ``root = stk.Root``          | |                                   |
      |                                   |                                   |
      |  | ``ro                         | |                                   |
      |                                   |                                   |
      |  | otMarshaller = STKDesktop.Cr | |                                   |
      |                                   |                                   |
      |  | eateThreadMarshaller(root)`` | |                                   |
      |                                   |                                   |
      |  | ``t = threa                  | |                                   |
      |                                   |                                   |
      |  | ding.Thread(target=asynchron | |                                   |
      |                                   |                                   |
      |  | ous_new_scenario, args=(root | |                                   |
      |                                   |                                   |
      |  | Marshaller,), daemon=True)`` | |                                   |
      |                                   |                                   |
      |  | ``t.start()``                | |                                   |
      |                                   |                                   |
      |  | ``t.join()``                 | |                                   |
      |                                   |                                   |
      |  | ``print(f'Term               | |                                   |
      |                                   |                                   |
      |  | inating example from thread  | |                                   |
      |                                   |                                   |
      |  | {threading.get_ident()}.')`` | |                                   |
      |                                   |                                   |
      |  | ``stk.ShutDown()``           | |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      +-----------------------------------+-----------------------------------+

STKRuntime
----------

STKRuntime is an executable that serves STK Engine functionality vai
gRPC. Use agi.stk.stkruntime to start or attach to a running STKRuntime
application. Once the STKRuntimeAPplication object is obtained, interact
with STK, via IAgStkObjectRoot obtained from calling
STKRuntimeApplication.NewObjectRoot(). Shutting down the remote
STKRuntime process is possible by calling
STKRuntimeApplication.ShutDown(), or using the userControl=False option
when starting the application.

Starting a new STKRuntime instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

STKRuntime may be started on the local machine using
STKRuntime.StartApplication(). While STKRuntime offers STK Engine
functionality similar to the STKEngine module, there are a few key
differences.

#. STKEngine runs STK in-process with Python, whereas STKRuntime is
   out-of-process using gRPC to communicate.
#. STKRuntime does not offer visualizations at this time.

+----------------------------------+----------------------------------+
| Options                          | Description                      |
+----------------------------------+----------------------------------+
| grpc_host (string, default =     | A valid DNS host name for the    |
| "0.0.0.0")                       | STKRuntime gRPC server.          |
+----------------------------------+----------------------------------+
| grpc_port (int, default = 40704) | A valid TCP port for the         |
|                                  | STKRuntime gRPC server.          |
+----------------------------------+----------------------------------+
| userControl (bool, default =     | Specify True to leave the        |
| False)                           | STKRuntime application running   |
|                                  | (in the user's control) after    |
|                                  | Python exits.                    |
+----------------------------------+----------------------------------+
| noGraphics (bool, default =      | Disables graphics calculations   |
| True)                            | within the STKRuntime            |
|                                  | application to improve           |
|                                  | performance and remove           |
|                                  | dependencies on graphics         |
|                                  | libraries.                       |
+----------------------------------+----------------------------------+

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [STKRuntime Python - API]         |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.st            | |                                   |
   |                                   |                                   |
   |  | kruntime import STKRuntime`` | |                                   |
   |                                   |                                   |
   |  | ``stk = st                   | |                                   |
   |                                   |                                   |
   |  | kRuntime.StartApplication(gr | |                                   |
   |                                   |                                   |
   |  | pc_host="0.0.0.0", grpc_port | |                                   |
   |                                   |                                   |
   |  | =40704, userControl=False)`` | |                                   |
   |                                   |                                   |
   |  | ``print(stk.Version)``       | |                                   |
   |                                   |                                   |
   |  | ``root=stk.NewObjectRoot()`` | |                                   |
   |                                   |                                   |
   |  | ``root                       | |                                   |
   |                                   |                                   |
   |  | .NewScenario("MyScenario")`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Attaching to a running STKRuntime instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To attach to a running STKRuntime application via gRPC, you can use
STKRuntime.AttachToApplication(). To shut down the STK Runtime
application, STKRuntimeApplication.ShutDown() must be called.

+----------------------------------+----------------------------------+
| Option                           | Description                      |
+----------------------------------+----------------------------------+
| grpc_host (string, default =     | A valid DNS host name for the    |
| "localhost")                     | STKRuntime gRPC server.          |
+----------------------------------+----------------------------------+
| grpc_port (int, default = 40704) | A valid TCP port for the         |
|                                  | STKRuntime gRPC server.          |
+----------------------------------+----------------------------------+

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [STKRuntime Python - API]         |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.st            | |                                   |
   |                                   |                                   |
   |  | kruntime import STKRuntime`` | |                                   |
   |                                   |                                   |
   |  | ``stk = stkRuntime.Attac     | |                                   |
   |                                   |                                   |
   |  | hToApplication(grpc_host="lo | |                                   |
   |                                   |                                   |
   |  | calhost", grpc_port=40704)`` | |                                   |
   |                                   |                                   |
   |  | ``print(stk.Version)``       | |                                   |
   |                                   |                                   |
   |  | ``root=stk.NewObjectRoot()`` | |                                   |
   |                                   |                                   |
   |  | ``stk.ShutDown()``           | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

STK Engine
----------

This section describes how to use the API with STK Engine. The STK
Engine API is supported on both Windows and Linux, although AGI has not
implemented some features, such as events. STK Engine runs in-process in
your Python script, so unlike STK Desktop, only one instance of engine
is possible, which is started using STKEngine.StartApplication,
returning the STKEngineApplication class and giving access to the
`AgSTKXApplication <../DocX/STKXLib~AgSTKXApplication.html>`__ API.
Unlike STKDesktopApplication, the object model root is not a property
and a new root object may be obtained from the NewObjectRoot method on
the STKEngineApplication object.

Starting STK Engine
~~~~~~~~~~~~~~~~~~~

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# Start new instance of ST | |                                   |
   |                                   |                                   |
   |  | K Engine using the new API`` | |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.              | |                                   |
   |                                   |                                   |
   |  | stkengine import STKEngine`` | |                                   |
   |                                   |                                   |
   |  | ``from a                     | |                                   |
   |                                   |                                   |
   |  | gi.stk.stkobjects import *`` | |                                   |
   |                                   |                                   |
   |  | ``                           | |                                   |
   |                                   |                                   |
   |  | stk = STKEngine.StartApplica | |                                   |
   |                                   |                                   |
   |  | tion(noGraphics=False) # opt | |                                   |
   |                                   |                                   |
   |  | ionally, noGraphics = True`` | |                                   |
   |                                   |                                   |
   |  | ``# Get the                  | |                                   |
   |                                   |                                   |
   |  | IAgStkObjectRoot interface`` | |                                   |
   |                                   |                                   |
   |  | ``                           | |                                   |
   |                                   |                                   |
   |  | root = stk.NewObjectRoot()`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Finishing your work with STK Engine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

STKEngineApplication provides a ShutDown method that is the recommended
way to terminate the connection to STK and free up resources. After
calling ShutDown, it is no longer valid to start a new engine
application in the current process.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# G                        | |                                   |
   |                                   |                                   |
   |  | et reference to running STK  | |                                   |
   |                                   |                                   |
   |  | instance using the new API`` | |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.              | |                                   |
   |                                   |                                   |
   |  | stkengine import STKEngine`` | |                                   |
   |                                   |                                   |
   |  | ``from a                     | |                                   |
   |                                   |                                   |
   |  | gi.stk.stkobjects import *`` | |                                   |
   |                                   |                                   |
   |  | ``stk = ST                   | |                                   |
   |                                   |                                   |
   |  | KEngine.StartApplication()`` | |                                   |
   |                                   |                                   |
   |  | ``# Do work...``             | |                                   |
   |                                   |                                   |
   |  | ``stk.ShutDown()``           | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Advanced topic: STK Engine timer loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Timer loops are an advanced topic that most API users can ignore. Some
features in STK rely on a timer loop to function properly, for example
updating graphics windows in a globe control, flushing the log file
messages, or establishing a Connect socket to STK Engine. There are
different ways of establishing a timer loop in a Python main thread, and
these ways have different trade-offs that may affect your application.

On Windows, the only way to activate a timer loop is to use the loops
implicitly available in the interactive Python interpreter or in the
Tkinter mainloop. One of these will need to be running to establish a
Connect socket, for example.

On Linux, when graphics are active, it is assumed that globe or map
controls will be used, and so the timer loop defaults to using the
Tkinter mainloop, which will be running when using the tkinter-based
controls. In no-graphics mode, signal-based timer loops are available.
By default, STKEngine will use a timer loop that uses the SIGALRM
signal. If this creates a conflict with your application, there is also
an option to specify a SIGRT signal number to use. Contact AGI support
to learn more.

If directed by AGI Tech Support, you may override timer operations on
Linux using the environment variable STK_PYTHONAPI_TIMERTYPE, by setting
it to a numeric value relating to the enum
agi.stk12.stkengine.STKEngineTimerType. The default value is SigAlarm
(4) in no-graphics mode and TkinterMainloop (2) in graphics mode. You
may use InteractivePython (3) in the interactive interpreter, and it
will not use any signals nor require the tkinter mainloop. Use SigRt (5)
to specify a different signal than SIGALRM. The default is SIGRTMIN, and
you may change this to SIGRTMIN+X, where X is specified using a second
environment variable STK_PYTHONAPI_TIMERTYPE5_SIGRTMIN_OFFSET=X. If
SIGRTMIN+X > SIGRTMAX, you will get an exception.

Tkinter Globe, Map and Gfx Analysis Controls
--------------------------------------------

This section shows how to use the API with the Tkinter GlobeControl,
MapControl, and GfxAnalysisControl classes. Refer to the `STK X controls
topic <../stkx/stkxlib_controls.htm>`__ for a description of the
controls. Refer to the `Custom Application Samples
table <../automationTree/TechnologyDevelopSamples.htm>`__ for a list of
`Python code
samples <../automationTree/TechnologyDevelopSamples.htm#PythonCustomAppSamples>`__
demonstrating the use of the STK Python controls.

Create a Tkinter window with a globe control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from tki                   | |                                   |
   |                                   |                                   |
   |  | nter import Tk, BOTH, LEFT`` | |                                   |
   |                                   |                                   |
   |  | ``from                       | |                                   |
   |                                   |                                   |
   |  | agi.stk.stkengine import *`` | |                                   |
   |                                   |                                   |
   |  | ``from agi.st                | |                                   |
   |                                   |                                   |
   |  | k.stkengine.tkcontrols impor | |                                   |
   |                                   |                                   |
   |  | t GlobeControl, MapControl`` | |                                   |
   |                                   |                                   |
   |  | ``stk = STKEngine.StartApp   | |                                   |
   |                                   |                                   |
   |  | lication(noGraphics=False)`` | |                                   |
   |                                   |                                   |
   |  | ``                           | |                                   |
   |                                   |                                   |
   |  | root = stk.NewObjectRoot()`` | |                                   |
   |                                   |                                   |
   |  | ``root.NewSc                 | |                                   |
   |                                   |                                   |
   |  | enario("Example_Scenario")`` | |                                   |
   |                                   |                                   |
   |  | ``window = Tk()``            | |                                   |
   |                                   |                                   |
   |  | ``# Cre                      | |                                   |
   |                                   |                                   |
   |  | ate the globe control and ad | |                                   |
   |                                   |                                   |
   |  | d it to the Tkinter window`` | |                                   |
   |                                   |                                   |
   |  | ``glob                       | |                                   |
   |                                   |                                   |
   |  | eControl = GlobeControl(wind | |                                   |
   |                                   |                                   |
   |  | ow, width=640, height=400)`` | |                                   |
   |                                   |                                   |
   |  | ``globeControl.              | |                                   |
   |                                   |                                   |
   |  | pack(fill=BOTH, side=LEFT)`` | |                                   |
   |                                   |                                   |
   |  | ``# C                        | |                                   |
   |                                   |                                   |
   |  | reate the map control and ad | |                                   |
   |                                   |                                   |
   |  | d it to the Tkinter window`` | |                                   |
   |                                   |                                   |
   |  | ``                           | |                                   |
   |                                   |                                   |
   |  | mapControl = MapControl(wind | |                                   |
   |                                   |                                   |
   |  | ow, width=640, height=400)`` | |                                   |
   |                                   |                                   |
   |  | ``mapControl.                | |                                   |
   |                                   |                                   |
   |  | pack(fill=BOTH, side=LEFT)`` | |                                   |
   |                                   |                                   |
   |  | ``window.mainloop()``        | |                                   |
   |                                   |                                   |
   |  | ``root.CloseScenario()``     | |                                   |
   |                                   |                                   |
   |  | ``stk.ShutDown()``           | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Data Types
----------

This section describes the more complex data types used with the STK
Python API beyond the basic Python data types such as float, int, str,
and bool.

Type hints
~~~~~~~~~~

Most argument and return types are specified using type hints with
Python's typing library. In the case that more than one type is possible
(such as an argument that may be a string or a float), typing.Any is
used as the type hint. In those situations, consulting the documentation
for that method is advised. Type hints that are STK interfaces may
represent objects that are subclasses of that interface.

Enumerations
~~~~~~~~~~~~

Enumeration classes are located in the STK Object Model modules (e.g.
agi.stk.stkobjects). Most inherit from Python's enum.IntEnum class while
a few inherit from enum.IntFlag and may be combined using the \|
operator to select multiple options from within the enumeration.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.stkobjec      | |                                   |
   |                                   |                                   |
   |  | ts import AgESTKObjectType`` | |                                   |
   |                                   |                                   |
   |  | `                            | |                                   |
   |                                   |                                   |
   |  | `fac = ObjectRoot.CurrentSce | |                                   |
   |                                   |                                   |
   |  | nario.Children.New(AgESTKObj | |                                   |
   |                                   |                                   |
   |  | ectType.eFacility, "fac1")`` | |                                   |
   |                                   |                                   |
   |  | ``f                          | |                                   |
   |                                   |                                   |
   |  | rom agi.stk.graphics import  | |                                   |
   |                                   |                                   |
   |  | AgEStkGraphicsCylinderFill`` | |                                   |
   |                                   |                                   |
   |  | ``#AgEStkGraphics            | |                                   |
   |                                   |                                   |
   |  | CylinderFill inherits from I | |                                   |
   |                                   |                                   |
   |  | ntFlag and may be combined`` | |                                   |
   |                                   |                                   |
   |  | ``cyl_fill = AgEStkGrap      | |                                   |
   |                                   |                                   |
   |  | hicsCylinderFill.eStkGraphic | |                                   |
   |                                   |                                   |
   |  | sCylinderFillBottomCap | AgE | |                                   |
   |                                   |                                   |
   |  | StkGraphicsCylinderFill.eStk | |                                   |
   |                                   |                                   |
   |  | GraphicsCylinderFillTopCap`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Arrays
~~~~~~

Many methods in the STK API take as input or return arrays. In the
Python API, array values are represented using the list class.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.st            | |                                   |
   |                                   |                                   |
   |  | kdesktop import STKDesktop`` | |                                   |
   |                                   |                                   |
   |  | ``f                          | |                                   |
   |                                   |                                   |
   |  | rom agi.stk.stkutil import A | |                                   |
   |                                   |                                   |
   |  | gEExecMultiCmdResultAction`` | |                                   |
   |                                   |                                   |
   |  | ``stk = STK                  | |                                   |
   |                                   |                                   |
   |  | Desktop.StartApplication()`` | |                                   |
   |                                   |                                   |
   |  | ``connect_comma              | |                                   |
   |                                   |                                   |
   |  | nds = ['GetStkVersion /', 'N | |                                   |
   |                                   |                                   |
   |  | ew / Scenario ExampleScenari | |                                   |
   |                                   |                                   |
   |  | o'] #use a list of strings`` | |                                   |
   |                                   |                                   |
   |  | ``command_results = s        | |                                   |
   |                                   |                                   |
   |  | tk.ExecuteMultipleCommands(c | |                                   |
   |                                   |                                   |
   |  | ommands, AgEExecMultiCmdResu | |                                   |
   |                                   |                                   |
   |  | ltAction.eContinueOnError)`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

STK interfaces and classes
~~~~~~~~~~~~~~~~~~~~~~~~~~

The STK object model is comprised of programming interfaces that are
implemented by Python classes located in the provided modules. With few
exceptions, classes returned from API methods begin with "Ag" and will
inherit from one or more interfaces (beginning with "IAg"). You may
immediately access any method from the inherited interfaces without
casting, although in some situations casting may help with your IDE
auto-complete feature (see `Refactoring comtypes QueryInterface
calls <pythonMigrationGuide.htm#refactoring-comtypes-calls>`__ for more
information). These classes have a reference to an STK object; this
reference will be removed upon calling del() on the Python class.
Because these classes are references to STK objects, creating them
directly from Python will not be successful; objects must be returned
from STK API methods.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from                       | |                                   |
   |                                   |                                   |
   |  | agi.stk.stkobjects import Ag | |                                   |
   |                                   |                                   |
   |  | Facility, AgESTKObjectType`` | |                                   |
   |                                   |                                   |
   |  | ``try:``                     | |                                   |
   |                                   |                                   |
   |  | ``# this facility is         | |                                   |
   |                                   |                                   |
   |  |  not a valid STK reference`` | |                                   |
   |                                   |                                   |
   |  | ``my_facil                   | |                                   |
   |                                   |                                   |
   |  | ity_attempt = AgFacility()`` | |                                   |
   |                                   |                                   |
   |  | ``my_facility_attempt        | |                                   |
   |                                   |                                   |
   |  | .HeightAboveGround = 123.4`` | |                                   |
   |                                   |                                   |
   |  | ``ex                         | |                                   |
   |                                   |                                   |
   |  | cept STKRuntimeError as e:`` | |                                   |
   |                                   |                                   |
   |  | ``print(e)``                 | |                                   |
   |                                   |                                   |
   |  | ``# this facility rep        | |                                   |
   |                                   |                                   |
   |  | resents a valid STK object`` | |                                   |
   |                                   |                                   |
   |  | ``my_facility = AgFac        | |                                   |
   |                                   |                                   |
   |  | ility(ObjectRoot.CurrentScen | |                                   |
   |                                   |                                   |
   |  | ario.Children.New(AgESTKObje | |                                   |
   |                                   |                                   |
   |  | ctType.eFacility, "fac1"))`` | |                                   |
   |                                   |                                   |
   |  | ``my_facility                | |                                   |
   |                                   |                                   |
   |  | .HeightAboveGround = 123.4`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Collections
~~~~~~~~~~~

Many of the interfaces in the STK API represent collections of items;
such interfaces have the word "Collection" as part of their name. These
classes have an "Item()" method that may be used to get an indexed item
from the collection, but they also support Python indexing and
iteration.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.st            | |                                   |
   |                                   |                                   |
   |  | kdesktop import STKDesktop`` | |                                   |
   |                                   |                                   |
   |  | ``f                          | |                                   |
   |                                   |                                   |
   |  | rom agi.stk.stkutil import A | |                                   |
   |                                   |                                   |
   |  | gEExecMultiCmdResultAction`` | |                                   |
   |                                   |                                   |
   |  | ``stk = STK                  | |                                   |
   |                                   |                                   |
   |  | Desktop.StartApplication()`` | |                                   |
   |                                   |                                   |
   |  | ``connect_commands =         | |                                   |
   |                                   |                                   |
   |  |  ['GetStkVersion /', 'New /  | |                                   |
   |                                   |                                   |
   |  | Scenario ExampleScenario']`` | |                                   |
   |                                   |                                   |
   |  | ``comm                       | |                                   |
   |                                   |                                   |
   |  | and_results = stk.Root.Execu | |                                   |
   |                                   |                                   |
   |  | teMultipleCommands(connect_c | |                                   |
   |                                   |                                   |
   |  | ommands, AgEExecMultiCmdResu | |                                   |
   |                                   |                                   |
   |  | ltAction.eContinueOnError)`` | |                                   |
   |                                   |                                   |
   |  | ``first_message              | |                                   |
   |                                   |                                   |
   |  |  = command_results.Item(0)`` | |                                   |
   |                                   |                                   |
   |  | ``also_first_me              | |                                   |
   |                                   |                                   |
   |  | ssage = command_results[0]`` | |                                   |
   |                                   |                                   |
   |  | ``for m                      | |                                   |
   |                                   |                                   |
   |  | essage in command_results:`` | |                                   |
   |                                   |                                   |
   |  | ``print(message.Count)``     | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Multiple return values
~~~~~~~~~~~~~~~~~~~~~~

Some methods in the API return multiple values rather than returning one
list. The multiple values are returned as a tuple.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``(x, y, z) = my_facility    | |                                   |
   |                                   |                                   |
   |  | .Position.QueryCartesian()`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Colors
~~~~~~

The agi.stk.utilities.colors module contains the Color, ColorRGBA, and
Colors classes used by the STK Python API. The Color class represents an
opaque color constructed from RGB values in the range [0, 255].
ColorRGBA represents a variably-translucent, 4-channel color constructed
from RGBA values in the range [0, 255]. ColorRGBA may not be used in
methods expecting a 3-channel color. Colors contains an assortment of
named colors as well as factory methods to create Color or ColorRGBA
objects from RGB(A) values.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.utilities.c   | |                                   |
   |                                   |                                   |
   |  | olors import Color, Colors`` | |                                   |
   |                                   |                                   |
   |  | `                            | |                                   |
   |                                   |                                   |
   |  | `fac = ObjectRoot.CurrentSce | |                                   |
   |                                   |                                   |
   |  | nario.Children.New(AgESTKObj | |                                   |
   |                                   |                                   |
   |  | ectType.eFacility, "fac1")`` | |                                   |
   |                                   |                                   |
   |  | ``fac.Gr                     | |                                   |
   |                                   |                                   |
   |  | aphics.Color = Colors.Blue`` | |                                   |
   |                                   |                                   |
   |  | ``fac.Graphics.Color = Co    | |                                   |
   |                                   |                                   |
   |  | lor.FromRGB(127, 255, 212)`` | |                                   |
   |                                   |                                   |
   |  | ``(r, g, b) = f              | |                                   |
   |                                   |                                   |
   |  | ac.Graphics.Color.GetRGB()`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Certain methods require a list of 4-channel RGBA color values for
defining per-vertex colors on a geometry. Such a list should be
constructed in Python as a list of Color and/or ColorRGBA objects. Color
objects always have alpha=255 (fully opaque), whereas alpha may be
specified when using the ColorRGBA class. An example of these usages is
provided below.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk12.st          | |                                   |
   |                                   |                                   |
   |  | kdesktop import STKDesktop`` | |                                   |
   |                                   |                                   |
   |  | ``from agi.                  | |                                   |
   |                                   |                                   |
   |  | stk12.utilities.colors impor | |                                   |
   |                                   |                                   |
   |  | t Color, Colors, ColorRGBA`` | |                                   |
   |                                   |                                   |
   |  | ``stk = STKDeskt             | |                                   |
   |                                   |                                   |
   |  | op.StartApplication(visible= | |                                   |
   |                                   |                                   |
   |  | True, userControl = False)`` | |                                   |
   |                                   |                                   |
   |  | ``root = stk.Root``          | |                                   |
   |                                   |                                   |
   |  | ``root.NewScenario('test')`` | |                                   |
   |                                   |                                   |
   |  | ``manager = root.Cu          | |                                   |
   |                                   |                                   |
   |  | rrentScenario.SceneManager`` | |                                   |
   |                                   |                                   |
   |  | ``point =                    | |                                   |
   |                                   |                                   |
   |  |  manager.Initializers.PointB | |                                   |
   |                                   |                                   |
   |  | atchPrimitive.Initialize()`` | |                                   |
   |                                   |                                   |
   |  | ``lla                        | |                                   |
   |                                   |                                   |
   |  | _pts = [ 39.88, -75.25, 0,`` | |                                   |
   |                                   |                                   |
   |  | ``38.85, -77.04, 0,``        | |                                   |
   |                                   |                                   |
   |  | ``37.37, -121.92, 0]``       | |                                   |
   |                                   |                                   |
   |  | ``colors = [ Colors.Red,``   | |                                   |
   |                                   |                                   |
   |  | ``Co                         | |                                   |
   |                                   |                                   |
   |  | lorRGBA(Colors.Blue, 127),`` | |                                   |
   |                                   |                                   |
   |  | ``Colors                     | |                                   |
   |                                   |                                   |
   |  | .FromRGBA(0, 255, 0, 127)]`` | |                                   |
   |                                   |                                   |
   |  | ``poi                        | |                                   |
   |                                   |                                   |
   |  | nt.SetCartographicWithColors | |                                   |
   |                                   |                                   |
   |  | ('Earth', lla_pts, colors)`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Data Types for Data Analysis
----------------------------

This section describes data types you can use in the STK Python API for
data analysis. These data types are standard data types used in popular
Python data science and scientific computing libraries. These data types
are available starting in the STK 12.6+.

NumPy arrays
~~~~~~~~~~~~

You can convert a dataset collection in row format to a NumPy array.
NumPy arrays are N-dimensional arrays with support for fast vector
operations, indexing, and broadcasting. NumPy also offers a broad
collection of standard mathematical functions used in scientific
computing. The NumPy array is a widely supported data structure, in
popular Python scientific computing and machine learning libraries.

The ToNumpyArray() method, called on IAgDrDataSetCollection, returns a
data provider’s results dataset collection as a 2D NumPy array. This
array has a shape equal to the total number of rows in the dataset
collection and the total number of unique columns fields in the dataset
collection. For example, if the computed **All Region By Pass** data
provider results dataset collection contains 100 rows and 11 column
fields, the ToNumpyArray() method would return a NumPy array of the
entire result set and would have a shape of (100, 11), where 100 is the
number of rows and 11 is the number of columns.

To use this functionality, you must have NumPy installed in your local
Python development environment.

Here is an example of using NumPy arrays for flight profile data.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from scipy                 | |                                   |
   |                                   |                                   |
   |  | .spatial import ConvexHull`` | |                                   |
   |                                   |                                   |
   |  | ``impor                      | |                                   |
   |                                   |                                   |
   |  | t matplotlib.pyplot as plt`` | |                                   |
   |                                   |                                   |
   |  | ``# compute data pro         | |                                   |
   |                                   |                                   |
   |  | vider results for an aircraf | |                                   |
   |                                   |                                   |
   |  | t's Flight Profile By Time`` | |                                   |
   |                                   |                                   |
   |  | ``field_name                 | |                                   |
   |                                   |                                   |
   |  | s = ['Mach #', 'Altitude']`` | |                                   |
   |                                   |                                   |
   |  | ``time_step_sec = 1.0``      | |                                   |
   |                                   |                                   |
   |  | ``fl                         | |                                   |
   |                                   |                                   |
   |  | ight_profile_data_provider = | |                                   |
   |                                   |                                   |
   |  |  aircraft.DataProviders.Item | |                                   |
   |                                   |                                   |
   |  | ('Flight Profile By Time')`` | |                                   |
   |                                   |                                   |
   |  | ``flight_profile_data        | |                                   |
   |                                   |                                   |
   |  | = flight_profile_data_provid | |                                   |
   |                                   |                                   |
   |  | er.ExecElements(scenario.Sta | |                                   |
   |                                   |                                   |
   |  | rtTime, scenario.StopTime, t | |                                   |
   |                                   |                                   |
   |  | ime_step_sec, field_names)`` | |                                   |
   |                                   |                                   |
   |  | ``# conve                    | |                                   |
   |                                   |                                   |
   |  | rt dataset collection in a r | |                                   |
   |                                   |                                   |
   |  | ow format as a Numpy array`` | |                                   |
   |                                   |                                   |
   |  | ``flight_profile_            | |                                   |
   |                                   |                                   |
   |  | data_arr = flight_profile_da | |                                   |
   |                                   |                                   |
   |  | ta.DataSets.ToNumpyArray()`` | |                                   |
   |                                   |                                   |
   |  | ``#                          | |                                   |
   |                                   |                                   |
   |  | get shape of array (number o | |                                   |
   |                                   |                                   |
   |  | f rows, number of columns)`` | |                                   |
   |                                   |                                   |
   |  | ``print(flig                 | |                                   |
   |                                   |                                   |
   |  | ht_profile_data_arr.shape)`` | |                                   |
   |                                   |                                   |
   |  | ``# plot estimated fligth    | |                                   |
   |                                   |                                   |
   |  |  envelope as a convex hull`` | |                                   |
   |                                   |                                   |
   |  | ``hull = ConvexHul           | |                                   |
   |                                   |                                   |
   |  | l(flight_profile_data_arr)`` | |                                   |
   |                                   |                                   |
   |  | ``p                          | |                                   |
   |                                   |                                   |
   |  | lt.figure(figsize=(15,10))`` | |                                   |
   |                                   |                                   |
   |  | ``for                        | |                                   |
   |                                   |                                   |
   |  | simplex in hull.simplices:`` | |                                   |
   |                                   |                                   |
   |  | ``plt.plot(flight_pr         | |                                   |
   |                                   |                                   |
   |  | ofile_data_arr[simplex, 1],  | |                                   |
   |                                   |                                   |
   |  | flight_profile_data_arr[simp | |                                   |
   |                                   |                                   |
   |  | lex, 0], color="darkblue")`` | |                                   |
   |                                   |                                   |
   |  | ``plt.title('Estimated Flig  | |                                   |
   |                                   |                                   |
   |  | ht Envelope', fontsize=15)`` | |                                   |
   |                                   |                                   |
   |  | ``plt.xlabel('               | |                                   |
   |                                   |                                   |
   |  | Mach Number', fontsize=15)`` | |                                   |
   |                                   |                                   |
   |  | ``plt.ylabe                  | |                                   |
   |                                   |                                   |
   |  | l('Altitude', fontsize=15)`` | |                                   |
   |                                   |                                   |
   |  | ``plt.tick_para              | |                                   |
   |                                   |                                   |
   |  | ms(axis='x', labelsize=15)`` | |                                   |
   |                                   |                                   |
   |  | ``plt.tick_para              | |                                   |
   |                                   |                                   |
   |  | ms(axis='y', labelsize=15)`` | |                                   |
   |                                   |                                   |
   |  | ``plt.grid()``               | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

The resulting flight data plot then looks like this:

|image1|

For more information, see `NumPy <https://numpy.org/>`__.

Pandas DataFrame
~~~~~~~~~~~~~~~~

You can convert a dataset collection in row format as a Pandas
DataFrame. DataFrames are the key to Pandas’ fast and efficient data
manipulation and analysis functionality. They are a two-dimensional,
tabular data structure with labeled indexing for rows and columns, where
the columns can contain data of various data types. DataFrames supports
powerful aggregation and transformation functionality, time series
functionality, merging and joining operations of datasets, hierarchical
indexing, vectorized operations, flexible reshaping functionality, and
much more.

The ToPandasDataFrame() method called on IAgDrDataSetCollection, returns
a data provider’s results dataset collection as Pandas DataFrame. The
DataFrame row index length, equal to the total number of rows in the
dataset collection and each column in the DataFrame, maps to a unique
field name in the dataset collection. For example, if the computed
**Flight Profile by Time** data provider results dataset collection
contains 6000 rows and 100 fields column fields, the returned DataFrame
will have a row index length of 6000 and 100 columns.

To use this functionality, you must have Pandas installed in your local
Python development environment.

Here are four examples of using Pandas DataFrame.

*Example 1*: Convert **All Regions By Pass** data provider results to a
Pandas DataFrame with a default numeric row index. The Python
implementation would look like this:

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# compute                  | |                                   |
   |                                   |                                   |
   |  | data provider results for Al | |                                   |
   |                                   |                                   |
   |  | l Regions by Pass coverage`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_data_provide      | |                                   |
   |                                   |                                   |
   |  | r = coverage.DataProviders.I | |                                   |
   |                                   |                                   |
   |  | tem('All Regions By Pass')`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_data = cov        | |                                   |
   |                                   |                                   |
   |  | erage_data_provider.Exec()`` | |                                   |
   |                                   |                                   |
   |  | ``# convert datas            | |                                   |
   |                                   |                                   |
   |  | et collection in a row forma | |                                   |
   |                                   |                                   |
   |  | t as a Pandas DataFrame with | |                                   |
   |                                   |                                   |
   |  |  default numeric row index`` | |                                   |
   |                                   |                                   |
   |  | ``cov                        | |                                   |
   |                                   |                                   |
   |  | erage_arr = coverage_data.Da | |                                   |
   |                                   |                                   |
   |  | taSets.ToPandasDataFrame()`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

The ToPandasDataFrame() method supports setting a single column as the
index. To create a hierarchical index or a composite index comprised of
more than a single column, get your data provider’s results dataset
collection as a Pandas DataFrame with the default numeric index, then
update the index accordingly.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# compute data provide     | |                                   |
   |                                   |                                   |
   |  | r results for basic Access`` | |                                   |
   |                                   |                                   |
   |  | ``field_names = ['           | |                                   |
   |                                   |                                   |
   |  | Access Number', 'Start Time' | |                                   |
   |                                   |                                   |
   |  | , 'Stop Time', 'Duration']`` | |                                   |
   |                                   |                                   |
   |  | ``time_step_sec = 1.0``      | |                                   |
   |                                   |                                   |
   |  | ``ac                         | |                                   |
   |                                   |                                   |
   |  | cess_data_provider = facilit | |                                   |
   |                                   |                                   |
   |  | y_sensor_satellite_access.Da | |                                   |
   |                                   |                                   |
   |  | taProviders.Item('Access')`` | |                                   |
   |                                   |                                   |
   |  | ``acce                       | |                                   |
   |                                   |                                   |
   |  | ss_data = access_data_provid | |                                   |
   |                                   |                                   |
   |  | er.ExecElements(scenario.Sta | |                                   |
   |                                   |                                   |
   |  | rtTime, scenario.StopTime, t | |                                   |
   |                                   |                                   |
   |  | ime_step_sec, field_names)`` | |                                   |
   |                                   |                                   |
   |  | ``# convert da               | |                                   |
   |                                   |                                   |
   |  | taset collection in a row fo | |                                   |
   |                                   |                                   |
   |  | rmat as a Pandas DataFrame`` | |                                   |
   |                                   |                                   |
   |  | ``inde                       | |                                   |
   |                                   |                                   |
   |  | x_column = 'Access Number'`` | |                                   |
   |                                   |                                   |
   |  | ``access                     | |                                   |
   |                                   |                                   |
   |  | _data_df = access_data.DataS | |                                   |
   |                                   |                                   |
   |  | ets.ToPandasDataFrame(index_ | |                                   |
   |                                   |                                   |
   |  | element_name=index_column)`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

*Example 2*: Compute descriptive statistics access measurements. The
implementation in Python would be:

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# compute                  | |                                   |
   |                                   |                                   |
   |  | data provider results for Al | |                                   |
   |                                   |                                   |
   |  | l Regions by Pass coverage`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_data_provide      | |                                   |
   |                                   |                                   |
   |  | r = coverage.DataProviders.I | |                                   |
   |                                   |                                   |
   |  | tem('All Regions By Pass')`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_data = cov        | |                                   |
   |                                   |                                   |
   |  | erage_data_provider.Exec()`` | |                                   |
   |                                   |                                   |
   |  | ``# convert datas            | |                                   |
   |                                   |                                   |
   |  | et collection in a row forma | |                                   |
   |                                   |                                   |
   |  | t as a Pandas DataFrame with | |                                   |
   |                                   |                                   |
   |  |  default numeric row index`` | |                                   |
   |                                   |                                   |
   |  | ``all_regions_co             | |                                   |
   |                                   |                                   |
   |  | verage_df = coverage_data.Da | |                                   |
   |                                   |                                   |
   |  | taSets.ToPandasDataFrame()`` | |                                   |
   |                                   |                                   |
   |  | ``# comptue descriptive s    | |                                   |
   |                                   |                                   |
   |  | tatistics of Duration, Perce | |                                   |
   |                                   |                                   |
   |  | nt Coverage, Area Coverage`` | |                                   |
   |                                   |                                   |
   |  | ``all                        | |                                   |
   |                                   |                                   |
   |  | _regions_coverage_df[['durat | |                                   |
   |                                   |                                   |
   |  | ion', 'percent coverage', 'a | |                                   |
   |                                   |                                   |
   |  | rea coverage']].describe()`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

This produces the following data table:

|image2|

*Example 3*: Compute descriptive statistics access measurements grouped
by **Asset Name** (Satellite Names). The Python implementation would be
as follows:

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``def q1(x):``               | |                                   |
   |                                   |                                   |
   |  | ``return x.quantile(0.25)``  | |                                   |
   |                                   |                                   |
   |  | ``def q2(x):``               | |                                   |
   |                                   |                                   |
   |  | ``return x.quantile(0.50)``  | |                                   |
   |                                   |                                   |
   |  | ``def q3(x):``               | |                                   |
   |                                   |                                   |
   |  | ``return x.quantile(0.75)``  | |                                   |
   |                                   |                                   |
   |  | ``# compute                  | |                                   |
   |                                   |                                   |
   |  | data provider results for Al | |                                   |
   |                                   |                                   |
   |  | l Regions by Pass coverage`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_data_provide      | |                                   |
   |                                   |                                   |
   |  | r = coverage.DataProviders.I | |                                   |
   |                                   |                                   |
   |  | tem('All Regions By Pass')`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_data = cov        | |                                   |
   |                                   |                                   |
   |  | erage_data_provider.Exec()`` | |                                   |
   |                                   |                                   |
   |  | ``# convert datas            | |                                   |
   |                                   |                                   |
   |  | et collection in a row forma | |                                   |
   |                                   |                                   |
   |  | t as a Pandas DataFrame with | |                                   |
   |                                   |                                   |
   |  |  default numeric row index`` | |                                   |
   |                                   |                                   |
   |  | ``all_regions_co             | |                                   |
   |                                   |                                   |
   |  | verage_df = coverage_data.Da | |                                   |
   |                                   |                                   |
   |  | taSets.ToPandasDataFrame()`` | |                                   |
   |                                   |                                   |
   |  | ``#                          | |                                   |
   |                                   |                                   |
   |  |  comptue descriptive statist | |                                   |
   |                                   |                                   |
   |  | ics of Duration, Percent Cov | |                                   |
   |                                   |                                   |
   |  | erage, Area Coverage grouped | |                                   |
   |                                   |                                   |
   |  |  by Asset Name (Satellite)`` | |                                   |
   |                                   |                                   |
   |  | ``all_region_cove            | |                                   |
   |                                   |                                   |
   |  | rage_df.groupby('asset name' | |                                   |
   |                                   |                                   |
   |  | ).agg({'duration': ['mean',  | |                                   |
   |                                   |                                   |
   |  | 'min', q1, q2, q3, 'max'],`` | |                                   |
   |                                   |                                   |
   |  | ``'                          | |                                   |
   |                                   |                                   |
   |  | percent coverage': ['mean',  | |                                   |
   |                                   |                                   |
   |  | 'min', q1, q2, q3, 'max'],`` | |                                   |
   |                                   |                                   |
   |  | ``'area coverage': ['mean',  | |                                   |
   |                                   |                                   |
   |  |  'min', q1, q2, q3, 'max']`` | |                                   |
   |                                   |                                   |
   |  | ``}).T``                     | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

This produces the following data table:

|image3|

*Example 4*: Plot a heat map of **Duration By Asset** (Satellite) for
each access region. The Python implementation would be:

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``import seaborn as s        | |                                   |
   |                                   |                                   |
   |  | ns; sns.set_style('ticks')`` | |                                   |
   |                                   |                                   |
   |  | ``from matpl                 | |                                   |
   |                                   |                                   |
   |  | otlib import pyplot as plt`` | |                                   |
   |                                   |                                   |
   |  | ``# compute                  | |                                   |
   |                                   |                                   |
   |  | data provider results for Al | |                                   |
   |                                   |                                   |
   |  | l Regions by Pass coverage`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_data_provide      | |                                   |
   |                                   |                                   |
   |  | r = coverage.DataProviders.I | |                                   |
   |                                   |                                   |
   |  | tem('All Regions By Pass')`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_data = cov        | |                                   |
   |                                   |                                   |
   |  | erage_data_provider.Exec()`` | |                                   |
   |                                   |                                   |
   |  | ``# convert datas            | |                                   |
   |                                   |                                   |
   |  | et collection in a row forma | |                                   |
   |                                   |                                   |
   |  | t as a Pandas DataFrame with | |                                   |
   |                                   |                                   |
   |  |  default numeric row index`` | |                                   |
   |                                   |                                   |
   |  | ``coverage_                  | |                                   |
   |                                   |                                   |
   |  | all_regions_elements = cover | |                                   |
   |                                   |                                   |
   |  | age_data_provider.Elements`` | |                                   |
   |                                   |                                   |
   |  | ``all_regi                   | |                                   |
   |                                   |                                   |
   |  | ons_coverage_df = coverage_d | |                                   |
   |                                   |                                   |
   |  | ata.DataSets.ToPandasDataFra | |                                   |
   |                                   |                                   |
   |  | me(dataProviderElements=cove | |                                   |
   |                                   |                                   |
   |  | rage_all_regions_elements)`` | |                                   |
   |                                   |                                   |
   |  | ``# reshape the DataFr       | |                                   |
   |                                   |                                   |
   |  | ame based on column values`` | |                                   |
   |                                   |                                   |
   |  | ``pivot = all_region_cov     | |                                   |
   |                                   |                                   |
   |  | erage_df.pivot_table(index=' | |                                   |
   |                                   |                                   |
   |  | region name', columns='asset | |                                   |
   |                                   |                                   |
   |  |  name', values='duration')`` | |                                   |
   |                                   |                                   |
   |  | ``# plo                      | |                                   |
   |                                   |                                   |
   |  | t heat map that shows durati | |                                   |
   |                                   |                                   |
   |  | on by asset name by region`` | |                                   |
   |                                   |                                   |
   |  | ``p                          | |                                   |
   |                                   |                                   |
   |  | lt.figure(figsize=(20,10))`` | |                                   |
   |                                   |                                   |
   |  | ``ax = sns.hea               | |                                   |
   |                                   |                                   |
   |  | tmap(pivot, cmap="YlGnBu")`` | |                                   |
   |                                   |                                   |
   |  | ``ax.set_xlabel('Durati      | |                                   |
   |                                   |                                   |
   |  | on by Asset', fontsize=20)`` | |                                   |
   |                                   |                                   |
   |  | ``ax.set_ylabel('            | |                                   |
   |                                   |                                   |
   |  | Region Name', fontsize=20)`` | |                                   |
   |                                   |                                   |
   |  | ``plt.tick_para              | |                                   |
   |                                   |                                   |
   |  | ms(axis='x', labelsize=15)`` | |                                   |
   |                                   |                                   |
   |  | ``plt.tick_para              | |                                   |
   |                                   |                                   |
   |  | ms(axis='y', labelsize=15)`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

This produces the following data map:

|image4|

See `Pandas <https://pandas.pydata.org/>`__ for more information,
including library documentation.

Exceptions
----------

The table below describes the exceptions that are provided by the
agi.stk.utilities.exceptions module with the STK Python API.

+-----------------------------------+-----------------------------------+
| Exception                         | Description                       |
+===================================+===================================+
| STKInitializationError            | Raised in STKDesktop and          |
|                                   | STKEngine when unable to          |
|                                   | initialize or attach to STK.      |
+-----------------------------------+-----------------------------------+
| STKInvalidCastError               | Raised when attempting to cast an |
|                                   | object to an unsupported          |
|                                   | interface or class type.          |
+-----------------------------------+-----------------------------------+
| STKRuntimeError                   | Raised when an STK method call    |
|                                   | fails.                            |
+-----------------------------------+-----------------------------------+
| STKAttributeError                 | Raised when attempting to set an  |
|                                   | unrecognized attribute within the |
|                                   | STK API.                          |
|                                   |                                   |
|                                   | Make sure the spelling and        |
|                                   | capitalization is correct.        |
+-----------------------------------+-----------------------------------+

Events
------

Support for events was added in STK 12.2.0. Events can be accessed
directly in applicable parent objects, as seen in the table below.

+----------------------------------+----------------------------------+
| Event Interface                  | Parent Object                    |
+==================================+==================================+
| `IAgStkObje                      | `IAgStkObjectRoot <../DocX/STKO  |
| ctRootEvents <../DocX/STKObjects | bjects~IAgStkObjectRoot.html>`__ |
| ~IAgStkObjectRootEvents.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `IAgS                            | `agi.stk.stkengine.STKE          |
| TKXApplicationEvents <../DocX/ST | ngineApplication <#STKEngine>`__ |
| KXLib~AgSTKXApplication.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `IAgUiAxVOCntrlEvents <../Doc    | `agi.stk.stkengine.tkcontrols.G  |
| X/STKXLib~AgUiAxVOCntrl.html>`__ | lobeControl <#TkinterContols>`__ |
+----------------------------------+----------------------------------+
| `IAgUiAx2DCntrlEvents <../Doc    | `agi.stk.stkengine.tkcontrols    |
| X/STKXLib~AgUiAx2DCntrl.html>`__ | .MapControl <#TkinterContols>`__ |
+----------------------------------+----------------------------------+
| `IAgStkGraphicsSceneEve          | `IAgStkGrap                      |
| nts <../DocX/AgSTKGraphicsLib~IA | hicsScene <../DocX/AgSTKGraphics |
| gStkGraphicsSceneEvents.html>`__ | Lib~IAgStkGraphicsScene.html>`__ |
+----------------------------------+----------------------------------+
| `IA                              | `IAgStkGraphicsKmlGraph          |
| gStkGraphicsKmlGraphicsEvents <. | ics <../DocX/AgSTKGraphicsLib~IA |
| ./DocX/AgSTKGraphicsLib~IAgStkGr | gStkGraphicsKmlGraphics.html>`__ |
| aphicsKmlGraphicsEvents.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `IAgStkGrap                      | `IAgStkGraphicsImageCollection   |
| hicsImageCollectionEvents <../Do | <../DocX/AgSTKGraphicsLib~IAgStk |
| cX/AgSTKGraphicsLib~IAgStkGraphi | GraphicsImageCollection.html>`__ |
| csImageCollectionEvents.html>`__ |                                  |
+----------------------------------+----------------------------------+
| `IAgStkGraphics                  | `IA                              |
| TerrainCollectionEvents <../DocX | gStkGraphicsTerrainCollection <. |
| /AgSTKGraphicsLib~IAgStkGraphics | ./DocX/AgSTKGraphicsLib~IAgStkGr |
| TerrainCollectionEvents.html>`__ | aphicsTerrainCollection.html>`__ |
+----------------------------------+----------------------------------+

Events are accessed through the Subscribe() method on the parent object,
which returns an event handler subscribed to events on the queried
object. You can add or remove Event callbacks in the event handler using
the "+=" and "-=" operators; these operators will change the callbacks
that will get executed by the event but will not affect whether the
handler remains subscribed. The event handler should be unsubscribed
using the Unsubscribe() method when event handling is no longer needed.
Refer to the following example for using IAgStkObjectRootEvents.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.              | |                                   |
   |                                   |                                   |
   |  | stkengine import STKEngine`` | |                                   |
   |                                   |                                   |
   |  | ``def onScen                 | |                                   |
   |                                   |                                   |
   |  | arioNewCallback(Path:str):`` | |                                   |
   |                                   |                                   |
   |  | ``print(f'Scenario           | |                                   |
   |                                   |                                   |
   |  | {Path} has been created.')`` | |                                   |
   |                                   |                                   |
   |  | ``stk = ST                   | |                                   |
   |                                   |                                   |
   |  | KEngine.StartApplication()`` | |                                   |
   |                                   |                                   |
   |  | ``                           | |                                   |
   |                                   |                                   |
   |  | root = stk.NewObjectRoot()`` | |                                   |
   |                                   |                                   |
   |  | ``stkObjectRoo               | |                                   |
   |                                   |                                   |
   |  | tEvents = root.Subscribe()`` | |                                   |
   |                                   |                                   |
   |  | ``stkO                       | |                                   |
   |                                   |                                   |
   |  | bjectRootEvents.OnScenarioNe | |                                   |
   |                                   |                                   |
   |  | w += onScenarioNewCallback`` | |                                   |
   |                                   |                                   |
   |  | ``root.NewS                  | |                                   |
   |                                   |                                   |
   |  | cenario('ExampleScenario')`` | |                                   |
   |                                   |                                   |
   |  | ``# callb                    | |                                   |
   |                                   |                                   |
   |  | ack should be executed now`` | |                                   |
   |                                   |                                   |
   |  | ``# remove the               | |                                   |
   |                                   |                                   |
   |  |  callback from the handler`` | |                                   |
   |                                   |                                   |
   |  | ``stkO                       | |                                   |
   |                                   |                                   |
   |  | bjectRootEvents.OnScenarioNe | |                                   |
   |                                   |                                   |
   |  | w -= onScenarioNewCallback`` | |                                   |
   |                                   |                                   |
   |  | ``# all finishe              | |                                   |
   |                                   |                                   |
   |  | d with events, unsubscribe`` | |                                   |
   |                                   |                                   |
   |  | ``stkObje                    | |                                   |
   |                                   |                                   |
   |  | ctRootEvents.Unsubscribe()`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

.. container::

   The STK Desktop application user interface might become unresponsive
   to user input when Python has event subscribers, and STK tries to
   call back into the Python interpreter to notify of an event. That
   callback relies on the Windows message loop to be dispatched. To work
   around this issue, Windows messages need to be dispatched through the
   Windows message queue. This can be accomplished in different ways
   depending on the type of Python script that is executing (console or
   user interface), and on the type of user interface library being
   used. For instance, if you use the tkinter user interface library, a
   simple way of accomplishing this with this library is to create a
   tkinter window while using the desktop application user interface. No
   action is needed if Python is used only for automation. The following
   script is an example showing this issue.

   .. container:: LanguageSpecific
      :name: Example_Python

      +-----------------------------------+-----------------------------------+
      | [Python - STK API]                |                                   |
      +===================================+===================================+
      | .. container:: LanguageSpecific   |                                   |
      |    :name: Code_Python             |                                   |
      |                                   |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      |                                   |                                   |
      |  | ``from agi.stk.st            | |                                   |
      |                                   |                                   |
      |  | kdesktop import STKDesktop`` | |                                   |
      |                                   |                                   |
      |  | ``from agi.stk.stkobjec      | |                                   |
      |                                   |                                   |
      |  | ts import AgESTKObjectType`` | |                                   |
      |                                   |                                   |
      |  | ``def onStkObje              | |                                   |
      |                                   |                                   |
      |  | ctAddedCallback(Path:str):`` | |                                   |
      |                                   |                                   |
      |  | ``print(                     | |                                   |
      |                                   |                                   |
      |  | f'{Path} has been added.')`` | |                                   |
      |                                   |                                   |
      |  | ``stk = STKDesktop.Star      | |                                   |
      |                                   |                                   |
      |  | tApplication(visible=True)`` | |                                   |
      |                                   |                                   |
      |  | ``root = stk.Root``          | |                                   |
      |                                   |                                   |
      |  | ``root.NewS                  | |                                   |
      |                                   |                                   |
      |  | cenario('ExampleScenario')`` | |                                   |
      |                                   |                                   |
      |  | ``stkObjectRoo               | |                                   |
      |                                   |                                   |
      |  | tEvents = root.Subscribe()`` | |                                   |
      |                                   |                                   |
      |  | ``stkObjectR                 | |                                   |
      |                                   |                                   |
      |  | ootEvents.OnStkObjectAdded + | |                                   |
      |                                   |                                   |
      |  | = onStkObjectAddedCallback`` | |                                   |
      |                                   |                                   |
      |  | `                            | |                                   |
      |                                   |                                   |
      |  | `sc = root.CurrentScenario`` | |                                   |
      |                                   |                                   |
      |  | ``#o                         | |                                   |
      |                                   |                                   |
      |  | nStkObjectAddedCallback will | |                                   |
      |                                   |                                   |
      |  |  be successfully called when | |                                   |
      |                                   |                                   |
      |  |  the next line is executed`` | |                                   |
      |                                   |                                   |
      |  | ``fac                        | |                                   |
      |                                   |                                   |
      |  | = sc.Children.New(AgESTKObje | |                                   |
      |                                   |                                   |
      |  | ctType.eFacility, 'AGIHQ')`` | |                                   |
      |                                   |                                   |
      |  | ``#Now switch control t      | |                                   |
      |                                   |                                   |
      |  | o the desktop application an | |                                   |
      |                                   |                                   |
      |  | d create another facility.`` | |                                   |
      |                                   |                                   |
      |  | ``#The user interface        | |                                   |
      |                                   |                                   |
      |  |  will become unresponsive.`` | |                                   |
      |                                   |                                   |
      |  | ``#N                         | |                                   |
      |                                   |                                   |
      |  | ow open a tkinter window tha | |                                   |
      |                                   |                                   |
      |  | t processing COM messages.`` | |                                   |
      |                                   |                                   |
      |  | ``from tkinter import Tk``   | |                                   |
      |                                   |                                   |
      |  | ``window = Tk()``            | |                                   |
      |                                   |                                   |
      |  | ``window.mainloop()``        | |                                   |
      |                                   |                                   |
      |  | ``#Switch control t          | |                                   |
      |                                   |                                   |
      |  | o the desktop application an | |                                   |
      |                                   |                                   |
      |  | d create another facility.`` | |                                   |
      |                                   |                                   |
      |  | `                            | |                                   |
      |                                   |                                   |
      |  | `#The user interface will be | |                                   |
      |                                   |                                   |
      |  |  responsive and the event ca | |                                   |
      |                                   |                                   |
      |  | llback will be successful.`` | |                                   |
      |                                   |                                   |
      |  +------------------------------+ |                                   |
      +-----------------------------------+-----------------------------------+

STK's Built-in Python Plugins
-----------------------------

Starting in version 12.4, STK has multi-platform Python plugins
available for some plugin points. You can use these plugin points d by
supplying STK with a Python script implementing the plugin interface.
For more information about configuring Python plugins, visit `the Python
plugin
documentation <../../Subsystems/pluginScripts/Content/pythonpoint.htm>`__.

API modules
~~~~~~~~~~~

Most plugins utilize interfaces in the STK API for getting data from and
sending data to STK. Interfaces specific to plugins have been added to
agi.stk.plugins. Using the STK object model within a plugin is possible
by obtaining the object root in the Init method of the plugin using
`IAgStkPluginSite.StkObjectRoot <../DocX/AgStkPlugin~IAgStkPluginSite~StkObjectRoot.html>`__.

File structure
~~~~~~~~~~~~~~

The following example Calc Scalar plugin is used to highlight the
structure of a Python plugin using the STK Python API. While the file
may have any name, the plugin class name is a requirement (e.g.,
CAgCrdnCalcScalarPythonPlugin). All methods defined in the plugin
interface (e.g., IAgCrdnCalcScalarPythonPlugin) must be defined in the
class.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``import typing``            | |                                   |
   |                                   |                                   |
   |  | ``from                       | |                                   |
   |                                   |                                   |
   |  |  agi.stk.plugins.crdnplugin  | |                                   |
   |                                   |                                   |
   |  | import IAgCrdnCalcScalarPlug | |                                   |
   |                                   |                                   |
   |  | inResultReg, IAgCrdnCalcScal | |                                   |
   |                                   |                                   |
   |  | arPluginResultReset, IAgCrdn | |                                   |
   |                                   |                                   |
   |  | CalcScalarPluginResultEval`` | |                                   |
   |                                   |                                   |
   |  | ``from agi.stk.plug          | |                                   |
   |                                   |                                   |
   |  | ins.utplugin import IAgUtPlu | |                                   |
   |                                   |                                   |
   |  | ginConfig, AgEUtLogMsgType`` | |                                   |
   |                                   |                                   |
   |  | ``from                       | |                                   |
   |                                   |                                   |
   |  |  agi.stk.plugins.attrautomat | |                                   |
   |                                   |                                   |
   |  | ion import AgEAttrAddFlags`` | |                                   |
   |                                   |                                   |
   |  | `                            | |                                   |
   |                                   |                                   |
   |  | `from agi.stk.plugins.stkplu | |                                   |
   |                                   |                                   |
   |  | gin import AgStkPluginSite`` | |                                   |
   |                                   |                                   |
   |  | ``# The cla                  | |                                   |
   |                                   |                                   |
   |  | ss name may not be changed`` | |                                   |
   |                                   |                                   |
   |  | ``class CAgCrd               | |                                   |
   |                                   |                                   |
   |  | nCalcScalarPlugin(object):`` | |                                   |
   |                                   |                                   |
   |  | ``def __init__(self):``      | |                                   |
   |                                   |                                   |
   |  | ``self.scope = None``        | |                                   |
   |                                   |                                   |
   |  | ``self.site = None``         | |                                   |
   |                                   |                                   |
   |  | ``self.root = None``         | |                                   |
   |                                   |                                   |
   |  | ``self.Object                | |                                   |
   |                                   |                                   |
   |  | TrajectoryCatesianX = None`` | |                                   |
   |                                   |                                   |
   |  | ``#plugin co                 | |                                   |
   |                                   |                                   |
   |  | nfiguration properties - mus | |                                   |
   |                                   |                                   |
   |  | t be configured in GetPlugin | |                                   |
   |                                   |                                   |
   |  | Config for STK to use them`` | |                                   |
   |                                   |                                   |
   |  | ``self.scale_factor = 1.23`` | |                                   |
   |                                   |                                   |
   |  | ``# Define all methods       | |                                   |
   |                                   |                                   |
   |  | in IAgCrdnCalcScalarPlugin`` | |                                   |
   |                                   |                                   |
   |  | ``def Init(self, site:"      | |                                   |
   |                                   |                                   |
   |  | IAgUtPluginSite") -> bool:`` | |                                   |
   |                                   |                                   |
   |  | ``self.si                    | |                                   |
   |                                   |                                   |
   |  | te = AgStkPluginSite(site)`` | |                                   |
   |                                   |                                   |
   |  | ``self.root = self.sit       | |                                   |
   |                                   |                                   |
   |  | e.StkRootObject # Gain acces | |                                   |
   |                                   |                                   |
   |  | s to STK Object Model for us | |                                   |
   |                                   |                                   |
   |  | e within the plugin script`` | |                                   |
   |                                   |                                   |
   |  | ``self.sit                   | |                                   |
   |                                   |                                   |
   |  | e.Message(AgEUtLogMsgType.eU | |                                   |
   |                                   |                                   |
   |  | tLogMsgInfo, f'{self.display | |                                   |
   |                                   |                                   |
   |  | _name} has been initialized  | |                                   |
   |                                   |                                   |
   |  | by {self.site.SiteName}.')`` | |                                   |
   |                                   |                                   |
   |  | ``return True``              | |                                   |
   |                                   |                                   |
   |  | ``def Register(sel           | |                                   |
   |                                   |                                   |
   |  | f, result:"IAgCrdnCalcScalar | |                                   |
   |                                   |                                   |
   |  | PluginResultReg") -> None:`` | |                                   |
   |                                   |                                   |
   |  | ``o                          | |                                   |
   |                                   |                                   |
   |  | bjPath = result.ObjectPath`` | |                                   |
   |                                   |                                   |
   |  | ``resul                      | |                                   |
   |                                   |                                   |
   |  | t.ShortDescription = "Compon | |                                   |
   |                                   |                                   |
   |  | ent created on " + objPath`` | |                                   |
   |                                   |                                   |
   |  | ``def Reset(self,            | |                                   |
   |                                   |                                   |
   |  |  result:"IAgCrdnCalcScalarPl | |                                   |
   |                                   |                                   |
   |  | uginResultReset") -> bool:`` | |                                   |
   |                                   |                                   |
   |  | ``#<                         | |                                   |
   |                                   |                                   |
   |  | MyObject>, <MySelf>, <MyPare | |                                   |
   |                                   |                                   |
   |  | nt>, <MyGrandParent> are val | |                                   |
   |                                   |                                   |
   |  | id keywords for sourceName`` | |                                   |
   |                                   |                                   |
   |  | ``self.                      | |                                   |
   |                                   |                                   |
   |  | ObjectTrajectoryCatesianX =  | |                                   |
   |                                   |                                   |
   |  | result.CalcToolProvider.GetC | |                                   |
   |                                   |                                   |
   |  | alcScalar("Trajectory(CBF).C | |                                   |
   |                                   |                                   |
   |  | artesian.X", "<MyObject>")`` | |                                   |
   |                                   |                                   |
   |  | ``return True``              | |                                   |
   |                                   |                                   |
   |  | ``def Evaluate(self          | |                                   |
   |                                   |                                   |
   |  | , result:"IAgCrdnCalcScalarP | |                                   |
   |                                   |                                   |
   |  | luginResultEval") -> bool:`` | |                                   |
   |                                   |                                   |
   |  | ``if self.ObjectTrajec       | |                                   |
   |                                   |                                   |
   |  | toryCatesianX is not None:`` | |                                   |
   |                                   |                                   |
   |  | ``(x, errFlag_x) = sel       | |                                   |
   |                                   |                                   |
   |  | f.ObjectTrajectoryCatesianX. | |                                   |
   |                                   |                                   |
   |  | CurrentValue_Array(result)`` | |                                   |
   |                                   |                                   |
   |  | ``if errFlag_x is            | |                                   |
   |                                   |                                   |
   |  | not None and errFlag_x!=0:`` | |                                   |
   |                                   |                                   |
   |  | ``result.Set                 | |                                   |
   |                                   |                                   |
   |  | Value(x*self.scale_factor)`` | |                                   |
   |                                   |                                   |
   |  | ``return True``              | |                                   |
   |                                   |                                   |
   |  | ``return False``             | |                                   |
   |                                   |                                   |
   |  | ``def Free(self) -> None:``  | |                                   |
   |                                   |                                   |
   |  | ``self.scope = None``        | |                                   |
   |                                   |                                   |
   |  | ``self.site = None``         | |                                   |
   |                                   |                                   |
   |  | ``self.root = None``         | |                                   |
   |                                   |                                   |
   |  | ``self.Object                | |                                   |
   |                                   |                                   |
   |  | TrajectoryCatesianX = None`` | |                                   |
   |                                   |                                   |
   |  | ``def GetPluginConf          | |                                   |
   |                                   |                                   |
   |  | ig(self, pAttrBuilder:"IAgAt | |                                   |
   |                                   |                                   |
   |  | trBuilder") -> typing.Any:`` | |                                   |
   |                                   |                                   |
   |  | ``''' Defining GetPlugi      | |                                   |
   |                                   |                                   |
   |  | nConfig is only necessary if | |                                   |
   |                                   |                                   |
   |  |  adding configuration proper | |                                   |
   |                                   |                                   |
   |  | ties accessible to STK '''`` | |                                   |
   |                                   |                                   |
   |  | ``if self.scope is None:``   | |                                   |
   |                                   |                                   |
   |  | ``self.scope                 | |                                   |
   |                                   |                                   |
   |  |  = pAttrBuilder.NewScope()`` | |                                   |
   |                                   |                                   |
   |  | ``pA                         | |                                   |
   |                                   |                                   |
   |  | ttrBuilder.AddDoubleDispatch | |                                   |
   |                                   |                                   |
   |  | Property( self.scope, "Scale | |                                   |
   |                                   |                                   |
   |  | Factor", "A double used to s | |                                   |
   |                                   |                                   |
   |  | cale the plugin evaluation r | |                                   |
   |                                   |                                   |
   |  | esult", "scale_factor", AgEA | |                                   |
   |                                   |                                   |
   |  | ttrAddFlags.eAddFlagNone )`` | |                                   |
   |                                   |                                   |
   |  | ``return self.scope``        | |                                   |
   |                                   |                                   |
   |  | ``def V                      | |                                   |
   |                                   |                                   |
   |  | erifyPluginConfig(self, pPlu | |                                   |
   |                                   |                                   |
   |  | ginCfgResult:"IAgUtPluginCon | |                                   |
   |                                   |                                   |
   |  | figVerifyResult") -> None:`` | |                                   |
   |                                   |                                   |
   |  | ``pass``                     | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Configuration
~~~~~~~~~~~~~

The above example specified a user configuration property called
"ScaleFactor" that will be accessible from STK. If two or more instances
of the above Calc Scalar plugin are instantiated, each instance will
have its own unique value for the configuration property. AGI recommends
that any name used for these configuration properties not include spaces
because certain interfaces to the properties may not work correctly.

Adding properties for Python plugins
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a plugin interface defines a property (see
`IAgAccessConstraintPlugin <../DocX/AgAccessConstraintPlugin~IAgAccessConstraintPlugin.html>`__
for an example), the property must also be defined in the class. There
are two ways the STK Python API supports the user in doing so.

The first way is to define the property as a member of the plugin class.
In the example below, the property from the link above is seen being
defined. The name of the member matches the name of the property from
the link, as this is necessary for the STK Python API to retrieve its
value.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Properties - Example 1]          |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``class CAgAcces             | |                                   |
   |                                   |                                   |
   |  | sConstraintPlugin(object):`` | |                                   |
   |                                   |                                   |
   |  | ``def __init__(self):``      | |                                   |
   |                                   |                                   |
   |  | ``self.DisplayN              | |                                   |
   |                                   |                                   |
   |  | ame = 'PythonRangeExample'`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

The second way to define the property is using the @property decorator
on a method with the property name. The return type must match the type
defined by the property.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Properties - Example 2]          |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``class CAgAcces             | |                                   |
   |                                   |                                   |
   |  | sConstraintPlugin(object):`` | |                                   |
   |                                   |                                   |
   |  | ``@property``                | |                                   |
   |                                   |                                   |
   |  | ``def                        | |                                   |
   |                                   |                                   |
   |  |  DisplayName(self) -> str:`` | |                                   |
   |                                   |                                   |
   |  | ``r                          | |                                   |
   |                                   |                                   |
   |  | eturn 'PythonRangeExample'`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

For the full implemented example of the property being defined for the
`IAgAccessConstraintPlugin <../DocX/AgAccessConstraintPlugin~IAgAccessConstraintPlugin.html>`__
interface, see the Code Samples folder.

Hidden parameters for the Object Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------+---------------------------------------------------------+
| Parameter | Description                                             |
+===========+=========================================================+
| root      | The STK Object Model root / starting point for the API. |
|           | The usual way of getting the Object Model root via a    |
|           | Python script doesn't work here since you need the      |
|           | running root context. The parameter to use              |
|           | ``v                                                     |
|           | ersionString = root.ExecuteCommand('GetStkVersion /')`` |
+-----------+---------------------------------------------------------+
| abortMCS  | boolean, initial value is False. "Output value" i.e.    |
|           | STK reads this after the script executes. Set to true   |
|           | and the MCS sequence stops.                             |
+-----------+---------------------------------------------------------+
| iteration | integer number of the sequence iteration. "input only"  |
|           | i.e. STK doesn't read this back. e.g. if integer > 100: |
|           | abortMCS=True                                           |
+-----------+---------------------------------------------------------+

.. |image1| image:: ../Resources/Images/NumpyDisplayPlot.png
.. |image2| image:: ../Resources/Images/PandasStats.png
.. |image3| image:: ../Resources/Images/PandasStats2.png
.. |image4| image:: ../Resources/Images/PandasHeatMap.png
