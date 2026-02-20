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
#
# The **phase angle** is the angular displacement between the two satellites at initial time. In this context, it is defined as always positive and between 0 and 360 degrees. To make the rendezvous between the satellites, it has to be reduced to 0 in a specified number of orbits (called **phasing orbits**), so each phase orbit will reduce the angular gap by just a fraction of the overall value.
#
# $$ \theta_{gap}=\frac{\theta}{n_{orbits}}$$
#
# , where $\theta$ is the phase angle, and $\theta_{gap}$ is the angular dispacement to recover after each phasing orbit.
#
# In the code below the **Kepler's equation** is used to calculate the period and semimajor axis of the phasing orbit, given the number of revolution around the phasing orbit itself. As first, the **eccentric anomaly E** is calculated from $\theta_{gap}$ :
#
# $$\tan\left(\frac{E}{2}\right)=\sqrt{\frac{1 - e}{1 + e}}\tan\left(\frac{\theta_{gap}}{2}\right)$$
#
# ...and then the period of the phasing orbit is derived:
#
# $$T_{phasing}=\frac{T_{chaser}}{2\pi}\left ( E-e \sin E \right )$$
#
# ## Problem statement
#
# Two geostationary satellites occupy the same orbit but at different angular positions. The target satellite is at a true anomaly of 20 degrees, while the chaser satellite is at 70 degrees. Design a phasing maneuver for the chaser satellite to rendezvous with the target satellite using 5 phasing orbits over a 16-day period.
#
# Both satellites have the following initial orbital parameters:
#
# - Semi-major axis: 42164 km (GEO altitude)
# - Eccentricity: 0.0001
# - Inclination: 0.0 degrees (equatorial)
# - RAAN: 0.0 degrees
# - Argument of periapsis: 0.0 degrees
#
# Compute the required $\Delta v$ for the phasing maneuvers and determine the phasing orbit parameters.

# +
semimajor_axis = 42164.0
eccentricity = 0.0001
inclination = 0.0
raan = 0.0
arg_of_periapsis = 0.0

true_anomaly_target = 20.0
true_anomaly_chaser = 70.0

propagation_time = 16 * 86400
phasing_orbits = 5
# -

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
scenario = root.current_scenario
# -

# Configure the scenario time:

start_time, stop_time = "today", "+16 day"
scenario.set_time_period(start_time, stop_time)

# Once created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Set up the target satellite
#
# Create the target satellite which will remain at a fixed position in geostationary orbit. This satellite serves as the reference point for the phasing maneuver:

target_satellite = scenario.children.new(STKObjectType.SATELLITE, "Target")

# Then, declare the type of orbit propagator used for the satellite. Ensure a clean main sequence:

target_satellite.set_propagator_type(PropagatorType.ASTROGATOR)
target_satellite.propagator.main_sequence.remove_all()

# Configure graphics settings:

target_satellite.propagator.options.draw_trajectory_in_3d = True

# ## Set up the initial state of the target satellite
#
# Access the existing initial state segment in the main sequence and configure the element type:

# +
from ansys.stk.core.stkobjects.astrogator import ElementSetType, SegmentType


target_initial_state = target_satellite.propagator.main_sequence.insert(
    SegmentType.INITIAL_STATE, "Initial State", "-"
)
target_initial_state.set_element_type(ElementSetType.KEPLERIAN)
target_initial_state.initial_state.epoch = scenario.start_time
# -

# Delcare the Keplerian elements for the initial state:

# +
target_keplerian_elements = target_initial_state.element

target_keplerian_elements.semimajor_axis = semimajor_axis
target_keplerian_elements.eccentricity = eccentricity
target_keplerian_elements.inclination = inclination
target_keplerian_elements.raan = raan
target_keplerian_elements.true_anomaly = true_anomaly_target
target_keplerian_elements.arg_of_periapsis = arg_of_periapsis
# -

# Configure the propagation segment. Propagate the orbit of the target for 16 days:

# +
from ansys.stk.core.utilities.colors import Colors

target_propagate_segment = target_satellite.propagator.main_sequence.insert(
    SegmentType.PROPAGATE, "Propagate", "-"
)
target_propagate_segment.propagator_name = "Earth point mass"

target_propagate_segment.stopping_conditions["Duration"].properties.trip = (
     propagation_time
)
# -

# Red color is used to identify the target satellite:

target_propagate_segment.properties.color = Colors.Red

# Propagate the target satellite and show it:

# +
from ansys.stk.core.stkobjects.astrogator import RunCode


run_code = target_satellite.propagator.run_mcs2()
if run_code != RunCode.MARCHING:
    raise ValueError("Could not propagate target satellite orbit.")
# -

# Finally, show the orbit of the satellite:

plotter.show()

# ## Setup the chaser satellite
#
# Create the chaser satellite which will get closer to the target satellite:

chaser_satellite = scenario.children.new(STKObjectType.SATELLITE, "Chaser")

# Then, declare the type of orbit propagator used for the satellite. Ensure a clean main sequence:

chaser_satellite.set_propagator_type(PropagatorType.ASTROGATOR)
chaser_satellite.propagator.main_sequence.remove_all()

# Configure graphics settings:

chaser_satellite.propagator.options.draw_trajectory_in_3d = True

# ## Setup the initial state of the chaser satellite
#
# Access the existing initial state segment in the main sequence and configure the element type:

# +
from ansys.stk.core.stkobjects.astrogator import ElementSetType, SegmentType


chaser_initial_state = chaser_satellite.propagator.main_sequence.insert(
    SegmentType.INITIAL_STATE, "Initial State", "-"
)
chaser_initial_state.set_element_type(ElementSetType.KEPLERIAN)
chaser_initial_state.initial_state.epoch = scenario.start_time
# -

# Declare the keplerian elements:

# +
chaser_keplerian_elements = chaser_initial_state.element

chaser_keplerian_elements.semimajor_axis = semimajor_axis
chaser_keplerian_elements.eccentricity = eccentricity
chaser_keplerian_elements.inclination = inclination
chaser_keplerian_elements.raan = raan
chaser_keplerian_elements.true_anomaly = true_anomaly_chaser
chaser_keplerian_elements.arg_of_periapsis = arg_of_periapsis
# -

# Configure the propagation segment. Propagate the orbit of the chaser for 16 days:

# +
chaser_propagate_segment = chaser_satellite.propagator.main_sequence.insert(
    SegmentType.PROPAGATE, "Propagate", "-"
)
chaser_propagate_segment.propagator_name = "Earth point mass"


chaser_propagate_segment.stopping_conditions.add("Periapsis")
chaser_propagate_segment.stopping_conditions.remove("Duration")
# -

# Run the mission control sequence of the chaser:

run_code = chaser_satellite.propagator.run_mcs2()
if run_code != RunCode.MARCHING:
    raise ValueError("Could not propagate chaser satellite orbit.")

# Finally, show the orbit of the satellite:

plotter.show()

# ## Calculate phasing parameters
#
# Now calculate the parameters for the phasing maneuver using Kepler's equation and orbital mechanics principles:

# +
import math

# Get the mean period and SMA of the initial orbit
mean_keplerian_data_provider = chaser_satellite.data_providers[
    "Kozai-Izsak Mean"
].group["ICRF"]
mean_keplerian_result = mean_keplerian_data_provider.execute(
    scenario.start_time, scenario.start_time, 60
)
mean_keplerian_dataframe = mean_keplerian_result.data_sets.to_pandas_dataframe()
mean_orbital_period = float(mean_keplerian_dataframe.at[0, "mean nodal period"])
mean_semi_major_axis = float(mean_keplerian_dataframe.at[0, "mean semi-major axis"])

# Calculate the phase angle
phase_angle = math.radians(true_anomaly_target - true_anomaly_chaser)

if phase_angle < 0:
    phase_angle = 2 * math.pi + phase_angle

print("#################### Initial geometry #####################")
print(f"Phase angle      = {math.degrees(phase_angle):.1f} deg")
print("")

# Recalculate the phase angle accordingly with the number of phasing orbits
phase_angle = phase_angle / phasing_orbits

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
    scenario.start_time, scenario.start_time, 60
)
keplerian_dataframe = keplerian_result.data_sets.to_pandas_dataframe()
initial_radius = float(keplerian_dataframe.at[0, "radius_of_periapsis"])

if transfer_semi_major_axis > semimajor_axis:
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
# -

# ## Set up the phasing maneuver sequence
#
# Add a target sequence to perform the first delta-V maneuver and propagate through the phasing orbits:

# +
from ansys.stk.core.stkobjects.astrogator import (
    AttitudeControl,
    ControlManeuver,
    ManeuverType,
    ProfileMode,
    TargetSequenceAction,
)

# Add the first Target Sequence segment
phasing_start_sequence = chaser_satellite.propagator.main_sequence.insert(
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
if transfer_semi_major_axis > semimajor_axis:
    phasing_orbit_propagate.stopping_conditions.add("Periapsis")
else:
    phasing_orbit_propagate.stopping_conditions.add("Apoapsis")
phasing_orbit_propagate.stopping_conditions.remove("Duration")
phasing_orbit_propagate.stopping_conditions.item(
    0
).properties.repeat_count = phasing_orbits
phasing_orbit_propagate.results.add("Vector/Angle Between Vectors")
phasing_orbit_propagate.results[0].vector1_name = "Satellite/Chaser Position"
phasing_orbit_propagate.results[0].vector2_name = "Satellite/Target Position"
# -

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
circularization_sequence = chaser_satellite.propagator.main_sequence.insert(
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

# +
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
# -

# ## Run the main control sequence
#
# Execute the mission control sequence to solve for the phasing maneuver:

chaser_satellite.propagator.run_mcs()
target_satellite.propagator.run_mcs()
root.rewind()

# ## Retrieve the results
#
# Once the analysis has been performed, retrieve the delta-V values and phasing orbit parameters:

# +
# Get the maneuver data providers
maneuver_data_provider = chaser_satellite.data_providers["Maneuver Summary"]
maneuver_result = maneuver_data_provider.execute(scenario.start_time, scenario.stop_time)
maneuver_dataframe = maneuver_result.data_sets.to_pandas_dataframe()
delta_v_actual = maneuver_dataframe.at[0, "delta v"]

print("")
print("################### Transfer orbit data ###################")
print(f"N phasing orbits = {phasing_orbits}")
print(f"Period           = {phasing_orbit_period:.2f} sec")
print(f"SMA              = {transfer_semi_major_axis:.2f} km")
print(f"Perigee radius   = {periapsis_radius:.2f} km")
print(f"Apogee radius    = {apoapsis_radius:.2f} km")
print(f"Delta V          = {delta_v_actual} m/sec")
print(f"Transfer time    = {phasing_orbit_period * phasing_orbits / 86400:.4f} days")
print("")
# -

# Finally, show the complete orbit trajectory:

plotter.show()

# ## Plot the phase angle history
#
# Retrieve and plot the phase angle between the chaser and target satellites over time:

# +
import matplotlib.pyplot as plt
import numpy as np

# Get the phase angle data over time
angle_data_provider = chaser_satellite.data_providers["Vector"].group["Angle Between Vectors"]
angle_result = angle_data_provider.execute(scenario.start_time, scenario.stop_time, 3600)
angle_dataframe = angle_result.data_sets.to_pandas_dataframe()

# Convert time to days
time_seconds = angle_dataframe["Time"].values
time_days = time_seconds / 86400.0

# Get the angle values
phase_angles = angle_dataframe["Angle"].values

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(time_days, phase_angles, 'b-', linewidth=2)
plt.xlabel('Time (days)', fontsize=12)
plt.ylabel('Phase Angle (degrees)', fontsize=12)
plt.title('Phase Angle History During Phasing Maneuver', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xlim([0, propagation_time / 86400])
plt.tight_layout()
plt.show()
# -

# ## Plot the orbital altitude history
#
# Retrieve and plot the altitude of both satellites to visualize the phasing orbit:

# +
# Get altitude data for chaser satellite
chaser_altitude_provider = chaser_satellite.data_providers["Cartesian Position"].group["Fixed"]
chaser_altitude_result = chaser_altitude_provider.execute(scenario.start_time, scenario.stop_time, 3600)
chaser_altitude_df = chaser_altitude_result.data_sets.to_pandas_dataframe()

# Calculate magnitude of position vector and subtract Earth radius
earth_radius = 6378.137  # km
chaser_x = chaser_altitude_df["x"].values
chaser_y = chaser_altitude_df["y"].values
chaser_z = chaser_altitude_df["z"].values
chaser_altitude = np.sqrt(chaser_x**2 + chaser_y**2 + chaser_z**2) - earth_radius

# Get altitude data for target satellite
target_altitude_provider = target_satellite.data_providers["Cartesian Position"].group["Fixed"]
target_altitude_result = target_altitude_provider.execute(scenario.start_time, scenario.stop_time, 3600)
target_altitude_df = target_altitude_result.data_sets.to_pandas_dataframe()

target_x = target_altitude_df["x"].values
target_y = target_altitude_df["y"].values
target_z = target_altitude_df["z"].values
target_altitude = np.sqrt(target_x**2 + target_y**2 + target_z**2) - earth_radius

# Convert time to days
chaser_time_days = chaser_altitude_df["Time"].values / 86400.0
target_time_days = target_altitude_df["Time"].values / 86400.0

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(chaser_time_days, chaser_altitude, 'b-', linewidth=2, label='Chaser')
plt.plot(target_time_days, target_altitude, 'r--', linewidth=2, label='Target')
plt.xlabel('Time (days)', fontsize=12)
plt.ylabel('Altitude (km)', fontsize=12)
plt.title('Altitude History During Phasing Maneuver', fontsize=14, fontweight='bold')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.xlim([0, propagation_time / 86400])
plt.tight_layout()
plt.show()
# -

# ## Summary
#
# This example demonstrates how to:
#
# 1. Set up two geostationary satellites with different true anomalies
# 2. Calculate the required phasing orbit parameters using Kepler's equation
# 3. Design a phasing maneuver sequence with differential corrector profiles
# 4. Execute the maneuver and retrieve the results
# 5. Visualize the phase angle and altitude histories
#
# The phasing maneuver successfully brings the chaser satellite to the same orbital position as the target satellite after the specified number of phasing orbits.
