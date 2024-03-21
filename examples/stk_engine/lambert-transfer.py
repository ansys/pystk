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
# The objective is to determine the transfer orbit from Earth to Mars, commencing on August 1, 2005, and reaching its destination by March 1, 2006. A Sun point mass force model is assumed for the transfer, ignoring the gravity influence of the Earth and Mars.

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


# ## Solving for the initial and final state vectors

def from_data_result_to_dict(data_result):
    """Convert an IResult
    return {
        key: data_result.data_sets.item(key_id).get_values() 
        for key_id, key in enumerate(data_result.data_sets.element_names)
    }


def get_object_pos_vel_at_epoch(stk_object: "StkObject", epoch: str, frame_name: str):
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
        data = from_data_result_to_dict(position_provider.exec_single_elements(epoch, ["x", "y", "z"]))
        state[path] = [coord[0] for coord in data.values()]
    return tuple(state.values())


pos, vel = get_object_pos_vel_at_epoch(planet, STOP_TIME, "ICRF")

pos

# +
positions = []
for planet, time in zip(planets, [START_TIME, STOP_TIME]):
    position_provider = planet.data_providers.get_data_provider_time_varying_from_path("Cartesian Position/ICRF")
    position_data = from_data_result_to_dict(position_provider.exec_single_elements(time, ["x", "y", "z"]))
    position = [value[0] for value in position_data.values()]
    positions.append(position)

r0_vec, rf_vec = positions

# +
velocities = []
for planet, time in zip(planets, [START_TIME, STOP_TIME]):
    velocity_provider = planet.data_providers.get_data_provider_time_varying_from_path("Cartesian Velocity/ICRF")
    velocity_data = from_data_result_to_dict(velocity_provider.exec_single_elements(time, ["x", "y", "z"]))
    velocity = [value[0] for value in velocity_data.values()]
    velocities.append(velocity)

v0_vec, vf_vec = velocities
# -

initial_state = []
initial_state.extend(r0_vec)
initial_state.extend(v0_vec)
for coord in initial_state:
    print(coord)

final_state = []
final_state.extend(rf_vec)
final_state.extend(vf_vec)
for coord in final_state:
    print(coord)

# ## Adding a satellite to the scenario
#
# Now that a new scenario is available, add a new satellite:

satellite = root.current_scenario.children.new_on_central_body(STK_OBJECT_TYPE.SATELLITE, "Satellite", "Sun")

# Then, declare the type of propagator used for the satellite:

# +
from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE


satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
satellite.propagator.main_sequence.remove_all()
# -

# Initialize the propagator by making sure that no previous sequence is present. Add any additional configurations for the propagator. For this example, its is requested to draw the maneuver in 3D.

# ## Set up the initial state of the satellite

# An initial state segment is required to specify the initial state of the satellite. To see the list of different segment types, run:

# +
from ansys.stk.core.stkobjects.astrogator import ELEMENT_TYPE, SEGMENT_TYPE

initial_state = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "Initial State", "-")

initial_state.coord_system_name = "CentralBody/Sun Inertial"
initial_state.set_element_type(ELEMENT_TYPE.CARTESIAN)
initial_state.orbit_epoch = START_TIME

initial_state.element.x = r0_vec[0]
initial_state.element.y = r0_vec[1]
initial_state.element.z = r0_vec[2]
initial_state.element.vx = v0_vec[0]
initial_state.element.vy = v0_vec[1]
initial_state.element.vz = v0_vec[2]
# -

print(initial_state.element.x)
print(initial_state.element.y)
print(initial_state.element.z)
print(initial_state.element.vx)
print(initial_state.element.vy)
print(initial_state.element.vz)

# ## Set up the transfer sequence

# +
from ansys.stk.core.stkobjects.astrogator import TARGET_SEQ_ACTION, MANEUVER_TYPE

lambert_transfer = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Lambert Transfer", "-")

# TODO: ensure desired propagator type in each segment
first_impulse = lambert_transfer.segments.insert(SEGMENT_TYPE.MANEUVER, "First Impulse", "-")
propagate = lambert_transfer.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
last_impulse = lambert_transfer.segments.insert(SEGMENT_TYPE.MANEUVER, "Last Impulse", "-")

# Remove any existing profiles
lambert_transfer.profiles.remove_all()

# TODO: removing this does not show the orbit in the plotter
first_impulse.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
propagate.propagator_name = "Sun Point Mass"
last_impulse.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
# -
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

for control_sequence in satellite.propagator.main_sequence:
    try:
        print(f"{control_sequence.name}")
        for segment in control_sequence.segments:
            print(f"    {segment.name}")
    except:
        continue

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
