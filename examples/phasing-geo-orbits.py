# # GEO Orbit Phasing
#
# Once we get the intended orbit, a change of the true anomaly is sometime needed to target a well-defined orbit slot. This could be the case of constellations that have more than one satellite in the same orbital plane and a certain relative geometry has to be respected or a geostationary satellite that is moved from its original location to another one for operational purposes.
#
# In both cases we can solve for a reference (or target) satellite in Astrogator, whose position over time is taken as reference by a maneuvering (or chaser) satellite using a targeted MCS.
#
# ## STK Scenario
#
# This lesson focuses on the design of phasing maneuver to be executed by a geostationary satellite who needs to change its position along the geostationary belt.
#
# <center><img src="../Images/geo_phasing.png" alt="Drawing" style="width: 700px;"/><center>

# ## Import Libraries

# +
import math

from ansys.stk.core.stkdesktop import STKDesktop
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.utilities.colors import Colors


# -

# ### Create a New Scenario and Configure Satellites
#
# We now create a new scenario containing 2 satellites: the *Target* and the *Chaser*. Their initial states are not defined yet, but they will be on the geostationary orbit as specified in the next code cell.

# +
stk = STKDesktop.start_application()
app = STKDesktop.start_application(visible=True)
root = app.root
root.new_scenario("Phasing_orbit")
scen = Scenario(root.current_scenario)

# configure the target satellite
targetSat = Satellite(scen.children.new(STKObjectType.SATELLITE, "Target"))
targetSat.set_propagator_type(PropagatorType.ASTROGATOR)
tDriver = MCSDriver(targetSat.propagator)
tDriver.options.draw_trajectory_in_3d = False
tInitState = MCSInitialState(tDriver.main_sequence["Initial State"])
tInitState.set_element_type(ElementSetType.KEPLERIAN)
tInitState.initial_state.epoch = scen.start_time
tPropagator = MCSPropagate(tDriver.main_sequence["Propagate"])
tPropagator.propagator_name = "Earth point mass"
tPropagator.properties.color = Colors.Red
tKep = tInitState.element

# configure the chaser satellite
chaserSat = Satellite(scen.children.new(STKObjectType.SATELLITE, "Chaser"))
chaserSat.set_propagator_type(PropagatorType.ASTROGATOR)
cDriver = MCSDriver(chaserSat.propagator)
cDriver.options.draw_trajectory_in_3d = False
cInitState = MCSInitialState(cDriver.main_sequence["Initial State"])
cInitState.set_element_type(ElementSetType.KEPLERIAN)
cInitState.initial_state.epoch = scen.start_time
cPropagator = MCSPropagate(cDriver.main_sequence["Propagate"])
cPropagator.propagator_name = "Earth point mass"
cPropagator.stopping_conditions.add("Periapsis")
cPropagator.stopping_conditions.remove("Duration")
cKep = cInitState.element

root.execute_command("VO */Satellite/Chaser Pass3D OrbitLead None")
root.execute_command("VO */Satellite/Chaser Pass3D OrbitTrail All")
root.execute_command("VO */Satellite/Target Pass3D OrbitLead None")
root.execute_command("VO */Satellite/Target Pass3D OrbitTrail All")
# -

# ### Define the Input Data and Run the Analysis
#
# The cell below defines and runs the MCS for both satellites.
#
# The **phase angle** is the angular displacement between the two satellites at initial time. In this context, it is defined as always positive and between 0 and 360 degrees. To make the rendezvous between the satellites, it has to be reduced to 0 in a specified number of orbits (called **phasing orbits**), so each phase orbit will reduce the angular gap by just a fraction of the overall value.
#
# #### $$ \theta_{gap}=\frac{\theta}{n_{orbits}}$$
#
# , where $\theta$ is the phase angle, and $\theta_{gap}$ is the angular dispacement to recover after each phasing orbit.
#
# In the code below the **Kepler's equation** is used to calculate the period and semimajor axis of the phasing orbit, given the number of revolution around the phasing orbit itself. As first, the **eccentric anomaly E** is calculated from $\theta_{gap}$ :
#
# ####  $$\tan\frac{E}{2} = \sqrt{\frac{1 - e}{1 + e}}\tan\frac{\theta_{gap}}{2}$$
#
# ...and then the period of the phasing orbit is derived:
#
# #### $$  T_{phasing}=\frac{T_{chaser}}{2\pi}\left ( E-e \sin E \right )$$
#
# Having those data available, a differential corrector is configured to let the two satellites be in the same position at the end of the transfer

# +
########################################## INPUT DATA ##########################################################
true_anom = 70  # deg - chaser true anomaly (between 0 and 360)
target_ta = 20  # deg - target true anomaly (between 0 and 360)
nOrbits = 5  # number of phasing orbits
prop_time = 16  # days
################################################################################################################

try:
    root.execute_command(
        'VectorTool * CentralBody/Earth Create Angle Phase "Dihedral Angle"'
    )
    root.execute_command(
        'VectorTool * CentralBody/Earth Modify Angle Phase "Dihedral Angle" "Satellite/Chaser Position" "Satellite/Target Position" "Satellite/Target Orbit_Normal" 0-360 Positive'
    )
    root.execute_command(
        'VO * SetVectorGeometry Add "CentralBody/Earth Phase Angle" Color #fcba03 Show On'
    )
    root.execute_command(
        'VO * SetVectorGeometry Add "Satellite/Target Position Vector"'
    )
    root.execute_command(
        'VO * SetVectorGeometry Modify "Satellite/Target Position Vector" Color red Thickness 5 Show On'
    )
    root.execute_command(
        'VO * SetVectorGeometry Add "Satellite/Chaser Position Vector"'
    )
    root.execute_command(
        'VO * SetVectorGeometry Modify "Satellite/Chaser Position Vector" Color green Thickness 5 Show On'
    )
except:
    print("")


# fixed keplerian parameters (geostationary orbit)
sma = 42164
ecc = 0.0001
inc = 0.0
raan = 0.0

# change the scenario duration
scen.stop_time = "+" + str(prop_time) + " day"
try:
    cDriver.main_sequence.remove("Start Phasing")
    cDriver.main_sequence.remove("Circularization")
except:
    print("")
finally:
    # set the chaser initial state
    cKep.semimajor_axis = sma
    cKep.eccentricity = ecc
    cKep.inclination = inc
    cKep.raan = raan
    cKep.true_anomaly = true_anom
    cKep.arg_of_periapsis = 0.0

    # set the target initial state
    tKep.semimajor_axis = sma
    tKep.eccentricity = ecc
    tKep.inclination = inc
    tKep.raan = raan
    tKep.true_anomaly = target_ta
    tKep.arg_of_periapsis = 0.0

    tPropagator.stopping_conditions["Duration"].properties.trip = prop_time * 86400

    cDriver.run_mcs()
    tDriver.run_mcs()

    # get the mean period and SMA of the initial orbit
    meanKepDp = chaserSat.data_providers["Kozai-Izsak Mean"].group["ICRF"]
    meanKep = meanKepDp.execute(scen.start_time, scen.start_time, 60)
    meanKepDf = meanKep.data_sets.to_pandas_dataframe()
    meanPeriod = float(meanKepDf.at[0, "mean nodal period"])
    meanSma = float(meanKepDf.at[0, "mean semi-major axis"])

    # calculate the phase angle
    phaseAngle = math.radians(target_ta - true_anom)

    if phaseAngle < 0:
        phaseAngle = 2 * math.pi + phaseAngle

    print("#################### Initial geometry #####################")
    print("Phase angle      = " + str(math.degrees(phaseAngle)) + " deg")
    print("")

    # recalculate the phase angle accordingly with the number of phasing orbits
    phaseAngle = phaseAngle / nOrbits

    # calculate the eccentric anomaly
    E = 2 * math.atan(math.sqrt((1 - ecc) / (1 + ecc)) * math.tan(phaseAngle / 2))

    # calculate the time elapsed to cover phase angle in original orbit (Kepler's equation)
    tPhaseAngle = (meanPeriod / (2 * math.pi)) * (E - ecc * math.sin(E))

    # calculate the period of the phasing orbit
    tPhasingOrbit = meanPeriod - tPhaseAngle

    # calculate the SMA of the phasing orbit
    mu = 398600.44
    transferSma = math.pow((tPhasingOrbit * math.sqrt(mu)) / (2 * math.pi), 2 / 3)

    ## calculate eccentricity and radii
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

    # estimate the needed Delta V for phasing
    vPeriInitial = math.sqrt(mu * ((2 / initRadius) - (1 / meanSma)))
    vPeriFinal = math.sqrt(mu * ((2 / initRadius) - (1 / transferSma)))
    deltaV = vPeriFinal - vPeriInitial

    # add the first Target Sequence segment
    ts1 = MCSTargetSequence(
        cDriver.main_sequence.insert(SegmentType.TARGET_SEQUENCE, "Start Phasing", "-")
    )
    ts1.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

    ## add a Maneuver segment
    dv1 = MCSManeuver(ts1.segments.insert(SegmentType.MANEUVER, "DV1", "-"))
    dv1.set_maneuver_type(ManeuverType.IMPULSIVE)
    dv1.enable_control_parameter(
        ControlManeuver.IMPULSIVE_CARTESIAN_X
    )  # control parameter

    #### maneuver attitude definition
    dv1.maneuver.set_attitude_control_type(AttitudeControl.THRUST_VECTOR)
    thrustVector = dv1.maneuver.attitude_control
    thrustVector.thrust_axes_name = "Satellite/Chaser VNC(Earth)"
    thrustVector.x = deltaV * 1000

    ## add a Propagate segment
    phasingOrbit = MCSPropagate(
        ts1.segments.insert(SegmentType.PROPAGATE, "Phasing Orbit", "-")
    )
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

    # customize the Differential Corrector
    dc1 = ProfileDifferentialCorrector(ts1.profiles["Differential Corrector"])
    dc1.mode = ProfileMode.ITERATE
    dc1.max_iterations = 50

    # set Control Parameters and Results
    xControlParam1 = dc1.control_parameters.get_control_by_paths(
        "DV1", "ImpulsiveMnvr.Cartesian.X"
    )
    xControlParam1.enable = True
    xControlParam1.max_step = 0.001

    roaResult = dc1.results.get_result_by_paths(
        "Phasing Orbit", "Angle_Between_Vectors"
    )
    roaResult.enable = True
    roaResult.desired_value = 0.0
    roaResult.tolerance = 0.1

    # add the second Target Sequence segment
    ts2 = MCSTargetSequence(
        cDriver.main_sequence.insert(
            SegmentType.TARGET_SEQUENCE, "Circularization", "-"
        )
    )
    ts2.action = TargetSequenceAction.RUN_ACTIVE_PROFILES

    ## add a Maneuver segment
    dv2 = MCSManeuver(ts2.segments.insert(SegmentType.MANEUVER, "DV2", "-"))
    dv2.set_maneuver_type(ManeuverType.IMPULSIVE)
    dv2.enable_control_parameter(
        ControlManeuver.IMPULSIVE_CARTESIAN_X
    )  # control parameter

    ## add a Propagate segment
    finalOrbit = MCSPropagate(
        ts2.segments.insert(SegmentType.PROPAGATE, "Final Orbit", "-")
    )
    finalOrbit.properties.color = Colors.Yellow
    finalOrbit.propagator_name = "Earth point mass"
    finalOrbit.stopping_conditions["Duration"].properties.trip = 86400
    finalOrbit.results.add("Keplerian Elems/Eccentricity")

    # customize the Differential Corrector
    dc2 = ProfileDifferentialCorrector(ts2.profiles["Differential Corrector"])
    dc2.mode = ProfileMode.ITERATE
    dc2.max_iterations = 50

    # set Control Parameters and Results
    xControlParam2 = dc2.control_parameters.get_control_by_paths(
        "DV2", "ImpulsiveMnvr.Cartesian.X"
    )
    xControlParam2.enable = True
    xControlParam2.max_step = 0.01

    roaResult = dc2.results.get_result_by_paths("Final Orbit", "Eccentricity")
    roaResult.enable = True
    roaResult.desired_value = 0.0001
    roaResult.tolerance = 0.00001
    cDriver.run_mcs()
    tDriver.run_mcs()
    root.rewind()

    # get the maneuver data providers
    manDp = chaserSat.data_providers["Maneuver Summary"]
    man = manDp.execute(scen.start_time, scen.stop_time)
    manDf = man.data_sets.to_pandas_dataframe()
    deltaV = manDf.at[0, "delta v"]

    # change orbit system
    try:
        root.execute_command(
            'VO */Satellite/Chaser OrbitSystem Modify System "InertialByWindow" Show Off'
        )
        root.execute_command(
            'VO */Satellite/Chaser OrbitSystem Add System "Satellite/Target Body"'
        )
        root.execute_command(
            'VO */Satellite/Chaser OrbitSystem Modify System "TargetBody" Show On'
        )
    except:
        print("")
    finally:
        print("################### Transfer orbit data ###################")
        print("N phasing orbits = " + str(nOrbits))
        print("Period           = " + str(tPhasingOrbit) + " sec")
        print("SMA              = " + str(transferSma) + " km")
        print("Perigee radius   = " + str(periRadius) + " km")
        print("Apogee radius    = " + str(apoRadius) + " km")
        print("Delta V          = " + str(deltaV) + " m/sec")
        print("Transfer time    = " + str(tPhasingOrbit * nOrbits / 86400) + " days")
# -
