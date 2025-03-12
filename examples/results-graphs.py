# # Results and graphs tutorial

# This tutorial demonstrates how the STK Object Model provides direct access to the data provider tools that are exposed by each object in STK and form the foundation of the report styles in the GUI. It is inspired by [this](https://help.agi.com/stkdevkit/LinkedDocuments/ReportsToDataProviders.pdf) tutorial.

# ## What are reports?

# Reports in STK are typically used to generate results like satellite positions, sensor coverage, or any time-dependent parameters. PySTK can be used to generate reports, extract their data, and export them to formats like CSV or Excel. This tutorial demonstrates how to translate a report into its corresponding set of data providers, and demonstrates how to retrieve the data contained within through the object model.

# ## About STK data providers

# Data providers in STK are essential for accessing detailed, time-dependent data from objects and systems in a scenario. They are part of STK's object model and are key to extracting and manipulating information, such as satellite positions, sensor coverage, communication links, and more. By using the STK object model, PySTK can automate the retrieval of this data for processing, visualization, or reporting.

# The content of a report or graph is generated from the selected data providers for the report or graph style.

# ## Report styles

# To browse the various report styles available for a particular object in STK, and their corresponding data droviders, right-click an object in the STK Object Browser of the GUI and navigate to the `Graph and Report Manager` menu. In the manager dialog, expand the `Installed Styles` folder. This displays a list of the various report styles that are available for a particular object.

# ![Installed styles for satellite objects](./img/results-graphs/report-styles-expand.png)

# To view the data providers being used by a particular report style, click a report style, and click the `Properties`
# button (![The properties button in STK](./img/results-graphs/properties-button.png)) to display the `Report Style` window.

# ![The Report Style window in STK](./img/results-graphs/report-style-window.png)

# ## Report contents

# In the `Report Contents` section of the `Report Style` window, the various data providers that are used to derive the particular report are listed. These data providers provide the actual data content to the report.

# ![An example of a report's contents](./img/results-graphs/report-contents.png)

#  **_NOTE:_**  The `Section`, `Line`, and `Time` elements are used to provide formatting for the report style; they are not actual data providers.

# ## Data providers

# In the `Data Providers` section of the `Report Style` window, the data providers available for a particular object are listed. Expand a particular group to view the nested data providers associated with that group. Expanding a particular data provider further to display the data elements that are associated with it.

# ![An example of a data provider's elements](./img/results-graphs/data-providers.png)

#  **_NOTE:_**  `Groups`, `Data Providers`, and `Elements` are the organizing principles of the data providers provided by the STK Object Model.

# ## Object model

# Now that you have explored the concepts of report styles and data providers, continue to use the preceding example report, `J2000 Position Velocity`, to demonstrate retrieving its data through the Object Model. First, recall what data providers the report was constructed from. In the `Report Contents` window, the `J2000 Position Velocity` report is made up of specific elements of the J2000 data provider from two groups: `Cartesian Velocity` and `Cartesian Position`.

# ![The J2000 Position Velocity report contents](./img/results-graphs/object-model-report-contents.png)

# ## Launch a new STK instance

# Start by launching a new STK instance. In this example, STKEngine is used.

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# Create an STK scenario using the STK Root object:

root = stk.new_object_root()
root.new_scenario("GraphsAndResults")

# Once the scenario is created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


globe_widget = GlobeWidget(root, 640, 480)
globe_widget.show()
# -

# Show a 2D graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import MapWidget


map_widget = MapWidget(root, 640, 480)
map_widget.show()
# -

# ## Set the scenario time period

# Using the newly created scenario, set the start and stop times. Rewind the scenario so that the graphics match the start and stop times of the scenario:

scenario = root.current_scenario
scenario.set_time_period("1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00")
root.rewind()

# ## Adding a satellite to the scenario

# Now that a new scenario is available, add a new satellite:

# +
from ansys.stk.core.stkobjects import STKObjectType


satellite = root.current_scenario.children.new(
    STKObjectType.SATELLITE, "SatelliteTwoBody"
)
# -

# Ensure that the satellite's associated times use the scenario's times as well.

# +
from ansys.stk.core.stkobjects import PropagatorTwoBody, PropagatorType


satellite.set_propagator_type(PropagatorType.TWO_BODY)

propagator = PropagatorTwoBody(satellite.propagator)
propagator.ephemeris_interval.set_start_and_stop_times(
    "1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00"
)

propagator.propagate()
# -

# ## Setup data providers for use in the object model

# To retrieve the data for the `J2000 Position Velocity` report, setup its specific data providers for use in the Object Model. Use the various `DataProvider` interfaces to do this:

# +
from ansys.stk.core.stkobjects import DataProviderGroup


cart_vel = DataProviderGroup(satellite.data_providers["Cartesian Velocity"])
cart_pos = DataProviderGroup(satellite.data_providers["Cartesian Position"])

cart_vel_j2000 = cart_vel.group.item("J2000")
cart_pos_j2000 = cart_pos.group.item("J2000")
# -

# The basic interfaces are now setup to compute information from the data providers that the report is using. Next, cast these objects to provide the `iDataProvider` interface with inputs so it can compute the proper data.

# ## Data provider "PreData" inputs

# Some data providers require input data before the calculation can provide data results. This data is known as PreData. There are two ways to ascertain if PreData is required for a particular data provider:
# - Refer to the data provider documentation which provides the format of the PreData if any is required.
# - Retrieve the data provider schema and parse it for PreData tags.
#
# Use the `DataProviderCollection.get_schema()` method to get the schema for all STK data providers.

schema = str(satellite.data_providers.get_schema())

# Once the format of the PreData is known, set the `IDataProvider.pre_data` property. This property must be set before issuing the data provider's calculation method.

# ## Set the `pre_data` property on the `IDataProvider` interface

# The following example demonstrates setting the satellite's object path as the PreData for the `RIC Coordinates` data provider and then calls the data provider's computation execution method.

# +
from ansys.stk.core.stkobjects import DataProviderResult, DataProviderTimeVarying


provider = DataProviderTimeVarying(satellite.data_providers["RIC Coordinates"])

provider.pre_data = "Satellite/SatelliteTwoBody"

result = DataProviderResult(
    provider.execute("1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00", 1)
)
# -

# ## Data provider time inputs

# In the `Time Period` section of the `Report` window in STK, highlight `J2000 Position Velocity` and click the `Specify Time Properties` radio button. The `J2000 Position Velocity` report uses a time period to provide the underlying data provider's information about what data to compute. Provide the same information to the object model data providers.

# ![Report time properties](./img/results-graphs/specify-time-properties.png)

# ## Retrieve the data

# There are three ways to compute the data, depending on the data provider type. The first method requires a time interval and step size, the second requires only a time interval, and the third is independent of time.
#
# Pprovide input information to the data providers by casting the data provider interfaces to the proper execution interface. In the case of the `Cartesian Velocity` and `Cartesian Position` data providers, cast to `DataProviderTimeVarying`:

vel_time_var = DataProviderTimeVarying(cart_vel_j2000)
pos_time_var = DataProviderTimeVarying(cart_pos_j2000)

# Retrieve the information from the data providers. The data is always returned as a `DataProviderResult` object. Provide the `DataProviderTimeVarying.execute()` method of the `DataProviderTimeVarying` interfaces with the data provider inputs (start time, stop time, and step size):

# +
vel_result = DataProviderResult(
    vel_time_var.execute("1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00", 1)
)

pos_result = DataProviderResult(
    pos_time_var.execute("1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00", 1)
)
# -

# `vel_result` and `pos_result` now contain the data from the `J2000 Cartesian Velocity` and `Cartesian Position` data providers, more data than the original report contained.
#
# ## Retrieve specific elements
#
# Recall that the original `Cartesian Position Velocity` report contained only four elements of the `Cartesian Velocity J2000` group: `x`, `y`, `z`, and `speed`. Similarly, the `Cartesian Position J2000` data provider contained within your report style only contains three elements: `x`, `y`, and `z`.
#
# ![The J2000 Position Velocity report contents](./img/results-graphs/object-model-report-contents.png)
#
# When the J2000 data provider of `Cartesian Velocity` was executed, seven elements were retrieved instead of the four specifically contained in the
# report, adding the `time`, `radial`, and `intrack` elements to the `DataProviderResult`. To be precise as possible, DataProviderResult` should contain only the elements which were contained in the original report. To do this, use the `DataProviderTimeVarying.execute_elements()` method.
#
# First, specify in an array the elements to retrieve from the data provider. Next, pass the array into `DataProviderTimeVarying.execute_elements()`:

# +
vel_elems = ["x", "y", "z", "speed"]
pos_elems = ["x", "y", "z"]

vel_result = vel_time_var.execute_elements(
    "1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00", 60, vel_elems
)
pos_result = pos_time_var.execute_elements(
    "1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00", 60, pos_elems
)


# -

# The original data from the `J2000 Position Velocity` report is now stored in `DataProviderResult` objects and ready to traverse.
#
# ## Traverse the result data
#
# Review the original report. The data in the report consisted of time intervals with various elements.
#
# ![Original report](./img/results-graphs/original-report-data.png)
#
# Similarly, the result needs to be cast to the appropriate interface to make use of the data. In the case of the `J2000 Cartesian Velocity` and `Position` data providers, that interface is the `DataProviderResultIntervalCollection`. Since each data provider result shares the same result type, consolidate the data traversal into one method, which takes a `DataProviderResult`:


def write_interval_data(result: DataProviderResult):
    """Traverse and write the data stored in a DataProviderResult."""

    intervals = result.intervals

    # iterate through the intervals
    for interval in intervals:
        print(f"Interval from {interval.start_time} to {interval.stop_time}:")

        # iterate through the datasets stored in the interval
        for data_set in interval.data_sets:
            print(
                f"\tFound {data_set.count} values for {data_set.element_name} (element type {data_set.element_type}, {data_set.dimension_name} dimension):"
            )

            # get the values stored in the datasets
            values = data_set.get_values()

            # iterate through the array of values
            for value in values:
                print(f"\t\t{str(value)}")


#  **_NOTE:_** The type of data returned by the DataProvider can be determined using the `DataProviderResult.category` property, which returns an enumeration describing the interface. The `DataProviderResult.value` property is then cast to one of three interfaces, depending on the category enumeration: `DataProviderResultIntervalCollection`, `DataProviderResultSubSectionCollection`, or `DataProviderResultTextMessage`.

# ## Complete the output

# Finally, call the method with `DataProviderResult` arguments. The data from the `J2000 Position Velocity` report is traversed and output:

print("Position Results:")
write_interval_data(pos_result)
print("Velocity Results:")
write_interval_data(vel_result)

# As previously noted, it is up to you to decide in what unit the data is returned. Issuing the following command before calling `write_interval_data()` changes the data that is output to be displayed in meters per second, rather then kilometers.

# +
root.units_preferences.set_current_unit("DistanceUnit", "m")

write_interval_data(pos_result)
write_interval_data(vel_result)
