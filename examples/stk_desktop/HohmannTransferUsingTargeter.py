import os

try:
    if os.name == "nt":
        from ansys.stk.core.stkdesktop import STKDesktop
    from ansys.stk.core.stkobjects import *
    from ansys.stk.core.stkobjects.astrogator import *
    from ansys.stk.core.utilities.colors import *
except:
    print("Failed to import stk modules. Make sure you have installed the STK Python API wheel (agi.stk<..ver..>-py3-none-any.whl) from the STK Install bin directory")

if os.name == "nt":
    app = STKDesktop.start_application(visible=True, userControl=True)
    stkRoot = app.root
else:
    print("Automation samples only work on windows with the desktop application, see Custom Applications for STK Engine examples.")
    quit()

if not stkRoot.available_features.is_propagator_type_available(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR):
    print("You do not have the required license.")
    
#part 1
print("New Scenario...")
stkRoot.new_scenario("HohmannTransfer")
sat1 = stkRoot.current_scenario.children.new(STK_OBJECT_TYPE.eSatellite, "Satellite1")
sat1.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
_driver = sat1.Propagator
_driver.MainSequence.RemoveAll()
_driver.Options.DrawTrajectoryIn3D = True
input("Press enter to continue...")

#part 2
print("Define the Initial State...")
initState = _driver.MainSequence.Insert(SEGMENT_TYPE.INITIAL_STATE, "Inner Orbit", "-")
initState.SetElementType(ELEMENT_TYPE.KEPLERIAN)
modKep = initState.Element
modKep.PeriapsisRadiusSize = 6700
modKep.ArgOfPeriapsis = 0
modKep.Eccentricity = 0
modKep.Inclination = 0
modKep.RAAN = 0
modKep.TrueAnomaly = 0
input("Press enter to continue...")

#part 3
print("Propagate the Parking Orbit...")
propagate = _driver.MainSequence.Insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
propagate.PropagatorName = "Earth Point Mass"
propagate.Properties.Color = Colors.Blue
propagate.StoppingConditions["Duration"].Properties.Trip = 7200
input("Press enter to continue...")

#part 4
print("Target Sequence containing Maneuver into the Transfer Ellipse...")
ts = _driver.MainSequence.Insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Start Transfer", "-")
dv1 = ts.Segments.Insert(SEGMENT_TYPE.MANEUVER, "DV1", "-")
dv1.SetManeuverType(MANEUVER_TYPE.IMPULSIVE)
impulsive = dv1.Maneuver
impulsive.SetAttitudeControlType(ATTITUDE_CONTROL.THRUST_VECTOR)
thrustVector = impulsive.AttitudeControl
thrustVector.ThrustAxesName = "Satellite/Satellite1 VNC(Earth)"
dv1.EnableControlParameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
dv1.Results.Add("Keplerian Elems/Radius of Apoapsis")
dc = ts.Profiles["Differential Corrector"]
xControlParam = dc.ControlParameters.GetControlByPaths("DV1", "ImpulsiveMnvr.Cartesian.X")
xControlParam.Enable = True
xControlParam.MaxStep = 0.3
roaResult = dc.Results.GetResultByPaths("DV1", "Radius Of Apoapsis")
roaResult.Enable = True
roaResult.DesiredValue = 42238
roaResult.Tolerance = 0.1
dc.MaxIterations = 50
dc.EnableDisplayStatus = True
dc.Mode = PROFILE_MODE.ITERATE
ts.Action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
input("Press enter to continue...")

#part 5
print("Propagate the Transfer Orbit to Apogee...")
transferEllipse = _driver.MainSequence.Insert(SEGMENT_TYPE.PROPAGATE, "Transfer Ellipse", "-")
transferEllipse.Properties.Color = Colors.Red
transferEllipse.PropagatorName = "Earth Point Mass"
transferEllipse.StoppingConditions.Add("Apoapsis")
transferEllipse.StoppingConditions.Remove("Duration")
input("Press enter to continue...")

#part 6
print("Target Sequence containing Maneuver into the Outer Orbit...")
ts = _driver.MainSequence.Insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Finish Transfer", "-")
dv2 = ts.Segments.Insert(SEGMENT_TYPE.MANEUVER, "DV2", "-")
dv2.SetManeuverType(MANEUVER_TYPE.IMPULSIVE)
impulsive = dv2.Maneuver
impulsive.SetAttitudeControlType(ATTITUDE_CONTROL.THRUST_VECTOR)
thrustVector = impulsive.AttitudeControl
thrustVector.ThrustAxesName = "Satellite/Satellite1 VNC(Earth)"
dv2.EnableControlParameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
dv2.Results.Add("Keplerian Elems/Eccentricity")
dc = ts.Profiles["Differential Corrector"]
xControlParam2 = dc.ControlParameters.GetControlByPaths("DV2", "ImpulsiveMnvr.Cartesian.X")
xControlParam2.Enable = True
xControlParam2.MaxStep = 0.3
eccResult = dc.Results.GetResultByPaths("DV2", "Eccentricity")
eccResult.Enable = True
eccResult.DesiredValue = 0
dc.EnableDisplayStatus = True
dc.Mode = PROFILE_MODE.ITERATE
ts.Action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
input("Press enter to continue...")

#part 7
print("Propagate the Outer Orbit...")
outerOrbit = _driver.MainSequence.Insert(SEGMENT_TYPE.PROPAGATE, "Outer Orbit", "-")
outerOrbit.Properties.Color = Colors.Green;
outerOrbit.PropagatorName = "Earth Point Mass"
outerOrbit.StoppingConditions["Duration"].Properties.Trip = 86400
input("Press enter to continue...")

#part 8
print("Run MCS...")
_driver.RunMCS()
startTransfer = _driver.MainSequence["Start Transfer"]
finishTransfer = _driver.MainSequence["Finish Transfer"]
startDC = startTransfer.Profiles["Differential Corrector"]
finishDC = finishTransfer.Profiles["Differential Corrector"]
dv1 = startTransfer.Segments["DV1"]
dv1Impulsive = dv1.Maneuver
dv1ThrustVector = dv1Impulsive.AttitudeControl
startTransfer.ApplyProfiles()
dv2 = finishTransfer.Segments["DV2"]
dv2Impulsive = dv2.Maneuver
dv2ThrustVector = dv2Impulsive.AttitudeControl
finishTransfer.ApplyProfiles()
input("Press enter to continue...")

#part 9
print("Print Results...")
reportData = ""
outerOrbit = _driver.MainSequence["Outer Orbit"]
result = outerOrbit.ExecSummary
print(result.Category)
intervals = result.Value
for i in range(0, intervals.Count):
    interval = intervals.Item(i)
    datasets = interval.DataSets
    for j in range(0, datasets.Count):
        dataset = datasets.Item(j)
        print("Title - " + dataset.ElementName)
        elements = dataset.GetValues()
        for o in elements:
            reportData += o + "\r\n";
print(reportData)
print("Finished...")
input("Press enter to close the application...")

#close scenario
stkRoot.close_scenario()
app.shutdown()