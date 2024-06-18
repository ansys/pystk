# # Satellite coverage area calculator
#
# This tutorial demonstrates how to calculate satellite coverage using PySTK. It is inspired by [this training](https://help.agi.com/stk/index.htm#training/GetStart_7_Coverage.htm).
#
# ## What is satellite coverage?
#
# Engineers and operators often need to determine the times that a satellite can "access" (or see) another object. Satellite coverage describes which areas of the Earth can access a satellite considering constraints defining what constitutes a valid access, including elevation angle, sun light or umbra restrictions, gimbal speed, range, and more. Satellite coverage can be calculated globally, or over a certain region.
#
# ## Problem statement
#
# Two satellites present circular orbits. The first satellite has an inclination of $97.3^\circ$ and an altitude of 400 km. The second satellite has a RAAN of $340^\circ$. Calculate the coverage these satellites provide over the tropics region of the Earth, defined as the area between the latitudes of $-23.5^\circ$ and $23.5^\circ$. Use a point resolution of $3.0^\circ$. Determine which satellite achieves higher coverage of the tropics region and if coverage is better or worse near the Equator. Finally, determine which areas of the tropics region receive coverage from both satellites at the same time.
#
# ## Launch a new STK instance
#
# Start by launching a new STK instance. In this example, STKEngine is used.

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(noGraphics=False)
print(f"Using {stk.version}")
# -
# ## Create a new scenario
#
# Create a new scenario in STK by running:

root = stk.new_object_root()
root.new_scenario("Coverage")

# Once the scenario is created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


globe_plotter = GlobeWidget(root, 640, 480)
globe_plotter.show()
# -

# A 2D graphics window can be created in order to better visualize the satellite coverage area:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import MapWidget


map_plotter = MapWidget(root, 640, 480)
map_plotter.show()
# -

# ## Set the scenario time period

# Using the newly created scenario, set the start and stop times. Rewind the scenario so that the graphics match the start and stop times of the scenario:

scenario = root.current_scenario
scenario.set_time_period("1 Jul 2016", "2 Jul 2016")
root.rewind()

# ## Add the satellites to the scenario

# First, add a satellite in a polar orbit:

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE


polar_sat = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "PolarSat")
# -

# Then, set the satellite's propagator to J4Pertubation:

# +
from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE


polar_sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)
# -

# The satellite should have a circular orbit with an inclination of $97.3^\circ$ and an altitude of 400 km, which translates to an initial state of X = -6374.8, Y = -2303.27, Z = -0.0000357827, X Velocity = -0.499065, Y Velocity = 1.38127, and Z Velocity = 7.6064 in a Cartesian coordinate system:

# +
from ansys.stk.core.stkobjects import COORDINATE_SYSTEM


polar_sat_propagator = polar_sat.propagator
r_vec = [-6374.8, -2303.27, -0.0000357827]
v_vec = [-0.499065, 1.38127, 7.6064]
polar_sat_propagator.initial_state.representation.assign_cartesian(
    COORDINATE_SYSTEM.J2000, *r_vec, *v_vec
)
# -

# Then, insert a satellite named Shuttle:

shuttle = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Shuttle")

# Set the satellite's propagator to J4Pertubation:

shuttle.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)

# The satellite should have a circular orbit with a RAAN of $340^\circ$, which translates to an initial state of X = -6878.12, Y = -16.3051, Z = 0.00199559, X Velocity = -0.0115701, Y Velocity = -4.88136, and Z Velocity = 5.38292 in a Cartesian coordinate system:

shuttle_propagator = shuttle.propagator
r_vec = [-6878.12, -16.3051, 0.00199559]
v_vec = [-0.0115701, -4.88136, 5.38292]
shuttle_propagator.initial_state.representation.assign_cartesian(
    COORDINATE_SYSTEM.J2000, *r_vec, *v_vec
)

# Finally, propagate both satellites:

polar_sat_propagator.propagate()
shuttle_propagator.propagate()

# View their paths in 2D or 3D using the graphics widgets:

map_plotter.show()

globe_plotter.show()

# ## Create a coverage definition

# Create a coverage definition object modeling the region of Tropics:

tropics = root.current_scenario.children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "Tropics")

# Assign the coverage definition a grid of type latitude bounds, with a minimum latitude of $-23.5^\circ$, a maximum latitude of $23.5^\circ$, and point granularity of $3.0^\circ$ lat/lon:

# +
from ansys.stk.core.stkobjects import COVERAGE_BOUNDS


tropics.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT
tropics.grid.bounds.min_latitude = -23.5
tropics.grid.bounds.max_latitude = 23.5
tropics.grid.resolution.lat_lon = 3
# -
# ### Assign the assets

# Assign the satellites (PolarSat and Shuttle) as assets on the coverage definition. To do so, use a path to the satellites of the form ``ItemType/ItemName``.

tropics.asset_list.add("Satellite/PolarSat")
tropics.asset_list.add("Satellite/Shuttle")

# ### Configure the 2D graphics

# Use the coverage definition's static property (which holds a ``ICoverageGraphics2DStatic`` object), to set the Show Regions, Show Region Labels, Show Points, and Points - Fill graphics properties.

tropics.graphics.static.is_region_visible = True
tropics.graphics.static.is_labels_visible = True
tropics.graphics.static.is_points_visible = True
tropics.graphics.static.fill_points = True

# To set the visibility for Progress of Computations, use a ``CoverageGraphics2DProgres``s object, which is available through the ``ICoverageGraphics`` object's ``progress`` property. 

tropics.graphics.progress.is_visible = True

# To set the satisfaction visibility, use an ``ICoverageGraphics2DAnimation`` object, which is accessible through the ``ICoverageGraphics`` object's ``animation`` property. 

tropics.graphics.animation.is_satisfaction_visible = False

# View the coverage definition's graphics using the 2D graphics window:

map_plotter.show()

# ## Compute coverage and create reports

# Use the tropics coverage definition object to compute accesses:

tropics.compute_accesses()


# ### Create reports

# To create reports, access the data providers associated with the coverage object. Then, select the type of report using the ``item`` method and the name of the report. The Coverage By Asset and Coverage by Latitude reports correspond to ``IDataProviderFixed`` objects. By using the ``exec`` method, compute the data needed for these reports. The ``exec`` method returns an ``IDataProviderResult`` object, through which it is possible to access an ``IDataProviderResultDataSetCollection`` through the ``data_sets`` property. This object corresponds to the desired data.

access_by_asset = tropics.data_providers.item("Coverage By Asset")
access_by_latitude = tropics.data_providers.item("Coverage by Latitude")
asset_data_provider_results = access_by_asset.exec()
latitude_data_provider_results = access_by_latitude.exec()

# Convert the results to pandas dataframes or numpy arrays to better understand the data:

# **Which satellite achieved a higher average coverage of the tropics region?**

# Converting to a pandas dataframe makes the answer clear:

asset_data_provider_results.data_sets.to_pandas_dataframe()

# **Answer:** PolarSat achieved higher average coverage of the tropics region with an average % coverage of 2.704572194409824.

# Or, convert to a numpy array:

asset_data_provider_results.data_sets.to_numpy_array()

# **Was coverage better or worse near the Equator?**

latitude_data_provider_results.data_sets.to_pandas_dataframe()

# **Answer:** Coverage was worse near the equator.

# ## Assess the quality of coverage with a Figure of Merit

# ### Set the graphics

# The Figure of Merit object has its own graphics which the Coverage Definition graphics interferes with. So, disable the Show Regions and Show Points options of the Coverage Definition:

tropics.graphics.static.is_region_visible = False
tropics.graphics.static.is_points_visible = False

# ### Create a Figure of Merit

# Create a Figure of Merit named TwoEyes:

two_eyes = tropics.children.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, "TwoEyes")

# ### Define the coverage

# Set the coverage definition to N Asset Coverage:

# +
from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_DEFINITION_TYPE


two_eyes.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.N_ASSET_COVERAGE)
# -

# Set the compute type to Maximum:

# +
from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_COMPUTE


two_eyes.definition.set_compute_type(FIGURE_OF_MERIT_COMPUTE.MAXIMUM)
# -

# ### Configure the graphics

# Set some animation graphics options for the Figure of Merit object:

# +
from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION


two_eyes.graphics.animation.is_visible = True
two_eyes.graphics.animation.accumulation = FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.CURRENT_TIME
two_eyes.graphics.animation.fill_points = False
two_eyes.graphics.animation.marker_style = "Star"
# -

# ### Configure the static graphics

# Set some static graphics options:

two_eyes.graphics.static.is_visible = True
two_eyes.graphics.static.fill_points = False
two_eyes.graphics.static.marker_style = "Circle"

# View the figure of merit using the 3d graphics window:

globe_plotter.show()

# ### Define the coverage for the Figure of Merit

# Adjust the definition of the Figure of Merit's coverage to determine which points have coverage from both satellites at the same time:

# +
from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_SATISFACTION_TYPE


two_eyes.definition.satisfaction.enable_satisfaction = True
two_eyes.definition.satisfaction.satisfaction_type = FIGURE_OF_MERIT_SATISFACTION_TYPE.AT_LEAST
two_eyes.definition.satisfaction.satisfaction_threshold = 2
# -

# The 3D Graphics window immediately reflects the reduction in the amount of the coverage region that satisfies the 'at least 2' criterion.

# ### Configure the animation graphics

# Set some animation graphics to see when points are covered by neither, one, or both satellites:

# +
from ansys.stk.core.utilities.colors import Color
from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD


two_eyes.graphics.static.is_visible = False
two_eyes.graphics.animation.contours.is_visible = True
two_eyes.graphics.animation.contours.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
level1 = two_eyes.graphics.animation.contours.level_attributes.add_level(1)
level1.color = Color.from_rgb(250, 7, 214)
level2 = two_eyes.graphics.animation.contours.level_attributes.add_level(2)
level2.color = Color.from_rgb(45, 250, 195)
# -

# Animate the scenario:

root.rewind()

globe_plotter.camera.position = [-10290, 33525, 780]
globe_plotter.show()

root.play_forward()

# Note that points are highlighted in pink when they are covered by only one satellite, and in blue when covered by both satellites.

# ### Create a Satisfied by Time report

# The Satisfied by Time report summarizes the percentage and true area of the grid that satisfies the Figure Of Merit at each time step:

satisfied_by_time_result = two_eyes.data_providers.item("Satisfied by Time").exec(scenario.start_time, scenario.stop_time, 60.0)
satisfied_by_time_result.data_sets.to_pandas_dataframe()
