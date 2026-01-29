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

# +
from ansys.stk.core.stkobjects.astrogator import ElementSetType
from ansys.stk.core.utilities.colors import Colors


targetSat = scen.children.new(STKObjectType.SATELLITE, "Target")
targetSat.set_propagator_type(PropagatorType.ASTROGATOR)
tDriver = targetSat.propagator
tDriver.options.draw_trajectory_in_3d = False
tInitState = tDriver.main_sequence["Initial State"]
tInitState.set_element_type(ElementSetType.KEPLERIAN)
tInitState.initial_state.epoch = scen.start_time
tPropagator = tDriver.main_sequence["Propagate"]
tPropagator.propagator_name = "Earth point mass"
tPropagator.properties.color = Colors.Red
tKep = tInitState.element
# -

# ## Configure the chaser satellite
#
# Create the chaser satellite which will perform the phasing maneuver to rendezvous with the target:

# +
chaserSat = scen.children.new(STKObjectType.SATELLITE, "Chaser")
chaserSat.set_propagator_type(PropagatorType.ASTROGATOR)
cDriver = chaserSat.propagator
cDriver.options.draw_trajectory_in_3d = False
cInitState = cDriver.main_sequence["Initial State"]
cInitState.set_element_type(ElementSetType.KEPLERIAN)
cInitState.initial_state.epoch = scen.start_time
cPropagator = cDriver.main_sequence["Propagate"]
cPropagator.propagator_name = "Earth point mass"
cPropagator.stopping_conditions.add("Periapsis")
cPropagator.stopping_conditions.remove("Duration")
cKep = cInitState.element
# -

# ## Define the input parameters
#
# The cell below defines the input parameters for the phasing maneuver analysis:

# +
import math


########################################## INPUT DATA ##########################################################
true_anom = 70  # deg - chaser true anomaly (between 0 and 360)
target_ta = 20  # deg - target true anomaly (between 0 and 360)
nOrbits = 5  # number of phasing orbits
prop_time = 16  # days - total propagation time
################################################################################################################

# Fixed Keplerian parameters (geostationary orbit)
sma = 42164  # km
ecc = 0.0001
inc = 0.0
raan = 0.0
# -

# ## Configure initial orbital states
#
# Set the initial orbital elements for both satellites and run an initial propagation:
# +
# Change the scenario duration
scen.stop_time = "+" + str(prop_time) + " day"

# Set the chaser initial state
cKep.semimajor_axis = sma
cKep.eccentricity = ecc
cKep.inclination = inc
cKep.raan = raan
cKep.true_anomaly = true_anom
cKep.arg_of_periapsis = 0.0

# Set the target initial state
tKep.semimajor_axis = sma
tKep.eccentricity = ecc
tKep.inclination = inc
tKep.raan = raan
tKep.true_anomaly = target_ta
tKep.arg_of_periapsis = 0.0

# Configure target propagation duration
tPropagator.stopping_conditions["Duration"].properties.trip = prop_time * 86400

# Run initial propagation for both satellites
cDriver.run_mcs()
tDriver.run_mcs()
# -

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

# +
# Get the mean period and SMA of the initial orbit
meanKepDp = chaserSat.data_providers["Kozai-Izsak Mean"].group["ICRF"]
meanKep = meanKepDp.execute(scen.start_time, scen.start_time, 60)
meanKepDf = meanKep.data_sets.to_pandas_dataframe()
meanPeriod = float(meanKepDf.at[0, "mean nodal period"])
meanSma = float(meanKepDf.at[0, "mean semi-major axis"])

# Calculate the phase angle
phaseAngle = math.radians(target_ta - true_anom)

if phaseAngle < 0:
    phaseAngle = 2 * math.pi + phaseAngle

print("#################### Initial geometry #####################")
print("Phase angle      = " + str(math.degrees(phaseAngle)) + " deg")
print("")

# Recalculate the phase angle accordingly with the number of phasing orbits
phaseAngle = phaseAngle / nOrbits

# Calculate the eccentric anomaly
E = 2 * math.atan(math.sqrt((1 - ecc) / (1 + ecc)) * math.tan(phaseAngle / 2))

# Calculate the time elapsed to cover phase angle in original orbit (Kepler's equation)
tPhaseAngle = (meanPeriod / (2 * math.pi)) * (E - ecc * math.sin(E))

# Calculate the period of the phasing orbit
tPhasingOrbit = meanPeriod - tPhaseAngle

# Calculate the SMA of the phasing orbit
mu = 398600.44
transferSma = math.pow((tPhasingOrbit * math.sqrt(mu)) / (2 * math.pi), 2 / 3)

# Calculate eccentricity and radii
kepDp = chaserSat.data_providers["Astrogator Values"].group["Keplerian Elems"]
kep = kepDp.execute(scen.start_time, scen.start_time, 60)
kepDf = kep.data_sets.to_pandas_dataframe()
initRadius = float(kepDf.at[0, "radius_of_periapsis"])

if transferSma > sma:
    periRadius = initRadius
    apoRadius = 2 * transferSma - periRadius
else:
    apoRadius = initRadius
    periRadius = 2 * transferSma - apoRadius

# Estimate the needed Delta V for phasing
vPeriInitial = math.sqrt(mu * ((2 / initRadius) - (1 / meanSma)))
vPeriFinal = math.sqrt(mu * ((2 / initRadius) - (1 / transferSma)))
deltaV = vPeriFinal - vPeriInitial
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
    SegmentType,
    TargetSequenceAction,
)


# Add the first Target Sequence segment
ts1 = cDriver.main_sequence.insert(SegmentType.TARGET_SEQUENCE, "Start Phasing", "-")
ts1.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

# Add a Maneuver segment
dv1 = ts1.segments.insert(SegmentType.MANEUVER, "DV1", "-")
dv1.set_maneuver_type(ManeuverType.IMPULSIVE)
dv1.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)

# Maneuver attitude definition
dv1.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
thrustVector = dv1.maneuver.attitude_control
thrustVector.thrust_axes_name = "Satellite/Chaser VNC(Earth)"
thrustVector.x = deltaV * 1000

# Add a Propagate segment
phasingOrbit = ts1.segments.insert(SegmentType.PROPAGATE, "Phasing Orbit", "-")
phasingOrbit.properties.color = Colors.Orange
phasingOrbit.propagator_name = "Earth point mass"
if transferSma > sma:
    phasingOrbit.stopping_conditions.add("Periapsis")
else:
    phasingOrbit.stopping_conditions.add("Apoapsis")
phasingOrbit.stopping_conditions.remove("Duration")
phasingOrbit.stopping_conditions.item(0).properties.repeat_count = nOrbits
phasingOrbit.results.add("Vector/Angle Between Vectors")
phasingOrbit.results[0].vector1_name = "Satellite/Chaser Position"
phasingOrbit.results[0].vector2_name = "Satellite/Target Position"
# -

# ## Configure the differential corrector for phasing
#
# Set up the differential corrector to adjust the first delta-V to achieve zero phase angle at the end of the phasing orbits:

# +
# Customize the Differential Corrector
dc1 = ts1.profiles["Differential Corrector"]
dc1.mode = ProfileMode.ITERATE
dc1.max_iterations = 50

# Set Control Parameters and Results
xControlParam1 = dc1.control_parameters.get_control_by_paths(
    "DV1", "ImpulsiveMnvr.Cartesian.X"
)
xControlParam1.enable = True
xControlParam1.max_step = 0.001

roaResult = dc1.results.get_result_by_paths("Phasing Orbit", "Angle_Between_Vectors")
roaResult.enable = True
roaResult.desired_value = 0.0
roaResult.tolerance = 0.1
# -

# ## Set up the circularization maneuver
#
# Add a second target sequence to perform the circularization delta-V to return to the original circular orbit:

# +
# Add the second Target Sequence segment
ts2 = cDriver.main_sequence.insert(SegmentType.TARGET_SEQUENCE, "Circularization", "-")
ts2.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

# Add a Maneuver segment
dv2 = ts2.segments.insert(SegmentType.MANEUVER, "DV2", "-")
dv2.set_maneuver_type(ManeuverType.IMPULSIVE)
dv2.enable_control_parameter(ControlManeuver.IMPULSIVE_CARTESIAN_X)

# Add a Propagate segment
finalOrbit = ts2.segments.insert(SegmentType.PROPAGATE, "Final Orbit", "-")
finalOrbit.properties.color = Colors.Yellow
finalOrbit.propagator_name = "Earth point mass"
finalOrbit.stopping_conditions["Duration"].properties.trip = 86400
finalOrbit.results.add("Keplerian Elems/Eccentricity")
# -

# ## Configure the differential corrector for circularization
#
# Set up the differential corrector to achieve a circular orbit with the desired eccentricity:

# +
# Customize the Differential Corrector
dc2 = ts2.profiles["Differential Corrector"]
dc2.mode = ProfileMode.ITERATE
dc2.max_iterations = 50

# Set Control Parameters and Results
xControlParam2 = dc2.control_parameters.get_control_by_paths(
    "DV2", "ImpulsiveMnvr.Cartesian.X"
)
xControlParam2.enable = True
xControlParam2.max_step = 0.01

roaResult = dc2.results.get_result_by_paths("Final Orbit", "Eccentricity")
roaResult.enable = True
roaResult.desired_value = 0.0001
roaResult.tolerance = 0.00001
# -

# ## Run the main control sequence
#
# Execute the mission control sequence to solve for the phasing maneuver:

# +
cDriver.run_mcs()
tDriver.run_mcs()
root.rewind()
# -

# ## Retrieve the results
#
# Once the analysis has been performed, retrieve the delta-V values and phasing orbit parameters:

# +
# Get the maneuver data providers
manDp = chaserSat.data_providers["Maneuver Summary"]
man = manDp.execute(scen.start_time, scen.stop_time)
manDf = man.data_sets.to_pandas_dataframe()
deltaV = manDf.at[0, "delta v"]

print("################### Transfer orbit data ###################")
print("N phasing orbits = " + str(nOrbits))
print("Period           = " + str(tPhasingOrbit) + " sec")
print("SMA              = " + str(transferSma) + " km")
print("Perigee radius   = " + str(periRadius) + " km")
print("Apogee radius    = " + str(apoRadius) + " km")
print("Delta V          = " + str(deltaV) + " m/sec")
print("Transfer time    = " + str(tPhasingOrbit * nOrbits / 86400) + " days")
# -
