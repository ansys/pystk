"""Demonstrates how to use Hohmann Transfer using Targeter with STK Engine."""

import os
import tkinter as tk

from ansys.stk.core.stkengine import STKEngine
from ansys.stk.core.stkengine.tkcontrols import GlobeControl
from ansys.stk.core.stkobjects import (
    STK_OBJECT_TYPE,
    VEHICLE_PROPAGATOR_TYPE,
)
from ansys.stk.core.utilities.colors import Color, Colors
from ansys.stk.core.stkobjects.astrogator import (
    ATTITUDE_CONTROL,
    CONTROL_MANEUVER,
    ELEMENT_TYPE,
    MANEUVER_TYPE,
    PROFILE_MODE,
    SEGMENT_TYPE,
    TARGET_SEQ_ACTION,
)

"""ffrom ansys.stk.core.stkobjects import *
rom ansys.stk.core.stkutil import *
from ansys.stk.core.stkobjects.astrogator import *
from ansys.stk.core.utilities.colors import *"""


class HohmannTransferUsingTargeter:
    """Demonstrates how to use Hohmann Transfer using Targeter with STK Engine."""

    def __init__(self):
        """Create a new instance and initialize the user interface."""
        self.stk = STKEngine.StartApplication(noGraphics=False)
        self.root = self.stk.NewObjectRoot()
        self.window = tk.Tk()
        self.window.title("Hohmann Transfer Using Targeter")
        self.window.protocol("WM_DELETE_WINDOW", self._exit)
        self.controlFrame = tk.Frame()
        self.globeControl = GlobeControl(self.controlFrame, width=800, height=600)
        self.globeControl.back_color = Color.FromRGB(217, 217, 217)
        self.globeControl.pack(fill=tk.BOTH, expand=tk.YES)
        self.controlFrame.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT)
        self.buttonFrame = tk.Frame()
        self.newScenarioBtn = tk.Button(self.buttonFrame, text="New Scenario", width=15, command=self._new_scenario)
        self.newScenarioBtn.pack(side=tk.TOP, pady=6)
        self.initialStateBtn = tk.Button(
            self.buttonFrame, text="Define the Initial State", width=15, wraplength=100, command=self._initial_state
        )
        self.initialStateBtn.pack(side=tk.TOP, pady=6)
        self.initialStateBtn["state"] = "disabled"
        self.parkingOrbitBtn = tk.Button(
            self.buttonFrame, text="Propagate the Parking Orbit", width=15, wraplength=100, command=self._parking_orbit
        )
        self.parkingOrbitBtn.pack(side=tk.TOP, pady=6)
        self.parkingOrbitBtn["state"] = "disabled"
        self.targetSequenceBtn = tk.Button(
            self.buttonFrame,
            text="Target Sequence containing Maneuver into the Transfer Ellipse",
            width=15,
            wraplength=100,
            command=self._target_sequence,
        )
        self.targetSequenceBtn.pack(side=tk.TOP, pady=6)
        self.targetSequenceBtn["state"] = "disabled"
        self.transferOrbitBtn = tk.Button(
            self.buttonFrame,
            text="Propagate the Transfer Orbit to Apogee",
            width=15,
            wraplength=100,
            command=self._transfer_orbit,
        )
        self.transferOrbitBtn.pack(side=tk.TOP, pady=6)
        self.transferOrbitBtn["state"] = "disabled"
        self.outerOrbitBtn = tk.Button(
            self.buttonFrame,
            text="Target Sequence containing Maneuver into the Outer Orbit",
            width=15,
            wraplength=100,
            command=self._ts_outer_orbit,
        )
        self.outerOrbitBtn.pack(side=tk.TOP, pady=6)
        self.outerOrbitBtn["state"] = "disabled"
        self.propagateOuterBtn = tk.Button(
            self.buttonFrame, text="Propagate the Outer Orbit", width=15, wraplength=100, command=self._propagate_outer
        )
        self.propagateOuterBtn.pack(side=tk.TOP, pady=6)
        self.propagateOuterBtn["state"] = "disabled"
        self.runMCSBtn = tk.Button(self.buttonFrame, text="Run MCS", width=15, command=self._run_mcs)
        self.runMCSBtn.pack(side=tk.TOP, pady=6)
        self.runMCSBtn["state"] = "disabled"
        self.displayResultsBtn = tk.Button(
            self.buttonFrame, text="Display Results", width=15, command=self._display_results
        )
        self.displayResultsBtn.pack(side=tk.TOP, pady=6)
        self.displayResultsBtn["state"] = "disabled"
        self.buttonFrame.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, padx=10)

    def _run(self):
        self.window.mainloop()

    def _exit(self):
        self.root.close_scenario()
        self.window.destroy()
        self.stk.ShutDown()

    def _new_scenario(self):
        self.root.new_scenario("HohmannTransfer")
        sat1 = self.root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1")
        sat1.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
        self._driver = sat1.Propagator
        self._driver.MainSequence.RemoveAll()
        self._driver.Options.DrawTrajectoryIn3D = True
        self.newScenarioBtn["state"] = "disabled"
        self.initialStateBtn["state"] = "normal"

    def _initial_state(self):
        initState = self._driver.MainSequence.Insert(SEGMENT_TYPE.INITIAL_STATE, "Inner Orbit", "-")
        initState.SetElementType(ELEMENT_TYPE.KEPLERIAN)
        modKep = initState.Element
        modKep.PeriapsisRadiusSize = 6700
        modKep.ArgOfPeriapsis = 0
        modKep.Eccentricity = 0
        modKep.Inclination = 0
        modKep.RAAN = 0
        modKep.TrueAnomaly = 0
        self.initialStateBtn["state"] = "disabled"
        self.parkingOrbitBtn["state"] = "normal"

    def _parking_orbit(self):
        propagate = self._driver.MainSequence.Insert(SEGMENT_TYPE.PROPAGATE, "Propagate", "-")
        propagate.PropagatorName = "Earth Point Mass"
        propagate.Properties.Color = Colors.Blue
        propagate.StoppingConditions["Duration"].Properties.Trip = 7200
        self.parkingOrbitBtn["state"] = "disabled"
        self.targetSequenceBtn["state"] = "normal"

    def _target_sequence(self):
        ts = self._driver.MainSequence.Insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Start Transfer", "-")
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
        self.targetSequenceBtn["state"] = "disabled"
        self.transferOrbitBtn["state"] = "normal"

    def _transfer_orbit(self):
        transferEllipse = self._driver.MainSequence.Insert(
            SEGMENT_TYPE.PROPAGATE, "Transfer Ellipse", "-"
        )
        transferEllipse.Properties.Color = Colors.Red
        transferEllipse.PropagatorName = "Earth Point Mass"
        transferEllipse.StoppingConditions.Add("Apoapsis")
        transferEllipse.StoppingConditions.Remove("Duration")
        self.transferOrbitBtn["state"] = "disabled"
        self.outerOrbitBtn["state"] = "normal"

    def _ts_outer_orbit(self):
        ts2 = self._driver.MainSequence.Insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Finish Transfer", "-")
        dv2 = ts2.Segments.Insert(SEGMENT_TYPE.MANEUVER, "DV2", "-")
        dv2.SetManeuverType(MANEUVER_TYPE.IMPULSIVE)
        impulsive2 = dv2.Maneuver
        impulsive2.SetAttitudeControlType(ATTITUDE_CONTROL.THRUST_VECTOR)
        thrustVector2 = impulsive2.AttitudeControl
        thrustVector2.ThrustAxesName = "Satellite/Satellite1 VNC(Earth)"
        dv2.EnableControlParameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
        dv2.Results.Add("Keplerian Elems/Eccentricity")
        dc2 = ts2.Profiles["Differential Corrector"]
        xControlParam2 = dc2.ControlParameters.GetControlByPaths("DV2", "ImpulsiveMnvr.Cartesian.X")
        xControlParam2.Enable = True
        xControlParam2.MaxStep = 0.3
        eccResult = dc2.Results.GetResultByPaths("DV2", "Eccentricity")
        eccResult.Enable = True
        eccResult.DesiredValue = 0
        dc2.EnableDisplayStatus = True
        dc2.Mode = PROFILE_MODE.ITERATE
        ts2.Action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES
        self.outerOrbitBtn["state"] = "disabled"
        self.propagateOuterBtn["state"] = "normal"

    def _propagate_outer(self):
        outerOrbit = self._driver.MainSequence.Insert(SEGMENT_TYPE.PROPAGATE, "Outer Orbit", "-")
        outerOrbit.Properties.Color = Colors.Green
        outerOrbit.PropagatorName = "Earth Point Mass"
        outerOrbit.StoppingConditions["Duration"].Properties.Trip = 86400
        self.propagateOuterBtn["state"] = "disabled"
        self.runMCSBtn["state"] = "normal"

    def _run_mcs(self):
        self._driver.RunMCS()
        startTransfer = self._driver.MainSequence["Start Transfer"]
        finishTransfer = self._driver.MainSequence["Finish Transfer"]
        startDC = startTransfer.Profiles["Differential Corrector"]
        print(startDC.ControlParameters.GetControlByPaths("DV1", "ImpulsiveMnvr.Cartesian.X").FinalValue)
        finishDC = finishTransfer.Profiles["Differential Corrector"]
        print(finishDC.ControlParameters.GetControlByPaths("DV2", "ImpulsiveMnvr.Cartesian.X").FinalValue)
        dv1 = startTransfer.Segments["DV1"]
        dv1Impulsive = dv1.Maneuver
        dv1ThrustVector = dv1Impulsive.AttitudeControl
        print(dv1ThrustVector.X)
        startTransfer.ApplyProfiles()
        print(dv1ThrustVector.X)

        dv2 = finishTransfer.Segments["DV2"]
        dv2Impulsive = dv2.Maneuver
        dv2ThrustVector = dv2Impulsive.AttitudeControl
        print(dv2ThrustVector.X)
        finishTransfer.ApplyProfiles()
        print(dv2ThrustVector.X)
        self.runMCSBtn["state"] = "disabled"
        self.displayResultsBtn["state"] = "normal"

    def _display_results(self):
        self.reportWindow = tk.Toplevel(self.window)
        self.reportWindow.title("Astrogator MCS Segment Summary")
        self.reportText = tk.Text(self.reportWindow)
        self.reportData = ""
        outerOrbit = self._driver.MainSequence["Outer Orbit"]
        result = outerOrbit.ExecSummary
        intervals = result.Value
        for interval in intervals:
            datasets = interval.DataSets
            for dataset in datasets:
                for obj in dataset.GetValues():
                    self.reportData += obj + os.linesep
        self.reportText.insert("0.0", self.reportData)
        self.reportText.pack(fill=tk.BOTH, expand=tk.YES)
        self.reportText["state"] = "disabled"
        self.reportWindow.update()


if __name__ == "__main__":
    hohmannTransferUsingTargeter = HohmannTransferUsingTargeter()
    hohmannTransferUsingTargeter._run()
