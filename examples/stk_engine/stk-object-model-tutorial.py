# # STK Object Model Tutorial (PySTK)

# This tutorial demonstrates some STK object model functions using PySTK. It corresponds to [this tutorial](https://help.agi.com/stkdevkit/index.htm#stkObjects/ObjectModelTutorial.html).

# ## Start STK

# Start by launching a new STK instance. In this example, STKEngine is used. We then get the STK Root object.

# +
from ansys.stk.core.stkengine import STKEngine

stk = STKEngine.start_application(noGraphics=False)
print(f"Using {stk.version}")
root = stk.new_object_root()
# -

# ## Scenario

# Now that you have the STK Root object, you need to create an STK scenario. The STK Root object has methods to create a new scenario or load an existing scenario.

# **Note:** There can be only one scenario open at a time.

root.new_scenario("MyScenario")

# The usual workflow of the STK Object Model applications is to set up the STK objects, establish a relationship between objects, perform analysis, and get results of the analysis.

# Once the scenario is created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget

plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## STK Objects

# The next step is to set up STK objects. STK has five main groups of objects: static/fixed objects (facility, place, and target), moving/vehicles (airplane, satellite, etc.), analysis objects (access and coverage), object groups (chain and constellation) and subobjects (antenna, receiver, transmitter, etc.)

# ### Create a facility object

# Create a Static STK Object (facility). All the new objects are attached to an existing parent object. Usually, the new objects are added to the children collection of the scenario.

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE

facility = root.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "MyFacility")
# -

# **Note:** the “new” method returns an object of the “IStkObject” type.

# #### Setting the facility position

# By default, new facility and place objects are created at AGI’s main office location. We want to change the facility position to one of our choosing.

# Don't make the mistake of assuming that you can use angle units as degree units. Be safe and set the unit to degrees before setting the position. Position units are special units and different for latitude and longitude. The longitude values can be in either -180 to 180 range or 0 to 360 range. As result, longitude units are unique and different from latitude units.

root.unit_preferences.item("LatitudeUnit").set_current_unit("deg")
root.unit_preferences.item("LongitudeUnit").set_current_unit("deg")

# Change the position of the facility to latitude 40 and longitude -80.

facility.position.assign_planetodetic(40, -80, 0)

# Let's take a look at the code used to get the current position of the facility.

positions = facility.position.query_planetodetic_array()
lat = positions[0]
lon = positions[1]
alt = positions[2]
print(f"Latitude:{lat}\nLongitude:{lon}\nAltitude:{alt}")

# The previous code shows how to set and get a cartodetic (latitude, longitude, altitude) position for a static STK object. If you take a look at the programming help, the "position" property is of the type IPosition located in the STK Utility library (ansys.stk.core.stkutil). Since we can set a position using cartesian coordinates (x,y,z) and query a position for cartodetic values, we can use the interface to convert a position between different coordinate types.

# #### Modifying graphics - changing the facility label

# The STK Object Model follows the logic of the STK desktop application. For example, if you want to change the label for facility, the IFacility interface contains the graphics property, which in turn contains the label_name property.

# +
# facility.graphics.label_name = "My Facility"
# -

# If you try to run the cell above, you will get an error that the LabelName is a read only property. To change the label, you must first disable the “Use Instance Name as Label” property. Since the object model follows the same logic as the user interface, the correct code is:

facility.graphics.use_inst_name_label = False
facility.graphics.label_name = "My Facility"

# ### Add a child object (sensor) to a facility

# The Sensor object belongs to a group of sub objects. The Sensor object cannot exist by itself. Instead, it has to be attached to another object, such as a facility or aircraft. Again, in order to create a new object, you need to add the object to the Children collection of the parent object; but in this case, we are going to do it the “right way” and check if the object exists first.

# You can use the children collection of the facility object to check if “MySensor” is already part of the list. If the sensor already exists, you could get the sensor object from the children collection, but in this case, we are using a “shortcut” way of getting the object directly from the root object. To get the sensor object, you need to pass the full path to the sensor object, which also includes the sensor’s parent object.

if (facility.children.contains(STK_OBJECT_TYPE.SENSOR, "MySensor")):
    sensor = root.get_object_from_path('Facility/MyFacility/Sensor/MySensor')
else:
    sensor = facility.children.new(STK_OBJECT_TYPE.SENSOR, "MySensor")

# #### Setting the sensor pattern

# Now, set the sensor’s pattern to complex conic. The default sensor object is defined as a simple conic sensor. So, the first step is to change the sensor type to complex conic. The API also provides a helper function to set the sensor pattern properties. To access this helper function, we must get an ISensorCommonTasks object through the sensor's common_tasks property. 

from ansys.stk.core.stkobjects import SENSOR_PATTERN
sensor.set_pattern_type(SENSOR_PATTERN.COMPLEX_CONIC)
sensor.common_tasks.set_pattern_complex_conic(50, 90, 0, 90)

# #### Adding access constraints to the sensor

# We will now add access constraints to the sensor. We will set the maximum range to 40 Km.

# The Intervisibility or access calculation is the starting calculation for most of the STK analysis. Imagine a two-dimensional coordinate system. Regardless of where you put two distinct points, you can always draw a line between the points. In order to get an accurate analysis, you need to restrict (constrain) the calculation. You do that by adding access constraints that are part of the access calculation to the object.

# The access_constraints property of the sensor holds an AccessConstraintCollection, which has an add_constraint method. We will use this method to add a range constraint using the ACCESS_CONSTRAINTS enum.

from ansys.stk.core.stkobjects import ACCESS_CONSTRAINTS
access_constraint = sensor.access_constraints.add_constraint(ACCESS_CONSTRAINTS.RANGE)

# This method returns an IAccessConstraintMinMax object, through which we can access the access constraint attributes. We can use this object to enable a maximum range value and set it to 40 Km (the units are set to Km by default).

access_constraint.enable_max = True
access_constraint.max = 40

# ### Create a vehicle (aircraft) using GreatArc propagator

from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE
aircraft = root.current_scenario.children.new(STK_OBJECT_TYPE.AIRCRAFT, "MyAircraft")
aircraft.set_route_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_GREAT_ARC)
great_arc_propagator = aircraft.route

# **Note:** The Aircraft object propagator is named “Route”, the satellite object propagator is named “Propagator”, and the missile object propagator is named “Trajectory”.

# #### Adding waypoints

# The next step is to add the waypoints. We will add waypoints (39,-79), (40,-80), and (41,-81).

# +
waypoint1 = great_arc_propagator.waypoints.add()
waypoint1.latitude = 39
waypoint1.longitude = -79
waypoint1.altitude = 10

waypoint2 = great_arc_propagator.waypoints.add()
waypoint2.latitude = 40
waypoint2.longitude = -80
waypoint2.altitude = 10

waypoint3 = great_arc_propagator.waypoints.add()
waypoint3.latitude = 41
waypoint3.longitude = -81
waypoint3.altitude = 10
# -

# We can then propagate the aircraft.

great_arc_propagator.propagate()

# We can zoom to the aircraft to visualize its path.

plotter.camera.position = [2200, 4940, 4500]
plotter.show()

# ### Create a vehicle (satellite) using the SPG4 propagator (if you have internet access) or the Two-Body propagator otherwise

# **Note:** This portion requires internet access. We provide alternate code using the Two-Body propagator if you do not have internet access. 

# First, create the satellite using online data for the International Space Station (SSN number 25544).

satellite = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "MySatellite")
satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
propagator = satellite.propagator
propagator.common_tasks.add_segs_from_online_source("25544")
propagator.propagate()

# The propagator property of the satellite returns an IVehiclePropagatorSGP4 object, which has a common_tasks property. Through this property, we can access IVehiclePropagatorSGP4CommonTasks, which holds helper methods for this propagator type. We can then use the add_segs_from_online_source helper method to add the satellite from the AGI server.

# Alternately, if you do not have internet access, you an add a satellite using a Two-Body propagator.

satellite = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "MySatellite")
satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
propagator = satellite.propagator
propagator.propagate()

# We can visualize the satellite's orbit.

plotter.camera.position = [7850, 17600, 16040]
plotter.show()

# #### Adding access constraints to the satellite

# Our scenario now includes one static object (facility) with a child object (sensor), and two vehicles (aircraft and satellite). STK performs analysis between objects in four-dimensional space (x, y, z, and time). In theory, any two points in a three dimensional system can always "see" each other. STK assumes that objects cannot "see" each other through the planet Earth by automatically enabling "Line of site" constraint on all objects. Similar to the way we restricted sensor range, we can add additional rules to our calculations. Since it is very hard to observe satellites when they are in the Earth's shadow, we will add a direct sun constraint to the satellite object.

from ansys.stk.core.stkobjects import CONSTRAINT_LIGHTING
lighting_constraint = satellite.access_constraints.add_constraint(ACCESS_CONSTRAINTS.LIGHTING)
lighting_constraint.condition = CONSTRAINT_LIGHTING.DIRECT_SUN

# Our scenario now contains facility, aircraft, and satellite. We made sure we can only "see" the satellite if it's illuminated by the Sun. Now we need to run some kind of analysis. The most common type of the analysis is access or the intervisibility calculation.

# ### Calculate access

# Create and calculate the access between facility and satellite.

access = facility.get_access_to_object(satellite)
access.compute_access()

# You can access results of the STK calculations through “data providers.” The data providers in the object model are the equivalent of the Report and Graph Manager in the user interface. Create a custom report in the desktop application to figure out which data you will need in the code.

# ### Get AER (azimuth, elevation, range) access results from the data provider

# The first thing that you need to determine is the time frame for the analysis. In most cases, the time frame will be equivalent to the scenario interval. In this case, we only care about data during the access periods. The computed access intervals property contains a list of the access periods.

access_intervals = access.computed_access_interval_times

# Next, we need to get appropriate data provider. You are going to use AER report with the default reference frame.

# By creating a sample report in the desktop application, we know that the data provider is time varying, and that data provider is located under the AER Data group. The data provider contains 15 “columns” of data. You can speed up the calculation by requesting only columns that you need. 

# Execute the element call return results based on the time interval and time step. The “data sets” represent columns of the report. The order of the columns is the same as in the report. The order of the columns requested in the elements array is ignored.
# Since the data is returned in the columns format and we usually work with rows of data, we will create a class that represents the row of data and add the information to the list collection.

# +
access_data_provider_aer = access.data_providers.item("AER Data").group.item("Default")
data_provider_elements = ["Time", "Azimuth", "Elevation", "Range"]

for i in range(0, access_intervals.count):
    times = access_intervals.get_interval(i)
    data_provider_result = access_data_provider_aer.exec_elements(times[0], times[1], 1, data_provider_elements)
    time_values = data_provider_result.data_sets.get_data_set_by_name("Time").get_values()
    azimuth_values = data_provider_result.data_sets.get_data_set_by_name("Azimuth").get_values()
    elevation_values = data_provider_result.data_sets.get_data_set_by_name("Elevation").get_values()
    range_values = data_provider_result.data_sets.get_data_set_by_name("Range").get_values()
# -

# We can also convert the data provider data sets to a pandas dataframe or numpy array.

data_provider_result.data_sets.to_pandas_dataframe()

data_provider_result.data_sets.to_numpy_array()[:10]

# ## Analysis Workbench

# ### Create a vector between the satellite and facility objects.

# AGI introduced the Vector Geometry Tool (VGT) with STK 9. In STK 10, VGT became part of the Analysis Workbench that also includes the Time Tool and Calculation Tool. To keep the interface clean and to maintain backward compatibility, all Analysis Workbench functionality is located in the VGT property of the IStkObject interface.

# +
from ansys.stk.core.vgt import VECTOR_GEOMETRY_TOOL_VECTOR_TYPE

vector = facility.vgt.vectors.factory.create("FromTo", "Vector description", VECTOR_GEOMETRY_TOOL_VECTOR_TYPE.DISPLACEMENT)
vector.destination.set_point(satellite.vgt.points.item("Center"))
# -

# ### Visualize the vector and set its size to 4.0:

from ansys.stk.core.stkobjects import GEOMETRIC_ELEM_TYPE
boresight_vector = facility.graphics_3d.vector.reference_crdns.add(GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, "Facility/MyFacility FromTo Vector")
facility.graphics_3d.vector.vector_size_scale = 4.0

# **Note:** All vectors on the single object are the same size. So, in order to modify the vector’s appearance, you will need to set the global vector properties.

# **Note:** The add method requires an object type as an enumeration and a fully qualified path to the Analysis Workbench object. The path consists of the path to the parent object, the object name, and the object type ("Facility/MyFacility FromTo Vector").

# STK reports times of the local minimum, so you need to get the vector between objects and calculate the vector’s magnitude for each local minimum time.

# ### Get the vector between objects and calculate magnitude.

# First, get the built in calculation object from Analysis Workbench.

parameter_sets = access.vgt.parameter_sets.item("From-To-AER(Body)")

# Then, get the magnitude vector.

magnitude = parameter_sets.embedded_components.item("From-To-AER(Body).Cartesian.Magnitude")

# Get the times of the minimum value for each access interval.

min_times = parameter_sets.embedded_components.item("From-To-AER(Body).Cartesian.Magnitude.TimesOfLocalMin")
time_array = min_times.find_times().times
for i in range(0, len(time_array)):
    result = magnitude.evaluate(time_array[i])
    print(f"result at time {time_array[i]}: {result.value}")

# **Note:** Both the magnitude vector and time array are referenced by a long string that can be daunting to enter. The preference is to create an equivalent STK scenario in the desktop application. Then, from the properties of the Analysis Workbench object, you will get the name value that corresponds to the string value in the code.
