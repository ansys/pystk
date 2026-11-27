# # Results and graphs

# This tutorial demonstrates how the STK Object Model provides direct access to the data provider tools exposed by each object in the STK application that form the foundation of the report styles in the GUI.

# The following example uses the `J2000 Position Velocity` report to demonstrate the retrieval of data through the object model. This report consists of specific J2000 data provider elements from two groups: `Cartesian Velocity` and `Cartesian Position`, to report position and velocity of the object with respect to the object’s central body, as observed from its central body’s J2000 coordinate system.


# ![The J2000 Position Velocity report contents](./img/object-model-report-contents.png)

# ## Launching a new STK application instance

# Start by launching a new instance of the STK application. In this example, the STK Engine technology platform is used.

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# Create an STK scenario using the STK Root object:

root = stk.new_object_root()
root.new_scenario("GraphsAndResults")

# Once the scenario is created, it is possible to show a 3D Graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


globe_widget = GlobeWidget(root, 640, 480)
globe_widget.show()
# -

# Show a 2D Graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import MapWidget


map_widget = MapWidget(root, 640, 480)
map_widget.show()
# -

# ## Setting the scenario time period

# Using the newly created scenario, set the start and stop times. Rewind the scenario so that the graphics match the start and stop times of the scenario:

scenario = root.current_scenario
scenario.set_time_period("1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00")
root.rewind()

# ## Adding a satellite to the scenario

# Now that a new scenario is available, add a new Satellite object:

# +
from ansys.stk.core.stkobjects import STKObjectType


satellite = root.current_scenario.children.new(
    STKObjectType.SATELLITE, "SatelliteTwoBody"
)
# -

# Ensure that the satellite’s associated start and stop times match the scenario’s analysis interval and define its propagator:

# +
from ansys.stk.core.stkobjects import PropagatorTwoBody, PropagatorType


satellite.set_propagator_type(PropagatorType.TWO_BODY)

propagator = PropagatorTwoBody(satellite.propagator)
propagator.ephemeris_interval.set_start_and_stop_times(
    "1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00"
)

propagator.propagate()
# -

# ## Setting up data providers for use in the object model

# To retrieve the data for a `J2000 Position Velocity` report, set up its specific data providers for use in the Object Model. Use the various `DataProvider` interfaces to do this:

# +
from ansys.stk.core.stkobjects import DataProviderGroup


cart_vel = DataProviderGroup(satellite.data_providers["Cartesian Velocity"])
cart_pos = DataProviderGroup(satellite.data_providers["Cartesian Position"])

cart_vel_j2000 = cart_vel.group.item("J2000")
cart_pos_j2000 = cart_pos.group.item("J2000")
# -

# The `DataProviderCollection` and `DataProviderGroup` variables can be used to access information about the `J2000 Position Velocity` report.

# +
print('Some data providers available for the the "SatelliteTwoBody" satellite:')

data_providers = list(satellite.data_providers)
for index in range(len(data_providers)):
    if index > 9:
        print(f"\t...and {len(data_providers) - 10} more ")
        break
    print("\t" + str(data_providers[index].name))

print("Some data providers within the Cartesian Velocity group:")

for item in cart_vel.group:
    print("\t" + str(item.name))

print("Some data providers within the Cartesian Position group:")

for item in cart_pos.group:
    print("\t" + str(item.name))
# -

# The basic interfaces are now setup to compute information from the data providers that the report is using. Next, cast these objects to provide the `IDataProvider` interface with inputs so it can compute the proper data.

# ## Setting data provider “PreData” inputs

# Some data providers require input data before the calculation can provide data results. This data is known as PreData. There are two ways to ascertain if PreData is required for a particular data provider:
# - Refer to the data provider documentation, which provides the format of the PreData if any is required.
# - Retrieve the data provider schema and parse it for PreData tags.
#
# Use the `DataProviderCollection.get_schema()` method to get the schema for all STK data providers.

schema = str(satellite.data_providers.get_schema())

# Once the format of the PreData is known, set the `IDataProvider.pre_data` property. This property must be set before issuing the data provider’s calculation method.

# ## Setting the `pre_data` property on the `IDataProvider` interface

# The following example demonstrates setting the Satellite object’s path as the PreData for the `RIC Coordinates` data provider and then calls the data provider’s computation execution method.

# +
from ansys.stk.core.stkobjects import DataProviderResult, DataProviderTimeVarying


provider = DataProviderTimeVarying(satellite.data_providers["RIC Coordinates"])

provider.pre_data = "Satellite/SatelliteTwoBody"

result = provider.execute("1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00", 1)
# -

# The J2000 Position Velocity report uses a time period to provide the underlying data provider’s information about what data to compute. In the STK application GUI, you would open the Report & Graph Manager with the Satellite object, select the J2000 Position Velocity report style in the Installed Styles folder, then select the Specify Time Properties option to enter the equivalent PreData for the report. In the section above, you provided the same information to the object model data providers.

# ![Report time properties](./img/specify-time-properties.png)

# ## Computing and retrieving the data

# There are three ways to compute the data, depending on the data provider type; the first method requires a time interval and step size, the second requires only a time interval, and the third is independent of time.
#
# Provide input information to the data providers by casting the data provider interfaces to the proper execution interface. In the case of the `Cartesian Velocity` and `Cartesian Position` data providers, cast to `DataProviderTimeVarying`:

vel_time_var = DataProviderTimeVarying(cart_vel_j2000)
pos_time_var = DataProviderTimeVarying(cart_pos_j2000)

# Retrieve the information from the data providers. The data is always returned as a `DataProviderResult` object. Provide the `DataProviderTimeVarying.execute()` method of the `DataProviderTimeVarying` interfaces with the data provider inputs (start time, stop time, and step size):

vel_result = vel_time_var.execute("1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00", 1)
pos_result = pos_time_var.execute("1 Jul 2020 17:14:00.00", "1 Jul 2020 17:29:00.00", 1)

# `vel_result` and `pos_result` now contain the data from the `J2000 Cartesian Velocity` and `Cartesian Position` data providers, more data than the original report contained.
#
# ## Retrieving specific elements
#
# Recall that the original `Cartesian Position Velocity` report contained only four data provider elements of the `J2000` data provider group: `x`, `y`, `z`, and `speed`. Similarly, the `Cartesian Position` data provider contained within your report style only contains three elements in the `J2000` group: `x`, `y`, and `z`.
#
# When the `Cartesian Velocity-J2000` data provider group was executed, seven elements were retrieved instead of the four specifically contained in the report, adding the `time`, `radial`, and `intrack` elements to the `DataProviderResult`. To be precise as possible, `DataProviderResult` should contain only the elements that were contained in the original report. To do this, use the `DataProviderTimeVarying.execute_elements()` method.
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
# ## Traversing the report
#
# Review the report as seen in the STK application GUI below. The data in the report consists of time intervals with various elements:
#
# ![Original report](./img/original-report-data.png)
#
# Similarly, the result needs to be cast to the appropriate interface to make use of the data. In the case of the `Cartesian Velocity` and `Cartesian Position` data providers, that interface is the `DataProviderResultIntervalCollection`. Since each data provider result shares the same result type, consolidate the data traversal into one method, which takes a `DataProviderResult`:


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


#  **Note:** the type of data returned by the DataProvider can be determined using the `DataProviderResult.category` property, which returns an enumeration describing the interface. The `DataProviderResult.value` property is then cast to one of three interfaces, depending on the category enumeration: `DataProviderResultIntervalCollection`, `DataProviderResultSubSectionCollection`, or `DataProviderResultTextMessage`.

# ## Completing the output

# Finally, call the method with `DataProviderResult` arguments. The data from the `J2000 Position Velocity` report is traversed and output:

print("Position Results:")
write_interval_data(pos_result)
print("Velocity Results:")
write_interval_data(vel_result)

# As previously noted, it is up to you to decide in what unit the data is returned. Issuing the following command before calling `write_interval_data()` changes the data that is output to be displayed in meters per second, rather then kilometers per second.

# +
root.units_preferences.set_current_unit("DistanceUnit", "m")

write_interval_data(pos_result)
write_interval_data(vel_result)
