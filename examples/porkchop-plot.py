# # Porkchop plots
#



# # Launch STK

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# ## Scenario

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE


root = stk.new_object_root()
scenario = root.children.new_on_central_body(STK_OBJECT_TYPE.SCENARIO, "PorkchopPlotter", "Sun")


# -

# # Utilities

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


# +
from datetime import datetime

def get_object_pos_vel_at_epoch(stk_object: "StkObject", epoch: datetime, frame_name: str) -> tuple:
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
    epoch = epoch.strftime("%d %B %Y")
    state = {"Position": None, "Velocity": None}
    for path in state:
        data_provider = stk_object.data_providers.get_data_provider_time_varying_from_path(f"Cartesian {path}/{frame_name}")
        data = from_data_result_to_dict(data_provider.execute_single_elements(epoch, ["x", "y", "z"]))
        state[path] = [coord[0] for coord in data.values()]
    return tuple(state.values())


# -

def get_transfer_angle(r1, r2, prograde):
    """
    Solves for the transfer angle being known the sense of rotation.

    Parameters
    ----------
    r1: np.array
        Initial position vector.
    r2: np.array
        Final position vector.
    prograde: bool
        If True, it assumes prograde motion, otherwise assumes retrograde.

    Returns
    -------
    dtheta: float
        Transfer angle in radians.

    """

    # Check if both position vectors are collinear. If so, check if the transfer
    # angle is 0 or pi.
    if np.all(np.cross(r1, r2) == 0):
        return 0 if np.all(np.sign(r1) == np.sign(r2)) else np.pi

    # Solve for a unitary vector normal to the vector plane. Its direction and
    # sense the one given by the cross product (right-hand) from r1 to r2.
    h = cross(r1, r2) / norm(np.cross(r1, r2))

    # Compute the projection of the normal vector onto the reference plane.
    alpha = dot(np.array([0, 0, 1]), h)

    # Get the minimum angle (0 <= dtheta <= pi) between r1 and r2.
    r1_norm, r2_norm = [norm(vec) for vec in [r1, r2]]
    theta0 = np.arccos(dot(r1, r2) / (r1_norm * r2_norm))

    # Fix the value of theta if necessary
    if prograde is True:
        dtheta = theta0 if alpha > 0 else 2 * np.pi - theta0
    else:
        dtheta = theta0 if alpha < 0 else 2 * np.pi - theta0

    return dtheta


# +
from datetime import datetime, timedelta

import numpy as np

from ansys.stk.core.stkobjects import PROPAGATOR_TYPE
from ansys.stk.core.stkobjects.astrogator import LAMBERT_SOLUTION_OPTION_TYPE, LAMBERT_DIRECTION_OF_MOTION_TYPE, ELEMENT_TYPE, SEGMENT_TYPE, TARGET_SEQUENCE_ACTION, MANEUVER_TYPE, LAMBERT_TARGET_COORDINATE_TYPE, PROFILE_MODE, PROFILES_FINISH


def lambert_solver(
    satellie: "Satellite",
    departure_body: "Planet",
    arrival_body: "Planet",
    departure_date: datetime,
    arrival_date: datetime,
    prograde: bool,
):
    # Compute the time of flight
    time_of_flight = (arrival_date - departure_date).total_seconds()
    if time_of_flight <= 0:
        return None, None
    lambert.time_of_flight = time_of_flight

    # Compute the departure and arrival state vectors
    departure_position, departure_velocity = get_object_pos_vel_at_epoch(departure_body, departure_date, "ICRF")
    arrival_position, arrival_velocity = get_object_pos_vel_at_epoch(arrival_body, arrival_date, "ICRF")

    r1_cross_r2 = np.cross(departure_position, arrival_position)
    r1_times_r2 = np.linalg.norm(departure_position) * np.linalg.norm(arrival_position)
    h0_z = (r1_cross_r2 / r1_times_r2)[-1]

    if prograde is True:
        path = LAMBERT_DIRECTION_OF_MOTION_TYPE.LONG if h0_z < 0 else LAMBERT_DIRECTION_OF_MOTION_TYPE.SHORT
    else:
        path = LAMBERT_DIRECTION_OF_MOTION_TYPE.SHORT if h0_z < 0 else LAMBERT_DIRECTION_OF_MOTION_TYPE.LONG
    lambert.direction_of_motion = path

    #print(f"Departure position {departure_position}")
    #print(f"Departure velocity {departure_velocity}")
    #print(f"Arrival position {arrival_position}")
    #print(f"Arrival velocity {arrival_velocity}")

    # Update the initial state of the satellite
    initial_state.orbit_epoch = departure_date.strftime("%d %B %Y")
    initial_state.element.x = departure_position[0]
    initial_state.element.y = departure_position[1]
    initial_state.element.z = departure_position[2]
    initial_state.element.vx = departure_velocity[0]
    initial_state.element.vy = departure_velocity[1]
    initial_state.element.vz = departure_velocity[2]
    
    # Declare the final state of the satellite
    lambert.target_position_x = arrival_position[0] * 1000
    lambert.target_position_y = arrival_position[1] * 1000
    lambert.target_position_z = arrival_position[2] * 1000
    lambert.target_velocity_x = arrival_velocity[0] * 1000
    lambert.target_velocity_y = arrival_velocity[1] * 1000
    lambert.target_velocity_z = arrival_velocity[2] * 1000

    # Run the mission control sequence
    satellite.propagator.run_mcs()
    satellite.propagator.apply_all_profile_changes()

    # Compute the deltaV
    delta_v1 = first_impulse.maneuver.attitude_control.magnitude / 1000
    delta_v2 = last_impulse.maneuver.attitude_control.magnitude / 1000
    return delta_v1, delta_v2, time_of_flight


# -

# ## Generate the time span

# +
from datetime import datetime, timedelta


def linspace_datetimes(start_date, end_date, num_dates=20):
    start, end = [datetime.strptime(date, "%d %b %Y") for date in [start_date, end_date]]
    delta_seconds = (end - start).total_seconds() / num_dates
    return [start + i * timedelta(seconds=delta_seconds) for i in range(num_dates)]


# -

# ## Add the planets

# +
from ansys.stk.core.stkobjects import PLANET_POSITION_SOURCE_TYPE, EPHEM_SOURCE_TYPE

for name in ["Earth", "Mars"]:
    planet = scenario.children.new_on_central_body(STK_OBJECT_TYPE.PLANET, name, "Sun")
    planet.common_tasks.set_position_source_central_body(name, EPHEM_SOURCE_TYPE.DEFAULT)

earth, mars = [scenario.children[object_name] for object_name in ["Earth", "Mars"]]
# -

# ## Add a satellite

satellite = scenario.children.new_on_central_body(STK_OBJECT_TYPE.SATELLITE, "Satellite", "Sun")
satellite.set_propagator_type(PROPAGATOR_TYPE.ASTROGATOR)
satellite.propagator.main_sequence.remove_all()

# ### Initial state

initial_state = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "Initial State", "-")
initial_state.coord_system_name = "CentralBody/Sun Inertial"
initial_state.set_element_type(ELEMENT_TYPE.CARTESIAN)

# ### Target sequence

# +
# Declare the segments
lambert_transfer = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Lambert Transfer", "-")
first_impulse = lambert_transfer.segments.insert(SEGMENT_TYPE.MANEUVER, "First Impulse", "-")
propagate = lambert_transfer.segments.insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
last_impulse = lambert_transfer.segments.insert(SEGMENT_TYPE.MANEUVER, "Last Impulse", "-")

# Configure the segments of the target sequence
first_impulse.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
propagate.propagator_name = "Sun Point Mass"
last_impulse.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)

# Add the Lambert transfer profile
lambert_transfer.profiles.remove_all()
lambert = lambert_transfer.profiles.add("Lambert Profile")

# Constant configuration for the profile
lambert.coord_system_name = "CentralBody/Sun Inertial"
lambert.set_target_coord_type(LAMBERT_TARGET_COORDINATE_TYPE.CARTESIAN)
lambert.enable_second_maneuver = True

# Additional configuration parameters
lambert.solution_option = LAMBERT_SOLUTION_OPTION_TYPE.FIXED_TIME
lambert.revolutions = 0
# TODO
#lambert.direction_of_motion = LAMBERT_DIRECTION_OF_MOTION_TYPE.SHORT 
lambert.central_body_collision_altitude_padding = 0

# Allow the profile to write the computations to the segments
lambert.enable_write_to_first_maneuver = True
lambert.first_maneuver_segment = first_impulse.name

lambert.enable_write_duration_to_propagate = True
lambert.disable_non_lambert_propagate_stop_conditions = True
lambert.propagate_segment = propagate.name

lambert.enable_write_to_second_maneuver = True
lambert.second_maneuver_segment = last_impulse.name

# Activate the profile
lambert.mode = PROFILE_MODE.ACTIVE

# Additional configuration
lambert_transfer.action = TARGET_SEQUENCE_ACTION.RUN_ACTIVE_PROFILES
lambert_transfer.when_profiles_finish = PROFILES_FINISH.RUN_TO_RETURN_AND_CONTINUE
lambert_transfer.continue_on_failure = False
lambert_transfer.reset_inner_targeters = False

# +
num_dates = 75

launch_span = linspace_datetimes("30 Apr 2005", "7 Oct 2005", num_dates)
arrival_span = linspace_datetimes("16 Nov 2005", "21 Dec 2006", num_dates)

dv_arrival = np.zeros((len(launch_span), len(arrival_span)))
c3_launch = np.zeros((len(launch_span), len(arrival_span)))
tof_values = np.zeros((len(launch_span), len(arrival_span)))

for i, launch_date in enumerate(launch_span):
    for j, arrival_date in enumerate(arrival_span):
        dv_launch, dv_arrival[j, i], tof = lambert_solver(satellite, earth, mars, launch_date, arrival_date, prograde=True)
        c3_launch[j, i] = dv_launch ** 2
        tof_values[j, i] = tof / 3600 / 24  

# +
import matplotlib.pyplot as plt



c3_levels = np.linspace(
    0, 45, 30
)
tof_levels = np.linspace(100, 500, 5)
dv_arrival_levels = np.linspace(0, 5, 5)


fig, ax = plt.subplots(figsize=(15, 15))
ax.set_title(f"Characteristic launch energy $C_{3}$\n{earth.instance_name.capitalize()} - {mars.instance_name.capitalize()}")
ax.set_xlabel("Launch date")
ax.set_ylabel("Arrival date")

# Characteristic energy contour
c3_launch_contourf = ax.contourf(
    launch_span, arrival_span, c3_launch, c3_levels
)
cbar = fig.colorbar(c3_launch_contourf)
cbar.set_label("km2 / s2")

c3_launch_contour = ax.contour(
    launch_span, arrival_span, c3_launch, c3_levels, 
    colors="black", linestyles="solid"
)
ax.clabel(c3_launch_contour, inline=1, fmt="%1.1f", colors="k", fontsize=10)

# Time of flight
tof_contour = ax.contour(
    launch_span, arrival_span, tof_values, tof_levels, 
    colors="red", linestyles="dashed", linewidths=3.5,
)
ax.clabel(
    tof_contour, inline=1, fmt="%1.0f days", colors="r", fontsize=14
)

# Arrival velocity
dv_arrival_contour = ax.contour(
    launch_span, arrival_span, dv_arrival, dv_arrival_levels, 
    colors="navy", linestyles="solid", linewidths=3.5,
)
ax.clabel(
    dv_arrival_contour, inline=1, fmt="%1.0f km/s", colors="navy", fontsize=12
)

plt.show()
