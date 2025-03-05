Extract results and graphs
##########################

The STK Object Model provides direct access to the data provider tools that are exposed by each object in STK, which are the foundation of the report styles in the GUI. 

Reports in STK are typically used to generate results like satellite positions, sensor coverage, or any time-dependent parameters. You can use PySTK to generate reports, extract their data, and export them to formats like CSV or Excel. This topic describes how to translate a report into its corresponding set of Data Providers, and demonstrates how to retrieve the data contained within through the Object Model. 

About STK data providers
========================

Data Providers in STK are essential for accessing detailed, time-dependent data from objects and systems in your scenario. They are part of STK's object model and are key to extracting and manipulating information related to different aspects of your model, such as satellite positions, sensor coverage, communication links, and more. By using the STK Object Model, you can automate the retrieval of this data for further processing, visualization, or reporting.

The content of a report or graph is generated from the selected data providers for the report or graph style. 

Report styles
=============

To browse the various Report styles available for a particular object in STK, and their corresponding Data Providers,
right-click an object in the STK Object Browser and navigate to the Graph and Report Manager menu. In the manager dialog, expand the Installed Styles folder. This displays a list of the various report styles that are available for particular object.

(./img/report-styles-expand.png)

To view the Data Providers being used by a particular report style, click a report style, and click the Properties
button (./img/properties-button.png) to display the Report Style window. 

(./img/report-style-window.png)

Report contents
===============

In the Report Contents section of the Report Style window, the various Data Providers that are used to derive the particular report are listed. These Data Providers provide the actual data content to the report. 

(./img/report-contents.png)

.. note::
    The Section, Line, and Time elements are used to provide formatting for the report style; they are not actual data providers.

Data providers
==============

In the Data Providers section of the Report Style window, the Data Providers available for a particular object are listed. Expand a particular group to view the nested Data Providers associated with that group. Expanding a particular Data Provider further to display the data Elements that are associated with it. 

(./img/data-providers.png)

Groups, Data Providers, and Elements are the organizing principles of the Data Providers provided by the STK Object Model. 

Object model
============

Now that you have explored the concepts of Report Styles and Data Providers, continue to use the preceding example report, J2000 Position Velocity, to demonstrate retrieving it's data through the Object Model. First, recall what Data Providers the report was constructed from. In the Report Contents window, the J2000 Position Velocity Report is made up of specific elements of the J2000 Data Provider from two groups—Cartesian Velocity and Cartesian Position. 

(./img/object-model-report-contents.png)

Get connected
=============

This example assumes that you have STK running with a scenario that contains a sattelite called “Satellite1”. The scenario's start date should be set to “1 Jul 2020, 17:14:00.00”. The scenario's stop date should be set to “1 Jul 2020, 17:29:00.00”. Ensure that the satellite's associated times use the scenario's times as well.

The following code example connects to STK, and establishes a reference to the satellite.

.. code-block::
    
    Dim Root As STKObjects.AgStkObjectRoot
    Dim App As Object
    App = GetObject(, "STK12.Application")
    Root = App.Personality2
    Dim Satellite As STKObjects.IAgStkObject
    Satellite = Root.CurrentScenario.Children(“Satellite1”)

Setup data providers for use in the object model
=================================================

To retrieve the data for the J2000 Position Velocity report, you must setup its specific Data Providers for use in the Object Model. Use the various IAgDataProvider interfaces to do this:

.. code-block::

    Dim CartVel, CartPos As STKObjects.IAgDataProviderGroup
    Dim CartVelJ2000, CartPosJ2000 As STKObjects.IAgDataProvider
    
    CartVel = Satellite.DataProviders("Cartesian Velocity"
    CartPos = Satellite.DataProviders("Cartesian Position")
    CartVelJ2000 = CartVel.Group.Item("J2000")
    CartPosJ2000 = CartPos.Group.Item("J2000")

The basic interfaces are now setup to compute information from the Data Providers that the report is using. Next, you need to cast your interfaces to a certain interface to provide the DataProvider with inputs so it can compute the proper data.

Data provider PreData inputs
============================

Some Data Providers require input data before the calculation can provide data results. This data is known as PreData. There are two ways to ascertain if PreData is required for a particular Data Provider:

- Refer to the Data Provider documentation which provides the format of the PreData if any is required.
- Retrieve the Data Provider Schema and parse it for PreData tags.

.. code-block::

    Dim Satellite2 As STKObjects.IAgStkObject
    Satellite2 = Root.CurrentScenario.Children(“Satellite2”)
    Dim schema As String = Satellite2.DataProviders.GetSchema()

Once the format of the PreData is know, you can set the PreData property on the Data Provider interface. This PreData property must be set before issuing the data provider's calculation method. 

Set the PreData property on the data provider interface
-------------------------------------------------------

The following example demonstrates setting the Object Path as the PreData for the “RIC Coordinates” Data Provider and then calls the Data Provider’s computation execution method. 

.. code-block::

    Dim Satellite2 As STKObjects.IAgStkObject
    Satellite2 = Root.CurrentScenario.Children(“Satellite2”)
    
    Dim oProvider As STKObjects.IAgDataPrvTimeVar
    oProvider = Satellite2.DataProviders("RIC Coordinates")
    
    oProvider.PreData = "Satellite/Satellite1"
    
    Dim oResult As STKObjects.IAgDrResult
    oResult = oProvider.Exec(0, 90000, 1000)

Data provider time inputs
-------------------------

In the Time Period section of the Report Window in STK, highlight J2000 Position Velocity and click the Specify Time Properties radio button. The J2000 Position Velocity Report uses a time period to provide the underlying Data Providers information about what data to compute. You need to provide the same information to the Object Model Data Providers. 

(./img/specify-time-properties.png)

Retrieve the data 
=================

There are three ways to compute the data, depending on the data provider type. The first method requires a time interval and step size, the second requires only a time interval, and the third is independent of time. 

You must provide input information to the Data Providers by casting the Data Provider interfaces to the proper execution interface. In the case of the Cartesian Velocity and Position Data Providers, you should cast to the IAgDataPrvTimeVar interface: 

.. code-block::

    Dim VelTimeVariable, PosTimeVariable As STKObjects.IAgDataPrvTimeVar
    
    VelTimeVariable = CartVelJ2000
    PosTimeVariable = CartPosJ2000

You are now ready to retrieve the information from the Data Providers. The data is always returned as an IAgDrResult interface. Provide the Exec method of the TimeVar interfaces with the Data Provider Inputs (Start Time, Stop Time, and Step Size):

.. code-block::

    Dim VelResult, PosResult As STKObjects.IAgDrResult
    
    VelResult = VelTimeVariable.Exec("18 Mar 2009 16:00:00.00", _"19 Mar 2009 16:00:00.00", _60)
    
    PosResult = PosTimeVariable.Exec("18 Mar 2009 16:00:00.00", _"19 Mar 2009 16:00:00.00", _60) 

VelResult and PosResult now contain the data from the J2000 Cartesian Velocity and Cartesian Position Data Providers. You now have more data than the original Report contained.

Retrieve specific elements
==========================

Recall that your original Cartesian Position Velocity Report contained only four elements of the Cartesian Velocity J2000 Group—x, y, z, and speed. Similarly, the Cartesian Position J2000 Data Provider contained within your Report Style only contains 3 elements—x, y, and z.

(./img/object-model-report-contents.png)

When you executed the J2000 Data Provider of Cartesian Velocity, you actually retrieved seven elements instead of the four specifically contained in the
report, adding the Time, radial, and in track elements to your DataProvider Result. To be precise as possible, you want IAgDRResult to contain only the elements which were contained in the original report. To do this, use the ExecElements() method. 

First, specify in an array the elements that you want to retrieve from the Data Provider. Next, pass the array into the ExecElements() method:

.. code-block::
    
    Dim VelResult, PosResult As STKObjects.IAgDrResult
    
    Dim VelElems = New Object(3) {"x", "y", "z", "speed"}
    Dim PosElems = New Object(2) {"x", "y", "z"}
    
    VelResult = VelTimeVariable.ExecElements("18 Mar 2009 16:00:00.00", _"19 Mar 2009 16:00:00.00", _60, _VelElems)
    
    PosResult = PosTimeVariable.ExecElements("18 Mar 2009 16:00:00.00", _"19 Mar 2009 16:00:00.00", _60, _PosElems) 

You now have the original data from the J2000 Position Velocity Report stored in IAgDrResults and are ready to traverse the data. 

Traverse the result data

If you review look your original report, the data in the report consisted of time intervals with various elements. 

(./img/original-report-data.png)

Similarly, you need to cast your result to the appropriate interface to make use of your data. In the case of the J2000 Cartesian Velocity and Position DataProviders, that interface is the IAgDrIntervalCollection. Since each data provider result shares the same result type, you can consolidate the data traversal into one method, which takes an IAgDrResult interface: 

.. code-block::

    Sub WriteIntervalData(ByVal Result As STKObjects.IAgDrResult)
        Dim IntervalsList As STKObjects.IAgDrIntervalCollection
        Dim Interval As STKObjects.IAgDrInterval
        Dim DataSet As STKObjects.IAgDrDataSet
        Dim Values As Object
        Dim Value As Object
    
        IntervalsList = Result.Intervals

        'Iterate through the Intervals
        For Each Interval In IntervalsList
            Console.WriteLine(Interval.StartTime)
            Console.WriteLine(Interval.StopTime)
            'Iterate through the DataSets stored in the Interval
            For Each DataSet In Interval.DataSets
                Console.WriteLine(DataSet.Count)
                Console.WriteLine(DataSet.ElementName)
                Console.WriteLine(DataSet.ElementType)
                Console.WriteLine(DataSet.UnitType)
                'Get the values stored in the DataSet
                Values = DataSet.GetValues()
                'Iterate through the array of values
                For Each Value In Values
                    Console.WriteLine(CStr(Value))
                Next
            Next
        Next
 End Sub

.. note::
    The type of data returned by the DataProvider can be determined using the Category property of the IAgDrResult interface, which returns an enumeration describing the interface. The Value property is then cast to one of three interfaces, depending on the Category enumeration—IAgDrIntervalCollection, IAgDrSubSectionCollection, or IAgDrTextMessage. 

Complete the output
===================

Finally, you must call the method with IAgDrResults, and the data from the J2000 Position Velocity Report is traversed and output: 

.. code-block::

    WriteIntervalData(PosResult)
    WriteIntervalData(VelResult)

As previously noted, it is up to you to decide in what unit the data is returned. Issuing the following command before calling WriteIntervalData() changes the data that is output to be displayed in meters per second, rather then kilometers.

.. code-block::
    
    Root.UnitPreferences.SetCurrentUnit("DistanceUnit", "m")







