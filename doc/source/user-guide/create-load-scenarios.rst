Creating and loading STK scenarios
##################################

What is a scenario?
===================

A scenario in STK is an instance of an analytical or operational task that you are modeling with STK. 

In the PySTK API, the :py:class:`ansys.stk.core.stkobjects.Scenario` object defines the context in which the properties and behavior of other objects are defined. Here you can enter global settings for time, units of measure, graphics attributes, and many other features, some of which can be overridden locally for specific objects.

Saving an STK scenario
======================

PySTK enables the automatic creation, saving, and loading of scenarios.

Unlike other applications that save a single file, STK saves a scenario as a group of files that comprise the collection of objects that are relevant to the scenario. When an STK scenario is saved, the scenario itself is saved as an object, and each object within the scenario is saved individually. The file extension for the scenario object is `.sc`. Additionally, the current layout of your workspace is saved in an Microsoft Excel Workbook file.

Satellites, aircraft, ground vehicles, ships, planets, stars, receivers and transmitters are examples of the objects that can constitute a scenario in STK. Within a scenario, you can set general properties, such as time period, units of measure, and the appearance of the 2D and 3D windows. Information that is contained in the scenario can be used to create reports and to perform other analytical tasks.

You can create an unlimited number of scenarios with STK; however, only one scenario can be open at a time.

STK scenarios in PySTK
======================

To learn more about using PySTK to automate the process of creating, saving, and loading scenarios, see :ref:`this example <Examples/create-load-scenarios>`.