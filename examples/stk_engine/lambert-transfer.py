# # Lambert transfer
#
# This example provides a practical example of how to use PySTK to solve for a Lambert transfer problem. A direct transfer arc between the Earth and Mars is solved by using the [Lamber Profile](https://help.agi.com/stk/index.htm#gator/ab-lambertprofile.htm) in astrogator.


# ### What is a Lamber transfer?
#
# The two-body boundary value problem in the framework of orbital mechanics and astrodynamics is known as the Lambert’s problem. Solutions to this problem find the orbit which connects two known position vectors over a finite time of flight.
#
# Lambert’s problem states to find for the Keplerian orbit which connects two known position vectors, $\vec{r_{1}}$ 1 and $\vec{r_{2}}$, over a finite amount of time, $\Delta t$, under a gravity field of gravitational parameter $\mu$. This problem is usually named the direct-arc transfer problem and it was posed by Johann Heinrich Lambert in a letter to Leonhard Euler.
#
# The direct transfer problem is the most common one when addressing the Lambert’s problem. However, it is also possible to specify the number of revolutions of
# the orbiting body before reaching the final position vector. This type of problem is known as the multi-revolution problem.
#
# It is important to say that perturbations are not considered in this noteboo. Only the Keplerian Lambert’s problem is studied. Despite this, STK is capable of using different force models during the propagation of the orbit, allowing for solving the so-called perturbed Lambert's problem.

# ## Proposed problem
#
# The objective is to determine the transfer orbit from Earth to Mars, commencing on August 1, 2005, and reaching its destination by March 1, 2006. A Sun point mass force model is assumed for the transfer, ignoring the gravity influence of the Earth and Mars. Despite visualizing the planets with a finite volume, these objects are assumed to be points during the whole analysis.

# ## Launch a new STK instance
#
# Start by launching a new STK instance. In this example, STKEngine is used in noGraphics mode. This means that the graphic user interface (GUI) of the product is not launched:

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(noGraphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario
#
# Next, create a new scenario. The central body for this scenario must be the Sun.

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE


root = stk.new_object_root()
scenario = root.children.new_on_central_body(STK_OBJECT_TYPE.SCENARIO, "LambertTransfer", "Sun")
# -

# Set the time period for the scenario:

START_TIME, STOP_TIME = "1 Aug 2005", "1 Mar 2006"
scenario.set_time_period(START_TIME, STOP_TIME)

# Rewind the scenario to the start time:

root.rewind()

# Once created, you can visualize the scenario in a 3D graphics window. Update the value of the far plane of the camera to ensure that distant objects are represented in the scene.

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.camera.far_plane = 1E12
plotter.show()
# -

# ## Add the planets to the scenario
#
# Once the scenario is created, planets can be added. The default ephemerides are used for modeling the orbit of the Earth and Mars. However, it is possible to use other sources for the ephemerides, as provided by the [EPHEM_SOURCE_TYPE](https://stk.docs.pyansys.com/version/dev/api/ansys/stk/core/stkobjects/index.html#ansys.stk.core.stkobjects.EPHEM_SOURCE_TYPE) enumeration. Finally, a royal blue color is used for representing the Earth while a salmon color is used for Mars.

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE, PLANET_POSITION_SOURCE_TYPE, EPHEM_SOURCE_TYPE
from ansys.stk.core.utilities.colors import Colors


planet_names_and_colors = {
    "Earth": Colors.RoyalBlue,
    "Mars": Colors.Salmon,
}

for planet_name, color in planet_names_and_colors.items():
    planet = scenario.children.new_on_central_body(STK_OBJECT_TYPE.PLANET, planet_name, "Sun")
    planet.common_tasks.set_position_source_central_body(planet_name, EPHEM_SOURCE_TYPE.DEFAULT)
    planet.graphics.color = color
# -

# Retrieve the instances created for each planet. These will be used later for finding the start and final state vectors at the desired epoch.

earth, mars = [scenario.children[object_name] for object_name in planet_names_and_colors]

# Next, the scenario graphics are updated to ensure a nice visualization of the planets.

# +
# General graphics configuration
scenario.graphics.labels_visible = True

# Vehicle specific graphics
scenario.graphics.orbits_visible = True

# Planet specific graphics
scenario.graphics.planet_orbits_visible = True
scenario.graphics.inertial_position_labels_visible = True
scenario.graphics.inertial_position_visible = True
scenario.graphics.sub_planet_points_visible = False
scenario.graphics.sub_planet_labels_visible = False
# -

# Finally, the camera position is updated to provite a better overview of the scene with the planets orbiting the Sun.

plotter.camera.position = [402322147.89965045, -554001077.0502352, 31332205.857333962]
plotter.show()


# ## Solve the initial and final state vectors
#
# The initial and final state vectors are required to solve for the transfer orbit. These state vectors can be computed using the [data providers](https://help.agi.com/stk/Subsystems/dataProviders/dataProviders.htm#html/dataProviders/Data_Provider_Summary.htm).

# First, a utility function for converting a [DataProviderResult](https://stk.docs.pyansys.com/version/dev/api/ansys/stk/core/stkobjects/index.html#ansys.stk.core.stkobjects.DataProviderResult) instance into a Python dictionary is implemented. This allows to easily structure and manipulate the computed values.

def from_data_result_to_dict(data_result: "DataProviderResult") -> dict:
    """Convert a data provider result to a dictionary.

    Parameters
    ----------
    data_result : DataProviderResult
        Data result instance to be converted.

    Returns
    -------
    dict
        Dictionary representing the elements and values of the data provider.

    """
    return {
        key: data_result.data_sets.item(key_id).get_values() 
        for key_id, key in enumerate(data_result.data_sets.element_names)
    }


# Next, a second utility function is declared. Its goal is to ease the retrieval of the state vector (position and velocity) for an object in the scenario at a given epoch and in the desired reference frame.

def get_object_pos_vel_at_epoch(stk_object: "StkObject", epoch: str, frame_name: str) -> tuple:
    """Compute the position and velocity vectors of an object in the desired reference frame.

    Parameters
    ----------
    stk_object : StkObject
        Name of the object.
    epoch : str
        Epoch in the form of a string.
    frame_name : str
        Reference frame name.

    Returns
    -------
    tuple(list[float, float, float], list[float, float, float])
        Tuple containing the position and velocity vectors as a list.

    """
    state = {"Position": None, "Velocity": None}
    for path in state:
        data_provider = stk_object.data_providers.get_data_provider_time_varying_from_path(f"Cartesian {path}/{frame_name}")
        data = from_data_result_to_dict(data_provider.exec_single_elements(epoch, ["x", "y", "z"]))
        state[path] = [coord[0] for coord in data.values()]
    return tuple(state.values())


# Now, it is possible to solve for the initial state:

# +
initial_position, initial_velocity = get_object_pos_vel_at_epoch(earth, START_TIME, "ICRF")

print(f"Initial position: {initial_position} km")
print(f"Initial velocity: {initial_velocity} km/s\n")
# -

# And the final state:

# +
final_position, final_velocity = get_object_pos_vel_at_epoch(mars, STOP_TIME, "ICRF")

print(f"Final position: {initial_position} km")
print(f"Final velocity: {initial_velocity} km/s")
# -

# ## Add a satellite to the scenario
#
# Once the initial and final states are known, it is time to add a new satellite to the scenario. This object is used to simulate the transfer orbit between Earth and Mars at the desired launch and arrival dates.
#
# The central body for the satellite must be the Sun to be compliant with the Kepelrian assumption of the Lambert transfer. Remember that the gravity for Earth and Mars are ignored in this example.

satellite = root.current_scenario.children.new_on_central_body(STK_OBJECT_TYPE.SATELLITE, "Satellite", "Sun")

# Then, indicate the type of propagator used for the satellite. In this case, the propagator must be astrogator.

# +
from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE


satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
# -

# Remove all the main sequence to ensure no prior segments lead to wrong results during the simulation.

satellite.propagator.main_sequence.remove_all()

# ## Declare the initial state of the satellite
#
# Now, declare the initial state of the satellite by using an initial state segment.

# +
from ansys.stk.core.stkobjects.astrogator import ELEMENT_TYPE, SEGMENT_TYPE


initial_state = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "Initial State", "-")
# -

# Use an inertial reference frame when declaring the initial state. Also, ensure that the epoch matches the launch date.

initial_state.coord_system_name = "CentralBody/Sun Inertial"
initial_state.orbit_epoch = START_TIME

#  The value of the initial state must match the initial state of the Earth. Cartesian elements are used in this case.

# +
initial_state.set_element_type(ELEMENT_TYPE.CARTESIAN)

initial_state.element.x = initial_position[0]
initial_state.element.y = initial_position[1]
initial_state.element.z = initial_position[2]

initial_state.element.vx = initial_velocity[0]
initial_state.element.vy = initial_velocity[1]
initial_state.element.vz = initial_velocity[2]
# -

# ## Construct the transfer sequence
#
# The transfer sequence can be modeled as a target sequence containing three segments: a first impulsive maneuver, a propagation, and a last impulsive maneuver.

# +
from ansys.stk.core.stkobjects.astrogator import TARGET_SEQ_ACTION, MANEUVER_TYPE


lambert_transfer = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Lambert Transfer", "-")

first_impulse = lambert_transfer.segments.insert(SEGMENT_TYPE.MANEUVER, "First Impulse", "-")
propagate = lambert_transfer.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
last_impulse = lambert_transfer.segments.insert(SEGMENT_TYPE.MANEUVER, "Last Impulse", "-")
# -

# Next, configure the maneuvers to be impulsive and ensure the propagation models the Sun as a point mass.

first_impulse.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
propagate.propagator_name = "Sun Point Mass"
last_impulse.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
# Then, remove any previous profiles that could be present in the target sequence:

lambert_transfer.profiles.remove_all()

# Finally, it is possible to visualize the layout for the main sequence by running:

for control_sequence in satellite.propagator.main_sequence:
    try:
        print(f"{control_sequence.name}")
        for segment in control_sequence.segments:
            print(f"    {segment.name}")
    except:
        continue

# ## Configure the lambert profile

# +
from ansys.stk.core.stkobjects.astrogator import LAMBERT_TARGET_COORD_TYPE, LAMBERT_SOLUTION_OPTION_TYPE, LAMBERT_DIRECTION_OF_MOTION_TYPE, PROFILE_MODE


lambert = lambert_transfer.profiles.add("Lambert Profile")

lambert.coord_system_name = "CentralBody/Sun Inertial"
lambert.set_target_coord_type(LAMBERT_TARGET_COORD_TYPE.CARTESIAN)

lambert.enable_second_maneuver = True
lambert.target_position_x = rf_vec[0] * 1000
lambert.target_position_y = rf_vec[1] * 1000
lambert.target_position_z = rf_vec[2] * 1000
lambert.target_velocity_x = vf_vec[0] * 1000
lambert.target_velocity_y = vf_vec[1] * 1000
lambert.target_velocity_z = vf_vec[2] * 1000

lambert.solution_option = LAMBERT_SOLUTION_OPTION_TYPE.FIXED_TIME
lambert.time_of_flight = 212 * 24 * 3600 # day * (hour / day) * (seconds / hour)
lambert.revolutions = 0
lambert.direction_of_motion = LAMBERT_DIRECTION_OF_MOTION_TYPE.SHORT
lambert.central_body_collision_altitude_padding = 200

lambert.enable_write_to_first_maneuver = True
lambert.first_maneuver_segment = first_impulse.name

lambert.enable_write_duration_to_propagate = True
lambert.disable_non_lambert_propagate_stop_conditions = True
lambert.propagate_segment = propagate.name

lambert.enable_write_to_second_maneuver = True
lambert.second_maneuver_segment = last_impulse.name

lambert.mode = PROFILE_MODE.ACTIVE
# -

# ## Show the MCS layout



# ## Run the MCS and apply all profiles

# +
from ansys.stk.core.stkobjects.astrogator import PROFILES_FINISH

# The following profile is inactive but even with this attribute it can not be removed
# propagate.stopping_conditions.remove("Duration")

lambert_transfer.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
lambert_transfer.when_profiles_finish = PROFILES_FINISH.RUN_TO_RETURN_AND_CONTINUE

lambert_transfer.continue_on_failure = False
lambert_transfer.reset_inner_targeters = False

lambert.mode = PROFILE_MODE.ACTIVE
satellite.propagator.run_mission_control_sequence()
satellite.propagator.apply_all_profile_changes()
#lambert_transfer.apply_profiles()
# -

# ## Results

print(f"First impulse: {[coord / 1000 for coord in first_impulse.maneuver.attitude_control.query_cartesian()]} km/s")
print(f"Last impulse:  {[coord / 1000 for coord in last_impulse.maneuver.attitude_control.query_cartesian()]} km/s")

# ## Draw the transfer trajectory

satellite.propagator.options.draw_trajectory_in_3d = True
satellite.graphics_3d.model.detail_threshold.all = 1E12

plotter.show()
