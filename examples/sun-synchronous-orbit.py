# # Sun-synchronous orbit design
#
# This tutorial provides a practical example on how to design and target a sun-synchronous orbit (SSO) using Python and PySTK.
#
# ## What is a sun-synchronous orbit?
#
# A sun-synchronous orbit (SSO) is a nearly polar, retrograde low Earth orbit (LEO) in which the orbital plane undergoes eastward nodal precession at the same average rate as Earth's mean motion around the Sun. Because the right ascension of the ascending node (RAAN, $\Omega$) advances by $360^\circ$ per tropical year of $365.2422$ days ($0.9856^\circ/\text{day}$), the orbital plane keeps a nearly constant angle with respect to the Earth-Sun vector throughout the year. Satellites in an SSO cross any given latitude at the same local solar time on every pass, which provides consistent surface illumination for optical Earth observation and stable thermal and solar-power conditions (such as dawn-dusk orbits).
#
# In a purely spherical gravity field, the orbital plane remains fixed in inertial space ($\dot{\Omega} = 0$). However, Earth's equatorial bulge (quantified by the second zonal harmonic $J_2 \approx 1.08263 \times 10^{-3}$) exerts a torque on inclined orbits, causing secular nodal precession. First-order secular perturbation theory gives the average rate of change of the RAAN as:
#
# $$\dot{\Omega} = -\frac{3}{2} n J_2 \left(\frac{R_\oplus}{a \left(1 - e^2\right)}\right)^2 \cos\left(i\right)$$
#
# where $n = \sqrt{\mu / a^3}$ is the mean motion, $\mu$ is Earth's gravitational parameter, $R_\oplus$ is Earth's mean equatorial radius, $a$ is the semimajor axis, $e$ is the eccentricity, and $i$ is the inclination.
#
# Because $\dot{\Omega}$ must be positive ($+0.9856^\circ/\text{day}$) to match the eastward apparent motion of the Sun, $\cos(i)$ must be negative. Therefore, a sun-synchronous orbit must be retrograde ($i > 90^\circ$). Solving the first-order relation for the inclination yields:
#
# $$i = \arccos\left(-\frac{2 \dot{\Omega}_{\text{SSO}}}{3 n J_2} \left(\frac{a \left(1 - e^2\right)}{R_\oplus}\right)^2\right)$$
#
# ## Problem statement
#
# An Earth observation satellite operates in a circular orbit at an altitude of $800\text{ km}$ ($a = 7178.137\text{ km}$).
#
# First, propagate a prograde reference orbit ($i = 81.4^\circ$) and a retrograde sun-synchronous orbit ($i \approx 98.6^\circ$) under the $J_2$ gravitational perturbation for $5$ days to compare their nodal precession directions. Next, use an Astrogator differential corrector to find the inclination that yields the sun-synchronous nodal drift of $0.9856^\circ/\text{day}$ ($4.928^\circ$ over $5$ days) and compare the evolution of the RAAN and orbital elements. Finally, perform a parametric analysis to study how the nodal precession rate and the required sun-synchronous inclination vary across LEO altitudes and eccentricities.

# ## Define the problem parameters
#
# Start by defining the physical constants of the Earth and the orbital parameters of the mission:

# +
import math


mu_earth = 398600.4418  # km^3/s^2
r_earth = 6378.137  # km
j2_earth = 1.08262668e-3

altitude = 800.0  # km
semimajor_axis = r_earth + altitude  # km
eccentricity = 0.0
propagation_days = 5.0
propagation_duration = propagation_days * 86400.0  # s

raan_rate_sso = 360.0 / 365.2421897  # deg/day
desired_raan_drift = raan_rate_sso * propagation_days  # deg

inclination_prograde = 81.4  # deg
# -

# Calculate the analytical first-order estimate of the sun-synchronous inclination at $800\text{ km}$ altitude to use as an initial guess for the differential corrector:

# +
mean_motion = math.sqrt(mu_earth / semimajor_axis**3)  # rad/s
raan_rate_sso_rad = math.radians(raan_rate_sso) / 86400.0  # rad/s

cos_i_sso = -(
    2.0
    * raan_rate_sso_rad
    * (semimajor_axis * (1.0 - eccentricity**2)) ** 2
    / (3.0 * mean_motion * j2_earth * r_earth**2)
)
inclination_sso_guess = math.degrees(math.acos(cos_i_sso))

print(
    f"Required SSO nodal rate: {raan_rate_sso:.4f} deg/day\n"
    f"Target RAAN drift over {propagation_days:.0f} days: {desired_raan_drift:.4f} deg\n"
    f"First-order analytical SSO inclination: {inclination_sso_guess:.3f} deg"
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
root.new_scenario("SunSynchronousOrbit")

# Set the analysis period of the scenario to $5$ days. The initial state of the satellites starts at the beginning of this period:

scenario = root.current_scenario
scenario.set_time_period("1 Jan 2026 12:00:00.000", "6 Jan 2026 12:00:00.000")

# Once created, show a 3D graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Compare prograde and retrograde nodal precession
#
# To observe the effect of the $J_2$ perturbation on the orbital plane, create two satellites at the same altitude of $800\text{ km}$. The first satellite (`ProgradeSat`) uses a prograde inclination of $81.4^\circ$, which is the supplementary angle to the sun-synchronous inclination ($180^\circ - 98.6^\circ$). The second satellite (`SSOSat`) uses a target sequence to solve for the sun-synchronous inclination.

# ### Set up the prograde reference satellite
#
# Add `ProgradeSat` to the scenario and configure its Astrogator propagator to use the ``Earth J2`` propagator for $5$ days:

# +
from ansys.stk.core.stkobjects import PropagatorType, STKObjectType
from ansys.stk.core.stkobjects.astrogator import ElementSetType, RunCode, SegmentType
from ansys.stk.core.utilities.colors import Colors


prograde_sat = scenario.children.new(STKObjectType.SATELLITE, "ProgradeSat")
prograde_sat.set_propagator_type(PropagatorType.ASTROGATOR)
prograde_sat.propagator.main_sequence.remove_all()
prograde_sat.propagator.options.draw_trajectory_in_3d = True

prograde_init = prograde_sat.propagator.main_sequence.insert(
    SegmentType.INITIAL_STATE, "Initial State", "-"
)
prograde_init.set_element_type(ElementSetType.KEPLERIAN)
prograde_init.orbit_epoch = scenario.start_time
prograde_init.element.semimajor_axis = semimajor_axis
prograde_init.element.eccentricity = eccentricity
prograde_init.element.inclination = inclination_prograde
prograde_init.element.raan = 0.00
prograde_init.element.arg_of_periapsis = 0.00
prograde_init.element.true_anomaly = 0.00

prograde_prop = prograde_sat.propagator.main_sequence.insert(
    SegmentType.PROPAGATE, "J2 Propagate", "-"
)
prograde_prop.properties.color = Colors.Red
prograde_prop.propagator_name = "Earth J2"
prograde_prop.stopping_conditions["Duration"].properties.trip = propagation_duration

run_code = prograde_sat.propagator.run_mcs()
if run_code != RunCode.MARCHING:
    raise RuntimeError(f"MCS run failed for ProgradeSat with code {run_code}")
# -

# ## Target the sun-synchronous orbit in Astrogator
#
# Now add `SSOSat` and place its initial state and propagation segment inside a `TARGET_SEQUENCE`. Enable `KEPLERIAN_INCLINATION` on the initial state as the control parameter, and add `Keplerian Elems/RAAN` at the end of the propagation segment as the target result. Because the initial RAAN is $0^\circ$, the final RAAN after $5$ days equals the total eastward nodal drift $\Delta \Omega = 4.928^\circ$:

# +
from ansys.stk.core.stkobjects.astrogator import (
    ControlInitState,
    ProfileMode,
    TargetSequenceAction,
)


sso_sat = scenario.children.new(STKObjectType.SATELLITE, "SSOSat")
sso_sat.set_propagator_type(PropagatorType.ASTROGATOR)
sso_sat.propagator.main_sequence.remove_all()
sso_sat.propagator.options.draw_trajectory_in_3d = True

target_sso = sso_sat.propagator.main_sequence.insert(
    SegmentType.TARGET_SEQUENCE, "Target SSO", "-"
)

sso_init = target_sso.segments.insert(SegmentType.INITIAL_STATE, "Initial State", "-")
sso_init.set_element_type(ElementSetType.KEPLERIAN)
sso_init.orbit_epoch = scenario.start_time
sso_init.element.semimajor_axis = semimajor_axis
sso_init.element.eccentricity = eccentricity
sso_init.element.inclination = inclination_sso_guess
sso_init.element.raan = 0.00
sso_init.element.arg_of_periapsis = 0.00
sso_init.element.true_anomaly = 0.00
sso_init.enable_control_parameter(ControlInitState.KEPLERIAN_INCLINATION)

sso_prop = target_sso.segments.insert(SegmentType.PROPAGATE, "J2 Propagate", "-")
sso_prop.properties.color = Colors.Green
sso_prop.propagator_name = "Earth J2"
sso_prop.stopping_conditions["Duration"].properties.trip = propagation_duration
sso_prop.results.add("Keplerian Elems/RAAN")
# -

# Configure the differential corrector to iterate on the initial inclination until the final RAAN matches the required $5$-day eastward drift within $10^{-4}$ degrees:

# +
sso_solver = target_sso.profiles["Differential Corrector"]
sso_solver.mode = ProfileMode.ITERATE
sso_solver.max_iterations = 50

inclination_control = sso_solver.control_parameters.get_control_by_paths(
    "Initial State", "InitialState.Keplerian.inc"
)
inclination_control.enable = True
inclination_control.max_step = 1.0

desired_raan = sso_solver.results.get_result_by_paths("J2 Propagate", "RAAN")
desired_raan.enable = True
desired_raan.desired_value = desired_raan_drift
desired_raan.tolerance = 0.0001
# -

# ## Run the main control sequence
#
# Let the target sequence run its active profiles. Define a function that runs the mission control sequence for `SSOSat`, verifies that the differential corrector converged, and returns the converged inclination. This function is reused in the parametric analysis:

# +
target_sso.action = TargetSequenceAction.RUN_ACTIVE_PROFILES


def solve_sso_inclination():
    """Run the SSO target sequence and return the converged inclination.

    Returns
    -------
    float
        Initial inclination in degrees that achieves the desired RAAN drift.
    """
    run_code = sso_sat.propagator.run_mcs()
    if run_code != RunCode.MARCHING:
        raise RuntimeError(
            f"The main control sequence failed with code {run_code.name}."
        )
    if sso_solver.status != "Converged":
        raise RuntimeError(
            f"The differential corrector did not converge: {sso_solver.status}."
        )
    return float(inclination_control.final_value)


inclination_converged = solve_sso_inclination()
print(
    f"Analytical initial guess: {inclination_sso_guess:.4f} deg\n"
    f"Astrogator converged SSO inclination: {inclination_converged:.4f} deg"
)
# -

# The two values differ slightly. The analytical expression uses mean elements, while the initial state of Astrogator defines osculating elements. Under $J_2$, the osculating semimajor axis differs from the mean semimajor axis by short-periodic terms of a few kilometers, which changes the mean nodal rate. The differential corrector accounts for these effects because it targets the propagated trajectory directly.

# Visualize both trajectories in the 3D globe widget. The red trajectory corresponds to the prograde orbit, whose node drifts westward, and the green trajectory corresponds to the sun-synchronous orbit, whose node drifts eastward:

# + tags=["nbsphinx-thumbnail"]
plotter.camera.position = [22000, 22000, 12000]
plotter.show()
# -

# ### Retrieve and plot the orbital elements
#
# Retrieve the Keplerian elements of both satellites over the $5$-day period at $300$-second intervals. Define a helper function to extract a group of Astrogator values as a pandas DataFrame:

# +
import pandas as pd


def get_astrogator_dataframe(stk_satellite, group: str, step: float = 300.0):
    """Return a group of Astrogator values of a satellite over the scenario period.

    Parameters
    ----------
    stk_satellite : Satellite
        Satellite with an Astrogator propagator that has already been run.
    group : str
        Name of the group of Astrogator values.
    step : float, default=300.0
        Time step in seconds.

    Returns
    -------
    pd.DataFrame
        DataFrame with the requested elements.

    """
    df = (
        stk_satellite.data_providers["Astrogator Values"]
        .group[group]
        .execute(scenario.start_time, scenario.stop_time, step)
        .data_sets.to_pandas_dataframe()
    )
    df["time"] = pd.to_datetime(df["time"])
    df["elapsed_days"] = (df["time"] - df["time"].iloc[0]).dt.total_seconds() / 86400.0
    return df


df_prograde = get_astrogator_dataframe(prograde_sat, "Keplerian Elems")
df_sso = get_astrogator_dataframe(sso_sat, "Keplerian Elems")
# -

# Wrap the RAAN angles to the $[-180^\circ, 180^\circ]$ interval so that the westward drift of `ProgradeSat` from $0^\circ$ into negative angles is continuous:

# +
import numpy as np


prograde_raan = ((df_prograde["raan"].astype(float) + 180.0) % 360.0) - 180.0
sso_raan = ((df_sso["raan"].astype(float) + 180.0) % 360.0) - 180.0

print(
    f"ProgradeSat final RAAN after {propagation_days:.0f} days: {prograde_raan.iloc[-1]:.4f} deg "
    f"({prograde_raan.iloc[-1] / propagation_days:.4f} deg/day)\n"
    f"SSOSat final RAAN after {propagation_days:.0f} days: {sso_raan.iloc[-1]:.4f} deg "
    f"({sso_raan.iloc[-1] / propagation_days:.4f} deg/day)"
)
# -

# Plot the evolution of the RAAN and the osculating inclination for both satellites over the $5$-day propagation:

# +
import matplotlib.pyplot as plt


fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
fig.suptitle("Evolution of RAAN and Inclination Under Earth J2 Perturbation")

axs[0].plot(
    df_sso["elapsed_days"],
    sso_raan,
    color="green",
    linewidth=1.5,
    label=f"Retrograde SSO (i = {inclination_converged:.2f}°)",
)
axs[0].plot(
    df_prograde["elapsed_days"],
    prograde_raan,
    color="tomato",
    linewidth=1.5,
    label=f"Prograde reference (i = {inclination_prograde:.2f}°)",
)
axs[0].plot(
    df_sso["elapsed_days"],
    df_sso["elapsed_days"] * raan_rate_sso,
    color="navy",
    linestyle="--",
    linewidth=1.2,
    label="Mean solar motion (+0.9856°/day)",
)
axs[0].set_ylabel("RAAN (deg)")
axs[0].legend()

axs[1].plot(
    df_sso["elapsed_days"],
    df_sso["inclination"].astype(float),
    color="green",
    linewidth=1.2,
    label="Retrograde SSO osculating inclination",
)
axs[1].set_xlabel("Elapsed time (days)")
axs[1].set_ylabel("Inclination (deg)")
axs[1].legend()

for ax in axs:
    ax.set_facecolor("whitesmoke")
    ax.grid(visible=True, which="both", linestyle="--")

plt.tight_layout()
plt.show()
# -

# The upper plot confirms that the retrograde SSO drifts eastward at $+0.9856^\circ/\text{day}$, tracking the mean apparent motion of the Sun, while the prograde orbit at the supplementary inclination drifts westward at $-0.9856^\circ/\text{day}$. In the lower plot, the osculating inclination exhibits short-periodic $J_2$ oscillations at twice the orbital frequency around its mean value, while showing no secular drift.

# ## Parametric analysis
#
# Having solved the sun-synchronous orbit at $800\text{ km}$ altitude, perform a parametric analysis to evaluate how the nodal precession rate and the required sun-synchronous inclination depend on the orbital altitude and inclination across the LEO regime.
#
# ### Influence of inclination on nodal precession rate in Astrogator
#
# First, use `ProgradeSat` in Astrogator to sweep the inclination from $5^\circ$ to $175^\circ$ at three circular orbit altitudes ($500\text{ km}$, $800\text{ km}$, and $1200\text{ km}$) over a $1$-day propagation, and compare the simulated nodal drift against the first-order $J_2$ analytical curve. Equatorial orbits ($i = 0^\circ$ and $i = 180^\circ$) are excluded because the ascending node, and therefore the RAAN, is undefined for them:

# +
altitudes_sweep = [500.0, 800.0, 1200.0]  # km
inclinations_sweep = np.linspace(5.0, 175.0, 18)  # deg
colors_sweep = ["dodgerblue", "green", "tomato"]

prograde_prop.stopping_conditions["Duration"].properties.trip = 86400.0
end_time_1day = "2 Jan 2026 12:00:00.000"
raan_dp = prograde_sat.data_providers["Astrogator Values"].group["Keplerian Elems"]

astrogator_rates = {alt: [] for alt in altitudes_sweep}

for alt in altitudes_sweep:
    prograde_init.element.semimajor_axis = r_earth + alt
    for inc in inclinations_sweep:
        prograde_init.element.inclination = float(inc)
        run_code = prograde_sat.propagator.run_mcs()
        if run_code != RunCode.MARCHING:
            raise RuntimeError(f"MCS failed at alt={alt}, inc={inc}")
        res_df = raan_dp.execute_single(end_time_1day).data_sets.to_pandas_dataframe()
        final_raan = float(res_df["raan"].iloc[0])
        wrapped_raan = ((final_raan + 180.0) % 360.0) - 180.0
        astrogator_rates[alt].append(wrapped_raan)
# -

# Plot the Astrogator nodal precession rates alongside the analytical $J_2$ curves and mark the sun-synchronous requirement ($+0.9856^\circ/\text{day}$):

# +
inc_fine = np.linspace(0.0, 180.0, 361)

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Nodal Precession Rate vs. Inclination for Different LEO Altitudes")
ax.set_xlabel("Inclination (deg)")
ax.set_ylabel("Nodal precession rate (deg/day)")

for alt, color in zip(altitudes_sweep, colors_sweep):
    sma = r_earth + alt
    n_orb = math.sqrt(mu_earth / sma**3)
    rate_analytical = (
        -1.5
        * n_orb
        * j2_earth
        * (r_earth / sma) ** 2
        * np.cos(np.radians(inc_fine))
        * (180.0 / math.pi)
        * 86400.0
    )
    ax.plot(
        inc_fine,
        rate_analytical,
        color=color,
        linewidth=1.5,
        label=f"h = {alt:.0f} km (analytical J2)",
    )
    ax.plot(
        inclinations_sweep,
        astrogator_rates[alt],
        color=color,
        marker="o",
        linestyle="None",
        markersize=5,
        label=f"h = {alt:.0f} km (Astrogator)",
    )

ax.axhline(
    raan_rate_sso,
    color="navy",
    linestyle="--",
    linewidth=1.5,
    label=f"SSO requirement (+{raan_rate_sso:.4f}°/day)",
)
ax.axhline(0.0, color="gray", linestyle=":", linewidth=1.0)

ax.set_xlim(0.0, 180.0)
ax.set_facecolor("whitesmoke")
ax.grid(visible=True, which="both", linestyle="--")
ax.legend(ncol=2)

plt.tight_layout()
plt.show()
# -

# Lower altitudes experience a stronger $J_2$ gravitational torque because of the $(R_\oplus / a)^{7/2}$ dependence of $\dot{\Omega}$. Consequently, a lower-altitude satellite requires a smaller retrograde component ($\cos(i)$ closer to zero, so $i$ closer to $90^\circ$) to achieve the $+0.9856^\circ/\text{day}$ nodal rate, whereas a higher-altitude satellite must tilt further retrograde.

# ### Target sun-synchronous inclination across LEO altitudes in Astrogator
#
# Next, use the Astrogator differential corrector on `SSOSat` to solve for the sun-synchronous inclination across circular altitudes from $300\text{ km}$ to $1500\text{ km}$. The first-order analytical inclination is the initial guess at each altitude:

# +
sso_altitudes = np.linspace(300.0, 1500.0, 13)  # km
sso_inclinations_astrogator = []
sso_periods_min = []

for alt in sso_altitudes:
    sma = r_earth + float(alt)
    n_orb = math.sqrt(mu_earth / sma**3)
    cos_i_est = -(2.0 * raan_rate_sso_rad * sma**2) / (
        3.0 * n_orb * j2_earth * r_earth**2
    )
    sso_init.element.semimajor_axis = sma
    sso_init.element.inclination = math.degrees(math.acos(cos_i_est))

    sso_inclinations_astrogator.append(solve_sso_inclination())
    sso_periods_min.append((2.0 * math.pi / n_orb) / 60.0)
# -

# Plot the converged sun-synchronous inclination and the corresponding Keplerian orbital period as functions of altitude:

# +
alt_fine = np.linspace(300.0, 1500.0, 200)
sma_fine = r_earth + alt_fine
n_fine = np.sqrt(mu_earth / sma_fine**3)
inc_analytical_fine = np.degrees(
    np.arccos(
        -(2.0 * raan_rate_sso_rad * sma_fine**2)
        / (3.0 * n_fine * j2_earth * r_earth**2)
    )
)

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.set_title("Sun-Synchronous Inclination and Orbital Period vs. Altitude")
ax1.set_xlabel("Circular orbit altitude (km)")
ax1.set_ylabel("Sun-synchronous inclination (deg)", color="dodgerblue")

line1 = ax1.plot(
    alt_fine,
    inc_analytical_fine,
    color="dodgerblue",
    linewidth=1.5,
    label="Analytical J2 SSO inclination",
)
pts1 = ax1.plot(
    sso_altitudes,
    sso_inclinations_astrogator,
    color="navy",
    marker="o",
    linestyle="None",
    markersize=6,
    label="Astrogator converged SSO inclination",
)
ax1.tick_params(axis="y", labelcolor="dodgerblue")
ax1.set_facecolor("whitesmoke")
ax1.grid(visible=True, which="both", linestyle="--")

ax2 = ax1.twinx()
ax2.set_ylabel("Orbital period (min)", color="tomato")
line2 = ax2.plot(
    sso_altitudes,
    sso_periods_min,
    color="tomato",
    linestyle="--",
    marker="s",
    markersize=5,
    linewidth=1.5,
    label="Orbital period",
)
ax2.tick_params(axis="y", labelcolor="tomato")

lines = line1 + pts1 + line2
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="upper left")

plt.tight_layout()
plt.show()
# -

# ### Design space across altitude and inclination
#
# Finally, build a 2D contour map of the nodal precession rate $\dot{\Omega}(a - R_\oplus, i)$ for circular orbits with $a - R_\oplus$ from $200\text{ km}$ to $2000\text{ km}$ and inclinations from $90^\circ$ to $120^\circ$. Overlay the sun-synchronous design locus ($\dot{\Omega} = +0.9856^\circ/\text{day}$) for eccentricities of $e = 0.00$, $0.05$, and $0.10$. For eccentric orbits, the horizontal axis is $a - R_\oplus$, and each locus is drawn only where the periapsis altitude stays above $200\text{ km}$:

# +
alt_grid = np.linspace(200.0, 2000.0, 200)
inc_grid = np.linspace(90.0, 120.0, 200)
ALT, INC = np.meshgrid(alt_grid, inc_grid)

SMA = r_earth + ALT
N_ORB = np.sqrt(mu_earth / SMA**3)
RAAN_RATE_GRID = (
    -1.5
    * N_ORB
    * j2_earth
    * (r_earth / SMA) ** 2
    * np.cos(np.radians(INC))
    * (180.0 / math.pi)
    * 86400.0
)

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title("Nodal Precession Rate of Retrograde Orbits and SSO Design Locus")
ax.set_xlabel("Semimajor axis minus Earth radius (km)")
ax.set_ylabel("Inclination (deg)")

contourf_plot = ax.contourf(
    ALT,
    INC,
    RAAN_RATE_GRID,
    levels=np.linspace(0.0, 4.0, 21),
    cmap="viridis",
)
cbar = fig.colorbar(contourf_plot, ax=ax)
cbar.set_label("Nodal precession rate for e = 0 (deg/day)")

contour_lines = ax.contour(
    ALT,
    INC,
    RAAN_RATE_GRID,
    levels=[0.5, 1.5, 2.0, 3.0],
    colors="white",
    linewidths=1.0,
)
ax.clabel(contour_lines, inline=True, fontsize=9, fmt="%.1f°/day")

min_periapsis_altitude = 200.0  # km
ecc_styles = [(0.00, "-", "tomato"), (0.05, "--", "orange"), (0.10, "-.", "gold")]
for ecc_val, ls, col in ecc_styles:
    sma_curve = r_earth + alt_grid
    cos_i_curve = -(
        2.0
        * raan_rate_sso_rad
        * (sma_curve * (1.0 - ecc_val**2)) ** 2
        / (3.0 * np.sqrt(mu_earth / sma_curve**3) * j2_earth * r_earth**2)
    )
    inc_curve = np.degrees(np.arccos(cos_i_curve))
    periapsis_altitude = sma_curve * (1.0 - ecc_val) - r_earth
    inc_curve[periapsis_altitude < min_periapsis_altitude] = np.nan
    ax.plot(
        alt_grid,
        inc_curve,
        color=col,
        linestyle=ls,
        linewidth=2.0,
        label=f"SSO locus (e = {ecc_val:.2f})",
    )

ax.set_xlim(200.0, 2000.0)
ax.set_ylim(90.0, 120.0)
ax.legend(loc="upper left")

plt.tight_layout()
plt.show()
# -

# For a fixed semimajor axis, a larger eccentricity reduces the semi-latus rectum $p = a(1 - e^2)$. Because $\dot{\Omega}$ scales with $p^{-2}$, the nodal precession becomes faster, so a smaller retrograde component ($i$ closer to $90^\circ$) is enough to reach the sun-synchronous rate. The effect is small for the near-circular orbits used by most Earth observation missions: at $e = 0.05$, $p$ decreases by only $0.25\%$. Most sun-synchronous missions also keep the orbit near-circular and use a frozen argument of periapsis to keep the altitude profile stable over each latitude.
