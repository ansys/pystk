# # Access between facility and satellite calculator

# This tutorial demonstrates how to calculate access between a facility and a satellite using PySTK. It is inspired by [this tutorial](https://help.agi.com/stkdevkit/Content/stkObjects/ObjectModelTutorial.html).

# ## What is access?

# The intervisibility or access calculation is the starting calculation for most STK analyses. Imagine a two-dimensional coordinate system. Regardless of where two distinct points are located, it is always possible to draw a line between the points. For an accurate analysis, the calculation needs to be restricted (constrained). This is done by adding access constraints. STK assumes that objects cannot "see" each other through the planet Earth by automatically enabling "Line of sight" constraint on all objects. However, in many cases, other access constraints are also needed. For example, it is possible to define constraints around many conditions including elevation angle, sun light or umbra restrictions, gimbal speed, range, and more. Access considering these constraints can be calculated between many kinds of objects, including sensors and satellites.

# ## Problem statement

# A facility is located at latitude $40^\circ$ and longitude $-80^\circ$. The facility includes a sensor with a pattern type of complex conic, with an inner cone half angle of $50^\circ$, an outer cone half angle of $90^\circ$, a minimum clock angle of $0^\circ$, and a maximum clock angle of $90^\circ$. The sensor has a maximum range of 40 km. The sensor interacts with the International Space Station (SSN number 25544), which has an SPG4 propagator. This satellite can also only be seen if it is directly illuminated by the Sun.
#
# Calculate the time periods during which the sensor can communicate with the satellite. Find the azimuth, elevation, and range of the satellite during these access periods. Finally, create a vector between the facility and satellite, and, for each access interval, determine at what time this vector was at a minimum magnitude.

# ## Launch a new STK instance

# Start by launching a new STK instance. In this example, STKEngine is used.

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(noGraphics=False)
print(f"Using {stk.version}")
root = stk.new_object_root()
# -

# ## Create a new scenario

# Create an STK scenario using the STK Root object:

# **Note:** There can be only one scenario open at a time.

root.new_scenario("MyScenario")

# Once the scenario is created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Create a facility object

# Create a Static STK Object (facility). All new objects are attached to an existing parent object. In this case, the new facility is added to the children collection of the scenario.

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE


facility = root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "MyFacility")
# -

# **Note:** the “new” method returns an object of the ``IStkObject`` type.

# ### Set the facility position

# By default, new facility and place objects are created at AGI’s main office location. It is possible to change the facility position.

# First set the position units to degrees:

root.unit_preferences.item("LatitudeUnit").set_current_unit("deg")
root.unit_preferences.item("LongitudeUnit").set_current_unit("deg")

# Change the position of the facility to latitude $40^\circ$ and longitude $-80^\circ$:

facility.position.assign_planetodetic(40, -80, 0)

# Get the current position of the facility:

positions = facility.position.query_planetodetic_array()
lat = positions[0]
lon = positions[1]
alt = positions[2]
print(f"Latitude:{lat}\nLongitude:{lon}\nAltitude:{alt}")

# The previous code shows how to set and get a cartodetic (latitude, longitude, altitude) position for a static STK object. The ``position`` property is of the type ``IPosition`` located in the STK Utility library (``ansys.stk.core.stkutil``).

# ### Change the facility label

# The STK Object Model follows the logic of the STK desktop application. For example, to change the label for the facility, the IFacility interface contains the ``graphics`` property, which in turn contains the ``label_name`` property. To change the label, the “Use Instance Name as Label” property must first be disabled.

facility.graphics.use_inst_name_label = False
facility.graphics.label_name = "My Facility"

# ### Add a child object (sensor) to a facility

# The Sensor object belongs to a group of sub objects. The Sensor object cannot exist by itself. It must be attached to another object, such as a facility or aircraft.

# It is possible to use the ``children`` collection of the facility object to check if “MySensor” is already part of the collection. If the sensor already exists, it is possible to get the sensor object from the children collection. It is also possible to get the object directly from the root object by passing the full path to the sensor object.

if (facility.children.contains(STK_OBJECT_TYPE.SENSOR, "MySensor")):
    sensor = root.get_object_from_path('Facility/MyFacility/Sensor/MySensor')
else:
    sensor = facility.children.new(STK_OBJECT_TYPE.SENSOR, "MySensor")

# #### Set the sensor pattern

# Now, set the sensor’s pattern to complex conic. The default sensor object is defined as a simple conic sensor. So, the first step is to change the sensor type to complex conic. The API also provides a helper function to set the sensor pattern properties. To access this helper function, get an ``ISensorCommonTasks`` object through the sensor's ``common_tasks`` property. 

# +
from ansys.stk.core.stkobjects import SENSOR_PATTERN


sensor.set_pattern_type(SENSOR_PATTERN.COMPLEX_CONIC)
sensor.common_tasks.set_pattern_complex_conic(50, 90, 0, 90)
# -

# #### Add access constraints to the sensor

# The ``access_constraints`` property of the sensor holds an ``AccessConstraintCollection``, which has an ``add_constraint`` method. Use this method to add a range constraint using the ``ACCESS_CONSTRAINTS`` enum.

# Add an access constraint to the sensor defining a maximum range of 40 km:

# +
from ansys.stk.core.stkobjects import ACCESS_CONSTRAINTS


access_constraint = sensor.access_constraints.add_constraint(ACCESS_CONSTRAINTS.RANGE)
# -

# This method returns an ``IAccessConstraintMinMax`` object, through it is possible to access the access constraint attributes. Use this object to enable a maximum range value and set it to 40 km (the units are set to km by default):

access_constraint.enable_max = True
access_constraint.max = 40

# ### Add a satellite using the SPG4 propagator

# **Note:** This portion requires internet access.

# First, create the satellite using online data for the International Space Station (SSN number 25544):

# +
from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE


satellite = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "MySatellite")
satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
propagator = satellite.propagator
propagator.common_tasks.add_segs_from_online_source("25544")
propagator.propagate()
# -

# The propagator property of the satellite returns an ``IVehiclePropagatorSGP4`` object, which has a ``common_tasks`` property. Through this property, it is possible to access ``IVehiclePropagatorSGP4CommonTasks``, which holds helper methods for this propagator type. Then, use the ``add_segs_from_online_source`` helper method to add the satellite from the AGI server.

# Visualize the satellite's orbit using the 3D graphics window:

plotter.camera.position = [7850, 17600, 16040]
plotter.show()

# #### Add access constraints to the satellite

# Since it is very hard to observe satellites when they are in the Earth's shadow, add a direct sun constraint to the satellite object:

# +
from ansys.stk.core.stkobjects import CONSTRAINT_LIGHTING


lighting_constraint = satellite.access_constraints.add_constraint(ACCESS_CONSTRAINTS.LIGHTING)
lighting_constraint.condition = CONSTRAINT_LIGHTING.DIRECT_SUN
# -

# Now that the satellite can only be "seen" if it is illuminated by the Sun, it is possible to run an access or intervisibility calculation.

# ### Calculate access

# Create and calculate the access between facility and satellite:

access = facility.get_access_to_object(satellite)
access.compute_access()

# It is possible to access results of STK calculations through data providers. The data providers in the object model are the equivalent of the Report and Graph Manager in the user interface.

# ### Get AER (azimuth, elevation, range) access results

# Determine the access periods using the ``computed_access_interval_times`` property:

access_intervals = access.computed_access_interval_times

# Next, get the data provider corresponding to an AER report with the default reference frame.

access_data_provider_aer = access.data_providers.item("AER Data").group.item("Default")
data_provider_elements = ["Time", "Azimuth", "Elevation", "Range"]

# Execute the element call return results based on the time interval and time step. The “data sets” represent columns of the report. The order of the columns is the same as in the report. The order of the columns requested in the elements array is ignored.
# Since the data is returned in the columns format, create lists that represents the rows of data:

for i in range(0, access_intervals.count):
    times = access_intervals.get_interval(i)
    data_provider_result = access_data_provider_aer.exec_elements(times[0], times[1], 1, data_provider_elements)
    time_values = data_provider_result.data_sets.get_data_set_by_name("Time").get_values()
    azimuth_values = data_provider_result.data_sets.get_data_set_by_name("Azimuth").get_values()
    elevation_values = data_provider_result.data_sets.get_data_set_by_name("Elevation").get_values()
    range_values = data_provider_result.data_sets.get_data_set_by_name("Range").get_values()

# Alternately, convert the data provider data sets to a pandas dataframe or numpy array:

aer_df = data_provider_result.data_sets.to_pandas_dataframe()
aer_df

# Visualize the data using a line chart:

# +
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md


# convert axes to correct types
aer_df['time'] = pd.to_datetime(aer_df["time"])
aer_df.set_index('time')
cols = ['azimuth', 'elevation', 'range']
aer_df[cols] = aer_df[cols].apply(pd.to_numeric)

# create plot
fig, aer_ax1 = plt.subplots(figsize=(8, 8))
# create second axis
aer_ax2 = aer_ax1.twinx()
# plot data
aer_ax2.plot(aer_df['time'], aer_df['range'], color='#ff73e8', label='range (km)')
aer_ax1.plot(aer_df['time'], aer_df['azimuth'], color='#63b1ff', label='azimuth (deg)')
aer_ax1.plot(aer_df['time'], aer_df['elevation'], color='#ffbe30', label='elevation (deg)')

# configure labels and grid
aer_ax2.set_ylabel('Distance')
aer_ax1.set_ylabel('Angle')
aer_ax1.set_xlabel('Time')
lines, labels = aer_ax1.get_legend_handles_labels()
lines2, labels2 = aer_ax2.get_legend_handles_labels()
plt.legend(lines + lines2, labels + labels2, loc='upper right')
plt.title('AER over Time')
aer_ax1.set_facecolor('#f7f7f7')
aer_ax1.grid(visible=True, which='both', linestyle='--')
formatter = md.DateFormatter('%H:%M')
aer_ax1.xaxis.set_major_formatter(formatter)
xlocator_major = md.MinuteLocator(interval = 2)
aer_ax1.xaxis.set_major_locator(xlocator_major)
xlocator_minor = md.MinuteLocator(interval = 1)
aer_ax1.xaxis.set_minor_locator(xlocator_minor)

plt.show()
# -

# Or, convert the data to a numpy array:

data_provider_result.data_sets.to_numpy_array()[:10]

# ## Analysis Workbench

# ### Create a vector between the satellite and facility objects

# AGI introduced the Vector Geometry Tool (VGT) with STK 9. In STK 10, VGT became part of the Analysis Workbench that also includes the Time Tool and Calculation Tool. To keep the interface clean and to maintain backward compatibility, all Analysis Workbench functionality is located in the ``vgt`` property of the ``IStkObject`` interface.

# Create a vector between the satellite and facility objects:

# +
from ansys.stk.core.vgt import VECTOR_GEOMETRY_TOOL_VECTOR_TYPE


vector = facility.vgt.vectors.factory.create("FromTo", "Vector description", VECTOR_GEOMETRY_TOOL_VECTOR_TYPE.DISPLACEMENT)
vector.destination.set_point(satellite.vgt.points.item("Center"))
# -

# Visualize the vector and set its size to 4.0:

# +
from ansys.stk.core.stkobjects import GEOMETRIC_ELEM_TYPE


boresight_vector = facility.graphics_3d.vector.reference_crdns.add(GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Facility/MyFacility FromTo Vector")
facility.graphics_3d.vector.vector_size_scale = 4.0
# -

# **Note:** All vectors on the single object are the same size. So, in order to modify the vector’s appearance, it is necessary to set the global vector properties.

# **Note:** The add method requires an object type as an enumeration and a fully qualified path to the Analysis Workbench object. The path consists of the path to the parent object, the object name, and the object type (``"Facility/MyFacility FromTo Vector"``).

# STK reports times of the local minimum, so get the vector between objects and calculate the vector’s magnitude for each local minimum time:

# First, get the built in calculation object from Analysis Workbench:

parameter_sets = access.vgt.parameter_sets.item("From-To-AER(Body)")

# Then, get the magnitude vector:

magnitude = parameter_sets.embedded_components.item("From-To-AER(Body).Cartesian.Magnitude")

# Get the times of the minimum value for each access interval:

min_times = parameter_sets.embedded_components.item("From-To-AER(Body).Cartesian.Magnitude.TimesOfLocalMin")
time_array = min_times.find_times().times
for i in range(0, len(time_array)):
    result = magnitude.evaluate(time_array[i])
    print(f"result at time {time_array[i]}: {result.value}")
