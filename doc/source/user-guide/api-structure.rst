API structure
##############

This topic explores the foundational stucture of PySTK, providing you with an understanding of its organization and key components. It covers topics such as the use of packages and namespaces, the available data types, common coding patterns, how exceptions are handled, and the event-driven mechanisms that enable interactions. Understanding these elements will help you navigate PySTK effectively.


Packages and namespaces
=======================
Packages and namespaces are fundamental to the organization and structure of PySTK. Packages contain groups of modules, while namespaces manage and avoid name conflicts by defining the scope of variables, functions, and classes.



Data types
==========
Data types form the building blocks for handling and processing information with PySTK. This section describes the more complex data types used with the PySTK beyond the basic Python data types such as float, int, str, and bool. 

Type hints
----------

Most argument and return types are specified using type hints with Python's typing library. In the case that more than one type is possible (such as an argument that may be a string or a float), typing.Any is used as the type hint. In those situations, consulting the documentation for that method is advised. Type hints that are STK interfaces may represent objects that are subclasses of that interface.

Enumerations
------------

Enumerations (enums) enable you to define a set of named constant values. Enumeration classes are located in the STK Object Model modules (e.g. agi.stk12.stkobjects). Most inherit from Python's enum.IntEnum class while a few inherit from enum.IntFlag and may be combined using the | operator to select multiple options from within the enumeration.

*INSERT PYTHON - PYSTK CODE*

Arrays
------
Arrays are used to store and manipulate collections of items in Python. Many methods in the STK API take as input or return arrays. In PySTK, array values are represented using the list class.

*INSERT PYTHON - PYSTK CODE*


STK interfaces and classes
--------------------------

The STK object model is comprised of programming interfaces that are implemented by Python classes located in the provided modules. With few exceptions, classes returned from API methods begin with "Ag" and will inherit from one or more interfaces (beginning with "IAg"). You may immediately access any method from the inherited interfaces without casting, although in some situations casting may help with your IDE auto-complete feature. These classes have a reference to an STK object; this reference will be removed upon calling del() on the Python class. Because these classes are references to STK objects, creating them directly from Python will not be successful; objects must be returned from STK API methods.

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

The agi.stk12.utilities.colors module contains the Color, ColorRGBA, and Colors classes used by the STK Python API. The Color class represents an opaque color constructed from RGB values in the range [0, 255]. ColorRGBA represents a variably-translucent, 4-channel color constructed from RGBA values in the range [0, 255]. ColorRGBA may not be used in methods expecting a 3-channel color. Colors contains an assortment of named colors as well as factory methods to create Color or ColorRGBA objects from RGB(A) values.

*INSERT PYTHON - PYSTK CODE*

Certain methods require a list of 4-channel RGBA color values for defining per-vertex colors on a geometry. Such a list should be constructed in Python as a list of Color and/or ColorRGBA objects. Color objects always have alpha=255 (fully opaque), whereas alpha may be specified when using the ColorRGBA class. An example of these usages is provided below.

*INSERT PYTHON - PYSTK CODE*


Coding patterns
===============

This section provides coding patterns that are commonly used when developing with PySTK. 



Strategy pattern
----------------

This section explores the Strategy Pattern as it relates to PySTK, which enables you to delegate behavior to different strategies that can be selected at runtime. 



gRPC call batching
------------------

gRPC call batching is used to optimize the performance of gRPC-based communication by combining multiple requests into a single batch. 

Calling the application method NewGrpcCallBatcher returns an object of type agi.stk12.utilities.grpcutilities.GrpcCallBatcher. This feature is provided as an option to reduce the communication over the gRPC server in performance-critical applications. API calls may be batched together and sent to STK in one remote procedure call if no return value is needed from the calls.

Activating batching causes the normal API exception behavior to be altered. Exceptions from one command may appear asyncronously. Therefore, it is not recommended to use call batching while building and debugging, but rather as a performance optimization.

Only calls that do not return a value may be batched together, such as set-property requests and methods without a return value. Any method that has a return value (including get-property requests) automatically execute any previously batched commands before the method with a return value is executed.

Therefore, to reduce the number of remote API requests and improve performance, code must be organized to group together commands that do not have a return value. Call chaining interrupts a batch request because of the get-property command within the chain.


Exceptions
==========

Exceptions provide a way to detect, report, and recover from runtime issues. The table below describes the exceptions that are provided by the agi.stk12.utilities.exceptions module within PySTK.

<INSERT TABLE>
Exception | Description


Events
======

Events enable different parts of an application to communicate and respond to changes in an efficient manner. Events can be accessed directly in applicable parent objects, as seen in the table below.

<INSERT TABLE>
Event interface | Parent object

