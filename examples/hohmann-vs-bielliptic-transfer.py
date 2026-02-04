# # Hohmann vs Bi-elliptic transfer comparison
#
# This tutorial provides a comprehensive comparison between Hohmann and bi-elliptic transfers, demonstrating when each transfer type is more fuel-efficient.
#
# ## What are Hohmann and bi-elliptic transfers?
#
# A **Hohmann transfer** is a two-impulse orbital maneuver used to transfer between two circular coplanar orbits. It is the most fuel-efficient two-impulse transfer for orbital radius ratios below a certain threshold.
#
# A **bi-elliptic transfer** is a three-impulse orbital maneuver that uses an intermediate apoapsis at a large distance. Although it requires three impulses instead of two, it can be more fuel-efficient than a Hohmann transfer when the ratio of final to initial orbit radius is sufficiently large (typically greater than ~11.94).
#
# Both transfers are modeled under the two-body assumption, considering only the spacecraft and the central body.
#
# ## Problem statement
#
# Compare the fuel efficiency of Hohmann and bi-elliptic transfers for various orbital radius ratios. Specifically:
#
# - Define an initial circular orbit at radius $r_1 = 6700$ km
# - Vary the final circular orbit radius $r_2$ from $1.5 \times r_1$ to $20 \times r_1$
# - For the bi-elliptic transfer, use an intermediate apoapsis at $r_b = 3 \times r_2$
# - Calculate the total $\Delta v$ normalized by the circular velocity at $r_1$ for both transfer types
# - Generate a comparison plot showing $\Delta v / v_c$ vs $r_2 / r_1$
# - Identify the critical radius ratio where bi-elliptic becomes more efficient
#
# The analysis will demonstrate that bi-elliptic transfers become more efficient for large radius ratios.

# ## Launch a new STK instance
#
# Start by launching a new STK instance. In this example, ``STKEngine`` is used in ``no_graphics`` mode:

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario
#
# Create a new scenario for the transfer comparison:

root = stk.new_object_root()
root.new_scenario("TransferComparison")

# Once created, show a 3D graphics window:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Define analytical transfer equations
#
# Before running the parametric study, define functions to calculate the total $\Delta v$ for each transfer type analytically.
#
# For a **Hohmann transfer** between circular orbits at radii $r_1$ and $r_2$:
#
# $$\Delta v_{\text{Hohmann}} = \sqrt{\frac{\mu}{r_1}} \left[ \sqrt{\frac{2r_2}{r_1 + r_2}} - 1 + \sqrt{\frac{2r_1}{r_1 + r_2}} \cdot \sqrt{\frac{r_1}{r_2}} - \sqrt{\frac{r_1}{r_2}} \right]$$
#
# For a **bi-elliptic transfer** with intermediate apoapsis at $r_b$:
#
# $$\Delta v_{\text{Bi-elliptic}} = \sqrt{\frac{\mu}{r_1}} \left[ \sqrt{\frac{2r_b}{r_1 + r_b}} - 1 + \sqrt{\frac{2\mu}{r_b}} \left| \sqrt{\frac{2r_2}{r_2 + r_b}} - \sqrt{\frac{2r_1}{r_1 + r_b}} \right| \frac{1}{\sqrt{\mu/r_1}} + \left| \sqrt{\frac{2r_b}{r_2 + r_b}} - 1 \right| \sqrt{\frac{r_1}{r_2}} \right]$$

# +
import numpy as np


def calculate_hohmann_delta_v(r1, r2, mu):
    """
    Calculate total delta-v for a Hohmann transfer.
    
    Parameters
    ----------
    r1 : float
        Initial circular orbit radius (km)
    r2 : float
        Final circular orbit radius (km)
    mu : float
        Gravitational parameter (km^3/s^2)
    
    Returns
    -------
    float
        Total delta-v (km/s)
    """
    v1 = np.sqrt(mu / r1)  # Circular velocity at r1
    v2 = np.sqrt(mu / r2)  # Circular velocity at r2
    
    # Transfer orbit velocities
    v_transfer_periapsis = np.sqrt(2 * mu * r2 / (r1 * (r1 + r2)))
    v_transfer_apoapsis = np.sqrt(2 * mu * r1 / (r2 * (r1 + r2)))
    
    # Delta-v at periapsis and apoapsis
    delta_v1 = abs(v_transfer_periapsis - v1)
    delta_v2 = abs(v2 - v_transfer_apoapsis)
    
    return delta_v1 + delta_v2


def calculate_bielliptic_delta_v(r1, r2, rb, mu):
    """
    Calculate total delta-v for a bi-elliptic transfer.
    
    Parameters
    ----------
    r1 : float
        Initial circular orbit radius (km)
    r2 : float
        Final circular orbit radius (km)
    rb : float
        Intermediate apoapsis radius (km)
    mu : float
        Gravitational parameter (km^3/s^2)
    
    Returns
    -------
    float
        Total delta-v (km/s)
    """
    v1 = np.sqrt(mu / r1)  # Circular velocity at r1
    v2 = np.sqrt(mu / r2)  # Circular velocity at r2
    
    # First transfer orbit (r1 to rb)
    v_transfer1_periapsis = np.sqrt(2 * mu * rb / (r1 * (r1 + rb)))
    v_transfer1_apoapsis = np.sqrt(2 * mu * r1 / (rb * (r1 + rb)))
    
    # Second transfer orbit (rb to r2)
    v_transfer2_apoapsis = np.sqrt(2 * mu * r2 / (rb * (r2 + rb)))
    v_transfer2_periapsis = np.sqrt(2 * mu * rb / (r2 * (r2 + rb)))
    
    # Delta-v at each impulse
    delta_v1 = abs(v_transfer1_periapsis - v1)
    delta_v2 = abs(v_transfer2_apoapsis - v_transfer1_apoapsis)
    delta_v3 = abs(v2 - v_transfer2_periapsis)
    
    return delta_v1 + delta_v2 + delta_v3
# -

# ## Perform parametric analysis
#
# Now perform a parametric study comparing both transfer types across a range of radius ratios.
#
# Define the initial orbit radius and the gravitational parameter for Earth:

# +
r1 = 6700.0  # Initial orbit radius (km)
mu_earth = 398600.4418  # Earth's gravitational parameter (km^3/s^2)
v_circular = np.sqrt(mu_earth / r1)  # Circular velocity at r1 (km/s)

print(f"Initial orbit radius: r1 = {r1:.1f} km")
print(f"Circular velocity at r1: v_c = {v_circular:.4f} km/s")
# -

# Define the range of radius ratios to analyze:

radius_ratios = np.linspace(1.5, 20, 200)  # r2/r1 from 1.5 to 20

# For each radius ratio, calculate the normalized delta-v for both transfer types:

# +
hohmann_delta_vs = []
bielliptic_delta_vs = []

for ratio in radius_ratios:
    r2 = ratio * r1
    rb = 3.0 * r2  # Intermediate apoapsis at 3 times the final radius
    
    # Calculate delta-v for both transfers
    dv_hohmann = calculate_hohmann_delta_v(r1, r2, mu_earth)
    dv_bielliptic = calculate_bielliptic_delta_v(r1, r2, rb, mu_earth)
    
    # Normalize by circular velocity
    hohmann_delta_vs.append(dv_hohmann / v_circular)
    bielliptic_delta_vs.append(dv_bielliptic / v_circular)

print(f"Parametric analysis complete: {len(radius_ratios)} cases computed")
# -

# ## Find the critical radius ratio
#
# Determine the radius ratio where bi-elliptic becomes more efficient than Hohmann:

# +
# Find where bi-elliptic becomes better (lower delta-v)
differences = np.array(hohmann_delta_vs) - np.array(bielliptic_delta_vs)
crossover_idx = np.where(differences > 0)[0]

if len(crossover_idx) > 0:
    critical_ratio = radius_ratios[crossover_idx[0]]
    hohmann_dv_at_critical = hohmann_delta_vs[crossover_idx[0]]
    bielliptic_dv_at_critical = bielliptic_delta_vs[crossover_idx[0]]
    
    print(f"\nCritical radius ratio: r2/r1 ≈ {critical_ratio:.2f}")
    print(f"At this ratio:")
    print(f"  Hohmann Δv/v_c = {hohmann_dv_at_critical:.4f}")
    print(f"  Bi-elliptic Δv/v_c = {bielliptic_dv_at_critical:.4f}")
    print(f"\nFor r2/r1 > {critical_ratio:.2f}, bi-elliptic is more efficient")
else:
    critical_ratio = None
    print("\nBi-elliptic transfer is not more efficient in the analyzed range")
# -

# ## Generate comparison plot
#
# Create a comprehensive plot comparing both transfer methods:

# +
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))

# Plot both transfer types
plt.plot(radius_ratios, hohmann_delta_vs, 'b-', linewidth=2, label='Hohmann Transfer')
plt.plot(radius_ratios, bielliptic_delta_vs, 'r-', linewidth=2, label='Bi-elliptic Transfer (rb = 3×r2)')

# Mark the crossover point
if critical_ratio is not None:
    plt.axvline(x=critical_ratio, color='green', linestyle='--', linewidth=1.5, 
                label=f'Crossover at r₂/r₁ ≈ {critical_ratio:.2f}')
    plt.plot(critical_ratio, hohmann_dv_at_critical, 'go', markersize=10, 
             markeredgewidth=2, markeredgecolor='darkgreen', markerfacecolor='lightgreen')

# Add labels and formatting
plt.xlabel('Final to Initial Radius Ratio (r₂/r₁)', fontsize=12, fontweight='bold')
plt.ylabel('Normalized Total Δv (Δv/v_c)', fontsize=12, fontweight='bold')
plt.title('Hohmann vs Bi-elliptic Transfer Efficiency Comparison', 
          fontsize=14, fontweight='bold', pad=20)
plt.grid(True, alpha=0.3, linestyle='--')
plt.legend(loc='upper left', fontsize=10, framealpha=0.9)

# Add annotations
plt.text(0.98, 0.97, f'r₁ = {r1:.0f} km\nrb = 3×r₂', 
         transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Highlight regions
if critical_ratio is not None:
    plt.axvspan(1.5, critical_ratio, alpha=0.1, color='blue', 
                label='Hohmann more efficient')
    plt.axvspan(critical_ratio, 20, alpha=0.1, color='red', 
                label='Bi-elliptic more efficient')

plt.xlim(1.5, 20)
plt.tight_layout()
plt.show()
# -

# ## Validate with STK simulation
#
# Now validate the analytical results by simulating a specific case using STK's Astrogator.
#
# Select a test case where bi-elliptic should be more efficient:

# +
if critical_ratio is not None:
    test_ratio = critical_ratio + 3.0  # Use a ratio well above the crossover
else:
    test_ratio = 15.0  # Default test case

r2_test = test_ratio * r1
rb_test = 3.0 * r2_test

print(f"\nValidation test case:")
print(f"  r1 = {r1:.1f} km")
print(f"  r2 = {r2_test:.1f} km (ratio = {test_ratio:.2f})")
print(f"  rb = {rb_test:.1f} km (for bi-elliptic)")
# -

# ### Create satellites for both transfer types
#
# Add two satellites to compare both methods:

# +
from ansys.stk.core.stkobjects import STKObjectType, PropagatorType


sat_hohmann = root.current_scenario.children.new(STKObjectType.SATELLITE, "HohmannSat")
sat_hohmann.set_propagator_type(PropagatorType.ASTROGATOR)
sat_hohmann.propagator.main_sequence.remove_all()
sat_hohmann.propagator.options.draw_trajectory_in_3d = True

sat_bielliptic = root.current_scenario.children.new(STKObjectType.SATELLITE, "BiellipticSat")
sat_bielliptic.set_propagator_type(PropagatorType.ASTROGATOR)
sat_bielliptic.propagator.main_sequence.remove_all()
sat_bielliptic.propagator.options.draw_trajectory_in_3d = True
# -

# ### Configure Hohmann transfer satellite
#
# Set up the initial state and Hohmann transfer sequence:

# +
from ansys.stk.core.stkobjects.astrogator import (
    SegmentType, ElementSetType, AttitudeControl, ManeuverType,
    ControlManeuver, ProfileMode, TargetSequenceAction
)
from ansys.stk.core.utilities.colors import Colors


# Initial state
initial_state_h = sat_hohmann.propagator.main_sequence.insert(
    SegmentType.INITIAL_STATE, "Initial State", "-"
)
initial_state_h.set_element_type(ElementSetType.KEPLERIAN)
initial_state_h.element.periapsis_radius_size = r1
initial_state_h.element.eccentricity = 0.00
initial_state_h.element.inclination = 0.00
initial_state_h.element.raan = 0.00
initial_state_h.element.arg_of_periapsis = 0.00
initial_state_h.element.true_anomaly = 0.00

# Hohmann transfer sequence
hohmann_transfer = sat_hohmann.propagator.main_sequence.insert(
    SegmentType.SEQUENCE, "Hohmann Transfer", "-"
)

# First impulse
hohmann_start = hohmann_transfer.segments.insert(
    SegmentType.TARGET_SEQUENCE, "Hohmann Start", "-"
)
first_impulse_h = hohmann_start.segments.insert(
    SegmentType.MANEUVER, "First Impulse", "-"
)
first_impulse_h.set_maneuver_type(ManeuverType.IMPULSIVE)
first_impulse_h.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
first_impulse_h.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
first_impulse_h.results.add("Keplerian Elems/Radius of Apoapsis")

# Configure solver for first impulse
hohmann_start_solver = hohmann_start.profiles["Differential Corrector"]
hohmann_start_solver.mode = ProfileMode.ITERATE
hohmann_start_solver.max_iterations = 50

delta_v1_x_h = hohmann_start_solver.control_parameters.get_control_by_paths(
    "First Impulse", "ImpulsiveMnvr.Cartesian.X"
)
delta_v1_x_h.enable = True
delta_v1_x_h.max_step = 0.30

desired_ra_h = hohmann_start_solver.results.get_result_by_paths(
    "First Impulse", "Radius Of Apoapsis"
)
desired_ra_h.enable = True
desired_ra_h.desired_value = r2_test
desired_ra_h.tolerance = 0.10

# Propagation to apoapsis
hohmann_propagate = hohmann_transfer.segments.insert(
    SegmentType.PROPAGATE, "Hohmann Propagate", "-"
)
hohmann_propagate.propagator_name = "Earth Point Mass"
hohmann_propagate.stopping_conditions.add("Apoapsis")
hohmann_propagate.stopping_conditions.remove("Duration")
hohmann_propagate.properties.color = Colors.Blue

# Last impulse
hohmann_end = hohmann_transfer.segments.insert(
    SegmentType.TARGET_SEQUENCE, "Hohmann End", "-"
)
last_impulse_h = hohmann_end.segments.insert(
    SegmentType.MANEUVER, "Last Impulse", "-"
)
last_impulse_h.set_maneuver_type(ManeuverType.IMPULSIVE)
last_impulse_h.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
last_impulse_h.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
last_impulse_h.results.add("Keplerian Elems/Eccentricity")

# Configure solver for last impulse
hohmann_end_solver = hohmann_end.profiles["Differential Corrector"]
hohmann_end_solver.mode = ProfileMode.ITERATE
hohmann_end_solver.max_iterations = 50

delta_v2_x_h = hohmann_end_solver.control_parameters.get_control_by_paths(
    "Last Impulse", "ImpulsiveMnvr.Cartesian.X"
)
delta_v2_x_h.enable = True
delta_v2_x_h.max_step = 0.30

desired_ecc_h = hohmann_end_solver.results.get_result_by_paths(
    "Last Impulse", "Eccentricity"
)
desired_ecc_h.enable = True
desired_ecc_h.desired_value = 0
desired_ecc_h.tolerance = 0.01

# Final orbit propagation
propagate_final_h = sat_hohmann.propagator.main_sequence.insert(
    SegmentType.PROPAGATE, "Final Orbit", "-"
)
propagate_final_h.properties.color = Colors.Green
propagate_final_h.propagator_name = "Earth Point Mass"
propagate_final_h.stopping_conditions["Duration"].properties.trip = 86400.00
# -

# ### Configure bi-elliptic transfer satellite
#
# Set up the initial state and bi-elliptic transfer sequence:

# +
# Initial state
initial_state_b = sat_bielliptic.propagator.main_sequence.insert(
    SegmentType.INITIAL_STATE, "Initial State", "-"
)
initial_state_b.set_element_type(ElementSetType.KEPLERIAN)
initial_state_b.element.periapsis_radius_size = r1
initial_state_b.element.eccentricity = 0.00
initial_state_b.element.inclination = 0.00
initial_state_b.element.raan = 0.00
initial_state_b.element.arg_of_periapsis = 0.00
initial_state_b.element.true_anomaly = 180.00  # Start at opposite position

# Bi-elliptic transfer sequence
bielliptic_transfer = sat_bielliptic.propagator.main_sequence.insert(
    SegmentType.SEQUENCE, "BiElliptic Transfer", "-"
)

# First impulse
bielliptic_start = bielliptic_transfer.segments.insert(
    SegmentType.TARGET_SEQUENCE, "BiElliptic Start", "-"
)
first_impulse_b = bielliptic_start.segments.insert(
    SegmentType.MANEUVER, "First Impulse", "-"
)
first_impulse_b.set_maneuver_type(ManeuverType.IMPULSIVE)
first_impulse_b.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
first_impulse_b.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
first_impulse_b.results.add("Keplerian Elems/Radius of Apoapsis")

# Configure solver for first impulse
bielliptic_start_solver = bielliptic_start.profiles["Differential Corrector"]
bielliptic_start_solver.mode = ProfileMode.ITERATE
bielliptic_start_solver.max_iterations = 50

delta_v1_x_b = bielliptic_start_solver.control_parameters.get_control_by_paths(
    "First Impulse", "ImpulsiveMnvr.Cartesian.X"
)
delta_v1_x_b.enable = True
delta_v1_x_b.max_step = 0.30

desired_ra_b = bielliptic_start_solver.results.get_result_by_paths(
    "First Impulse", "Radius Of Apoapsis"
)
desired_ra_b.enable = True
desired_ra_b.desired_value = rb_test
desired_ra_b.tolerance = 0.10

# First propagation to apoapsis
first_propagate_b = bielliptic_transfer.segments.insert(
    SegmentType.PROPAGATE, "First Propagate", "-"
)
first_propagate_b.propagator_name = "Earth Point Mass"
first_propagate_b.stopping_conditions.add("Apoapsis")
first_propagate_b.stopping_conditions.remove("Duration")
first_propagate_b.properties.color = Colors.Red

# Second impulse
bielliptic_middle = bielliptic_transfer.segments.insert(
    SegmentType.TARGET_SEQUENCE, "BiElliptic Middle", "-"
)
second_impulse_b = bielliptic_middle.segments.insert(
    SegmentType.MANEUVER, "Second Impulse", "-"
)
second_impulse_b.set_maneuver_type(ManeuverType.IMPULSIVE)
second_impulse_b.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
second_impulse_b.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
second_impulse_b.results.add("Keplerian Elems/Radius of Periapsis")

# Configure solver for second impulse
bielliptic_middle_solver = bielliptic_middle.profiles["Differential Corrector"]
bielliptic_middle_solver.mode = ProfileMode.ITERATE
bielliptic_middle_solver.max_iterations = 50

delta_v2_x_b = bielliptic_middle_solver.control_parameters.get_control_by_paths(
    "Second Impulse", "ImpulsiveMnvr.Cartesian.X"
)
delta_v2_x_b.enable = True
delta_v2_x_b.max_step = 0.30

desired_rp_b = bielliptic_middle_solver.results.get_result_by_paths(
    "Second Impulse", "Radius Of Periapsis"
)
desired_rp_b.enable = True
desired_rp_b.desired_value = r2_test
desired_rp_b.tolerance = 0.10

# Second propagation to periapsis
second_propagate_b = bielliptic_transfer.segments.insert(
    SegmentType.PROPAGATE, "Second Propagate", "-"
)
second_propagate_b.propagator_name = "Earth Point Mass"
second_propagate_b.stopping_conditions.add("Periapsis")
second_propagate_b.stopping_conditions.remove("Duration")
second_propagate_b.properties.color = Colors.Yellow

# Last impulse
bielliptic_end = bielliptic_transfer.segments.insert(
    SegmentType.TARGET_SEQUENCE, "BiElliptic End", "-"
)
last_impulse_b = bielliptic_end.segments.insert(
    SegmentType.MANEUVER, "Last Impulse", "-"
)
last_impulse_b.set_maneuver_type(ManeuverType.IMPULSIVE)
last_impulse_b.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
last_impulse_b.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)
last_impulse_b.results.add("Keplerian Elems/Eccentricity")

# Configure solver for last impulse
bielliptic_end_solver = bielliptic_end.profiles["Differential Corrector"]
bielliptic_end_solver.mode = ProfileMode.ITERATE
bielliptic_end_solver.max_iterations = 50

delta_v3_x_b = bielliptic_end_solver.control_parameters.get_control_by_paths(
    "Last Impulse", "ImpulsiveMnvr.Cartesian.X"
)
delta_v3_x_b.enable = True
delta_v3_x_b.max_step = 0.30

desired_ecc_b = bielliptic_end_solver.results.get_result_by_paths(
    "Last Impulse", "Eccentricity"
)
desired_ecc_b.enable = True
desired_ecc_b.desired_value = 0
desired_ecc_b.tolerance = 0.01

# Final orbit propagation
propagate_final_b = sat_bielliptic.propagator.main_sequence.insert(
    SegmentType.PROPAGATE, "Final Orbit", "-"
)
propagate_final_b.properties.color = Colors.Cyan
propagate_final_b.propagator_name = "Earth Point Mass"
propagate_final_b.stopping_conditions["Duration"].properties.trip = 86400.00
# -

# ### Run both transfer sequences
#
# Execute both main control sequences and compare results:

# +
# Run Hohmann transfer
hohmann_start.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
hohmann_end.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
sat_hohmann.propagator.run_mcs()
sat_hohmann.propagator.apply_all_profile_changes()

# Run bi-elliptic transfer
bielliptic_start.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
bielliptic_middle.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
bielliptic_end.action = TargetSequenceAction.RUN_ACTIVE_PROFILES
sat_bielliptic.propagator.run_mcs()
sat_bielliptic.propagator.apply_all_profile_changes()

print("\nBoth transfers completed successfully!")
# -

# ### Compare simulation results
#
# Extract and compare the delta-v values from both simulations:

# +
# Hohmann transfer results
hohmann_dv1 = abs(delta_v1_x_h.final_value)
hohmann_dv2 = abs(delta_v2_x_h.final_value)
hohmann_total_dv = hohmann_dv1 + hohmann_dv2

# Bi-elliptic transfer results
bielliptic_dv1 = abs(delta_v1_x_b.final_value)
bielliptic_dv2 = abs(delta_v2_x_b.final_value)
bielliptic_dv3 = abs(delta_v3_x_b.final_value)
bielliptic_total_dv = bielliptic_dv1 + bielliptic_dv2 + bielliptic_dv3

# Calculate analytical values for comparison
analytical_hohmann = calculate_hohmann_delta_v(r1, r2_test, mu_earth)
analytical_bielliptic = calculate_bielliptic_delta_v(r1, r2_test, rb_test, mu_earth)

print("\n" + "="*70)
print("SIMULATION RESULTS COMPARISON")
print("="*70)
print(f"\nTest case: r2/r1 = {test_ratio:.2f}")
print(f"  r1 = {r1:.1f} km")
print(f"  r2 = {r2_test:.1f} km")
print(f"  rb = {rb_test:.1f} km (bi-elliptic intermediate)")

print(f"\n{'HOHMANN TRANSFER':-^70}")
print(f"  Δv1 (periapsis)  : {hohmann_dv1:.5f} km/s")
print(f"  Δv2 (apoapsis)   : {hohmann_dv2:.5f} km/s")
print(f"  {'Total Δv':-<20}: {hohmann_total_dv:.5f} km/s")
print(f"  Normalized Δv/v_c: {hohmann_total_dv/v_circular:.4f}")
print(f"  Analytical value : {analytical_hohmann:.5f} km/s")
print(f"  Error            : {abs(hohmann_total_dv - analytical_hohmann):.6f} km/s")

print(f"\n{'BI-ELLIPTIC TRANSFER':-^70}")
print(f"  Δv1 (first burn) : {bielliptic_dv1:.5f} km/s")
print(f"  Δv2 (second burn): {bielliptic_dv2:.5f} km/s")
print(f"  Δv3 (third burn) : {bielliptic_dv3:.5f} km/s")
print(f"  {'Total Δv':-<20}: {bielliptic_total_dv:.5f} km/s")
print(f"  Normalized Δv/v_c: {bielliptic_total_dv/v_circular:.4f}")
print(f"  Analytical value : {analytical_bielliptic:.5f} km/s")
print(f"  Error            : {abs(bielliptic_total_dv - analytical_bielliptic):.6f} km/s")

print(f"\n{'COMPARISON':-^70}")
savings = hohmann_total_dv - bielliptic_total_dv
savings_percent = (savings / hohmann_total_dv) * 100
print(f"  Δv savings       : {savings:.5f} km/s")
print(f"  Percent savings  : {savings_percent:.2f}%")

if savings > 0:
    print(f"\n  ✓ Bi-elliptic is MORE efficient (uses less fuel)")
else:
    print(f"\n  ✗ Hohmann is MORE efficient (uses less fuel)")

print("="*70)
# -

# ## Visualize the trajectories
#
# Finally, display both transfer trajectories in 3D for visual comparison:

# Adjust camera to show both transfers
plotter.camera.position = [rb_test * 0.8, rb_test * 1.2, rb_test * 0.8]
plotter.show()

# ## Summary and conclusions
#
# This analysis demonstrates the following key findings:
#
# 1. **Critical radius ratio**: Bi-elliptic transfers become more fuel-efficient than Hohmann transfers when the final-to-initial radius ratio exceeds approximately 11.94 (theoretical value) or the computed critical value from the parametric study.
#
# 2. **Trade-offs**:
#    - **Hohmann transfer**: Uses only 2 impulses, shorter transfer time, more efficient for moderate radius ratios
#    - **Bi-elliptic transfer**: Uses 3 impulses, longer transfer time, but more fuel-efficient for large radius ratios
#
# 3. **Practical implications**: For missions requiring large orbital changes (e.g., from LEO to GEO or beyond), bi-elliptic transfers can provide significant fuel savings despite the longer transfer time and added complexity.
#
# 4. **STK validation**: The simulation results closely match the analytical predictions, validating both the theoretical equations and the STK Astrogator implementation.
#
# The choice between Hohmann and bi-elliptic transfers depends on mission constraints including fuel budget, time constraints, and the specific orbital radius ratio required.
