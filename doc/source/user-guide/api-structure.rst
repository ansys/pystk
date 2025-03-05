API structure
##############

This topic explores the foundational structure of PySTK, providing you with an understanding of its organization and key components. It covers topics such as the use of packages and namespaces, the available data types, common coding patterns, how exceptions are handled, and the event-driven mechanisms that enable interactions. Understanding these elements can help you navigate PySTK effectively.


Packages and namespaces
=======================

Packages and namespaces are fundamental to the organization and structure of PySTK. Packages contain groups of modules, while namespaces manage and avoid name conflicts by defining the scope of variables, functions, and classes.

Data types
==========
Data types form the building blocks for handling and processing information with PySTK. This section describes the more complex data types used with PySTK beyond the basic Python data types such as float, int, str, and boolean. 

Type hints
----------

Most argument and return types are specified using type hints with Python's typing library. In the case that more than one type is possible (such as an argument that may be a string or a float), typing. Any is used as the type hint. In those situations, consulting the documentation for that method is advised. Type hints that are STK interfaces may represent objects that are subclasses of that interface.

Enumerations
------------

Enumerations enable you to define a set of named constant values. Enumeration classes are located in the STK Object Model modules (for example—agi.stk12.stkobjects). Most inherit from Python's enum.IntEnum class while a few inherit from enum.IntFlag and may be combined using the | operator to select multiple options from within the enumeration.

*INSERT PYTHON - PYSTK CODE*


Arrays
------
Arrays are used to store and manipulate collections of items in Python. Many methods in the STK API take as input or return arrays. In PySTK, array values are represented using the list class.

*INSERT PYTHON - PYSTK CODE*


STK interfaces and classes
--------------------------

The STK object model is comprised of programming interfaces that are implemented by Python classes located in the provided modules. With few exceptions, classes returned from API methods begin with "Ag" and inherits from one or more interfaces (beginning with "IAg"). You may immediately access any method from the inherited interfaces without casting, although in some situations casting may help with your IDE auto-complete feature. These classes have a reference to an STK object; this reference is removed upon calling del() on the Python class. Because these classes are references to STK objects, you cannot create them directly from Python; objects must be returned from STK API methods.

*INSERT PYTHON - PYSTK CODE*


Collections
-----------

Collections enable you to store, organize, and manipulate groups of related items. Many of the interfaces in the STK API represent collections of items; such interfaces have the word "Collection" as part of their name. These classes have an "Item()" method that may be used to get an indexed item from the collection, but they also support Python indexing and iteration.

*INSERT PYTHON - PYSTK CODE*


Multiple return values
----------------------

Some methods in PYSTK return multiple values rather than returning one list. The multiple values are returned as a tuple.

*INSERT PYTHON - PYSTK CODE*


Colors
------

The agi.stk12.utilities.colors module contains the Color, ColorRGBA, and Colors classes used by the STK Python API. The Color class represents an opaque color constructed from RGB values in the range [0, 255]. ColorRGBA represents a variably translucent, 4-channel color constructed from RGBA values in the range [0, 255]. ColorRGBA may not be used in methods expecting a 3-channel color. Colors contains an assortment of named colors as well as factory methods to create Color or ColorRGBA objects from RGB(A) values.

*INSERT PYTHON - PYSTK CODE*

Certain methods require a list of 4-channel RGBA color values for defining per-vertex colors on a geometry. Such a list should be constructed in Python as a list of Color and/or ColorRGBA objects. Color objects always have alpha=255 (fully opaque), whereas alpha may be specified when using the ColorRGBA class. An example of these usages is provided below.

*INSERT PYTHON - PYSTK CODE*


Coding patterns
===============

This section provides coding patterns that are commonly used when developing with PySTK. 



Strategy pattern
----------------

This section provides information on the Strategy Pattern as it relates to PySTK. The Strategy Pattern enables you to delegate behavior to different strategies that can be selected at runtime. It is useful when you need to vary the behavior of certain components, such as authentication methods or request handling strategies, without altering the objects that use them.



gRPC call batching
------------------

Making multiple network calls can introduce latency, especially when those calls are made sequentially. gRPC call batching is used to optimize the performance of gRPC-based communication by combining multiple requests into a single batch. This reduces the overhead of multiple round trips, improves performance, and enhances scalability.

Calling the application method NewGrpcCallBatcher returns an object of type agi.stk12.utilities.grpcutilities.GrpcCallBatcher. This feature is provided as an option to reduce the communication over the gRPC server in performance-critical applications. API calls may be batched together and sent to STK in one remote procedure call if no return value is needed from the calls.

Activating batching causes the normal API exception behavior to be altered. Exceptions from one command may appear asynchronously. Therefore, it is not recommended to use call batching while building and debugging, but rather as a performance optimization.

Only calls that do not return a value may be batched together, such as set-property requests and methods without a return value. Any method that has a return value (including get-property requests) automatically execute any previously batched commands before the method with a return value is executed.

Therefore, to reduce the number of remote API requests and improve performance, code must be organized to group together commands that do not have a return value. Call chaining interrupts a batch request because of the get-property command within the chain.


Exceptions
==========

Exceptions are used to signal errors or unexpected conditions that arise during the execution of a script. When working with the API, you may encounter situations where something goes wrong, such as trying to access a non-existent object, providing invalid input, or encountering a runtime error while manipulating your scenario. Exceptions provide a mechanism for handling these errors in a controlled and predictable way.

The table below describes the exceptions that are provided by the agi.stk12.utilities.exceptions module with PySTK.

[INSERT TABLE]

Exception | Description


Events
======

Events are mechanisms that enable you to respond to specific changes or actions occurring within an STK scenario or the application itself. Events enable you to automate responses to particular triggers, such as when a scenario reaches a certain time, when an object's state changes, or when specific conditions are met during a simulation.

Using events, you can build more dynamic and interactive simulations by attaching custom Python functions or scripts that are executed automatically when predefined conditions are satisfied. For instance, you might want to log specific data whenever a satellite enters a certain region or when a communication link is established between two objects. Events enable you to hook into the STK application's processes and respond in real-time, streamlining workflows and enhancing your scenario's capabilities.

You can access events directly in applicable parent objects, as displayed in the table below.

[INSERT TABLE]

Event interface | Parent object

Events are accessed through the Subscribe() method on the parent object, which returns an event handler subscribed to events on the queried object. You can add or remove Event callbacks in the event handler using the "+=" and "-=" operators; these operators change the callbacks that get executed by the event but do not affect whether the handler remains subscribed. The event handler should be unsubscribed using the Unsubscribe() method when event handling is no longer needed. Refer to the following example for using IAgStkObjectRootEvents.

.. code-block:: python

    from agi.stk12.stkengine import STKEngine

    def onScenarioNewCallback(Path:str):
    print(f'Scenario {Path} has been created.')

    stk = STKEngine.StartApplication()
    root = stk.NewObjectRoot()
    stkObjectRootEvents = root.Subscribe()
    stkObjectRootEvents.OnScenarioNew += onScenarioNewCallback
    root.NewScenario('ExampleScenario')
    # callback should be executed now

    # remove the callback from the handler
    stkObjectRootEvents.OnScenarioNew -= onScenarioNewCallback

    # all finished with events, unsubscribe
    stkObjectRootEvents.Unsubscribe()

The STK Desktop application user interface might become unresponsive to user input when Python has event subscribers, and the STK application tries to call back into the Python interpreter to notify of an event. That callback relies on the Windows message loop to be dispatched. To work around this issue, Windows messages need to be dispatched through the Windows message queue. This can be accomplished in different ways depending on the type of Python script that is executing (console or user interface), and on the type of user interface library being used. For instance, if you use the tkinter user interface library, a simple way of accomplishing this with this library is to create a tkinter window while using the desktop application user interface. No action is needed if Python is used only for automation. The following script is an example showing this issue.

.. code-block:: python
    
    from agi.stk12.stkdesktop import STKDesktop
    from agi.stk12.stkobjects import AgESTKObjectType

    def onStkObjectAddedCallback(Path:str):
    print(f'{Path} has been added.')
    stk = STKDesktop.StartApplication(visible=True)
    root = stk.Root
    root.NewScenario('ExampleScenario')
    stkObjectRootEvents = root.Subscribe()
    stkObjectRootEvents.OnStkObjectAdded += onStkObjectAddedCallback
    sc = root.CurrentScenario

    #onStkObjectAddedCallback is successfully called when the next line is executed
    fac = sc.Children.New(AgESTKObjectType.eFacility, 'AGIHQ')

    #Now switch control to the desktop application and create another facility.
    #The user interface becomes unresponsive.

    #Now open a tkinter window that processing COM messages.
    from tkinter import Tk
    window = Tk()
    window.mainloop()
    #Switch control to the desktop application and create another facility.
    #The user interface is responsive and the event callback is successful.


