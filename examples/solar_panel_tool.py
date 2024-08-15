# # Solar Panel
#
# This example demonstrates how to use Solar Panel Tool in STK Engine using PySTK. it is desired to look at the power generation based off of specified solar panels on a given satellite's model. 
#
#
# ## What is a Solar Panel Tool
# The Solar Panel tool enables modeling the exposure of solar panels mounted on spacecraft, aircraft, and ground vehicles over a given time interval. The result of the analysis can be used to determine the availability of electrical power for operations that the vehicle and onboard apparatus will perform.
#
# The Solar Panel tool can not be used on any model that contains the FaceEmissionColor parameter or on any model that has a texture on the solar panel.

#
# ## Launch a new STK instance
#
# Create a new instance and initialize the user interface for STK Engine Application. This STK Engine Application embeds a Globe Control for 3D window and a  Graphics Analysis control for solar panel computations. 


#  Create STK Engine instance.

# +
import tkinter as tk

class SolarPanelTool:    
    def __init__(self):     
        from ansys.stk.core.stkengine import STKEngine

        self.stk = STKEngine.start_application(noGraphics=False)
# -

#  Set object model root instance.

        self.root = self.stk.new_object_root()

#  Intialize reoprt file path.

        self.reportFilePath = ""

#  Initialize applicatton parameters.

        self.firstTime = True
        self.window = tk.Tk()

#  Initialize the graphical user interface for the STK Engine application. Set and initialize various UI parameters such as application tile, size and placement of the Globe control, Graphics Analysis control and buttons.

        self.window.title("Solar Panel Tool")
        self.window.protocol("WM_DELETE_WINDOW", self._exit)
        self.controlFrame = tk.Frame()


#  Initialize the Globe control and its placemnet in UI application.

        from ansys.stk.core.stkengine.tkcontrols import GlobeControl
        from ansys.stk.core.utilities.colors import Color
        
        self.globeControl = GlobeControl(self.controlFrame, width=320, height=200)
        self.globeControl.back_color = Color.from_rgb(217, 217, 217)
        self.globeControl.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)

#  Initialize the Graphics Analysis control and its placemnet in UI application.

        from ansys.stk.core.stkengine.tkcontrols import GfxAnalysisControl
        from ansys.stk.core.utilities.colors import Colors
        
        self.gfxAnalysisControl = GfxAnalysisControl(self.controlFrame, width=320, height=200)
        self.gfxAnalysisControl.back_color = Colors.from_rgb(217, 217, 217)
        self.gfxAnalysisControl.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)


#  Organize various UI widgets, their state, size and postions.
#  Intialize UI application frame.

        self.controlFrame.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT)
        self.buttonFrame = tk.Frame()

#  Initialize "New Scenario" button with its initial state, size and placement.

        self.newScenarioBtn = tk.Button(
            self.buttonFrame,
            text="New Scenario",
            width=15,
            command=self._new_scenario,
        )
        self.newScenarioBtn.pack(side=tk.TOP, pady=6)

#  Initialize "New Satellite" button with its initial state, size and placement.

        self.newSatelliteBtn = tk.Button(
            self.buttonFrame,
            text="New Satellite",
            width=15,
            command=self._new_satellite,
        )
        self.newSatelliteBtn.pack(side=tk.TOP, pady=6)
        self.newSatelliteBtn["state"] = "disabled"

#  Initialize "Compute" button with its initial state, size and placement.

        self.computeBtn = tk.Button(self.buttonFrame, text="Compute", width=15, command=self._compute)
        self.computeBtn.pack(side=tk.TOP, pady=6)
        self.computeBtn["state"] = "disabled"

#  Initialize "Report" button with its initial state, size and placement.

        self.reportBtn = tk.Button(self.buttonFrame, text="Report", width=15, command=self._report)
        self.reportBtn.pack(side=tk.TOP, pady=6)
        self.reportBtn["state"] = "disabled"

#  Initialize "Close Scenario" button with its initial state, size and placement.

        self.closeScenarioBtn = tk.Button(
            self.buttonFrame,
            text="Close Scenario",
            width=15,
            command=self._close_scenario,
        )
        self.closeScenarioBtn.pack(side=tk.TOP, pady=6)
        self.closeScenarioBtn["state"] = "disabled"
        self.buttonFrame.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, padx=10)


#  Start the application.

    def _run(self):
        self.window.mainloop()

#  Close the scenario and exit the application

    def _exit(self):
        self.root.close_scenario()
        self.window.destroy()
        self.stk.shutdown()

#
# ## Create a new scenario
#
# Set up the STK Engine application by creating a new scenario.

    def _new_scenario(self):

#  When the "New Scenario" button is clicked, create a new scenario with the specified name and initliaze its various parameters.

        self.root.new_scenario("SolarPanelTest")

#  Set unit prefrences for the scenario.

        self.root.unit_preferences.set_current_unit("DistanceUnit", "km")
        self.root.unit_preferences.set_current_unit("DateFormat", "UTCG")

#  Set scenario start and stop times.

        oScenario = self.root.current_scenario
        oScenario.SetTimePeriod("1 Jul 2007 12:00:00.000", "2 Jul 2007 12:00:00.000")


#  Set scenario epoch.

        oScenario.Epoch = "1 Jul 2007 12:00:00.000"

#  Set scenario animation start time.

        oScenario.Animation.StartTime = "1 Jul 2007 12:00:00.000"

#  Reset scenario animation time to the previously set start time.

        self.root.rewind()

#  Update the state of the UI widgets. 

        self.newScenarioBtn["state"] = "disabled"
        self.newSatelliteBtn["state"] = "normal"
        self.closeScenarioBtn["state"] = "normal"

#
# ## Create a new satellite 
#
#  When the "New Satellite" button is clicked, set up a new satellite.

    def _new_satellite(self):

#   Create and add a satellite to the scenario.

        from ansys.stk.core.stkobjects import STK_OBJECT_TYPE


        oSat = self.root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1")
        oSat.VO.Model.ScaleValue = 0.0

#  Set up and initialize two body propagator in the satelite properties.

        from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE

        oSat.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        oTwobody = oSat.Propagator

#  Set up ephemeris interval and epoch of the satellite.

        interval = oTwobody.EphemerisInterval
        interval.SetExplicitInterval("1 Jul 2007 12:00:00.000", "2 Jul 2007 12:00:00.000")
        oTwobody.Step = 60
        oOrb = oTwobody.InitialState.Representation
        oOrb.Epoch = "1 Jul 2007 12:00:00.000"

#  Initialize coordinate system for the two body propagator.

        from ansys.stk.core.stkobjects import COORDINATE_SYSTEM

        oTwobody.InitialState.Representation.AssignClassical(
            COORDINATE_SYSTEM.J2000,
            6878.14,
            0.0,
            45.0,
            0.0,
            0.0,
            0.0,
        )

#  Initialize the propagator with currently configured parameters.

        oTwobody.Propagate()

#  Initialize satellite model by loading a model file.

        modelFile = oSat.VO.Model.ModelData
        modelFile.Filename = r"\STKData\VO\Models\Space\satellite.mdl"

#  Initialize the state of the buttons.

        self.newSatelliteBtn["state"] = "disabled"
        self.computeBtn["state"] = "normal"


#  A helper function to clean report file path.

    import os

    def _clean_report_file(self):
        if os.path.exists(self.reportFilePath):
            os.remove(self.reportFilePath)


#  A helper function to create a temporray file path for report file.

    import tempfile

    def _get_report_file_path(self):
        self._clean_report_file()
        self.reportFilePath = os.path.join(
            tempfile._get_default_tempdir(),
            next(tempfile._get_candidate_names()),
        )

#
# ## Compute solar panel exposure
#
#  When the "Compute" button is clicked, calculate solar obscuration over the specified time interval, using the specified step size.
#

    def _compute(self):

#  Retrieve file name and path for report file.

        self._get_report_file_path()

#  Initialize solar panel group name.

        if self.firstTime:
            self.root.execute_command("VO */Satellite/Satellite1 SolarPanel " + "Visualization AddGroup Panels")
            self.firstTime = False
        else:

#  Clean up and delete previous solar panel computation data.

            self.root.execute_command("VO */Satellite/Satellite1 SolarPanel DeleteData")

#  Specify radius in small distance units. 

        self.root.execute_command("VO */Satellite/Satellite1 SolarPanel " + "Visualization Radius On 25.00")

#  Compute area of the solar panels illuminated by the sun, the effective area (defined above) and the solar intensity at each time step.

        self.root.execute_command(
            "VO */Satellite/Satellite1 SolarPanel Compute "
            + '"1 Jul 2007 12:00:00.000" '
            + '"1 Jul 2007 18:00:00.000" 300 '
            + "Area "
            + '"'
            + self.reportFilePath
            + '" '
        )

#  Update the state of the UI widgets. 

        self.computeBtn["state"] = "disabled"
        self.reportBtn["state"] = "normal"


#
# ## Launch solar panel report window
#
#  When the "Report" button is clicked, display the report in a separet window.
#

    def _report(self):

#  Initialize the report window.

        with open(self.reportFilePath, "r") as file:
            self.report = file.read()
        self.reportWindow = tk.Toplevel(self.window)

#  Set and organize report window title.

        self.reportWindow.title("Solar Panel Report")
        self.reportText = tk.Text(self.reportWindow)
        self.reportText.insert("0.0", self.report)
        self.reportText.pack(fill=tk.BOTH, expand=tk.YES)

#  Update the state of the UI widgets.

        self.reportText["state"] = "disabled"
        self.reportWindow.update()
        self.reportBtn["state"] = "disabled"

#
# ## Close scenario
#
#  When the "Close Scenario" button is clicked, scenario is closed.
#

    def _close_scenario(self):

#  Clean up and delete solar panel computation data.

        if not self.firstTime:
            self.firstTime = True
            self.root.execute_command("VO */Satellite/Satellite1 SolarPanel DeleteData")

#  Close scenario.

        self.root.close_scenario()


#  Clean up report file path.

        self._clean_report_file()

#  Update the state of the UI widgets.

        self.newScenarioBtn["state"] = "normal"
        self.newSatelliteBtn["state"] = "disabled"
        self.computeBtn["state"] = "disabled"
        self.reportBtn["state"] = "disabled"
        self.closeScenarioBtn["state"] = "disabled"

#  Application entry point main function.

if __name__ == "__main__":
    solarPanelTool = SolarPanelTool()
    solarPanelTool._run()
    