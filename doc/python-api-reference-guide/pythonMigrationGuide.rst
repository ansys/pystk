Migration Guide
===============

If you have existing code that uses win32com or comtypes to exercise
STK, your existing code should be compatible with the new library once
you update the initialization code.

Update your existing code using win32com or comtypes to initialize STK
with the corresponding code for each use case:

-  `Starting new STK Desktop
   instance <#starting-new-stk-desktop-instance>`__
-  `Attaching to running instance of STK
   Desktop <#attaching-to-running-instance-of-stk-desktop>`__
-  `Starting STK Engine <#starting-stk-engine>`__
-  `Refactoring comtypes QueryInterface
   calls <#refactoring-comtypes-calls>`__
-  `OleColor to Color <#olecolor-to-color>`__
-  `Enumeration Migration <#enum-migration>`__

Starting new STK Desktop instance
---------------------------------

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - win32com]               |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# Start new inst           | |                                   |
   |                                   |                                   |
   |  | ance of STK using win32com`` | |                                   |
   |                                   |                                   |
   |  | ``from win32                 | |                                   |
   |                                   |                                   |
   |  | com.client import Dispatch`` | |                                   |
   |                                   |                                   |
   |  | ``stk = Dis                  | |                                   |
   |                                   |                                   |
   |  | patch('STK12.Application')`` | |                                   |
   |                                   |                                   |
   |  | ``stk.Visible = True``       | |                                   |
   |                                   |                                   |
   |  | ``# Get the                  | |                                   |
   |                                   |                                   |
   |  | IAgStkObjectRoot interface`` | |                                   |
   |                                   |                                   |
   |  | ``root = stk.Personality2``  | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - comtypes]               |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# Start new inst           | |                                   |
   |                                   |                                   |
   |  | ance of STK using comtypes`` | |                                   |
   |                                   |                                   |
   |  | ``from comtypes.             | |                                   |
   |                                   |                                   |
   |  | client import CreateObject`` | |                                   |
   |                                   |                                   |
   |  | ``stk = CreateO              | |                                   |
   |                                   |                                   |
   |  | bject('STK12.Application')`` | |                                   |
   |                                   |                                   |
   |  | ``stk.Visible = True``       | |                                   |
   |                                   |                                   |
   |  | ``# Get the                  | |                                   |
   |                                   |                                   |
   |  | IAgStkObjectRoot interface`` | |                                   |
   |                                   |                                   |
   |  | ``root = stk.Personality2``  | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

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
   |  | ``from agi.stk12.st          | |                                   |
   |                                   |                                   |
   |  | kdesktop import STKDesktop`` | |                                   |
   |                                   |                                   |
   |  | ``stk = STKDesktop.Star      | |                                   |
   |                                   |                                   |
   |  | tApplication(visible=True)`` | |                                   |
   |                                   |                                   |
   |  | ``# Get the                  | |                                   |
   |                                   |                                   |
   |  | IAgStkObjectRoot interface`` | |                                   |
   |                                   |                                   |
   |  | ``root = stk.Root``          | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

Attaching to running instance of STK Desktop
--------------------------------------------

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - win32com]               |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# Attach to running inst   | |                                   |
   |                                   |                                   |
   |  | ance of STK using win32com`` | |                                   |
   |                                   |                                   |
   |  | ``from win32com.cli          | |                                   |
   |                                   |                                   |
   |  | ent import GetActiveObject`` | |                                   |
   |                                   |                                   |
   |  | ``stk = GetActiveO           | |                                   |
   |                                   |                                   |
   |  | bject('STK12.Application')`` | |                                   |
   |                                   |                                   |
   |  | ``stk.Visible = True``       | |                                   |
   |                                   |                                   |
   |  | ``# Get the                  | |                                   |
   |                                   |                                   |
   |  | IAgStkObjectRoot interface`` | |                                   |
   |                                   |                                   |
   |  | ``root = stk.Personality2``  | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - comtypes]               |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``                           | |                                   |
   |                                   |                                   |
   |  | # Get reference to running S | |                                   |
   |                                   |                                   |
   |  | TK instance using comtypes`` | |                                   |
   |                                   |                                   |
   |  | ``from comtypes.cli          | |                                   |
   |                                   |                                   |
   |  | ent import GetActiveObject`` | |                                   |
   |                                   |                                   |
   |  | ``stk = GetActiveO           | |                                   |
   |                                   |                                   |
   |  | bject('STK12.Application')`` | |                                   |
   |                                   |                                   |
   |  | ``stk.Visible = True``       | |                                   |
   |                                   |                                   |
   |  | ``# Get the                  | |                                   |
   |                                   |                                   |
   |  | IAgStkObjectRoot interface`` | |                                   |
   |                                   |                                   |
   |  | ``root = stk.Personality2``  | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

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
   |  | ``from agi.stk12.st          | |                                   |
   |                                   |                                   |
   |  | kdesktop import STKDesktop`` | |                                   |
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

Starting STK Engine
-------------------

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - win32com]               |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# Start new instance of    | |                                   |
   |                                   |                                   |
   |  |  STK Engine using win32com`` | |                                   |
   |                                   |                                   |
   |  | ``from win32                 | |                                   |
   |                                   |                                   |
   |  | com.client import Dispatch`` | |                                   |
   |                                   |                                   |
   |  | ``stk = Disp                 | |                                   |
   |                                   |                                   |
   |  | atch('STKX12.Application')`` | |                                   |
   |                                   |                                   |
   |  | ``# optiona                  | |                                   |
   |                                   |                                   |
   |  | lly, stk.NoGraphics = True`` | |                                   |
   |                                   |                                   |
   |  | ``# Get the                  | |                                   |
   |                                   |                                   |
   |  | IAgStkObjectRoot interface`` | |                                   |
   |                                   |                                   |
   |  | ``root = Dispatch('AgStkO    | |                                   |
   |                                   |                                   |
   |  | bjects12.AgStkObjectRoot')`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - comtypes]               |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``# Start new instance of    | |                                   |
   |                                   |                                   |
   |  |  STK Engine using comtypes`` | |                                   |
   |                                   |                                   |
   |  | ``from comtypes.             | |                                   |
   |                                   |                                   |
   |  | client import CreateObject`` | |                                   |
   |                                   |                                   |
   |  | ``stk = CreateOb             | |                                   |
   |                                   |                                   |
   |  | ject('STKX12.Application')`` | |                                   |
   |                                   |                                   |
   |  | ``# optiona                  | |                                   |
   |                                   |                                   |
   |  | lly, stk.NoGraphics = True`` | |                                   |
   |                                   |                                   |
   |  | ``# Get the                  | |                                   |
   |                                   |                                   |
   |  | IAgStkObjectRoot interface`` | |                                   |
   |                                   |                                   |
   |  | `                            | |                                   |
   |                                   |                                   |
   |  | `root = CreateObject('AgStkO | |                                   |
   |                                   |                                   |
   |  | bjects12.AgStkObjectRoot')`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

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
   |  | ``from agi.stk12.            | |                                   |
   |                                   |                                   |
   |  | stkengine import STKEngine`` | |                                   |
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

Refactoring comtypes QueryInterface calls
-----------------------------------------

In order to access the properties and methods on another interface,
comtypes requires the use of the QueryInterface method. Without this
call those properties and methods are not accessible. This constraint
does not exist with the new API. When an object implements multiple
interfaces, all the methods and properties from those interfaces are
directly accessible at runtime.

Note that you can optionally explicitly navigate interfaces exposed by
the same object. This helps your IDE in providing better auto-completion
hints. The IDE auto-completion engines need to determinate statically
the type of a variable. Certain methods such as
IAgStkObjectCollection.New return an IAgStkObject interface but it may
be desirable for IDE code completion to work on the underlying object
type (e.g. AgFacility, AgSatellite). Without the explicit cast, the IDE
will not be able to know which object has been returned, although
runtime method availability will be unaffected by the choice of whether
or not to explicitly cast.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - comtypes]               |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   |                                   |                                   |
   |  | ``facility                   | |                                   |
   |                                   |                                   |
   |  | Obj = root.CurrentScenario.C | |                                   |
   |                                   |                                   |
   |  | hildren.New(STKObjects.eFaci | |                                   |
   |                                   |                                   |
   |  | lity, 'facility') # New retu | |                                   |
   |                                   |                                   |
   |  | rns IAgStkObject interface`` | |                                   |
   |                                   |                                   |
   |  | ``print                      | |                                   |
   |                                   |                                   |
   |  | (facilityObj.InstanceName)`` | |                                   |
   |                                   |                                   |
   |  | ``facility = facility        | |                                   |
   |                                   |                                   |
   |  | Obj.QueryInterface(STKObject | |                                   |
   |                                   |                                   |
   |  | s.IAgFacility) # Switches to | |                                   |
   |                                   |                                   |
   |  |  the IAgFacility interface`` | |                                   |
   |                                   |                                   |
   |  | ``                           | |                                   |
   |                                   |                                   |
   |  | print(facility.UseTerrain)`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

STK API, option 1 - explicit cast, best for IDE code completion:

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
   |  | ``facili                     | |                                   |
   |                                   |                                   |
   |  | ty = AgFacility(root.Current | |                                   |
   |                                   |                                   |
   |  | Scenario.Children.New(AgESTK | |                                   |
   |                                   |                                   |
   |  | ObjectType.eFacility, 'facil | |                                   |
   |                                   |                                   |
   |  | ity')) # facility variable's | |                                   |
   |                                   |                                   |
   |  |  static type is AgFacility`` | |                                   |
   |                                   |                                   |
   |  | ``print(facility.Inst        | |                                   |
   |                                   |                                   |
   |  | anceName) # InstanceName is  | |                                   |
   |                                   |                                   |
   |  | suggested by the IDE as AgFa | |                                   |
   |                                   |                                   |
   |  | cility exposes that method`` | |                                   |
   |                                   |                                   |
   |  | ``print(facility.UseTe       | |                                   |
   |                                   |                                   |
   |  | rrain) # UseTerrain is also  | |                                   |
   |                                   |                                   |
   |  | suggested by the IDE as AgFa | |                                   |
   |                                   |                                   |
   |  | cility exposes that method`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

STK API, option 2 - limited IDE code completion:

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
   |  | ``facility = root.CurrentS   | |                                   |
   |                                   |                                   |
   |  | cenario.Children.New(AgESTKO | |                                   |
   |                                   |                                   |
   |  | bjectType.eFacility, 'facili | |                                   |
   |                                   |                                   |
   |  | ty') # facility variable's s | |                                   |
   |                                   |                                   |
   |  | tatic type is IAgStkObject`` | |                                   |
   |                                   |                                   |
   |  | ``print(facility.Instance    | |                                   |
   |                                   |                                   |
   |  | Name) # InstanceName is sugg | |                                   |
   |                                   |                                   |
   |  | ested by the IDE as IAgStkOb | |                                   |
   |                                   |                                   |
   |  | ject exposes that property`` | |                                   |
   |                                   |                                   |
   |  | ``print(facility.U           | |                                   |
   |                                   |                                   |
   |  | seTerrain) # UseTerrain is n | |                                   |
   |                                   |                                   |
   |  | ot suggested by the IDE as i | |                                   |
   |                                   |                                   |
   |  | t is a property of IAgFacili | |                                   |
   |                                   |                                   |
   |  | ty and not of IAgStkObject`` | |                                   |
   |                                   |                                   |
   |  +------------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

OleColor to Color
-----------------

In win32com and comtypes you had to pass the OleColor value to
properties and methods. You can now use the predefined colors from
agi.stk12.utilities.colors.Colors class. Alternatively, use the below
method to convert the OleColor value to RGB values (for example,
OleColor 16776960 yields r,g,b = 0, 255, 255 or Cyan). You can then use
the agi.stk12.utilities.colors.Color.FromRGB method.

+-----------------------------------------------------------------------+
| Method                                                                |
+=======================================================================+
| red = oleValue % 256                                                  |
|                                                                       |
| green = (oleValue / 256) % 256                                        |
|                                                                       |
| blue = ((oleValue / (256*256)) % 256                                  |
+-----------------------------------------------------------------------+

Enumeration Migration
---------------------

With the STK Python API, Enumerations are now class types. In win32com
and comtypes you passed the int value for enumerations. To migrate old
code search for the enumeration class in the help to get a table showing
what each int value is. If you do not know the enumeration class type
then find the method, property or interface in the help and it should
link to the enumeration class.

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - win32com]               |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |   +-----------------------------+ |                                   |
   |                                   |                                   |
   |   | ``fac1 = scenari            | |                                   |
   |                                   |                                   |
   |   | o.Children.New(8, 'fac1')`` | |                                   |
   |                                   |                                   |
   |   +-----------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+

.. container:: LanguageSpecific
   :name: Example_Python

   +-----------------------------------+-----------------------------------+
   | [Python - STK API]                |                                   |
   +===================================+===================================+
   | .. container:: LanguageSpecific   |                                   |
   |    :name: Code_Python             |                                   |
   |                                   |                                   |
   |                                   |                                   |
   |   +-----------------------------+ |                                   |
   |                                   |                                   |
   |   | ``fac1 = scenario.          | |                                   |
   |                                   |                                   |
   |   | Children.``\ ```New`` <../D | |                                   |
   |                                   |                                   |
   |   | ocX/STKObjects~IAgStkObject | |                                   |
   |                                   |                                   |
   |   | ~Children.html>`__\ ``(``\  | |                                   |
   |                                   |                                   |
   |   | ```AgESTKObjectType`` <../D | |                                   |
   |                                   |                                   |
   |   | ocX/STKObjects~Enumerations | |                                   |
   |                                   |                                   |
   |   | ~AgESTKObjectType_EN.html>` | |                                   |
   |                                   |                                   |
   |   | __\ ``.eFacility, 'fac1')`` | |                                   |
   |                                   |                                   |
   |   +-----------------------------+ |                                   |
   +-----------------------------------+-----------------------------------+
