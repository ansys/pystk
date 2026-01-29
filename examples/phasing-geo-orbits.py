# # GEO Orbit Phasing
#
# This tutorial provides a practical example on how to solve a phasing maneuver problem using Python.
#
# ## What is orbit phasing?
#
# Orbit phasing is an orbital maneuver used to adjust the position of a spacecraft within its orbit without changing the orbit's shape or orientation. This is particularly important for satellites in geostationary orbit (GEO) that need to move along the geostationary belt to a different orbital slot, or for constellation satellites that must maintain specific relative positions within the same orbital plane.
#
# The phasing maneuver involves temporarily changing the orbital period by adjusting the semi-major axis. By placing the satellite into a slightly different orbit (the phasing orbit), it will drift relative to its target position. After a specified number of orbits, the satellite returns to the original orbit at the desired location.
#
# The key parameters for a phasing maneuver are:
# - **Phase angle**: The angular displacement between the chaser and target satellites
# - **Number of phasing orbits**: How many orbits are used to close the phase angle
# - **Phasing orbit**: A temporary orbit with a different period to achieve the desired drift
#
# ## Problem statement
#
# Two geostationary satellites occupy the same orbit but at different angular positions. The target satellite is at a true anomaly of 20 degrees, while the chaser satellite is at 70 degrees. Design a phasing maneuver for the chaser satellite to rendezvous with the target satellite using 5 phasing orbits over a 16-day period.
#
# Both satellites have the following initial orbital parameters:
# - Semi-major axis: 42164 km (GEO altitude)
# - Eccentricity: 0.0001
# - Inclination: 0.0 degrees (equatorial)
# - RAAN: 0.0 degrees
#
# Compute the required $\Delta v$ for the phasing maneuvers and determine the phasing orbit parameters.

# ## Launch a new STK instance
#
# Start by launching a new STK instance. In this example, ``STKEngine`` is used with graphics (``no_graphics`` mode set to ``False``). This means that the graphic user interface (GUI) of the product is not launched but 2D and 3D visualization is still available through the STK Engine controls:

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario
#
# Start by creating a new scenario in STK:

# +
from ansys.stk.core.stkobjects import PropagatorType, STKObjectType


root = stk.new_object_root()
root.new_scenario("Phasing_orbit")
scen = root.current_scenario

# -

# ## Configure the target satellite
#
# Create the target satellite which will remain at a fixed position in geostationary orbit. This satellite serves as the reference point for the phasing maneuver:

from ansys.stk.core.stkobjects.astrogator import ElementSetType
from ansys.stk.core.utilities.colors import Colors


target_satellite = scen.children.new(STKObjectType.SATELLITE, "Target")
target_satellite.set_propagator_type(PropagatorType.ASTROGATOR)
target_propagator = target_satellite.propagator
target_propagator.options.draw_trajectory_in_3d = False
target_initial_state = target_propagator.main_sequence["Initial State"]
target_initial_state.set_element_type(ElementSetType.KEPLERIAN)
target_initial_state.initial_state.epoch = scen.start_time
target_propagate_segment = target_propagator.main_sequence["Propagate"]
target_propagate_segment.propagator_name = "Earth point mass"
target_propagate_segment.properties.color = Colors.Red
target_keplerian_elements = target_initial_state.element

# ## Configure the chaser satellite
#
# Create the chaser satellite which will perform the phasing maneuver to rendezvous with the target:

chaser_satellite = scen.children.new(STKObjectType.SATELLITE, "Chaser")
chaser_satellite.set_propagator_type(PropagatorType.ASTROGATOR)
chaser_propagator = chaser_satellite.propagator
chaser_propagator.options.draw_trajectory_in_3d = False
chaser_initial_state = chaser_propagator.main_sequence["Initial State"]
chaser_initial_state.set_element_type(ElementSetType.KEPLERIAN)
chaser_initial_state.initial_state.epoch = scen.start_time
chaser_propagate_segment = chaser_propagator.main_sequence["Propagate"]
chaser_propagate_segment.propagator_name = "Earth point mass"
chaser_propagate_segment.stopping_conditions.add("Periapsis")
chaser_propagate_segment.stopping_conditions.remove("Duration")
chaser_keplerian_elements = chaser_initial_state.element

# ## Define the input parameters
#
# The cell below defines the input parameters for the phasing maneuver analysis:

import math


# Input parameters for phasing maneuver
chaser_true_anomaly = 70  # deg - chaser true anomaly (between 0 and 360)
target_true_anomaly = 20  # deg - target true anomaly (between 0 and 360)
number_of_phasing_orbits = 5  # number of phasing orbits
propagation_time = 16  # days - total propagation time

# Fixed Keplerian parameters (geostationary orbit)
semi_major_axis = 42164  # km
eccentricity = 0.0001
inclination = 0.0
right_ascension_ascending_node = 0.0

# ## Configure initial orbital states
#
# Set the initial orbital elements for both satellites and run an initial propagation:

# Change the scenario duration
scen.stop_time = "+" + str(propagation_time) + " day"

# Set the chaser initial state
chaser_keplerian_elements.semimajor_axis = semi_major_axis
chaser_keplerian_elements.eccentricity = eccentricity
chaser_keplerian_elements.inclination = inclination
chaser_keplerian_elements.raan = right_ascension_ascending_node
chaser_keplerian_elements.true_anomaly = chaser_true_anomaly
chaser_keplerian_elements.arg_of_periapsis = 0.0

# Set the target initial state
target_keplerian_elements.semimajor_axis = semi_major_axis
target_keplerian_elements.eccentricity = eccentricity
target_keplerian_elements.inclination = inclination
target_keplerian_elements.raan = right_ascension_ascending_node
target_keplerian_elements.true_anomaly = target_true_anomaly
target_keplerian_elements.arg_of_periapsis = 0.0

# Configure target propagation duration
target_propagate_segment.stopping_conditions["Duration"].properties.trip = (
    propagation_time * 86400
)

# Run initial propagation for both satellites
chaser_propagator.run_mcs()
target_propagator.run_mcs()

# ## Calculate phasing orbit parameters
#
# The **phase angle** is the angular displacement between the two satellites at initial time. To achieve rendezvous, this angle must be reduced to 0 over a specified number of phasing orbits.
#
# The angular gap per orbit is:
# $$ \theta_{gap}=\frac{\theta}{n_{orbits}}$$
#
# where $\theta$ is the phase angle, and $\theta_{gap}$ is the angular displacement to recover after each phasing orbit.
#
# Using **Kepler's equation**, we calculate the period and semi-major axis of the phasing orbit. First, the **eccentric anomaly E** is calculated from $\theta_{gap}$:
#
# $$\tan\frac{E}{2} = \sqrt{\frac{1 - e}{1 + e}}\tan\frac{\theta_{gap}}{2}$$
#
# Then the period of the phasing orbit is derived:
#
# $$ T_{phasing}=\frac{T_{chaser}}{2\pi}\left ( E-e \sin E \right )$$

# Get the mean period and SMA of the initial orbit
mean_keplerian_data_provider = chaser_satellite.data_providers[
    "Kozai-Izsak Mean"
].group["ICRF"]
mean_keplerian_result = mean_keplerian_data_provider.execute(
    scen.start_time, scen.start_time, 60
)
mean_keplerian_dataframe = mean_keplerian_result.data_sets.to_pandas_dataframe()
mean_orbital_period = float(mean_keplerian_dataframe.at[0, "mean nodal period"])
mean_semi_major_axis = float(mean_keplerian_dataframe.at[0, "mean semi-major axis"])

# Calculate the phase angle
phase_angle = math.radians(target_true_anomaly - chaser_true_anomaly)

if phase_angle < 0:
    phase_angle = 2 * math.pi + phase_angle

print("#################### Initial geometry #####################")
print("Phase angle      = " + str(math.degrees(phase_angle)) + " deg")
print("")

# Recalculate the phase angle accordingly with the number of phasing orbits
phase_angle = phase_angle / number_of_phasing_orbits

# Calculate the eccentric anomaly
eccentric_anomaly = 2 * math.atan(
    math.sqrt((1 - eccentricity) / (1 + eccentricity)) * math.tan(phase_angle / 2)
)

# Calculate the time elapsed to cover phase angle in original orbit (Kepler's equation)
time_to_cover_phase_angle = (mean_orbital_period / (2 * math.pi)) * (
    eccentric_anomaly - eccentricity * math.sin(eccentric_anomaly)
)

# Calculate the period of the phasing orbit
phasing_orbit_period = mean_orbital_period - time_to_cover_phase_angle

# Calculate the SMA of the phasing orbit
earth_gravitational_parameter = 398600.44
transfer_semi_major_axis = math.pow(
    (phasing_orbit_period * math.sqrt(earth_gravitational_parameter)) / (2 * math.pi),
    2 / 3,
)

# Calculate eccentricity and radii
keplerian_elements_data_provider = chaser_satellite.data_providers[
    "Astrogator Values"
].group["Keplerian Elems"]
keplerian_result = keplerian_elements_data_provider.execute(
    scen.start_time, scen.start_time, 60
)
keplerian_dataframe = keplerian_result.data_sets.to_pandas_dataframe()
initial_radius = float(keplerian_dataframe.at[0, "radius_of_periapsis"])

if transfer_semi_major_axis > semi_major_axis:
    periapsis_radius = initial_radius
    apoapsis_radius = 2 * transfer_semi_major_axis - periapsis_radius
else:
    apoapsis_radius = initial_radius
    periapsis_radius = 2 * transfer_semi_major_axis - apoapsis_radius

# Estimate the needed Delta V for phasing
velocity_periapsis_initial = math.sqrt(
    earth_gravitational_parameter * ((2 / initial_radius) - (1 / mean_semi_major_axis))
)
velocity_periapsis_final = math.sqrt(
    earth_gravitational_parameter
    * ((2 / initial_radius) - (1 / transfer_semi_major_axis))
)
delta_v_estimate = velocity_periapsis_final - velocity_periapsis_initial

# ## Set up the phasing maneuver sequence
#
# Add a target sequence to perform the first delta-V maneuver and propagate through the phasing orbits:

from ansys.stk.core.stkobjects.astrogator import (
    AttitudeControl,
    ControlManeuver,
    ManeuverType,
    ProfileMode,
    SegmentType,
    TargetSequenceAction,
)


# Add the first Target Sequence segment
phasing_start_sequence = chaser_propagator.main_sequence.insert(
    SegmentType.TARGET_SEQUENCE, "Start Phasing", "-"
)
phasing_start_sequence.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

# Add a Maneuver segment
first_delta_v_maneuver = phasing_start_sequence.segments.insert(
    SegmentType.MANEUVER, "DV1", "-"
)
first_delta_v_maneuver.set_maneuver_type(ManeuverType.IMPULSIVE)
first_delta_v_maneuver.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)

# Maneuver attitude definition
first_delta_v_maneuver.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
thrust_vector = first_delta_v_maneuver.maneuver.attitude_control
thrust_vector.thrust_axes_name = "Satellite/Chaser VNC(Earth)"
thrust_vector.x = delta_v_estimate * 1000

# Add a Propagate segment
phasing_orbit_propagate = phasing_start_sequence.segments.insert(
    SegmentType.PROPAGATE, "Phasing Orbit", "-"
)
phasing_orbit_propagate.properties.color = Colors.Orange
phasing_orbit_propagate.propagator_name = "Earth point mass"
if transfer_semi_major_axis > semi_major_axis:
    phasing_orbit_propagate.stopping_conditions.add("Periapsis")
else:
    phasing_orbit_propagate.stopping_conditions.add("Apoapsis")
phasing_orbit_propagate.stopping_conditions.remove("Duration")
phasing_orbit_propagate.stopping_conditions.item(
    0
).properties.repeat_count = number_of_phasing_orbits
phasing_orbit_propagate.results.add("Vector/Angle Between Vectors")
phasing_orbit_propagate.results[0].vector1_name = "Satellite/Chaser Position"
phasing_orbit_propagate.results[0].vector2_name = "Satellite/Target Position"

# ## Configure the differential corrector for phasing
#
# Set up the differential corrector to adjust the first delta-V to achieve zero phase angle at the end of the phasing orbits:

# Customize the Differential Corrector
phasing_differential_corrector = phasing_start_sequence.profiles[
    "Differential Corrector"
]
phasing_differential_corrector.mode = ProfileMode.ITERATE
phasing_differential_corrector.max_iterations = 50

# Set Control Parameters and Results
phasing_x_control_parameter = (
    phasing_differential_corrector.control_parameters.get_control_by_paths(
        "DV1", "ImpulsiveMnvr.Cartesian.X"
    )
)
phasing_x_control_parameter.enable = True
phasing_x_control_parameter.max_step = 0.001

phasing_angle_result = phasing_differential_corrector.results.get_result_by_paths(
    "Phasing Orbit", "Angle_Between_Vectors"
)
phasing_angle_result.enable = True
phasing_angle_result.desired_value = 0.0
phasing_angle_result.tolerance = 0.1

# ## Set up the circularization maneuver
#
# Add a second target sequence to perform the circularization delta-V to return to the original circular orbit:

# Add the second Target Sequence segment
circularization_sequence = chaser_propagator.main_sequence.insert(
    SegmentType.TARGET_SEQUENCE, "Circularization", "-"
)
circularization_sequence.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

# Add a Maneuver segment
second_delta_v_maneuver = circularization_sequence.segments.insert(
    SegmentType.MANEUVER, "DV2", "-"
)
second_delta_v_maneuver.set_maneuver_type(ManeuverType.IMPULSIVE)
second_delta_v_maneuver.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)

# Add a Propagate segment
final_orbit_propagate = circularization_sequence.segments.insert(
    SegmentType.PROPAGATE, "Final Orbit", "-"
)
final_orbit_propagate.properties.color = Colors.Yellow
final_orbit_propagate.propagator_name = "Earth point mass"
final_orbit_propagate.stopping_conditions["Duration"].properties.trip = 86400
final_orbit_propagate.results.add("Keplerian Elems/Eccentricity")

# ## Configure the differential corrector for circularization
#
# Set up the differential corrector to achieve a circular orbit with the desired eccentricity:

# Customize the Differential Corrector
circularization_differential_corrector = circularization_sequence.profiles[
    "Differential Corrector"
]
circularization_differential_corrector.mode = ProfileMode.ITERATE
circularization_differential_corrector.max_iterations = 50

# Set Control Parameters and Results
circularization_x_control_parameter = (
    circularization_differential_corrector.control_parameters.get_control_by_paths(
        "DV2", "ImpulsiveMnvr.Cartesian.X"
    )
)
circularization_x_control_parameter.enable = True
circularization_x_control_parameter.max_step = 0.01

circularization_eccentricity_result = (
    circularization_differential_corrector.results.get_result_by_paths(
        "Final Orbit", "Eccentricity"
    )
)
circularization_eccentricity_result.enable = True
circularization_eccentricity_result.desired_value = 0.0001
circularization_eccentricity_result.tolerance = 0.00001

# ## Run the main control sequence
#
# Execute the mission control sequence to solve for the phasing maneuver:

chaser_propagator.run_mcs()
target_propagator.run_mcs()
root.rewind()

# ## Retrieve the results
#
# Once the analysis has been performed, retrieve the delta-V values and phasing orbit parameters:

# Get the maneuver data providers
maneuver_data_provider = chaser_satellite.data_providers["Maneuver Summary"]
maneuver_result = maneuver_data_provider.execute(scen.start_time, scen.stop_time)
maneuver_dataframe = maneuver_result.data_sets.to_pandas_dataframe()
delta_v_actual = maneuver_dataframe.at[0, "delta v"]

print("################### Transfer orbit data ###################")
print("N phasing orbits = " + str(number_of_phasing_orbits))
print("Period           = " + str(phasing_orbit_period) + " sec")
print("SMA              = " + str(transfer_semi_major_axis) + " km")
print("Perigee radius   = " + str(periapsis_radius) + " km")
print("Apogee radius    = " + str(apoapsis_radius) + " km")
print("Delta V          = " + str(delta_v_actual) + " m/sec")
print(
    "Transfer time    = "
    + str(phasing_orbit_period * number_of_phasing_orbits / 86400)
    + " days"
)
