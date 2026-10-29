# # Low-thrust spiral transfer
#
# This tutorial provides a practical example on how to model a low-thrust orbit raising maneuver with an electric thruster using Python and PySTK.
#
# ## What is a low-thrust spiral transfer?
#
# Electric propulsion systems, such as Hall-effect and gridded ion thrusters, deliver a specific impulse ($I_{sp}$) between $1000\text{ s}$ and $3000\text{ s}$, several times higher than chemical thrusters ($I_{sp} \approx 300\text{ s}$). The price for this efficiency is a very small thrust, typically tens to hundreds of millinewtons. The thrust acceleration is then several orders of magnitude smaller than the local gravitational acceleration, so an orbit transfer can't be modeled as a set of impulses. Instead, the thruster fires continuously for days or months and the spacecraft slowly spirals outward over hundreds of revolutions.
#
# If the thrust is aligned with the velocity vector and the thrust acceleration is small, the orbit remains nearly circular at every instant. For a circular orbit, the orbital velocity is $v = \sqrt{\mu / r}$, where $\mu$ is Earth's gravitational parameter and $r$ is the orbital radius. Raising the orbit therefore decreases the orbital velocity. Under these assumptions, the velocity change ($\Delta v$) that the thruster must provide to move between two coplanar circular orbits is the difference between their circular velocities, a special case of the Edelbaum approximation without plane change:
#
# $$\Delta v_{\text{spiral}} = v_0 - v_f = \sqrt{\frac{\mu}{r_0}} - \sqrt{\frac{\mu}{r_f}}$$
#
# This value is always greater than the $\Delta v$ of a Hohmann transfer between two distinct orbits, because the thruster continuously circularizes the orbit at intermediate radii instead of concentrating two impulsive burns at the periapsis and apoapsis of an elliptical transfer orbit. However, the high $I_{sp}$ of the thruster greatly reduces the propellant mass $m_p$ predicted by the Tsiolkovsky rocket equation:
#
# $$m_p = m_0 \left(1 - e^{-\Delta v / \left(g_0 I_{sp}\right)}\right)$$
#
# where $m_0$ is the initial mass of the spacecraft and $g_0 = 9.80665\text{ m/s}^2$ is the standard gravitational acceleration. For a thruster with constant thrust $F$, the mass flow rate is $\dot{m} = F / \left(g_0 I_{sp}\right)$, and the transfer time is $t = m_p / \dot{m}$.
#
# ## Problem statement
#
# A rideshare launch releases a small satellite into a circular orbit at an altitude of $500\text{ km}$ with an inclination of $53^\circ$. The satellite must reach a circular operational orbit at $1200\text{ km}$ altitude in the same plane. The satellite has a dry mass of $250\text{ kg}$ and carries $50\text{ kg}$ of xenon propellant. Its Hall-effect thruster provides a constant thrust of $50\text{ mN}$ at a specific impulse of $1500\text{ s}$.
#
# First, model the spiral transfer in Astrogator with a finite maneuver that thrusts along the velocity vector until the satellite reaches the target orbital radius. Next, compare the propagated altitude, eccentricity, and mass history with the analytical model. Finally, perform a parametric analysis to study how the thrust level and the specific impulse change the transfer time, the $\Delta v$, and the propellant consumption, and when the near-circular spiral assumption stops being valid.

# ## Define the problem parameters
#
# Start by defining the physical constants of the Earth, the orbits, and the propulsion system:

# +
import math


mu_earth = 398600.4418  # km^3/s^2
r_earth = 6378.137  # km
g0 = 9.80665  # m/s^2

initial_altitude = 500.0  # km
final_altitude = 1200.0  # km
inclination = 53.0  # deg
initial_radius = r_earth + initial_altitude  # km
final_radius = r_earth + final_altitude  # km

dry_mass = 250.0  # kg
propellant_mass = 50.0  # kg
initial_mass = dry_mass + propellant_mass  # kg

thrust = 0.05  # N
specific_impulse = 1500.0  # s
# -

# Calculate the analytical estimates for the spiral transfer and compare its $\Delta v$ with the $\Delta v$ of a Hohmann transfer between the same orbits:


# +
def spiral_delta_v(r_0, r_f):
    """Return the delta-v in m/s of a tangential low-thrust spiral between circular orbits."""
    return 1000.0 * (math.sqrt(mu_earth / r_0) - math.sqrt(mu_earth / r_f))


def hohmann_delta_v(r_0, r_f):
    """Return the total delta-v in m/s of a Hohmann transfer between circular orbits."""
    v_0 = math.sqrt(mu_earth / r_0)
    v_f = math.sqrt(mu_earth / r_f)
    dv_1 = v_0 * (math.sqrt(2.0 * r_f / (r_0 + r_f)) - 1.0)
    dv_2 = v_f * (1.0 - math.sqrt(2.0 * r_0 / (r_0 + r_f)))
    return 1000.0 * (dv_1 + dv_2)


def propellant_used(delta_v, isp, m_0=initial_mass):
    """Return the propellant mass in kg given by the rocket equation."""
    return m_0 * (1.0 - math.exp(-delta_v / (g0 * isp)))


def spiral_transfer_time(delta_v, force, isp, m_0=initial_mass):
    """Return the transfer time in days of a constant-thrust spiral."""
    mass_flow_rate = force / (g0 * isp)
    return propellant_used(delta_v, isp, m_0) / mass_flow_rate / 86400.0


dv_spiral = spiral_delta_v(initial_radius, final_radius)
dv_hohmann = hohmann_delta_v(initial_radius, final_radius)
mp_spiral = propellant_used(dv_spiral, specific_impulse)
t_spiral = spiral_transfer_time(dv_spiral, thrust, specific_impulse)

print(
    f"Spiral delta-v: {dv_spiral:.2f} m/s\n"
    f"Hohmann delta-v: {dv_hohmann:.2f} m/s\n"
    f"Spiral propellant mass: {mp_spiral:.3f} kg\n"
    f"Spiral transfer time: {t_spiral:.2f} days"
)
# -

# ## Launch a new STK instance
#
# Start by launching a new STK instance. In this example, ``STKEngine`` is used with the graphical user interface (GUI) components enabled:

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario
#
# Start by creating a new scenario in STK:

root = stk.new_object_root()
root.new_scenario("LowThrustSpiral")

# Set the analysis period of the scenario to $1$ year. This period is long enough to cover the slowest transfer of the parametric analysis:

scenario = root.current_scenario
scenario.set_time_period("1 Jan 2026 12:00:00.000", "1 Jan 2027 12:00:00.000")

# Once created, show a 3D graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Define the electric thruster
#
# Astrogator models engines as components of the scenario. Duplicate the ``Constant Thrust and Isp`` engine model and set the thrust and the specific impulse of the Hall-effect thruster:

# +
from ansys.stk.core.stkobjects import Component


engine_models = scenario.component_directory.get_components(
    Component.ASTROGATOR
).get_folder("Engine Models")
hall_thruster = engine_models.duplicate_component(
    "Constant Thrust and Isp", "Hall Thruster"
)
hall_thruster.thrust = thrust
hall_thruster.isp = specific_impulse
# -

# ## Set up the satellite
#
# Add a satellite to the scenario and configure its Astrogator propagator. The initial state defines the circular parking orbit and the mass properties of the spacecraft:

# +
from ansys.stk.core.stkobjects import PropagatorType, STKObjectType
from ansys.stk.core.stkobjects.astrogator import ElementSetType, SegmentType


satellite = scenario.children.new(STKObjectType.SATELLITE, "SpiralSat")
satellite.set_propagator_type(PropagatorType.ASTROGATOR)
satellite.propagator.main_sequence.remove_all()
satellite.propagator.options.draw_trajectory_in_3d = True

initial_state = satellite.propagator.main_sequence.insert(
    SegmentType.INITIAL_STATE, "Initial State", "-"
)
initial_state.set_element_type(ElementSetType.KEPLERIAN)
initial_state.orbit_epoch = scenario.start_time
initial_state.element.semimajor_axis = initial_radius
initial_state.element.eccentricity = 0.0
initial_state.element.inclination = inclination
initial_state.element.raan = 0.0
initial_state.element.arg_of_periapsis = 0.0
initial_state.element.true_anomaly = 0.0
initial_state.spacecraft_parameters.dry_mass = dry_mass
initial_state.fuel_tank.fuel_mass = propellant_mass
# -

# ## Set up the spiral transfer
#
# Insert a finite maneuver segment that fires the Hall thruster along the velocity vector. The maneuver uses the ``Earth Point Mass`` propagator, so the propagated trajectory and the analytical model share the same force model. The burn stops when the orbital radius first reaches the radius of the target orbit. Because the orbit stays nearly circular during the spiral, this radius is a good proxy for the semimajor axis. Remove the default ``Duration`` stopping condition and disable the maximum propagation time of the segment, so that the burn lasts as long as the transfer requires:

# +
from ansys.stk.core.stkobjects.astrogator import (
    AttitudeControl,
    ManeuverType,
    PropulsionMethod,
)
from ansys.stk.core.utilities.colors import Colors


spiral = satellite.propagator.main_sequence.insert(
    SegmentType.MANEUVER, "Spiral Transfer", "-"
)
spiral.properties.color = Colors.Orange
spiral.set_maneuver_type(ManeuverType.FINITE)

finite_burn = spiral.maneuver
finite_burn.set_attitude_control_type(AttitudeControl.VELOCITY_VECTOR)
finite_burn.set_propulsion_method(PropulsionMethod.ENGINE_MODEL, "Hall Thruster")

burn_propagator = finite_burn.propagator
burn_propagator.propagator_name = "Earth Point Mass"
burn_propagator.stopping_conditions.add("R Magnitude").properties.trip = final_radius
burn_propagator.stopping_conditions.remove("Duration")
burn_propagator.enable_max_propagation_time = False
# -

# After the burn, propagate the final orbit for $1$ day:

coast = satellite.propagator.main_sequence.insert(
    SegmentType.PROPAGATE, "Final Orbit", "-"
)
coast.properties.color = Colors.DodgerBlue
coast.propagator_name = "Earth Point Mass"
coast.stopping_conditions["Duration"].properties.trip = 86400.0

# ## Run the main control sequence
#
# Define a function that runs the mission control sequence, verifies that it succeeded, and returns the main figures of the spiral transfer from the ``Maneuver Summary`` data provider. The function also returns the eccentricity at the end of the burn. This function is reused in the parametric analysis:

# +
from ansys.stk.core.stkobjects.astrogator import RunCode


def run_spiral_transfer():
    """Run the main control sequence and return the results of the spiral transfer.

    Returns
    -------
    dict
        Burn stop time, transfer time in days, delta-v in m/s, propellant used in kg,
        and eccentricity at the end of the burn.
    """
    run_code = satellite.propagator.run_mcs()
    if run_code != RunCode.MARCHING:
        raise RuntimeError(
            f"The main control sequence failed with code {run_code.name}."
        )

    summary = (
        satellite.data_providers["Maneuver Summary"]
        .execute(scenario.start_time, scenario.stop_time)
        .data_sets.to_pandas_dataframe()
    )
    burn_stop_time = summary["stop time"].iloc[0]
    final_elements = (
        satellite.data_providers["Astrogator Values"]
        .group["Keplerian Elems"]
        .execute_single(burn_stop_time)
        .data_sets.to_pandas_dataframe()
    )
    return {
        "stop_time": burn_stop_time,
        "duration_days": float(summary["finite burn duration"].iloc[0]) / 86400.0,
        "delta_v": float(summary["delta v"].iloc[0]),
        "propellant": float(summary["fuel used"].iloc[0]),
        "eccentricity": float(final_elements["eccentricity"].iloc[0]),
    }


nominal = run_spiral_transfer()
print(
    f"Transfer time: {nominal['duration_days']:.2f} days "
    f"(analytical {t_spiral:.2f} days)\n"
    f"Delta-v: {nominal['delta_v']:.2f} m/s (analytical {dv_spiral:.2f} m/s)\n"
    f"Propellant used: {nominal['propellant']:.3f} kg "
    f"(analytical {mp_spiral:.3f} kg)\n"
    f"Eccentricity at the end of the burn: {nominal['eccentricity']:.2e}"
)
# -

# The propagated transfer agrees with the analytical model. The small differences come from the stopping condition: the burn stops when the osculating radius first reaches the target radius, which happens slightly before or after the semimajor axis reaches the same value.

# Visualize the spiral in the 3D globe widget. The orange trajectory corresponds to the spiral transfer and the blue trajectory to the final orbit:

# + tags=["nbsphinx-thumbnail"]
plotter.camera.position = [25000, 25000, 15000]
plotter.show()
# -

# ## Retrieve and plot the transfer history
#
# Retrieve the Keplerian elements and the mass of the satellite every $10$ minutes from the start of the transfer to the end of the final orbit. Define a helper function to extract a group of Astrogator values as a pandas DataFrame:

# +
import pandas as pd


def get_astrogator_dataframe(group: str, stop_time: str, step: float = 600.0):
    """Return a group of Astrogator values of the satellite.

    Parameters
    ----------
    group : str
        Name of the group of Astrogator values.
    stop_time : str
        Last time of the requested interval.
    step : float, default=600.0
        Time step in seconds.

    Returns
    -------
    pd.DataFrame
        DataFrame with the requested elements.

    """
    df = (
        satellite.data_providers["Astrogator Values"]
        .group[group]
        .execute(scenario.start_time, stop_time, step)
        .data_sets.to_pandas_dataframe()
    )
    df["time"] = pd.to_datetime(df["time"])
    df["elapsed_days"] = (df["time"] - df["time"].iloc[0]).dt.total_seconds() / 86400.0
    return df


history_stop_time = coast.final_state.epoch
df_elements = get_astrogator_dataframe("Keplerian Elems", history_stop_time)
df_mass = get_astrogator_dataframe("Maneuver", history_stop_time)
# -

# Compute the analytical history of the near-circular spiral. The mass decreases linearly with time, the accumulated $\Delta v$ follows from the rocket equation, and the circular radius follows from $r = \mu / v^2$:

# +
import numpy as np


mass_flow_rate = thrust / (g0 * specific_impulse)  # kg/s
t_analytical = np.linspace(0.0, t_spiral * 86400.0, 500)  # s
mass_analytical = initial_mass - mass_flow_rate * t_analytical
dv_analytical = g0 * specific_impulse * np.log(initial_mass / mass_analytical)
velocity_analytical = math.sqrt(mu_earth / initial_radius) - dv_analytical / 1000.0
altitude_analytical = mu_earth / velocity_analytical**2 - r_earth

orbital_period = 2.0 * np.pi * np.sqrt((altitude_analytical + r_earth) ** 3 / mu_earth)
revolutions = np.trapezoid(1.0 / orbital_period, t_analytical)
print(f"Number of revolutions during the spiral: {revolutions:.0f}")
# -

# Plot the altitude of the apsides, the eccentricity, and the mass of the satellite over the transfer and the final orbit:

# +
import matplotlib.pyplot as plt


fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
fig.suptitle("Low-Thrust Spiral From 500 km to 1200 km")

axs[0].plot(
    df_elements["elapsed_days"],
    df_elements["altitude_of_apoapsis"].astype(float),
    color="tomato",
    linewidth=1.2,
    label="Apoapsis altitude (Astrogator)",
)
axs[0].plot(
    df_elements["elapsed_days"],
    df_elements["altitude_of_periapsis"].astype(float),
    color="dodgerblue",
    linewidth=1.2,
    label="Periapsis altitude (Astrogator)",
)
axs[0].plot(
    t_analytical / 86400.0,
    altitude_analytical,
    color="black",
    linestyle="--",
    linewidth=1.2,
    label="Circular altitude (analytical)",
)
axs[0].set_ylabel("Altitude (km)")
axs[0].legend()

axs[1].plot(
    df_elements["elapsed_days"],
    df_elements["eccentricity"].astype(float),
    color="green",
    linewidth=1.2,
    label="Osculating eccentricity (Astrogator)",
)
axs[1].set_ylabel("Eccentricity")
axs[1].legend()

axs[2].plot(
    df_mass["elapsed_days"],
    df_mass["total_mass"].astype(float),
    color="purple",
    linewidth=1.5,
    label="Total mass (Astrogator)",
)
axs[2].plot(
    t_analytical / 86400.0,
    mass_analytical,
    color="black",
    linestyle="--",
    linewidth=1.2,
    label="Total mass (analytical)",
)
axs[2].set_xlabel("Elapsed time (days)")
axs[2].set_ylabel("Mass (kg)")
axs[2].legend()

for ax in axs:
    ax.set_facecolor("whitesmoke")
    ax.grid(visible=True, which="both", linestyle="--")

plt.tight_layout()
plt.show()
# -

# The apoapsis and periapsis altitudes overlap during the whole transfer and follow the analytical circular altitude, which confirms that the orbit stays nearly circular. The osculating eccentricity oscillates between $0$ and about $4 a_T / g < 10^{-4}$ once per revolution without secular growth, because tangential thrust on opposite sides of the orbit shifts the eccentricity vector in opposite directions that cancel over each full revolution. The rate of climb increases slightly toward the end of the transfer for two reasons: the spacecraft is lighter, so the thrust acceleration $a_T$ is larger, and a given velocity increment $d(\Delta v) = -dv$ produces a larger change of radius at higher altitudes, since $dr / d(\Delta v) = 2 r / v$. The mass decreases linearly with time because the thrust and the specific impulse are constant.

# ## Parametric analysis
#
# Having modeled the nominal spiral, perform a parametric analysis to evaluate how the propulsion system affects the transfer.
#
# ### Influence of the thrust level
#
# First, sweep the thrust of the engine from $20\text{ mN}$ to $20\text{ N}$ while keeping the specific impulse at $1500\text{ s}$. A higher thrust shortens the transfer, but the thrust acceleration also becomes a larger fraction of the local gravitational acceleration. The ratio between both accelerations at the start of the transfer measures how well the near-circular spiral assumption holds:

# +
thrust_sweep = np.geomspace(0.02, 20.0, 10)  # N
thrust_results = []

for force in thrust_sweep:
    hall_thruster.thrust = float(force)
    thrust_results.append(run_spiral_transfer())

hall_thruster.thrust = thrust

df_thrust = pd.DataFrame(thrust_results)
df_thrust["thrust"] = thrust_sweep
df_thrust["acceleration_ratio"] = (thrust_sweep / initial_mass) / (
    1000.0 * mu_earth / initial_radius**2
)
print(
    df_thrust[
        ["thrust", "acceleration_ratio", "duration_days", "delta_v", "eccentricity"]
    ].to_string(index=False, float_format="{:.4g}".format)
)
# -

# Plot the transfer time, the $\Delta v$, and the eccentricity at the end of the burn against the thrust:

# +
thrust_fine = np.geomspace(0.02, 20.0, 200)

fig, axs = plt.subplots(3, 1, figsize=(10, 10), sharex=True)
fig.suptitle("Influence of the Thrust Level on the Spiral Transfer")

axs[0].loglog(
    thrust_fine,
    [spiral_transfer_time(dv_spiral, f, specific_impulse) for f in thrust_fine],
    color="black",
    linestyle="--",
    linewidth=1.2,
    label="Analytical",
)
axs[0].loglog(
    df_thrust["thrust"],
    df_thrust["duration_days"],
    color="tomato",
    marker="o",
    linestyle="None",
    label="Astrogator",
)
axs[0].set_ylabel("Transfer time (days)")
axs[0].legend()

axs[1].semilogx(
    df_thrust["thrust"],
    df_thrust["delta_v"],
    color="tomato",
    marker="o",
    linestyle="None",
    label="Astrogator",
)
axs[1].axhline(
    dv_spiral,
    color="black",
    linestyle="--",
    linewidth=1.2,
    label=f"Spiral, analytical ({dv_spiral:.1f} m/s)",
)
axs[1].axhline(
    dv_hohmann,
    color="navy",
    linestyle=":",
    linewidth=1.5,
    label=f"Hohmann ({dv_hohmann:.1f} m/s)",
)
axs[1].set_ylabel("Delta-v (m/s)")
axs[1].legend()

axs[2].loglog(
    df_thrust["thrust"],
    df_thrust["eccentricity"],
    color="green",
    marker="o",
    linestyle="-",
    label="Astrogator",
)
axs[2].set_xlabel("Thrust (N)")
axs[2].set_ylabel("Eccentricity at burn end")
axs[2].legend()

for ax in axs:
    ax.set_facecolor("whitesmoke")
    ax.grid(visible=True, which="both", linestyle="--")

plt.tight_layout()
plt.show()
# -

# For thrust levels up to about $0.5\text{ N}$, the thrust acceleration is less than $2 \times 10^{-4}$ times the gravitational acceleration and the transfer takes more than two days. In this regime, the Astrogator transfer time follows the analytical $1/F$ law, the $\Delta v$ stays within $0.2\%$ of the analytical value of the spiral, and the eccentricity stays below $10^{-3}$. As the thrust increases further, the transfer lasts only a few revolutions and the eccentricity at the end of the burn grows to $0.024$ at $20\text{ N}$. Because the stopping condition checks the osculating radius $r$ rather than the semimajor axis $a$, the cutoff depends on the orbital phase: at $4.31\text{ N}$, $r$ reaches the target radius near the periapsis side of the osculating cycle after $a$ has already overshot $r_f$ ($\Delta v = 370.6\text{ m/s}$), whereas at $9.28\text{ N}$ and $20\text{ N}$, $r$ reaches $r_f$ near apoapsis while $a$ is still well below $r_f$ ($\Delta v = 335.2\text{ m/s}$ and $307.2\text{ m/s}$, below the Hohmann $\Delta v$ because the target semimajor axis hasn't been reached). Moreover, at $e \approx 0.024$ and $a \approx 7500\text{ km}$, the periapsis and apoapsis altitudes differ by $2 a e \approx 360\text{ km}$, so reaching the circular target orbit would require an additional circularization maneuver. As the thrust grows, the transfer approaches the impulsive regime, where a two-burn Hohmann transfer is the appropriate model.

# ### Influence of the specific impulse
#
# Next, sweep the specific impulse from $300\text{ s}$, a value typical of chemical thrusters, to $3000\text{ s}$, a value typical of gridded ion thrusters, while keeping the nominal thrust of $50\text{ mN}$:

# +
isp_sweep = np.array([300.0, 500.0, 750.0, 1000.0, 1500.0, 2000.0, 3000.0])  # s
isp_results = []

for isp in isp_sweep:
    hall_thruster.isp = float(isp)
    isp_results.append(run_spiral_transfer())

hall_thruster.isp = specific_impulse

df_isp = pd.DataFrame(isp_results)
df_isp["isp"] = isp_sweep
print(
    df_isp[["isp", "duration_days", "delta_v", "propellant"]].to_string(
        index=False, float_format="{:.4g}".format
    )
)
# -

# Plot the propellant mass and the transfer time against the specific impulse. As a reference, add the propellant mass of a Hohmann transfer performed with a chemical thruster of $I_{sp} = 320\text{ s}$:

# +
isp_fine = np.linspace(300.0, 3000.0, 200)
chemical_isp = 320.0
mp_hohmann_chemical = propellant_used(dv_hohmann, chemical_isp)

fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Influence of the Specific Impulse on the Spiral Transfer")

axs[0].plot(
    isp_fine,
    [propellant_used(dv_spiral, isp) for isp in isp_fine],
    color="black",
    linestyle="--",
    linewidth=1.2,
    label="Spiral, rocket equation",
)
axs[0].plot(
    df_isp["isp"],
    df_isp["propellant"],
    color="purple",
    marker="o",
    linestyle="None",
    label="Spiral, Astrogator",
)
axs[0].plot(
    chemical_isp,
    mp_hohmann_chemical,
    color="navy",
    marker="*",
    markersize=12,
    linestyle="None",
    label=f"Chemical Hohmann (Isp = {chemical_isp:.0f} s)",
)
axs[0].set_ylabel("Propellant mass (kg)")
axs[0].legend()

axs[1].plot(
    isp_fine,
    [spiral_transfer_time(dv_spiral, thrust, isp) for isp in isp_fine],
    color="black",
    linestyle="--",
    linewidth=1.2,
    label="Analytical",
)
axs[1].plot(
    df_isp["isp"],
    df_isp["duration_days"],
    color="purple",
    marker="o",
    linestyle="None",
    label="Astrogator",
)
axs[1].set_xlabel("Specific impulse (s)")
axs[1].set_ylabel("Transfer time (days)")
axs[1].legend()

for ax in axs:
    ax.set_facecolor("whitesmoke")
    ax.grid(visible=True, which="both", linestyle="--")

plt.tight_layout()
plt.show()
# -

# Astrogator reproduces the rocket equation for every specific impulse. Increasing the specific impulse from $300\text{ s}$ to $3000\text{ s}$ reduces the propellant mass by a factor of almost $10$, from $34.6\text{ kg}$ to $3.7\text{ kg}$. At $I_{sp} = 300\text{ s}$, the spiral consumes slightly more propellant than the chemical Hohmann transfer because its $\Delta v$ is larger and its specific impulse is lower. The transfer time increases slightly with the specific impulse. At constant thrust, a higher specific impulse means a lower mass flow rate, so the spacecraft stays heavier during the transfer and its thrust acceleration is lower.

# ### Design space across target orbits
#
# Finally, use the analytical model to compare the spiral and the Hohmann transfer for coplanar target orbits from the initial orbit up to the geosynchronous radius of $42164\text{ km}$. The first plot compares the $\Delta v$ of both transfers. The second plot compares the propellant mass fraction $m_p / m_0$ of an electric spiral with $I_{sp} = 1500\text{ s}$ and of a chemical Hohmann transfer with $I_{sp} = 320\text{ s}$:

# +
geo_radius = 42164.137  # km
radius_fine = np.linspace(initial_radius, geo_radius, 300)
dv_spiral_fine = np.array([spiral_delta_v(initial_radius, r) for r in radius_fine])
dv_hohmann_fine = np.array([hohmann_delta_v(initial_radius, r) for r in radius_fine])
fraction_spiral = 1.0 - np.exp(-dv_spiral_fine / (g0 * specific_impulse))
fraction_hohmann = 1.0 - np.exp(-dv_hohmann_fine / (g0 * chemical_isp))

fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Spiral and Hohmann Transfers From a 500 km Circular Orbit")

axs[0].plot(
    radius_fine / initial_radius,
    dv_spiral_fine / 1000.0,
    color="tomato",
    linewidth=1.5,
    label="Low-thrust spiral",
)
axs[0].plot(
    radius_fine / initial_radius,
    dv_hohmann_fine / 1000.0,
    color="navy",
    linewidth=1.5,
    label="Hohmann transfer",
)
axs[0].set_ylabel("Delta-v (km/s)")
axs[0].legend()

axs[1].plot(
    radius_fine / initial_radius,
    fraction_spiral,
    color="tomato",
    linewidth=1.5,
    label=f"Electric spiral (Isp = {specific_impulse:.0f} s)",
)
axs[1].plot(
    radius_fine / initial_radius,
    fraction_hohmann,
    color="navy",
    linewidth=1.5,
    label=f"Chemical Hohmann (Isp = {chemical_isp:.0f} s)",
)
axs[1].set_xlabel("Radius ratio r_f / r_0")
axs[1].set_ylabel("Propellant mass fraction")
axs[1].legend()

for ax in axs:
    ax.axvline(
        final_radius / initial_radius,
        color="gray",
        linestyle=":",
        linewidth=1.2,
    )
    ax.axvline(
        geo_radius / initial_radius,
        color="gray",
        linestyle="-.",
        linewidth=1.2,
    )
    ax.set_facecolor("whitesmoke")
    ax.grid(visible=True, which="both", linestyle="--")

axs[0].text(final_radius / initial_radius, 0.2, " 1200 km", color="gray")
axs[0].text(geo_radius / initial_radius, 0.2, " GSO", color="gray")

plt.tight_layout()
plt.show()
# -

# For small radius ratios, such as the $500\text{ km}$ to $1200\text{ km}$ transfer of this example, the $\Delta v$ of the spiral and of the Hohmann transfer are almost identical. The $\Delta v$ penalty of the spiral grows with the radius ratio. For a coplanar transfer from $500\text{ km}$ to the geosynchronous radius, the spiral requires $4.54\text{ km/s}$, about $19\%$ more than the $3.82\text{ km/s}$ of the Hohmann transfer. Despite this penalty, the electric spiral consumes about $27\%$ of the initial mass in propellant, while the chemical Hohmann transfer consumes about $70\%$. The cost of this saving is time: with the $50\text{ mN}$ thruster of this example, the spiral to the geosynchronous radius would last about $270$ days. Reaching an equatorial geostationary orbit ($i = 0^\circ$) from an inclined parking orbit also requires a plane change, which increases the $\Delta v$ of both transfers.
