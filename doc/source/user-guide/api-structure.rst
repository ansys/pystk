API structure
#############

This topic explores the foundational structure of PySTK, providing you with an
understanding of its organization and key components. It covers topics such as 
the use of packages and namespaces, the available data types, common coding 
patterns, how exceptions are handled, and the event-driven mechanisms that 
enable interactions. Understanding these elements can help you navigate PySTK 
effectively.

Packages and namespaces
=======================

Packages and namespaces are fundamental to the organization and structure of 
PySTK. Packages contain groups of modules, while namespaces manage and avoid 
name conflicts by defining the scope of variables, functions, and classes.

Data types
==========

Data types form the building blocks for handling and processing information 
with PySTK. This section describes the more complex data types used with PySTK
beyond the basic Python data types such as :obj:`float`, :obj:`int`, 
:obj:`str`, and :obj:`bool`. 

Type hints
----------

Most argument and return types are specified using type hints with Python's
:py:mod:`typing` library. In the case that more than one type is possible 
(such as an argument that may be a :obj:`str` or a :obj:`float`), 
:obj:`typing.Any` is used as the type hint. In those situations, consulting 
the documentation for that method is advised. Type hints that are STK 
interfaces may represent objects that are subclasses of that interface.

Enumerations
------------

Enumerations enable you to define a set of named constant values. Enumeration 
classes are located in the STK Object Model modules (for 
example—:py:mod:`~ansys.stk.core.stkobjects`). Most inherit from Python's 
:obj:`enum.IntEnum` class while a few inherit from :obj:`enum.IntFlag` and may
be combined using the logical OR operator to select multiple options from within the 
enumeration.

.. literalinclude:: /../../tests/doc_snippets_tests/graphics/graphics_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def CylinderFillEnumerationSnippet
  :end-at: cyl_fill = CylinderFillOptions.BOTTOM_CAP | CylinderFillOptions.TOP_CAP
  :dedent:

Arrays
------

Arrays are used to store and manipulate collections of items in Python. Many
PySTK methods return arrays or take them as input. In PySTK, array values are 
represented using the :obj:`list` class.

.. literalinclude:: /../../tests/doc_snippets_tests/connect/connect_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def ConnectCommandArraysSnippet
  :end-at: command_results = root.execute_multiple_commands(connect_commands, ExecuteMultipleCommandsMode.CONTINUE_ON_ERROR)
  :dedent:

STK interfaces and classes
--------------------------

The STK object model is comprised of programming interfaces that are 
implemented by Python classes located in the provided modules. With few 
exceptions, classes returned from PySTK methods inherit from one or more 
interfaces. You may immediately access any method from the inherited 
interfaces without casting, although in some situations casting may improve 
IDE auto-complete feature results. These classes have a reference to an STK 
object; this reference is removed upon calling ``del()`` on the Python class. 
Because these classes are references to STK objects, you cannot create them 
directly from Python; objects must be returned from PySTK methods.

.. literalinclude:: /../../tests/doc_snippets_tests/stk_objects/facility/facility_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def SetHeightFacilitySnippet
  :end-at: facility.height_above_ground = 123.4
  :dedent:

Collections
-----------

Collections enable you to store, organize, and manipulate groups of related 
items. Many PySTK interfaces represent collections of items; such interfaces
have the word "Collection" as part of their name. These classes have an 
``item()`` method that may be used to get an indexed item from the collection,
but they also support Python indexing and iteration.

.. literalinclude:: /../../tests/doc_snippets_tests/connect/connect_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def ConnectCommandArraysSnippet
  :end-at: print(message.count)
  :dedent:

Multiple return values
----------------------

Some methods in PYSTK return multiple values rather than returning one list. 
The multiple values are returned as a tuple.

.. literalinclude:: /../../tests/doc_snippets_tests/stk_objects/facility/facility_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def GetPositionFacilitySnippet
  :end-at: (x, y, z) = facility.position.query_cartesian()
  :dedent:


Colors
------

The :py:mod:`~ansys.stk.core.utilities.colors` module contains the :py:class:`~ansys.stk.core.utilities.colors.Color`, 
:py:class:`~ansys.stk.core.utilities.colors.ColorRGBA`, and :py:class:`~ansys.stk.core.utilities.colors.Colors` classes used by PySTK. 

.. list-table::
    :widths: auto
    :header-rows: 1

    * - **Class name**
      - **Description**
    * - ``Color``
      - Represents an opaque color constructed from RGB values in the range ``[0, 255]``. 
    * - ``ColorRGBA``
      - Represents a variably translucent, 4-channel color constructed from RGBA values in the range ``[0, 255]``. Instances of this class may not be used in methods expecting a 3-channel color. 
    * - ``Colors``
      - Contains an assortment of named colors as well as factory methods to create ``Color`` or ``ColorRGBA`` objects from RGB(A) values.

.. literalinclude:: /../../tests/doc_snippets_tests/colors/colors_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def GetSetRGBColorSnippet
  :end-at: (r, g, b) = facility.graphics.color.get_rgb()
  :dedent:

Certain methods require a list of 4-channel RGBA color values for defining 
per-vertex colors on a geometry. Such a list should be constructed in Python 
as a list of ``Color`` and/or ``ColorRGBA`` objects. ``Color`` objects always have 
``alpha=255`` (fully opaque), whereas ``alpha`` may be specified when using the 
``ColorRGBA`` class. An example of these usages is provided below.

.. literalinclude:: /../../tests/doc_snippets_tests/colors/colors_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def GetSetRGBAColorSnippet
  :end-at: point.set_cartographic_with_colors('Earth', lla_pts, colors)
  :dedent:


Coding patterns
===============

This section provides coding patterns that are commonly used when developing with PySTK. 

Strategy pattern
----------------

This section provides information on the strategy pattern as it relates to 
PySTK. The strategy pattern enables you to delegate behavior to different 
strategies that can be selected at runtime. It is useful when you need to vary
the behavior of certain components, such as authentication methods or request 
handling strategies, without altering the objects that use them.

gRPC call batching
------------------

Making multiple network calls can introduce latency, especially when those 
calls are made sequentially. gRPC call batching is used to optimize the 
performance of gRPC-based communication by combining multiple requests into a 
single batch. This reduces the overhead of multiple round trips, improves 
performance, and enhances scalability.

Calling the application-level method ``new_grpc_call_batcher`` returns an object
of type :py:class:`~ansys.stk.core.utilities.grpcutilities.GrpcCallBatcher`. 
This feature is provided as an option to reduce the communication over the 
gRPC server in performance-critical applications. API calls may be batched 
together and sent to STK in one remote procedure call if no return value is 
needed from the calls.

Activating batching causes the normal API exception behavior to be altered. 
Exceptions from one command may appear asynchronously. Therefore, it is not 
recommended to use call batching while building and debugging, but rather as a
performance optimization.

Only calls that do not return a value may be batched together, such as 
set-property requests and methods without a return value. Any method that has 
a return value (including get-property requests) automatically execute any 
previously batched commands before the method with a return value is executed.

Therefore, to reduce the number of remote API requests and improve 
performance, code must be organized to group together commands that do not 
have a return value. Call chaining interrupts a batch request because of the 
get-property command within the chain.

Exceptions
==========

Exceptions are used to signal errors or unexpected conditions that arise 
during the execution of a script. When working with PySTK, you may encounter
situations where something goes wrong, such as trying to access a non-existent
object, providing invalid input, or encountering a runtime error while 
manipulating your scenario. Exceptions provide a mechanism for handling these 
errors in a controlled and predictable way.

See the table on the :py:mod:`~ansys.stk.core.utilities.exceptions` module 
page for a description of the exceptions provided by PySTK. 

Events
======

Events are mechanisms that enable you to respond to specific changes or 
actions occurring within an STK scenario or the application itself. Events 
enable you to automate responses to particular triggers, such as when a 
scenario reaches a certain time, when an object's state changes, or when 
specific conditions are met during a simulation.

Using events, you can build more dynamic and interactive simulations by 
attaching custom Python functions or scripts that are executed automatically 
when predefined conditions are satisfied. For instance, you might want to log 
specific data whenever a satellite enters a certain region or when a 
communication link is established between two objects. Events enable you to 
hook into the STK application's processes and respond in real-time, 
streamlining workflows and enhancing your scenario's capabilities.

You can access events directly in applicable parent objects, as displayed in 
the table below.

.. list-table::
    :widths: auto
    :header-rows: 1

    * - **Event interface**
      - **Parent object**
    * - ``IStkObjectRootEvents``
      - :py:class:`~ansys.stk.core.stkobjects.StkObjectRoot`
    * - ``ISTKXApplicationEvents``
      - :py:class:`~ansys.stk.core.stkengine.STKEngineApplication`
    * - ``IUiAxGraphics3DCntrlEvents``
      - :py:class:`~ansys.stk.core.stkengine.tkcontrols.GlobeControl`
    * - ``IUiAxGraphics2DCntrlEvents``
      - :py:class:`~ansys.stk.core.stkengine.tkcontrols.MapControl`
    * - ``ISceneEventHandlers``
      - :py:class:`~ansys.stk.core.graphics.Scene`
    * - ``IKmlGraphicsEvents``
      - :py:class:`~ansys.stk.core.graphics.KmlGraphics`
    * - ``IImageCollectionEvents``
      - :py:class:`~ansys.stk.core.graphics.ImageCollection`
    * - ``ITerrainOverlayCollectionEvents``
      - :py:class:`~ansys.stk.core.graphics.TerrainOverlayCollection`

Events are accessed through the ``subscribe()`` method on the parent object, 
which returns an event handler subscribed to events on the queried object. You
can add or remove event callbacks in the event handler using the ``+=`` and ``-=``
operators. These operators change the callbacks that get executed by the event
but do not affect whether the handler remains subscribed. The event handler 
should be unsubscribed using the ``unsubscribe()`` method when event handling is
no longer needed. Refer to the following example for using 
``IStkObjectRootEvents``.

.. literalinclude:: /../../tests/doc_snippets_tests/scenario/scenario_management/scenario_management_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def STKEngineEventsSnippet
  :end-at: skt_object_root_events.unsubscribe()
  :dedent:

The STK Desktop application user interface might become unresponsive to user 
input when Python has event subscribers, and the STK application tries to call
back into the Python interpreter to notify of an event. That callback relies 
on the Windows message loop to be dispatched. To work around this issue, 
Windows messages need to be dispatched through the Windows message queue. This
can be accomplished in different ways depending on the type of Python script 
that is executing (console or user interface), and on the type of user 
interface library being used. For instance, if you use the tkinter user 
interface library, a simple way of accomplishing this with this library is to 
create a tkinter window while using the desktop application user interface. No
action is needed if Python is used only for automation. The following script 
is an example showing this issue.

.. literalinclude:: /../../tests/doc_snippets_tests/scenario/scenario_management/scenario_management_snippets.py
  :language: py
  :tab-width: 4
  :start-after: def STKDesktopEventsSnippet
  :end-at: # The user interface is responsive and the event callback is successful.
  :dedent: