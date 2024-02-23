"""Demonstrates how to use VGT using STK Engine."""

import math
import os
import tkinter as tk

from ansys.stk.core.stkengine import STKEngine
from ansys.stk.core.stkengine.tkcontrols import GlobeControl
from ansys.stk.core.stkobjects import (
    VECTOR_GEOMETRY_TOOL_ANGLE_TYPE,
    VECTOR_GEOMETRY_TOOL_PLANE_TYPE,
    VECTOR_GEOMETRY_TOOL_POINT_TYPE,
    VECTOR_GEOMETRY_TOOL_VECTOR_TYPE,
    GEOMETRIC_ELEM_TYPE,
    STK_OBJECT_TYPE,
    VEHICLE_PROPAGATOR_TYPE,
)
from ansys.stk.core.utilities.colors import Color, Colors


class VGTTutorial:
    """Demonstrates how to use VGT using STK Engine."""

    def __init__(self):
        """Create a new instance and initialize the user interface."""
        self.stk = STKEngine.start_application(noGraphics=False)
        self.stkRoot = self.stk.new_object_root()
        self._satellite = None
        self.OnAnimUpdateSubscription = self.stkRoot.Subscribe()
        self.OnAnimUpdateSubscription.on_anim_update += self._on_anim_update
        self.window = tk.Tk()
        self.window.title("VGT Tutorial")
        self.window.protocol("WM_DELETE_WINDOW", self._exit)
        self.animationBtnFrame = tk.Frame(self.window)
        working_dir = os.path.dirname(os.path.realpath(__file__))
        self.resetImage = tk.PhotoImage(
            file=os.path.join(
                working_dir,
                "..",
                "..",
                "SharedResources",
                "Icons",
                "reset.gif",
            )
        )
        self.resetBtn = tk.Button(
            self.animationBtnFrame,
            image=self.resetImage,
            width=22,
            height=22,
            command=self.stkRoot.rewind,
        )
        self.resetBtn.pack(side=tk.LEFT)
        self.stepBackImage = tk.PhotoImage(
            file=os.path.join(
                working_dir,
                "..",
                "..",
                "SharedResources",
                "Icons",
                "stepbak.gif",
            )
        )
        self.stepBackBtn = tk.Button(
            self.animationBtnFrame,
            image=self.stepBackImage,
            width=22,
            height=22,
            command=self.stkRoot.step_backward,
        )
        self.stepBackBtn.pack(side=tk.LEFT)
        self.playReverseImage = tk.PhotoImage(
            file=os.path.join(
                working_dir,
                "..",
                "..",
                "SharedResources",
                "Icons",
                "playbak.GIF",
            )
        )
        self.playReverseBtn = tk.Button(
            self.animationBtnFrame,
            image=self.playReverseImage,
            width=22,
            height=22,
            command=self.stkRoot.play_backward,
        )
        self.playReverseBtn.pack(side=tk.LEFT)
        self.pauseImage = tk.PhotoImage(
            file=os.path.join(
                working_dir,
                "..",
                "..",
                "SharedResources",
                "Icons",
                "pause.gif",
            )
        )
        self.pauseBtn = tk.Button(
            self.animationBtnFrame,
            image=self.pauseImage,
            width=22,
            height=22,
            command=self.stkRoot.pause,
        )
        self.pauseBtn.pack(side=tk.LEFT)
        self.playImage = tk.PhotoImage(
            file=os.path.join(working_dir, "..", "..", "SharedResources", "Icons", "play.gif")
        )
        self.playBtn = tk.Button(
            self.animationBtnFrame,
            image=self.playImage,
            width=22,
            height=22,
            command=self.stkRoot.play_forward,
        )
        self.playBtn.pack(side=tk.LEFT)
        self.stepForwardImage = tk.PhotoImage(
            file=os.path.join(working_dir, "..", "..", "SharedResources", "Icons", "step.gif")
        )
        self.stepForwardBtn = tk.Button(
            self.animationBtnFrame,
            image=self.stepForwardImage,
            width=22,
            height=22,
            command=self.stkRoot.step_forward,
        )
        self.stepForwardBtn.pack(side=tk.LEFT)
        self.decreaseSpeedImage = tk.PhotoImage(
            file=os.path.join(
                working_dir,
                "..",
                "..",
                "SharedResources",
                "Icons",
                "slowdown.gif",
            )
        )
        self.decreaseSpeedBtn = tk.Button(
            self.animationBtnFrame,
            image=self.decreaseSpeedImage,
            width=22,
            height=22,
            command=self.stkRoot.slower,
        )
        self.decreaseSpeedBtn.pack(side=tk.LEFT)
        self.increaseSpeedImage = tk.PhotoImage(
            file=os.path.join(
                working_dir,
                "..",
                "..",
                "SharedResources",
                "Icons",
                "speedup.gif",
            )
        )
        self.increaseSpeedBtn = tk.Button(
            self.animationBtnFrame,
            image=self.increaseSpeedImage,
            width=22,
            height=22,
            command=self.stkRoot.faster,
        )
        self.increaseSpeedBtn.pack(side=tk.LEFT)
        self.animationBtnFrame.pack(side=tk.TOP, anchor=tk.W)
        self.globeControl = GlobeControl(self.window, width=873, height=429)
        self.globeControl.back_color = Color.from_rgb(217, 217, 217)
        self.globeControl.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
        self.lowerFrame = tk.Frame(self.window, width=873)
        self.descriptionFrame = tk.LabelFrame(self.lowerFrame, text="Description")
        self.informationFrame = tk.LabelFrame(self.lowerFrame, text="Information")
        self.descriptionLabel = tk.Label(
            self.descriptionFrame,
            anchor=tk.N,
            text='Welcome to AGI\'s tutorial for VGT. In this tutorial,\
                 we will show the basics of VGT (Vector Geometry Tool). \
                 Please click "New Scenario" to get started.',
            justify=tk.LEFT,
            wraplength=250,
        )

        self.descriptionLabel = tk.Label(
            self.descriptionFrame,
            anchor=tk.N,
            text="Welcome to AGI's tutorial for VGT. "
            + "In this tutorial, we will "
            + "show the basics of VGT "
            + "(Vector Geometry Tool). Please "
            + 'click "New Scenario" to get started.',
            justify=tk.LEFT,
            wraplength=250,
        )

        self.distanceEntry = tk.Entry(self.informationFrame)
        self.distanceEntry.pack(side=tk.TOP, fill=tk.X, padx=8)
        self.distanceEntry["state"] = "disabled"
        self.informationFrame.grid(row=0, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
        self.actionFrame = tk.LabelFrame(self.lowerFrame, text="Actions")
        self.newScenarioBtn = tk.Button(
            self.actionFrame,
            text="New Scenario",
            width=16,
            command=self._new_scenario,
        )
        self.newScenarioBtn.grid(padx=2, pady=2)
        self.createSatBtn = tk.Button(
            self.actionFrame,
            text="Create Satellite",
            width=16,
            command=self._create_satellite,
        )
        self.createSatBtn.grid(row=1, padx=2, pady=2)
        self.createSatBtn["state"] = "disabled"
        self.createVectorBtn = tk.Button(
            self.actionFrame,
            text="Create Vector",
            width=16,
            command=self._create_vector,
        )
        self.createVectorBtn.grid(row=2, padx=2, pady=2)
        self.createVectorBtn["state"] = "disabled"
        self.showVelocityBtn = tk.Button(
            self.actionFrame,
            text="Show Velocity Vector",
            width=16,
            command=self._show_velocity,
        )
        self.showVelocityBtn.grid(row=3, padx=2, pady=2)
        self.showVelocityBtn["state"] = "disabled"
        self.createAxesBtn = tk.Button(
            self.actionFrame,
            text="Create Axes",
            width=16,
            command=self._create_axes,
        )
        self.createAxesBtn.grid(row=0, column=1, padx=2, pady=2)
        self.createAxesBtn["state"] = "disabled"
        self.createPlaneBtn = tk.Button(
            self.actionFrame,
            text="Create Plane",
            width=16,
            command=self._create_Plane,
        )
        self.createPlaneBtn.grid(row=1, column=1, padx=2, pady=2)
        self.createPlaneBtn["state"] = "disabled"
        self.createAngleBtn = tk.Button(
            self.actionFrame,
            text="Create Angle",
            width=16,
            command=self._create_angle,
        )
        self.createAngleBtn.grid(row=2, column=1, padx=2, pady=2)
        self.createAngleBtn["state"] = "disabled"
        self.exitBtn = tk.Button(self.actionFrame, text="Exit", width=16, command=self._exit)
        self.exitBtn.grid(row=3, column=1, padx=2, pady=2)
        self.exitBtn["state"] = "disabled"
        self.actionFrame.grid(row=0, column=2, sticky=tk.N + tk.E + tk.S + tk.W)
        self.lowerFrame.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

    def _run(self):
        self.window.mainloop()

    def _exit(self):
        self.stkRoot.close_scenario()
        self.window.destroy()
        self.stk.shutdown()

    def _new_scenario(self):
        self.descriptionLabel[
            "text"
        ] = 'Now that we have loaded our control, \
                                        we will create a satellite and \
                                        facility for our demonstration.  \
                                        Please click "Create Satellite".'

        self.stkRoot.new_scenario("VGTTutorial")
        self.stkRoot.unit_preferences.set_current_unit("TimeUnit", "sec")
        self.stkRoot.unit_preferences.set_current_unit("DateFormat", "EpSec")
        scenario = self.stkRoot.current_scenario
        scenario.Animation.AnimStepValue = 5

        self.createSatBtn["state"] = "normal"
        self.newScenarioBtn["state"] = "disabled"

    def _create_satellite(self):
        self.descriptionLabel[
            "text"
        ] = 'We have created a satellite and \
                                        facility.  Let\'s demonstrate the \
                                        vector geometry tool\'s ability to \
                                        display vectors and calculations \
                                        regarding STK objects.  We will \
                                        display the distance to the facility\
                                        in "km".  Click "Create Vector" \
                                        to create a Displacement vector to \
                                        accessFac.  The magnitude \
                                        (or distance) will be displayed.'

        self._satellite = self.stkRoot.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "AGILE_31135")
        self._satellite.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
        prop = self._satellite.Propagator
        prop.Step = 10
        prop.Propagate()

        self._facility = self.stkRoot.current_scenario.children.new(STK_OBJECT_TYPE.FACILITY, "accessFac")
        self._facility.Graphics.LabelVisible = True
        self._facility.VO.Model.Visible = True

        self._satellite = self.stkRoot.current_scenario.children["AGILE_31135"]
        self._satellite.VO.Vector.VectorSizeScale = 1.3
        self._satellite.VO.Vector.AngleSizeScale = 1

        provider = self._satellite.vgt
        viewPoint = provider.points.factory.create(
            "ViewPoint",
            "View sat from this point",
            VECTOR_GEOMETRY_TOOL_POINT_TYPE.FIXED_IN_SYSTEM,
        )
        viewPoint.FixedPoint.AssignCartesian(0.09, -0.1, -0.025)

        self.createVectorBtn["state"] = "normal"
        self.createSatBtn["state"] = "disabled"

        self._zoom_to()

    def _zoom_to(self):
        viewPoint = self._satellite.vgt.points["ViewPoint"]
        zoomCmd = 'VO * View FromTo FromRegName "STK Object" \
                   FromName "{1}" ToRegName "STK Object" \
                   ToName "{0}"'.format(
            "{0}/{1}".format(self._satellite.class_name, self._satellite.instance_name),
            viewPoint.QualifiedPath,
        )
        self.stkRoot.execute_command(zoomCmd)

    def _create_vector(self):
        self.descriptionLabel[
            "text"
        ] = 'We have created a vector from the \
                                         center of the our Satellite to \
                                         accessFac.  Let\'s display the \
                                         velocity vector that comes as a \
                                         standard template to VGT satellite \
                                         objects. Click \
                                         "Show Velocity Vector".'

        provider = self._satellite.vgt
        self.stkRoot.begin_update()
        try:
            vDisplacement = provider.vectors.factory.create(
                "accessFac",
                "Vector to facility",
                VECTOR_GEOMETRY_TOOL_VECTOR_TYPE.DISPLACEMENT,
            )
            vDisplacement.Origin.SetPoint(provider.points["Center"])
            vDisplacement.Destination.SetPoint(self._facility.vgt.points["Center"])
            vDisplacement.Apparent = True

            self._satellite.VO.Vector.RefCrdns.Add(GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, vDisplacement.QualifiedPath)
            voVectorToFac = self._satellite.VO.Vector.RefCrdns.GetCrdnByName(
                GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, vDisplacement.QualifiedPath
            )
            voVectorToFac.MagnitudeVisible = True
            voVectorToFac.LabelVisible = True
            voVectorToFac.Color = Colors.AliceBlue
        finally:
            self.stkRoot.end_update()

        self.showVelocityBtn["state"] = "normal"
        self.createVectorBtn["state"] = "disabled"

    def _show_velocity(self):
        self.descriptionLabel[
            "text"
        ] = 'VGT can provide user defined\
                                        "Templates".  Once a template is \
                                        defined (such as our Velocity Vector) \
                                        every object of the same type created \
                                        after it will contain the same vector\
                                        , plane, point, axes, angle, or \
                                        system.  Click "Create Axes" \
                                        to show a predefined Axes.'

        provider = self._satellite.vgt
        path = provider.vectors["Velocity"].QualifiedPath
        self.stkRoot.begin_update()
        try:
            voVelocity = self._satellite.VO.Vector.RefCrdns.GetCrdnByName(GEOMETRIC_ELEM_TYPE.VECTOR_ELEM, path)
            voVelocity.Visible = True
            voVelocity.MagnitudeVisible = True
            voVelocity.LabelVisible = True
        finally:
            self.stkRoot.end_update()

        self.createAxesBtn["state"] = "normal"
        self.showVelocityBtn["state"] = "disabled"

    def _create_axes(self):
        self.descriptionLabel[
            "text"
        ] = 'Here we have displayed the "Body" \
                                         Axes to demonstrate Axes.  Axes can \
                                         be based on vectors, central bodies, \
                                         axes, points, and a variety of other \
                                         components.  Please click \
                                         "Create Plane".'

        provider = self._satellite.vgt
        path = provider.axes["ICR"].QualifiedPath
        self.stkRoot.begin_update()
        try:
            self._satellite.VO.Vector.RefCrdns.Add(GEOMETRIC_ELEM_TYPE.AXES_ELEM, path)
            voAxes = self._satellite.VO.Vector.RefCrdns.GetCrdnByName(GEOMETRIC_ELEM_TYPE.AXES_ELEM, path)
            voAxes.Visible = True
            voAxes.Color = Colors.Tomato

            self._satellite.VO.Vector.RefCrdns.GetCrdnByName(
                GEOMETRIC_ELEM_TYPE.VECTOR_ELEM,
                provider.vectors["Velocity"].QualifiedPath,
            ).Visible = False
        finally:
            self.stkRoot.end_update()

        self.createPlaneBtn["state"] = "normal"
        self.createAxesBtn["state"] = "disabled"

    def _create_Plane(self):
        self.descriptionLabel[
            "text"
        ] = "We have created a plane normal to \
                                        the satellite's velocity vector, with \
                                        the satellite's center point as the \
                                        start location and a displacement \
                                        vector to Earth as a reference.  \
                                        Click \"Create Angle\" in order to \
                                        display the angles between the VGT \
                                        components we have displayed thus far."

        provider = self._satellite.vgt
        self.stkRoot.begin_update()
        try:
            plane = provider.planes.factory.create(
                "NormalPlane",
                "Normal to Velocity vector.",
                VECTOR_GEOMETRY_TOOL_PLANE_TYPE.NORMAL,
            )
            plane.NormalVector.SetVector(provider.vectors["Velocity"])
            plane.ReferenceVector.SetVector(provider.vectors["Earth"])
            plane.ReferencePoint.SetPoint(provider.points["Center"])

            path = provider.planes["NormalPlane"].QualifiedPath
            self._satellite.VO.Vector.RefCrdns.Add(GEOMETRIC_ELEM_TYPE.PLANE_ELEM, path)
            voPlane = self._satellite.VO.Vector.RefCrdns.GetCrdnByName(GEOMETRIC_ELEM_TYPE.PLANE_ELEM, path)
            voPlane.TransparentPlaneVisible = True
            voPlane.Color = Colors.Yellow
            voPlane.AxisLabelsVisible = True

            pathXY = provider.planes["BodyXY"].QualifiedPath
            voPlaneBodyXY = self._satellite.VO.Vector.RefCrdns.GetCrdnByName(GEOMETRIC_ELEM_TYPE.PLANE_ELEM, pathXY)
            voPlaneBodyXY.Visible = True
            voPlaneBodyXY.TransparentPlaneVisible = True
            voPlaneBodyXY.Color = Colors.Yellow
            voPlaneBodyXY.AxisLabelsVisible = True

            path = provider.axes["ICR"].QualifiedPath
            axes = self._satellite.VO.Vector.RefCrdns.GetCrdnByName(GEOMETRIC_ELEM_TYPE.AXES_ELEM, path)
            axes.LabelVisible = False
        finally:
            self.stkRoot.end_update()

        self.createAngleBtn["state"] = "normal"
        self.createPlaneBtn["state"] = "disabled"

    def _create_angle(self):
        self.descriptionLabel[
            "text"
        ] = 'As you can see, we have created \
                                         three angles referencing \
                                         "NormalPlane", the velocity \
                                         vector, and the distance vector \
                                         to our accessFac.  By clicking \
                                         "Play" in the upper left hand \
                                         corner, you will be able to see the \
                                         angles and vectors automatically \
                                         adjust as the satellite makes its \
                                         rotation around the central body \
                                         Earth.'

        vector3d = self._satellite.VO.Vector
        provider = self._satellite.vgt
        self.stkRoot.begin_update()
        try:
            anglePlane = provider.angles.factory.create(
                "AngleBetweenPlanes",
                "Angle from PlaneXY to NormalPlane",
                VECTOR_GEOMETRY_TOOL_ANGLE_TYPE.BETWEEN_PLANES,
            )
            anglePlane.FromPlane.SetPlane(provider.planes["BodyXY"])
            anglePlane.ToPlane.SetPlane(provider.planes["NormalPlane"])

            vector3d.RefCrdns.Add(GEOMETRIC_ELEM_TYPE.ANGLE_ELEM, anglePlane.QualifiedPath)
            voAnglePlane = vector3d.RefCrdns.GetCrdnByName(GEOMETRIC_ELEM_TYPE.ANGLE_ELEM, anglePlane.QualifiedPath)
            voAnglePlane.AngleValueVisible = True

            angleVector = provider.angles.factory.create(
                "AngleToVector",
                "Angle from Vector to Plane",
                VECTOR_GEOMETRY_TOOL_ANGLE_TYPE.BETWEEN_VECTORS,
            )
            angleVector.FromVector.SetVector(provider.vectors["Velocity"])
            angleVector.ToVector.SetVector(provider.vectors["accessFac"])

            vector3d.RefCrdns.Add(GEOMETRIC_ELEM_TYPE.ANGLE_ELEM, angleVector.QualifiedPath)
            voAngleVector = vector3d.RefCrdns.GetCrdnByName(GEOMETRIC_ELEM_TYPE.ANGLE_ELEM, angleVector.QualifiedPath)
            voAngleVector.AngleValueVisible = True
            voAngleVector.Color = Colors.SpringGreen

            anglePlaneFac = provider.angles.factory.create(
                "AngleFromFac",
                "Angle from Plane to Vector",
                VECTOR_GEOMETRY_TOOL_ANGLE_TYPE.TO_PLANE,
            )
            anglePlaneFac.ReferenceVector.SetVector(provider.vectors["accessFac"])
            anglePlaneFac.ReferencePlane.SetPlane(provider.planes["NormalPlane"])
            self._satellite.VO.Vector.RefCrdns.Add(GEOMETRIC_ELEM_TYPE.ANGLE_ELEM, anglePlaneFac.QualifiedPath)
            voAngleFac = vector3d.RefCrdns.GetCrdnByName(GEOMETRIC_ELEM_TYPE.ANGLE_ELEM, anglePlaneFac.QualifiedPath)
            voAngleFac.AngleValueVisible = True
        finally:
            self.stkRoot.end_update()

        self.exitBtn["state"] = "normal"
        self.createAngleBtn["state"] = "disabled"

    def _on_anim_update(self, TimeEpSec):
        if self._satellite is not None:
            provider = self._satellite.vgt
            if provider.vectors.contains("accessFac"):
                vector = provider.vectors["accessFac"]
                result = vector.find_in_axes(TimeEpSec, provider.well_known_axes.earth.fixed)
                if result.is_valid:
                    cartVec = result.vector
                    mag = math.sqrt(cartVec.x * cartVec.x + cartVec.y * cartVec.y + cartVec.z * cartVec.z)
                    self.distanceEntry["state"] = "normal"
                    self.distanceEntry.delete(0, tk.END)
                    self.distanceEntry.insert(0, "{:0.2f} km".format(mag / 1000))
                    self.distanceEntry["state"] = "disabled"


if __name__ == "__main__":
    vgtTutorial = VGTTutorial()
    vgtTutorial._run()
