# # Inclination change maneuver
#
# This tutorial provides a practical example on how to solve a combined inclination change and orbit raising maneuver using Python and PySTK.
#
# ## What is an inclination change maneuver?
#
# An inclination change maneuver rotates the orbital plane of a spacecraft around the line of nodes. It is one of the most expensive maneuvers in spaceflight because the impulse must rotate the whole velocity vector, not only change its magnitude. For a circular orbit with velocity $v$, a pure plane change of $\Delta i$ requires:
#
# $$\Delta v = 2 v \sin\left(\frac{\Delta i}{2}\right)$$
#
# Since the required $\Delta v$ is proportional to the velocity, it is cheaper to change the plane where the spacecraft moves slowly, that is, far from the central body. This is the reason why geostationary transfers rarely change the inclination in low Earth orbit (LEO). Instead, the inclination change is combined with the circularization burn at the apoapsis of the transfer orbit. In that case, the required $\Delta v$ is obtained from the law of cosines:
#
# $$\Delta v = \sqrt{v_a^2 + v_c^2 - 2 v_a v_c \cos\left(\Delta i\right)}$$
#
# where $v_a$ is the velocity at the apoapsis of the transfer orbit and $v_c$ is the velocity of the final circular orbit.
#
# ## Problem statement
#
# A satellite presents a circular orbit with a radius of $7000$ kilometers and an inclination of $51.6$ degrees. Use a Hohmann transfer to raise the orbit up to a geostationary radius of $42164$ kilometers. At the same time, change the inclination of the orbit down to $28.5$ degrees.
#
# Compute the required $\Delta v$ for each impulse of the maneuver. Then, study how the total $\Delta v$ changes when the plane change is shared between the first and the last impulse.

# ## Define the problem parameters
#
# Start by defining the parameters of the problem:

# +
r_initial = 7000.0  # km
r_final = 42164.0  # km
inclination_initial = 51.6  # deg
inclination_final = 28.5  # deg
# -

# ## Launch a new STK instance
#
# Start by launching a new STK instance. In this example, ``STKEngine`` is used with the graphic user interface (GUI) components enabled:

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario
#
# Start by creating a new scenario in STK by running:

root = stk.new_object_root()
root.new_scenario("InclinationManeuver")

# Set the analysis period of the scenario to one day. The initial state of the satellite is set to start at the beginning of this period:

root.current_scenario.set_time_period(
    "1 Jan 2026 12:00:00.000", "2 Jan 2026 12:00:00.000"
)

# Once created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Adding a satellite to the scenario
#
# Now that a new scenario is available, add a new satellite and declare the type of orbit propagator used:

# +
from ansys.stk.core.stkobjects import PropagatorType, STKObjectType


scenario = root.current_scenario
satellite = scenario.children.new(STKObjectType.SATELLITE, "Satellite")
satellite.set_propagator_type(PropagatorType.ASTROGATOR)
# -

# Initialize the propagator by making sure that no previous sequence is present. For this example, it is requested to draw the maneuver in 3D.

satellite.propagator.main_sequence.remove_all()
satellite.propagator.options.draw_trajectory_in_3d = True

# ## Set up the initial state of the satellite
#
# Add a new segment to the main sequence for modeling the initial state of the satellite. The satellite starts at the ascending node, which is the location of the periapsis of the transfer orbit:

# +
from ansys.stk.core.stkobjects.astrogator import ElementSetType, SegmentType


initial_state = satellite.propagator.main_sequence.insert(
    SegmentType.INITIAL_STATE, "Initial State", "-"
)
initial_state.set_element_type(ElementSetType.KEPLERIAN)
initial_state.orbit_epoch = scenario.start_time

initial_state.element.periapsis_radius_size = r_initial
initial_state.element.eccentricity = 0.00
initial_state.element.inclination = inclination_initial
initial_state.element.raan = 0.00
initial_state.element.arg_of_periapsis = 0.00
initial_state.element.true_anomaly = 0.00
# -

# ## Set up the maneuver
#
# The maneuver is modeled as a sequence of three segments:
#
# - **First impulse**: it is applied at the periapsis to raise the radius of apoapsis up to the geostationary radius.
# - **Propagation**: the satellite is propagated along its transfer orbit until it reaches the apoapsis.
# - **Last impulse**: it is applied at the apoapsis to circularize the orbit and change the inclination at the same time.
#
# Differential correctors are required for solving both impulses. Therefore, these segments are modeled using a `TARGET_SEQUENCE` segment type. All maneuvers are modeled as `IMPULSIVE` maneuver type with a `THRUST_VECTOR` attitude control. By default, the thrust vector is defined in the velocity-normal-conormal (VNC) axes. The X component of the impulse is aligned with the velocity and the Y component is aligned with the orbit normal.

# +
from ansys.stk.core.stkobjects.astrogator import AttitudeControl, ManeuverType


transfer = satellite.propagator.main_sequence.insert(
    SegmentType.SEQUENCE, "Transfer", "-"
)

transfer_start = transfer.segments.insert(
    SegmentType.TARGET_SEQUENCE, "Transfer Start", "-"
)
first_impulse = transfer_start.segments.insert(
    SegmentType.MANEUVER, "First Impulse", "-"
)
first_impulse.set_maneuver_type(ManeuverType.IMPULSIVE)
first_impulse.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)

transfer_propagate = transfer.segments.insert(
    SegmentType.PROPAGATE, "Transfer Propagate", "-"
)
transfer_propagate.propagator_name = "Earth Point Mass"

transfer_end = transfer.segments.insert(
    SegmentType.TARGET_SEQUENCE, "Transfer End", "-"
)
last_impulse = transfer_end.segments.insert(SegmentType.MANEUVER, "Last Impulse", "-")
last_impulse.set_maneuver_type(ManeuverType.IMPULSIVE)
last_impulse.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
# -

# ### First impulse
#
# Enable the component of the velocity impulse along the X axis as a control parameter. Add the radius of apoapsis as a result to be achieved:

# +
from ansys.stk.core.stkobjects.astrogator import ControlManeuver


first_impulse.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
first_impulse.results.add("Keplerian Elems/Radius of Apoapsis")
# -

# Configure the differential corrector for this first impulse:

# +
from ansys.stk.core.stkobjects.astrogator import ProfileMode


transfer_start_solver = transfer_start.profiles["Differential Corrector"]
transfer_start_solver.mode = ProfileMode.ITERATE
transfer_start_solver.max_iterations = 50

delta_v1_x = transfer_start_solver.control_parameters.get_control_by_paths(
    "First Impulse", "ImpulsiveMnvr.Cartesian.X"
)
delta_v1_x.enable = True
delta_v1_x.max_step = 0.30

desired_radius_of_apoapsis = transfer_start_solver.results.get_result_by_paths(
    "First Impulse", "Radius Of Apoapsis"
)
desired_radius_of_apoapsis.enable = True
desired_radius_of_apoapsis.desired_value = r_final
desired_radius_of_apoapsis.tolerance = 0.10
# -

# ### Propagation
#
# The satellite is propagated until it reaches the apoapsis of the transfer orbit. The segment is colored in red to differentiate it from the other segments:

# +
from ansys.stk.core.utilities.colors import Colors


transfer_propagate.stopping_conditions.add("Apoapsis")
transfer_propagate.stopping_conditions.remove("Duration")
transfer_propagate.properties.color = Colors.Red
# -

# ### Last impulse
#
# In this case, two control parameters are required. The component along the velocity circularizes the orbit and the component along the orbit normal rotates the plane. Add the eccentricity and the inclination as results to be achieved:

last_impulse.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
last_impulse.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_Y)
last_impulse.results.add("Keplerian Elems/Eccentricity")
last_impulse.results.add("Keplerian Elems/Inclination")

# Configure the differential corrector for this last impulse:

# +
transfer_end_solver = transfer_end.profiles["Differential Corrector"]
transfer_end_solver.mode = ProfileMode.ITERATE
transfer_end_solver.max_iterations = 50

delta_v2_x = transfer_end_solver.control_parameters.get_control_by_paths(
    "Last Impulse", "ImpulsiveMnvr.Cartesian.X"
)
delta_v2_x.enable = True
delta_v2_x.max_step = 0.30

delta_v2_y = transfer_end_solver.control_parameters.get_control_by_paths(
    "Last Impulse", "ImpulsiveMnvr.Cartesian.Y"
)
delta_v2_y.enable = True
delta_v2_y.max_step = 0.30

desired_eccentricity = transfer_end_solver.results.get_result_by_paths(
    "Last Impulse", "Eccentricity"
)
desired_eccentricity.enable = True
desired_eccentricity.desired_value = 0
desired_eccentricity.tolerance = 0.0001

desired_inclination = transfer_end_solver.results.get_result_by_paths(
    "Last Impulse", "Inclination"
)
desired_inclination.enable = True
desired_inclination.desired_value = inclination_final
desired_inclination.tolerance = 0.001
# -

# ## Propagation along the final orbit
#
# Once the last impulse has been applied, propagate the satellite along its final orbit for $12$ hours:

# +
propagate_final_orbit = satellite.propagator.main_sequence.insert(
    SegmentType.PROPAGATE, "Final State Propagate", "-"
)
propagate_final_orbit.properties.color = Colors.Green
propagate_final_orbit.propagator_name = "Earth Point Mass"
propagate_final_orbit.stopping_conditions["Duration"].properties.trip = 43200.00
# -

# ## Running the main control sequence
#
# Once that all the segments for the main sequence are defined, run the main control sequence to solve for the desired values in each target sequence:

# +
from ansys.stk.core.stkobjects.astrogator import TargetSequenceAction


transfer_start.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
transfer_end.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

satellite.propagator.run_mcs()
# -


# ## Retrieve the results
#
# Retrieve the $\Delta v$ of each impulse from the final values of the control parameters. The first impulse only has a component along the velocity direction. The last impulse has components along the velocity and the orbit normal directions, so its magnitude is the norm of both:

# +
import math


delta_v1 = abs(delta_v1_x.final_value)
delta_v2 = math.hypot(delta_v2_x.final_value, delta_v2_y.final_value)

print(f"\N{GREEK CAPITAL LETTER DELTA}V1 = {delta_v1:.4f} [km/s]")
print(f"\N{GREEK CAPITAL LETTER DELTA}V2 = {delta_v2:.4f} [km/s]")
print(f"Total = {delta_v1 + delta_v2:.4f} [km/s]")
# -

# ## Plot the trajectory
#
# Apply the results of the differential correctors to the main sequence and show the complete maneuver. Since the transfer gets out of the field of view of the plotter's camera, the position of the camera is updated:

# + tags=["nbsphinx-thumbnail"]
satellite.propagator.apply_all_profile_changes()

plotter.camera.position = [57000, 85000, 55000]
plotter.show()
# -

# ## Plot the inclination and radius history
#
# Retrieve the Keplerian elements of the satellite during the maneuver at 60 second intervals:

# +
import pandas as pd


keplerian_result = (
    satellite.data_providers["Astrogator Values"]
    .group["Keplerian Elems"]
    .execute(scenario.start_time, scenario.stop_time, 60)
)
keplerian_dataframe = keplerian_result.data_sets.to_pandas_dataframe()

keplerian_dataframe["time"] = pd.to_datetime(keplerian_dataframe["time"])
time_hours = (
    keplerian_dataframe["time"] - keplerian_dataframe["time"].iloc[0]
).dt.total_seconds() / 3600
inclination = keplerian_dataframe["inclination"].astype(float)
radius_of_apoapsis = keplerian_dataframe["radius_of_apoapsis"].astype(float)
# -

# The inclination remains constant at $51.6$ degrees during the transfer. The whole plane change is applied instantaneously with the last impulse, when the satellite reaches the apoapsis. At that point, the radius of apoapsis stops changing and the orbit becomes circular:

# +
import matplotlib.pyplot as plt


figure, (inclination_axis, radius_axis) = plt.subplots(
    2, 1, figsize=(10, 8), sharex=True
)

inclination_axis.plot(time_hours, inclination, linewidth=2, color="dodgerblue")
inclination_axis.set_ylabel("Inclination (degrees)", fontsize=12)
inclination_axis.set_title("Orbit Evolution During the Combined Maneuver", fontsize=14)

radius_axis.plot(time_hours, radius_of_apoapsis, linewidth=2, color="tomato")
radius_axis.set_xlabel("Time (hours from start of maneuver)", fontsize=12)
radius_axis.set_ylabel("Radius of apoapsis (km)", fontsize=12)

for axis in (inclination_axis, radius_axis):
    axis.set_facecolor("whitesmoke")
    axis.grid(visible=True, which="both", linestyle="--")
plt.tight_layout()
plt.show()
# -

# ## Share the plane change between both impulses
#
# The plane change does not need to take place only at the apoapsis. It can also be shared with the first impulse, at the periapsis of the transfer orbit. The inclination change applied at the first impulse is an additional parameter that can be explored with STK. To do so, define a function that creates a satellite with the same maneuver sequence as before. The first impulse now targets both the radius of apoapsis and the inclination:


# +
def create_transfer_satellite(name, inclination_after_first_impulse):
    """Create a satellite with a two-impulse Hohmann transfer and plane change.

    Parameters
    ----------
    name : str
        Name of the satellite.
    inclination_after_first_impulse : float
        Inclination in degrees targeted by the first impulse. The last impulse
        applies the remaining plane change.

    Returns
    -------
    tuple
        Satellite with the maneuver sequence defined but not yet run, and the
        control parameters of the first and last impulses.
    """
    new_satellite = scenario.children.new(STKObjectType.SATELLITE, name)
    new_satellite.set_propagator_type(PropagatorType.ASTROGATOR)
    new_satellite.propagator.options.draw_trajectory_in_3d = False
    sequence = new_satellite.propagator.main_sequence
    sequence.remove_all()

    state = sequence.insert(SegmentType.INITIAL_STATE, "Initial State", "-")
    state.set_element_type(ElementSetType.KEPLERIAN)
    state.orbit_epoch = scenario.start_time
    state.element.periapsis_radius_size = r_initial
    state.element.eccentricity = 0.00
    state.element.inclination = inclination_initial
    state.element.raan = 0.00
    state.element.arg_of_periapsis = 0.00
    state.element.true_anomaly = 0.00

    start = sequence.insert(SegmentType.TARGET_SEQUENCE, "Transfer Start", "-")
    first = start.segments.insert(SegmentType.MANEUVER, "First Impulse", "-")
    first.set_maneuver_type(ManeuverType.IMPULSIVE)
    first.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
    first.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
    first.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_Y)
    first.results.add("Keplerian Elems/Radius of Apoapsis")
    first.results.add("Keplerian Elems/Inclination")

    propagate = sequence.insert(SegmentType.PROPAGATE, "Transfer Propagate", "-")
    propagate.propagator_name = "Earth Point Mass"
    propagate.stopping_conditions.add("Apoapsis")
    propagate.stopping_conditions.remove("Duration")

    end = sequence.insert(SegmentType.TARGET_SEQUENCE, "Transfer End", "-")
    last = end.segments.insert(SegmentType.MANEUVER, "Last Impulse", "-")
    last.set_maneuver_type(ManeuverType.IMPULSIVE)
    last.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
    last.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
    last.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_Y)
    last.results.add("Keplerian Elems/Eccentricity")
    last.results.add("Keplerian Elems/Inclination")

    solver_settings = [
        (
            start,
            "First Impulse",
            {
                "Radius Of Apoapsis": (r_final, 0.10),
                "Inclination": (inclination_after_first_impulse, 0.001),
            },
        ),
        (
            end,
            "Last Impulse",
            {
                "Eccentricity": (0, 0.0001),
                "Inclination": (inclination_final, 0.001),
            },
        ),
    ]
    impulse_controls = []
    for target_sequence, segment_name, results in solver_settings:
        solver = target_sequence.profiles["Differential Corrector"]
        solver.mode = ProfileMode.ITERATE
        solver.max_iterations = 50
        for control_path in ("ImpulsiveMnvr.Cartesian.X", "ImpulsiveMnvr.Cartesian.Y"):
            control = solver.control_parameters.get_control_by_paths(
                segment_name, control_path
            )
            control.enable = True
            control.max_step = 0.30
            impulse_controls.append(control)
        for result_name, (desired_value, tolerance) in results.items():
            result = solver.results.get_result_by_paths(segment_name, result_name)
            result.enable = True
            result.desired_value = desired_value
            result.tolerance = tolerance
        target_sequence.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

    return new_satellite, impulse_controls


# -

# Create one satellite for each value of the inclination change applied at the first impulse. A value of zero is equivalent to the maneuver solved in the previous sections. The largest value applies the whole plane change in LEO. Run the mission control sequence of each satellite and retrieve the $\Delta v$ of both impulses:

# +
total_inclination_change = inclination_initial - inclination_final
splits = [0.0, 1.0, 2.0, 3.0, 5.0, 10.0, 15.0, total_inclination_change]

results = []
for split in splits:
    split_satellite, controls = create_transfer_satellite(
        f"Split_{split:.1f}".replace(".", "_"), inclination_initial - split
    )
    split_satellite.propagator.run_mcs()
    first_x, first_y, last_x, last_y = controls
    results.append(
        {
            "split": split,
            "first_impulse": math.hypot(first_x.final_value, first_y.final_value),
            "last_impulse": math.hypot(last_x.final_value, last_y.final_value),
        }
    )

split_dataframe = pd.DataFrame(results)
split_dataframe["total"] = (
    split_dataframe["first_impulse"] + split_dataframe["last_impulse"]
)
split_dataframe
# -

# ## Compare the results
#
# Plot the $\Delta v$ of each impulse and the total $\Delta v$ as a function of the inclination change applied at the first impulse. Mark the best split and the two extreme strategies: the whole plane change at the apoapsis and the whole plane change in LEO:

# +
best = split_dataframe.loc[split_dataframe["total"].idxmin()]
apoapsis_only = split_dataframe.iloc[0]
periapsis_only = split_dataframe.iloc[-1]

figure, (total_axis, impulse_axis) = plt.subplots(2, 1, figsize=(10, 9), sharex=True)

total_axis.plot(
    split_dataframe["split"],
    split_dataframe["total"],
    "o-",
    linewidth=2,
    color="dodgerblue",
)
total_axis.plot(
    best["split"],
    best["total"],
    "o",
    color="green",
    markersize=11,
    label=f"Best split ({best['split']:.1f} deg): {best['total']:.3f} km/s",
)
total_axis.axhline(
    apoapsis_only["total"],
    color="gray",
    linestyle=":",
    label=f"Apoapsis only: {apoapsis_only['total']:.3f} km/s",
)
total_axis.axhline(
    periapsis_only["total"],
    color="tomato",
    linestyle="--",
    label=f"Periapsis (LEO) only: {periapsis_only['total']:.3f} km/s",
)
total_axis.set_ylabel("Total Delta-V (km/s)", fontsize=12)
total_axis.set_title("Total Delta-V by Plane Change Split", fontsize=14)
total_axis.legend(fontsize=11)

impulse_axis.plot(
    split_dataframe["split"],
    split_dataframe["first_impulse"],
    "o-",
    linewidth=2,
    color="tomato",
    label="First impulse (periapsis)",
)
impulse_axis.plot(
    split_dataframe["split"],
    split_dataframe["last_impulse"],
    "o-",
    linewidth=2,
    color="navy",
    label="Last impulse (apoapsis)",
)
impulse_axis.set_xlabel(
    "Inclination change at the first impulse (degrees)", fontsize=12
)
impulse_axis.set_ylabel("Delta-V (km/s)", fontsize=12)
impulse_axis.legend(fontsize=11)

for axis in (total_axis, impulse_axis):
    axis.set_facecolor("whitesmoke")
    axis.grid(visible=True, which="both", linestyle="--")
plt.tight_layout()
plt.show()
# -

# Print the savings of the best split compared with the two extreme strategies:

# +
print(f"Best split: {best['split']:.1f} deg at the first impulse")
print(
    f"Saving against the apoapsis only plane change: {apoapsis_only['total'] - best['total']:.4f} [km/s]"
)
print(
    f"Saving against the LEO only plane change:      {periapsis_only['total'] - best['total']:.4f} [km/s]"
)
# -

# Moving the plane change from the apoapsis to the periapsis makes the first impulse more expensive, because the satellite moves much faster in LEO. The last impulse becomes cheaper, but by a smaller amount. As a result, applying the whole plane change in LEO is the most expensive strategy by a large margin, about $1.6$ km/s more than the best split. Applying it all at the apoapsis is close to the minimum. Sharing about $2$ degrees with the first impulse reduces the total $\Delta v$ by only about $0.02$ km/s.
