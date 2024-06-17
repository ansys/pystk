# # Using Coverage
#
# This tutorial corresponds to [this training](https://help.agi.com/stk/index.htm#training/GetStart_7_Coverage.htm?TocPath=Training%257CLevel%25203%2520-%2520Focused%257CFeature%2520Specific%257CCoverage%257C_____1).
#
# In this exercise you will use STK's Coverage capability to define and evaluate the coverage of a region, using available Coverage assets. In this lesson, you will learn to use:
# - the Coverage Definition object
# - the Figure of Merit object
#
# ## Problem statement
#
# You want to define a coverage region in the tropics and compute the coverage using two satellites.
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

plotter3d = GlobeWidget(root, 640, 480)
plotter3d.show()
# -

# We can also show a 2d graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import MapWidget

plotter2d = MapWidget(root, 640, 480)
plotter2d.show()
# -

# ## Set the scenario time period

# Using the newly created scenario, set the start and stop times. We will also rewind the scenario so that the graphics we see match the start and stop times that we set.

scenario = root.current_scenario
scenario.set_time_period("1 Jul 2016", "2 Jul 2016")
root.rewind()

# ## Create 2 satellites

# First insert a satellite named PolarSat:

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE

polar_sat = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "PolarSat")
# -

# Then, set the satellite's propagator to J4Pertubation:

from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE, COORDINATE_SYSTEM, ORBIT_STATE_TYPE
polar_sat.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)

# The satellite should have a circular orbit with an inclination of 97.3&deg; and an altitude of 400 km, which translates to an initial state of X = -6374.8, Y = -2303.27, Z = -0.0000357827, X Velocity = -0.499065, Y Velocity = 1.38127, and Z Velocity = 7.6064 in a Cartesian coordinate system.

polar_sat_propagator = polar_sat.propagator
polar_sat_propagator.initial_state.representation.assign_cartesian(ORBIT_STATE_TYPE.CARTESIAN, -6374.8, -2303.27, -0.0000357827, -0.499065, 1.38127, 7.6064)

# Then, insert a satellite named Shuttle:

shuttle = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Shuttle")

# Set the satellite's propagator to J4Pertubation:

shuttle.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_J4_PERTURBATION)

# The satellite should have a circular orbit with a RAAN of 340&deg;, which translates to an initial state of X = -6878.12, Y = -16.3051, Z = 0.00199559, X Velocity = -0.0115701, Y Velocity = -4.88136, and Z Velocity = 5.38292 in a Cartesian coordinate system.

shuttle_propagator = shuttle.propagator
shuttle_propagator.initial_state.representation.assign_cartesian(ORBIT_STATE_TYPE.CARTESIAN, -6878.12, -16.3051, 0.00199559, -0.0115701, -4.88136, 5.38292)

# Finally, propagate both satellites:

polar_sat_propagator.propagate()
shuttle_propagator.propagate()

# We can view their paths in 2D or 3D using the graphics widgets.

plotter2d.show()

plotter3d.show()

# ## Create a coverage definition

# Insert a coverage definition named Tropics:

tropics = root.current_scenario.children.new(STK_OBJECT_TYPE.COVERAGE_DEFINITION, "Tropics")

# Assign the coverage definition a grid of type latitude bounds, with a minimum latitude of -23.5&deg;, a maximum latitude of 23.5&deg;, and point granularity of 3.0&deg; lat/lon:

# +
from ansys.stk.core.stkobjects import COVERAGE_BOUNDS

tropics.grid.bounds_type = COVERAGE_BOUNDS.BOUNDS_LAT
tropics.grid.bounds.min_latitude = -23.5
tropics.grid.bounds.max_latitude = 23.5
tropics.grid.resolution.lat_lon = 3
# -
# ### Assign the Assets:

# Assign the satellites (PolarSat and Shuttle) that you previously inserted as assets on the coverage definition. To do so, use a path to the satellites of the form ItemType/ItemName.

tropics.asset_list.add("Satellite/PolarSat")
tropics.asset_list.add("Satellite/Shuttle")

# ### Set the 2D Graphics Attributes

# We can use the coverage definition's static property (which holds a ICoverageGraphics2DStatic object), to set the Show Regions, Show Region Labels, Show Points, and Points - Fill graphics properties.

tropics.graphics.static.is_region_visible = True
tropics.graphics.static.is_labels_visible = True
tropics.graphics.static.is_points_visible = True
tropics.graphics.static.fill_points = True

# To set the visibility for Progress of Computations, we need a CoverageGraphics2DProgress object, which is available through the ICoverageGraphics object's progress property. 

tropics.graphics.progress.is_visible = True

# We need an ICoverageGraphics2DAnimation to set the satisfaction visibility. This object is accessible through the ICoverageGraphics object's animation property. 

tropics.graphics.animation.is_satisfaction_visible = False

# We can now view the coverage definition's graphics using the 2D graphics window:

plotter2d.show()

# ## Compute coverage and create reports

# Use the tropics coverage definition object to compute accesses:

tropics.compute_accesses()


# ### Create reports

# To create reports, we must access the data providers associated with the coverage object. We can then select which kind of report we want to access by using the .item method and the name of the report we are interested in. .item in this case returns an IDataProviderFixed object. By using the .exec method, we can compute the data. .exec returns an IDataProviderResult object, through which we can access an IDataProviderResultDataSetCollection through the data_sets property. From this object, we can see the data returned.

access_by_asset = tropics.data_providers.item("Coverage By Asset")
access_by_latitude = tropics.data_providers.item("Coverage by Latitude")
asset_data_provider_results = access_by_asset.exec()
latitude_data_provider_results = access_by_latitude.exec()

# We can convert the results to pandas dataframes or numpy arrays to better understand the data.

# **Which satellite achieved a higher average coverage of the tropics region?**

# Converting to a pandas dataframe makes the answer clear:

asset_data_provider_results.data_sets.to_pandas_dataframe()

# **Answer:** PolarSat achieved higher average coverage of the tropics region with an average % coverage of 2.704572194409824.

# We could also have converted to a numpy array:

asset_data_provider_results.data_sets.to_numpy_array()

# **Was coverage better or worse near the Equator?**

latitude_data_provider_results.data_sets.to_pandas_dataframe()

# **Answer:** Coverage was worse near the equator.

# ## Assess the Quality of Coverage with a Figure of Merit

# ### Set the Graphics

# The Figure of Merit object we are creating next has its own graphics and we do not want the Coverage Definition graphics to interfere. We will disable the Show Regions and Show Points options of the Coverage Definition.

tropics.graphics.static.is_region_visible = False
tropics.graphics.static.is_points_visible = False

# ### Create a Figure of Merit

# Create a figure of merit named TwoEyes:

two_eyes = tropics.children.new(STK_OBJECT_TYPE.FIGURE_OF_MERIT, "TwoEyes")

# ### Define the Coverage

# Set the coverage definition to N Asset Coverage:

from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_DEFINITION_TYPE
two_eyes.set_definition_type(FIGURE_OF_MERIT_DEFINITION_TYPE.N_ASSET_COVERAGE)

# Set the compute field to Maximum:

from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_COMPUTE
two_eyes.definition.set_compute_type(FIGURE_OF_MERIT_COMPUTE.MAXIMUM)

# ### Set the Graphics

# We will set some animation graphics options for the figure of merit object:

from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION
two_eyes.graphics.animation.is_visible = True
two_eyes.graphics.animation.accumulation = FIGURE_OF_MERIT_GRAPHICS_2D_ACCUMULATION.CURRENT_TIME
two_eyes.graphics.animation.fill_points = False
two_eyes.graphics.animation.marker_style = "Star"

# ### Set the Static Graphics

# We will also set some static graphics options:

two_eyes.graphics.static.is_visible = True
two_eyes.graphics.static.fill_points = False
two_eyes.graphics.static.marker_style = "Circle"

# We can view the figure of merit using the 3d graphics window:

plotter3d.show()

# ### Define the Coverage for the Figure of Merit

# We will adjust the definition of the figure of merit's coverage so that we can see which points have coverage from both satellites at the same time.

from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_SATISFACTION_TYPE
two_eyes.definition.satisfaction.enable_satisfaction = True
two_eyes.definition.satisfaction.satisfaction_type = FIGURE_OF_MERIT_SATISFACTION_TYPE.AT_LEAST
two_eyes.definition.satisfaction.satisfaction_threshold = 2

# The 3D Graphics window will immediately reflect the reduction in the amount of the coverage region that satisfies the 'at least 2' criterion.

# ### Set the Animation Graphics

# We will set some animation graphics so that we can see when points are covered by neither, one, or both satellites.

from ansys.stk.core.utilities.colors import Color
from ansys.stk.core.stkobjects import FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD
two_eyes.graphics.static.is_visible = False
two_eyes.graphics.animation.contours.is_visible = True
two_eyes.graphics.animation.contours.color_method = FIGURE_OF_MERIT_GRAPHICS_2D_COLOR_METHOD.EXPLICIT
level1 = two_eyes.graphics.animation.contours.level_attributes.add_level(1)
level1.color = Color.from_rgb(250, 7, 214)
level2 = two_eyes.graphics.animation.contours.level_attributes.add_level(2)
level2.color = Color.from_rgb(45, 250, 195)

# ### Animate the Scenario

root.rewind()

plotter3d.camera.position = [-10290, 33525, 780]
plotter3d.show()

root.play_forward()

# Note that points are highlighted in pink when they are covered by only one satellite, and in blue when covered by both satellites.

# ### Create a Satisfied by Time Report

# The Satisfied by Time report summarizes the percentage and true area of the grid that satisfies the Figure Of Merit at each time step.

satisfied_by_time_result = two_eyes.data_providers.item("Satisfied by Time").exec(scenario.start_time, scenario.stop_time, 60.0)
satisfied_by_time_result.data_sets.to_pandas_dataframe()
