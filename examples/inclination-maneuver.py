# # Inclination change maneuver
#
# This tutorial provides a practical example on how to solve a combined inclination change and orbit raising maneuver using Python and PySTK.
#
# ## What is an inclination change maneuver?
#
# An inclination change maneuver rotates the orbital plane of a spacecraft around the line of intersection between the initial and final orbital planes. It is one of the most expensive maneuvers in spaceflight because the impulse must rotate the velocity vector, not only change its magnitude. For a circular orbit with velocity $v$, a pure plane change of $\Delta i$ requires:
#
# $$\Delta v = 2 v \sin\left(\frac{\Delta i}{2}\right)$$
#
# To change the inclination without altering the right ascension of the ascending node (RAAN), the impulse must take place at the equatorial ascending or descending node. An out-of-plane impulse at any other latitude also rotates the RAAN.
#
# Since the required $\Delta v$ is proportional to the velocity, it is cheaper to change the plane where the spacecraft moves slowly, that is, far from the central body. This is the reason why geosynchronous transfers rarely change the inclination in low Earth orbit (LEO). Instead, the inclination change is combined with the circularization burn at the apoapsis of the transfer orbit. In that case, the required $\Delta v$ is obtained from the law of cosines:
#
# $$\Delta v = \sqrt{v_a^2 + v_c^2 - 2 v_a v_c \cos\left(\Delta i\right)}$$
#
# where $v_a$ is the velocity at the apoapsis of the transfer orbit and $v_c$ is the velocity of the final circular orbit.
#
# ## Problem statement
#
# A satellite is in a circular orbit with a radius of $7000$ kilometers and an inclination of $51.6$ degrees. Use a Hohmann transfer to raise the orbit up to a geosynchronous radius of $42164$ kilometers. At the same time, change the inclination of the orbit down to $28.5$ degrees.
#
# Compute the required $\Delta v$ for each impulse of the maneuver when the whole plane change takes place at the apoapsis. Then, compare it with the cost of changing the plane in LEO before the transfer. Next, find how to share the plane change between both impulses of the transfer to minimize the total $\Delta v$. Finally, perform a parametric analysis to study how these results change with the inclination change and with the radius of the final orbit.

# ## Define the problem parameters
#
# Start by defining the parameters of the problem:

# +
r_initial = 7000.0  # km
r_final = 42164.0  # km
inclination_initial = 51.6  # deg
inclination_final = 28.5  # deg
total_inclination_change = inclination_initial - inclination_final  # deg
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

# Set the analysis period of the scenario to one day. The initial state of the satellites is set to start at the beginning of this period:

scenario = root.current_scenario
scenario.set_time_period("1 Jan 2026 12:00:00.000", "2 Jan 2026 12:00:00.000")

# Once created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Add a satellite to the scenario
#
# Now that a new scenario is available, add a new satellite and declare the type of orbit propagator used:

# +
from ansys.stk.core.stkobjects import PropagatorType, STKObjectType


satellite = scenario.children.new(STKObjectType.SATELLITE, "Satellite")
satellite.set_propagator_type(PropagatorType.ASTROGATOR)
# -

# Initialize the propagator by making sure that no previous sequence is present. For this example, it is requested to draw the maneuver in 3D.

satellite.propagator.main_sequence.remove_all()
satellite.propagator.options.draw_trajectory_in_3d = True

# ## Set up the initial state of the satellite
#
# Add a new segment to the main sequence for modeling the initial state of the satellite. The satellite starts at the equatorial ascending node ($\omega = 0^\circ, \nu = 0^\circ$), which is the location of the periapsis of the transfer orbit. Half an orbit later, the satellite reaches the apoapsis at the equatorial descending node. Because both impulses take place on the equator at an apsis, they change the inclination without altering the RAAN or the argument of periapsis:

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
# - **First impulse**: it is applied at the periapsis to raise the radius of apoapsis up to the geosynchronous radius. It can also apply part of the plane change.
# - **Propagation**: the satellite is propagated along its transfer orbit until it reaches the apoapsis.
# - **Last impulse**: it is applied at the apoapsis to circularize the orbit and complete the plane change.
#
# Differential correctors are required for solving both impulses. Therefore, these segments are modeled using a `TARGET_SEQUENCE` segment type. All maneuvers are modeled as `IMPULSIVE` maneuver type with a `THRUST_VECTOR` attitude control. By default, the thrust vector is defined in the velocity-normal-conormal (VNC) axes of the pre-burn orbit. The X component of the impulse is aligned with the pre-burn velocity and the Y component is aligned with the pre-burn orbit normal. Because rotating the velocity vector requires both an out-of-plane (Y) component and a retrograde along-track (X) adjustment, the two components act together to achieve the target orbital size and inclination.

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
# Enable the components of the velocity impulse along the X and Y axes as control parameters. Add the radius of apoapsis and the inclination as results to be achieved:

# +
from ansys.stk.core.stkobjects.astrogator import ControlManeuver


first_impulse.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
first_impulse.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_Y)
first_impulse.results.add("Keplerian Elems/Radius of Apoapsis")
first_impulse.results.add("Keplerian Elems/Inclination")
# -

# Configure the differential corrector for this first impulse. For now, the desired inclination after the first impulse is the initial inclination. This means that the whole plane change takes place at the apoapsis. This value is modified later in this tutorial:

# +
from ansys.stk.core.stkobjects.astrogator import ProfileMode


transfer_start_solver = transfer_start.profiles["Differential Corrector"]
transfer_start_solver.mode = ProfileMode.ITERATE
transfer_start_solver.max_iterations = 50

for control_path in ["ImpulsiveMnvr.Cartesian.X", "ImpulsiveMnvr.Cartesian.Y"]:
    control = transfer_start_solver.control_parameters.get_control_by_paths(
        "First Impulse", control_path
    )
    control.enable = True
    control.max_step = 0.30

desired_radius_of_apoapsis = transfer_start_solver.results.get_result_by_paths(
    "First Impulse", "Radius Of Apoapsis"
)
desired_radius_of_apoapsis.enable = True
desired_radius_of_apoapsis.desired_value = r_final
desired_radius_of_apoapsis.tolerance = 0.10

desired_first_inclination = transfer_start_solver.results.get_result_by_paths(
    "First Impulse", "Inclination"
)
desired_first_inclination.enable = True
desired_first_inclination.desired_value = inclination_initial
desired_first_inclination.tolerance = 0.001
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
# Again, the X (along-track) and Y (orbit-normal) impulse components are used as control parameters to simultaneously circularize the orbit and complete the plane change. Add the eccentricity and the inclination as results to be achieved:

last_impulse.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
last_impulse.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_Y)
last_impulse.results.add("Keplerian Elems/Eccentricity")
last_impulse.results.add("Keplerian Elems/Inclination")

# Configure the differential corrector for this last impulse:

# +
transfer_end_solver = transfer_end.profiles["Differential Corrector"]
transfer_end_solver.mode = ProfileMode.ITERATE
transfer_end_solver.max_iterations = 50

for control_path in ["ImpulsiveMnvr.Cartesian.X", "ImpulsiveMnvr.Cartesian.Y"]:
    control = transfer_end_solver.control_parameters.get_control_by_paths(
        "Last Impulse", control_path
    )
    control.enable = True
    control.max_step = 0.30

desired_eccentricity = transfer_end_solver.results.get_result_by_paths(
    "Last Impulse", "Eccentricity"
)
desired_eccentricity.enable = True
desired_eccentricity.desired_value = 0
desired_eccentricity.tolerance = 0.0001

desired_final_inclination = transfer_end_solver.results.get_result_by_paths(
    "Last Impulse", "Inclination"
)
desired_final_inclination.enable = True
desired_final_inclination.desired_value = inclination_final
desired_final_inclination.tolerance = 0.001
# -

# ## Propagate along the final orbit
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

# ## Run the main control sequence
#
# Once that all the segments for the main sequence are defined, run the main control sequence to solve for the desired values in each target sequence. A run code different from `MARCHING` means that a differential corrector did not converge:

# +
from ansys.stk.core.stkobjects.astrogator import RunCode, TargetSequenceAction


transfer_start.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
transfer_end.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

run_code = satellite.propagator.run_mcs()
if run_code != RunCode.MARCHING:
    raise RuntimeError(f"The main control sequence failed with code {run_code.name}.")
# -

# ## Retrieve the results
#
# Retrieve the time and the $\Delta v$ of each impulse from the Maneuver Summary data provider. The same steps are required later for other satellites, so define a function for them. The $\Delta v$ values are reported in meters per second. Convert them to kilometers per second:

# +
import pandas as pd


def get_maneuver_summary(stk_satellite):
    """Return the time and the delta-v in km/s of each maneuver of a satellite.

    Parameters
    ----------
    stk_satellite : Satellite
        Satellite with an Astrogator propagator that has already been run.

    Returns
    -------
    pandas.DataFrame
        One row per maneuver with the ``segment``, ``time``, and ``delta v``
        columns.
    """
    summary = (
        stk_satellite.data_providers["Maneuver Summary"]
        .execute(scenario.start_time, scenario.stop_time)
        .data_sets.to_pandas_dataframe()
    )
    return pd.DataFrame(
        {
            "segment": summary["segment"],
            "time": pd.to_datetime(
                summary["start time"], format="%d %b %Y %H:%M:%S.%f"
            ),
            "delta v": summary["delta v"].astype(float) / 1000,
        }
    )


combined_summary = get_maneuver_summary(satellite)
combined_summary
# -

# ## Plot the trajectory
#
# Apply the results of the differential correctors to the main sequence and show the complete maneuver. Since the transfer gets out of the field of view of the plotter's camera, the position of the camera is updated:

# + tags=["nbsphinx-thumbnail"]
satellite.propagator.apply_all_profile_changes()

plotter.camera.position = [57000, 85000, 55000]
plotter.show()
# -

# ## Plot the orbit history
#
# Retrieve the Keplerian and spherical elements of the satellite during the maneuver at 60 second intervals. Define a function for retrieving a group of Astrogator values as a dataframe:


# +
def get_astrogator_values(group):
    """Return a group of Astrogator values of the first satellite every 60 seconds.

    Parameters
    ----------
    group : str
        Name of the group of Astrogator values.

    Returns
    -------
    pandas.DataFrame
        Values of the group with a ``time`` column of type ``datetime``.
    """
    dataframe = (
        satellite.data_providers["Astrogator Values"]
        .group[group]
        .execute(scenario.start_time, scenario.stop_time, 60)
        .data_sets.to_pandas_dataframe()
    )
    dataframe["time"] = pd.to_datetime(dataframe["time"], format="%d %b %Y %H:%M:%S.%f")
    return dataframe


keplerian_dataframe = get_astrogator_values("Keplerian Elems")
spherical_dataframe = get_astrogator_values("Spherical Elems")

start = keplerian_dataframe["time"].iloc[0]
time_hours = (keplerian_dataframe["time"] - start).dt.total_seconds() / 3600
burn_hours = (combined_summary["time"] - start).dt.total_seconds() / 3600
# -

# Plot the inclination, the RAAN, and the orbital radius. Mark the time of each impulse with a vertical line. STK reports the RAAN between $0$ and $360$ degrees, so wrap it between $-180$ and $180$ degrees to avoid a jump when it crosses zero:

# +
import matplotlib.pyplot as plt


history = [
    (keplerian_dataframe["inclination"], "Inclination (degrees)", "dodgerblue"),
    (
        (keplerian_dataframe["raan"].astype(float) + 180) % 360 - 180,
        "RAAN (degrees)",
        "green",
    ),
    (spherical_dataframe["r_mag"], "Orbital radius (km)", "tomato"),
]

figure, axes = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
for axis, (values, label, color) in zip(axes, history):
    axis.plot(time_hours, values.astype(float), linewidth=2, color=color)
    axis.set_ylabel(label, fontsize=12)
    for burn_index, burn_hour in enumerate(burn_hours):
        axis.axvline(
            burn_hour,
            color="gray",
            linestyle="--",
            label="Impulse" if burn_index == 0 else None,
        )
    axis.set_facecolor("whitesmoke")
    axis.grid(visible=True, which="both", linestyle="--")

axes[1].set_ylim(-10, 10)
axes[0].set_title("Orbit Evolution During the Combined Maneuver", fontsize=14)
axes[0].legend(fontsize=11)
axes[-1].set_xlabel("Time (hours from start of maneuver)", fontsize=12)
plt.tight_layout()
plt.show()
# -

# The first impulse places the satellite on the transfer orbit, and the orbital radius grows until the satellite reaches the apoapsis. There, the last impulse applies the whole plane change and circularizes the orbit, so the radius remains constant afterwards. The RAAN does not change during the maneuver, since both impulses take place at a node.

# ## Change the plane in LEO
#
# To evaluate the benefit of the combined maneuver, model a second satellite that performs a pure plane change in LEO and then a Hohmann transfer without any plane change. This strategy requires three impulses. Each impulse is modeled with the same steps used before: a target sequence with an impulsive maneuver, its control parameters, and its desired results. Define a function to add these segments to a sequence:


# +
def add_impulse(sequence, name, controls, results):
    """Add a target sequence with an impulsive maneuver to a sequence.

    Parameters
    ----------
    sequence : MCSSequence
        Sequence where the target sequence is appended.
    name : str
        Name of the maneuver segment.
    controls : list[str]
        Components of the impulse used as control parameters, for example ``"X"``.
    results : dict[str, tuple[float, float]]
        Desired value and tolerance for each Keplerian element to achieve.

    Returns
    -------
    ProfileDifferentialCorrector
        Differential corrector of the target sequence.
    """
    target_sequence = sequence.insert(
        SegmentType.TARGET_SEQUENCE, f"{name} Target", "-"
    )
    maneuver = target_sequence.segments.insert(SegmentType.MANEUVER, name, "-")
    maneuver.set_maneuver_type(ManeuverType.IMPULSIVE)
    maneuver.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)

    solver = target_sequence.profiles["Differential Corrector"]
    solver.mode = ProfileMode.ITERATE
    solver.max_iterations = 50

    for axis in controls:
        maneuver.enable_control_parameter(
            getattr(ControlManeuver, f"IMPULSIVE_CARTESIAN_{axis}")
        )
        control = solver.control_parameters.get_control_by_paths(
            name, f"ImpulsiveMnvr.Cartesian.{axis}"
        )
        control.enable = True
        control.max_step = 0.30

    for element, (desired_value, tolerance) in results.items():
        maneuver.results.add(f"Keplerian Elems/{element}")
        result = solver.results.get_result_by_paths(name, element)
        result.enable = True
        result.desired_value = desired_value
        result.tolerance = tolerance

    target_sequence.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
    return solver


# -

# Create the new satellite with the same initial state as the first one:

# +
separate_satellite = scenario.children.new(STKObjectType.SATELLITE, "SeparateSatellite")
separate_satellite.set_propagator_type(PropagatorType.ASTROGATOR)
separate_sequence = separate_satellite.propagator.main_sequence
separate_sequence.remove_all()

separate_state = separate_sequence.insert(
    SegmentType.INITIAL_STATE, "Initial State", "-"
)
separate_state.set_element_type(ElementSetType.KEPLERIAN)
separate_state.orbit_epoch = scenario.start_time
separate_state.element.periapsis_radius_size = r_initial
separate_state.element.eccentricity = 0.00
separate_state.element.inclination = inclination_initial
separate_state.element.raan = 0.00
separate_state.element.arg_of_periapsis = 0.00
separate_state.element.true_anomaly = 0.00
# -

# Add the plane change at the ascending node, followed by the two impulses of the Hohmann transfer. The plane change keeps the orbit circular. The first impulse of the Hohmann transfer only needs the X component, since the plane is already correct:

# +
plane_change_solver = add_impulse(
    separate_sequence,
    "Plane Change",
    ["X", "Y"],
    {"Inclination": (inclination_final, 0.001), "Eccentricity": (0, 0.0001)},
)
hohmann_start_solver = add_impulse(
    separate_sequence, "Hohmann Start", ["X"], {"Radius Of Apoapsis": (r_final, 0.10)}
)

separate_propagate = separate_sequence.insert(
    SegmentType.PROPAGATE, "Transfer Propagate", "-"
)
separate_propagate.propagator_name = "Earth Point Mass"
separate_propagate.stopping_conditions.add("Apoapsis")
separate_propagate.stopping_conditions.remove("Duration")

add_impulse(separate_sequence, "Hohmann End", ["X"], {"Eccentricity": (0, 0.0001)})

run_code = separate_satellite.propagator.run_mcs()
if run_code != RunCode.MARCHING:
    raise RuntimeError(f"The main control sequence failed with code {run_code.name}.")

separate_summary = get_maneuver_summary(separate_satellite)
separate_summary
# -

# ## Share the plane change between both impulses
#
# The plane change at the transfer does not need to take place only at the apoapsis. It can also be shared with the first impulse, at the periapsis. The inclination change applied at the first impulse, called the split, is set by the desired inclination of the first differential corrector. Define a function that changes this value, runs the main control sequence of the first satellite, and returns the $\Delta v$ of both impulses. The function also accepts the total inclination change and the final radius, which are used later in the parametric analysis:


# +
def evaluate_split(
    split, inclination_change=total_inclination_change, final_radius=r_final
):
    """Solve the combined maneuver for a given plane change at the first impulse.

    Parameters
    ----------
    split : float
        Inclination change in degrees applied at the first impulse.
    inclination_change : float
        Total inclination change in degrees.
    final_radius : float
        Radius of the final circular orbit in kilometers.

    Returns
    -------
    pandas.Series
        Delta-v in km/s of the first and the last impulse.
    """
    desired_first_inclination.desired_value = float(inclination_initial - split)
    desired_final_inclination.desired_value = float(
        inclination_initial - inclination_change
    )
    desired_radius_of_apoapsis.desired_value = float(final_radius)
    run_code = satellite.propagator.run_mcs()
    if run_code != RunCode.MARCHING:
        raise RuntimeError(
            f"The split of {split} degrees failed with code {run_code.name}."
        )
    return get_maneuver_summary(satellite)["delta v"]


# -

# Evaluate the total $\Delta v$ for several splits, from the whole plane change at the apoapsis to the whole plane change at the periapsis:

# +
import numpy as np


split_rows = []
for split in np.linspace(0, total_inclination_change, 12):
    first_delta_v, last_delta_v = evaluate_split(split)
    split_rows.append(
        {"split": split, "first impulse": first_delta_v, "last impulse": last_delta_v}
    )

split_dataframe = pd.DataFrame(split_rows)
split_dataframe["total"] = (
    split_dataframe["first impulse"] + split_dataframe["last impulse"]
)
split_dataframe
# -

# The total $\Delta v$ reaches its minimum for a small split. To find its exact value, use a bounded scalar minimizer from SciPy. Each evaluation of the cost function solves the maneuver in STK. Define a function for this search, since it is also used in the parametric analysis:

# +
from scipy.optimize import minimize_scalar


def find_optimal_split(
    inclination_change=total_inclination_change, final_radius=r_final
):
    """Find the split that minimizes the total delta-v of the combined maneuver.

    Parameters
    ----------
    inclination_change : float
        Total inclination change in degrees.
    final_radius : float
        Radius of the final circular orbit in kilometers.

    Returns
    -------
    tuple[float, float]
        Optimal split in degrees and its total delta-v in km/s.
    """
    optimum = minimize_scalar(
        lambda split: evaluate_split(split, inclination_change, final_radius).sum(),
        bounds=(0, inclination_change),
        method="bounded",
        options={"xatol": 0.01},
    )
    return optimum.x, optimum.fun


optimal_split, optimal_delta_v = find_optimal_split()

print(f"Optimal split = {optimal_split:.2f} [deg]")
print(f"Total \N{GREEK CAPITAL LETTER DELTA}V = {optimal_delta_v:.4f} [km/s]")
# -

# Plot the $\Delta v$ of each impulse and the total $\Delta v$ as a function of the split:

# +
figure, (total_axis, impulse_axis) = plt.subplots(2, 1, figsize=(10, 9), sharex=True)

total_axis.plot(
    split_dataframe["split"],
    split_dataframe["total"],
    "o-",
    linewidth=2,
    color="dodgerblue",
    label="Total",
)
total_axis.plot(
    optimal_split,
    optimal_delta_v,
    "*",
    color="green",
    markersize=16,
    label=f"Optimal split ({optimal_split:.2f} deg)",
)
total_axis.set_ylabel("Total Delta-V (km/s)", fontsize=12)
total_axis.set_title("Delta-V by Plane Change Split", fontsize=14)
total_axis.legend(fontsize=11)

impulse_axis.plot(
    split_dataframe["split"],
    split_dataframe["first impulse"],
    "o-",
    linewidth=2,
    color="tomato",
    label="First impulse (periapsis)",
)
impulse_axis.plot(
    split_dataframe["split"],
    split_dataframe["last impulse"],
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

# Moving the plane change from the apoapsis to the periapsis makes the first impulse more expensive, because the satellite moves much faster in LEO. The last impulse becomes cheaper, but by a smaller amount. As a result, the total $\Delta v$ grows quickly with the split, except for the first few degrees.

# ## Compare the strategies
#
# Finally, compare the total $\Delta v$ of the four strategies studied in this tutorial:

# +
strategies = pd.Series(
    {
        "Plane change in LEO,\nthen Hohmann": separate_summary["delta v"].sum(),
        "Plane change at\nperiapsis": split_dataframe["total"].iloc[-1],
        "Plane change at\napoapsis": combined_summary["delta v"].sum(),
        "Optimal split": optimal_delta_v,
    }
)

plt.figure(figsize=(10, 6))
bars = plt.bar(
    strategies.index,
    strategies.values,
    color=["tomato", "orange", "dodgerblue", "green"],
)
plt.bar_label(bars, fmt="%.3f km/s", fontsize=11)
plt.ylabel("Total Delta-V (km/s)", fontsize=12)
plt.title("Total Delta-V by Maneuver Strategy", fontsize=14)
plt.ylim(0, strategies.max() * 1.15)
plt.tight_layout()
plt.gca().set_facecolor("whitesmoke")
plt.gca().grid(visible=True, axis="y", linestyle="--")
plt.show()
# -

# Print the savings of the optimal split compared with the other strategies:

for strategy, delta_v in strategies.drop("Optimal split").items():
    print(
        f"{strategy.replace(chr(10), ' ')}: "
        f"{delta_v - optimal_delta_v:.4f} [km/s] more than the optimal split"
    )

# Changing the plane in LEO before the transfer is by far the most expensive strategy. Combining the plane change with the impulses of the Hohmann transfer is much cheaper, especially when it takes place at the apoapsis, where the satellite moves slowly. Sharing a small part of the plane change with the first impulse gives the minimum total $\Delta v$, although the saving compared with the apoapsis-only strategy is small.

# ## Parametric analysis
#
# The previous results are valid for a single combination of inclination change and final orbit. This section studies how the cost of each strategy and the optimal split change when these parameters vary. Start by defining a function that solves the strategy that changes the plane in LEO for any inclination change and final radius. The function modifies the desired values of the differential correctors of the second satellite and runs its main control sequence:


# +
def evaluate_separate(inclination_change, final_radius):
    """Solve the plane change in LEO followed by a Hohmann transfer.

    Parameters
    ----------
    inclination_change : float
        Total inclination change in degrees.
    final_radius : float
        Radius of the final circular orbit in kilometers.

    Returns
    -------
    float
        Total delta-v in km/s.
    """
    plane_change_solver.results.get_result_by_paths(
        "Plane Change", "Inclination"
    ).desired_value = float(inclination_initial - inclination_change)
    hohmann_start_solver.results.get_result_by_paths(
        "Hohmann Start", "Radius Of Apoapsis"
    ).desired_value = float(final_radius)
    run_code = separate_satellite.propagator.run_mcs()
    if run_code != RunCode.MARCHING:
        raise RuntimeError(
            f"The main control sequence failed with code {run_code.name}."
        )
    return get_maneuver_summary(separate_satellite)["delta v"].sum()


# -

# Next, define a function that evaluates the three strategies for a given inclination change and final radius:


# +
def evaluate_strategies(inclination_change, final_radius):
    """Evaluate the total delta-v of each strategy.

    Parameters
    ----------
    inclination_change : float
        Total inclination change in degrees.
    final_radius : float
        Radius of the final circular orbit in kilometers.

    Returns
    -------
    dict
        Total delta-v in km/s of each strategy and the optimal split in degrees.
    """
    split, delta_v = find_optimal_split(inclination_change, final_radius)
    return {
        "inclination change": inclination_change,
        "final radius": final_radius,
        "optimal split": split,
        "plane change in LEO": evaluate_separate(inclination_change, final_radius),
        "plane change at apoapsis": evaluate_split(
            0, inclination_change, final_radius
        ).sum(),
        "optimal split delta v": delta_v,
    }


# -

# The following function plots the results of a parametric study. The top plot shows the total $\Delta v$ of each strategy. The bottom plot shows the optimal split and the saving of the optimal split compared with the plane change at the apoapsis:


# +
def plot_parametric_study(dataframe, parameter, label):
    """Plot the total delta-v of each strategy and the optimal split.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Results of the parametric study.
    parameter : str
        Name of the column with the parameter of the study.
    label : str
        Label of the parameter axis.
    """
    figure, (delta_v_axis, split_axis) = plt.subplots(
        2, 1, figsize=(10, 9), sharex=True
    )

    for column, color, legend in [
        ("plane change in LEO", "tomato", "Plane change in LEO"),
        ("plane change at apoapsis", "dodgerblue", "Plane change at apoapsis"),
        ("optimal split delta v", "green", "Optimal split"),
    ]:
        delta_v_axis.plot(
            dataframe[parameter],
            dataframe[column],
            "o-",
            linewidth=2,
            color=color,
            label=legend,
        )
    delta_v_axis.set_ylabel("Total Delta-V (km/s)", fontsize=12)
    delta_v_axis.set_title(f"Delta-V by {label.split(' (')[0]}", fontsize=14)
    delta_v_axis.legend(fontsize=11)

    split_axis.plot(
        dataframe[parameter],
        dataframe["optimal split"],
        "o-",
        linewidth=2,
        color="green",
        label="Optimal split",
    )
    split_axis.set_xlabel(label, fontsize=12)
    split_axis.set_ylabel("Optimal split (degrees)", fontsize=12)

    saving_axis = split_axis.twinx()
    saving_axis.plot(
        dataframe[parameter],
        1000
        * (dataframe["plane change at apoapsis"] - dataframe["optimal split delta v"]),
        "s--",
        linewidth=2,
        color="purple",
        label="Saving against apoapsis",
    )
    saving_axis.set_ylabel("Saving (m/s)", fontsize=12)

    lines = split_axis.get_legend_handles_labels()
    saving_lines = saving_axis.get_legend_handles_labels()
    split_axis.legend(
        lines[0] + saving_lines[0], lines[1] + saving_lines[1], fontsize=11
    )

    for axis in (delta_v_axis, split_axis):
        axis.set_facecolor("whitesmoke")
        axis.grid(visible=True, which="both", linestyle="--")
    plt.tight_layout()
    plt.show()


# -

# The line plots only show the optimal split. To see how the cost changes for any split, compute the total $\Delta v$ on a grid of parameter values and split fractions. The split fraction is the split divided by the total inclination change, so it ranges from $0$, the whole plane change at the apoapsis, to $1$, the whole plane change at the periapsis. Normalize the total $\Delta v$ of each grid point by the optimal value for the same parameter. The result is the excess $\Delta v$ compared with the optimal split, in percent:


# +
split_fractions = np.linspace(0, 1, 11)


def compute_excess_map(dataframe):
    """Compute the excess delta-v of each split compared with the optimal split.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Results of the parametric study.

    Returns
    -------
    numpy.ndarray
        Excess delta-v in percent, with one row per split fraction and one
        column per row of the parametric study.
    """
    excess = np.zeros((len(split_fractions), len(dataframe)))
    indices = np.arange(len(split_fractions))
    for column, row in enumerate(dataframe.to_dict("records")):
        # Alternate the sweep direction so that each solution starts close to
        # the previous one, and finish with the split at zero.
        forward = (len(dataframe) - column) % 2 == 0
        for index in indices if forward else indices[::-1]:
            fraction = split_fractions[index]
            delta_v = evaluate_split(
                fraction * row["inclination change"],
                row["inclination change"],
                row["final radius"],
            ).sum()
            excess[index, column] = 100 * (delta_v / row["optimal split delta v"] - 1)
    return excess


def plot_excess_map(dataframe, excess, parameter, label):
    """Plot a contour map of the excess delta-v.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Results of the parametric study.
    excess : numpy.ndarray
        Excess delta-v in percent from ``compute_excess_map``.
    parameter : str
        Name of the column with the parameter of the study.
    label : str
        Label of the parameter axis.
    """
    figure, axis = plt.subplots(figsize=(10, 6))
    levels = [0, 0.5, 1, 2, 5, 10, 20, 30, 40, 50]
    filled = axis.contourf(
        dataframe[parameter],
        split_fractions,
        excess,
        levels=levels,
        cmap="viridis",
        extend="max",
    )
    lines = axis.contour(
        dataframe[parameter],
        split_fractions,
        excess,
        levels=levels,
        colors="white",
        linewidths=0.8,
    )
    axis.clabel(lines, fmt="%g%%", fontsize=9)
    figure.colorbar(filled, ax=axis, label="Excess Delta-V (%)")

    axis.plot(
        dataframe[parameter],
        dataframe["optimal split"] / dataframe["inclination change"],
        "o-",
        linewidth=2,
        color="tomato",
        label="Optimal split",
    )
    axis.set_xlabel(label, fontsize=12)
    axis.set_ylabel("Split fraction", fontsize=12)
    axis.set_title("Excess Delta-V compared with the optimal split", fontsize=14)
    axis.legend(fontsize=11, loc="upper right")
    plt.tight_layout()
    plt.show()


# -

# ### Inclination change
#
# Evaluate the strategies for a total inclination change between $5$ and $50$ degrees. The final orbit is at the geosynchronous radius in all cases:

# +
inclination_dataframe = pd.DataFrame(
    [
        evaluate_strategies(inclination_change, r_final)
        for inclination_change in [5.0, 10.0, 20.0, 30.0, 40.0, 50.0]
    ]
)
inclination_dataframe
# -

# Plot the results of the study:

plot_parametric_study(
    inclination_dataframe, "inclination change", "Total inclination change (degrees)"
)

# Compute and plot the excess $\Delta v$ map for the inclination change:

# +
inclination_excess = compute_excess_map(inclination_dataframe)
plot_excess_map(
    inclination_dataframe,
    inclination_excess,
    "inclination change",
    "Total inclination change (degrees)",
)
# -

# The cost of changing the plane in LEO grows much faster with the inclination change than the cost of the combined strategies. For large inclination changes, the difference between them reaches several kilometers per second. The optimal split also grows with the inclination change, together with the saving that it provides compared with the plane change at the apoapsis.
#
# The map shows that the penalty for a poor split also grows with the inclination change. For small inclination changes, any split costs only a few percent more than the optimal one. For large inclination changes, applying most of the plane change at the periapsis becomes very expensive. In all cases, the optimal split fraction stays small.

# ### Final orbit radius
#
# Now, evaluate the strategies for a final orbit radius between $10000$ kilometers and the geosynchronous radius. The total inclination change is the one from the problem statement in all cases:

# +
radius_dataframe = pd.DataFrame(
    [
        evaluate_strategies(total_inclination_change, final_radius)
        for final_radius in [10000.0, 15000.0, 20000.0, 26560.0, 35000.0, r_final]
    ]
)
radius_dataframe
# -

# Plot the results of the study:

plot_parametric_study(radius_dataframe, "final radius", "Final orbit radius (km)")

# Compute and plot the excess $\Delta v$ map for the final orbit radius:

# +
radius_excess = compute_excess_map(radius_dataframe)
plot_excess_map(
    radius_dataframe, radius_excess, "final radius", "Final orbit radius (km)"
)
# -

# For a low final orbit, the velocity at the apoapsis of the transfer orbit is closer to the velocity in LEO. Therefore, applying part of the plane change at the first impulse is more useful, and both the optimal split and its saving compared with the plane change at the apoapsis are larger. As the final radius grows, the velocity at the apoapsis decreases, and the optimal strategy moves almost all of the plane change to the last impulse. At the same time, the saving of the combined maneuver compared with the plane change in LEO grows with the final radius. The map confirms this trend. For a low final orbit, applying the whole plane change at the apoapsis costs several percent more than the optimal split. For the geosynchronous radius, the difference is below one percent.
