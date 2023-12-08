import os
import tempfile
import tkinter as tk

from ansys.stk.core.stkengine import STKEngine
from ansys.stk.core.stkobjects import *
from ansys.stk.core.stkutil import *
from ansys.stk.core.utilities.colors import *
from ansys.stk.core.stkengine.tkcontrols import GlobeControl, GfxAnalysisControl

class SolarPanelTool:
    def __init__(self):
        self.stk = STKEngine.start_application(noGraphics=False)
        self.root = self.stk.new_object_root()
        self.reportFilePath = ""
        self.firstTime = True
        self.window = tk.Tk()
        self.window.title("Solar Panel Tool")
        self.window.protocol("WM_DELETE_WINDOW", self.exit)
        self.controlFrame = tk.Frame()
        self.globeControl = GlobeControl(self.controlFrame, width=320, height=200)
        self.globeControl.back_color = Color.FromRGB(217, 217, 217)
        self.globeControl.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
        self.gfxAnalysisControl = GfxAnalysisControl(self.controlFrame, width=320, height=200)
        self.gfxAnalysisControl.back_color = Color.FromRGB(217, 217, 217)
        self.gfxAnalysisControl.pack(fill=tk.BOTH, expand=tk.YES, side=tk.TOP)
        self.controlFrame.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT)
        self.buttonFrame = tk.Frame()
        self.newScenarioBtn = tk.Button(self.buttonFrame, text="New Scenario", width=15, command=self.newScenario)
        self.newScenarioBtn.pack(side=tk.TOP, pady=6)
        self.newSatelliteBtn = tk.Button(self.buttonFrame, text="New Satellite", width=15, command=self.newSatellite)
        self.newSatelliteBtn.pack(side=tk.TOP, pady=6)
        self.newSatelliteBtn['state'] = "disabled"
        self.computeBtn = tk.Button(self.buttonFrame, text="Compute", width=15, command=self.compute)
        self.computeBtn.pack(side=tk.TOP, pady=6)
        self.computeBtn['state'] = "disabled"
        self.reportBtn = tk.Button(self.buttonFrame, text="Report", width=15, command=self.report)
        self.reportBtn.pack(side=tk.TOP, pady=6)
        self.reportBtn['state'] = "disabled"
        self.closeScenarioBtn = tk.Button(self.buttonFrame, text="Close Scenario", width=15, command=self.closeScenario)
        self.closeScenarioBtn.pack(side=tk.TOP, pady=6)
        self.closeScenarioBtn['state'] = "disabled"
        self.buttonFrame.pack(fill=tk.BOTH, expand=tk.YES, side=tk.LEFT, padx=10)
        
    def run(self):
        self.window.mainloop()
        
    def exit(self):
        self.root.close_scenario()
        self.window.destroy()
        self.stk.shutdown()
        
    def newScenario(self):
        self.root.new_scenario("SolarPanelTest")
        self.root.unit_preferences.set_current_unit("DistanceUnit", "km")
        self.root.unit_preferences.set_current_unit("DateFormat", "UTCG")
        oScenario = self.root.current_scenario
        oScenario.SetTimePeriod("1 Jul 2007 12:00:00.000", "2 Jul 2007 12:00:00.000")
        oScenario.Epoch = "1 Jul 2007 12:00:00.000"
        oScenario.Animation.StartTime = "1 Jul 2007 12:00:00.000"
        self.root.rewind()
        self.newScenarioBtn['state'] = "disabled"
        self.newSatelliteBtn['state'] = "normal"
        self.closeScenarioBtn['state'] = "normal"
        
    def newSatellite(self):
        oSat = self.root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite1")
        oSat.VO.Model.ScaleValue = 0.0
        oSat.SetPropagatorType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_TWO_BODY)
        oTwobody = oSat.Propagator
        interval = oTwobody.EphemerisInterval
        interval.SetExplicitInterval("1 Jul 2007 12:00:00.000", "2 Jul 2007 12:00:00.000")
        oTwobody.Step = 60
        oOrb = oTwobody.InitialState.Representation
        oOrb.Epoch = "1 Jul 2007 12:00:00.000"
        oTwobody.InitialState.Representation.AssignClassical(COORDINATE_SYSTEM.J2000, 6878.14, 0.0, 45.0, 0.0, 0.0, 0.0)
        oTwobody.Propagate()

        modelFile = oSat.VO.Model.ModelData
        modelFile.Filename = r"\STKData\VO\Models\Space\satellite.mdl"
        
        self.newSatelliteBtn['state'] = "disabled"
        self.computeBtn['state'] = "normal"
    
    def cleanReportFile(self):
        if os.path.exists(self.reportFilePath):
            os.remove(self.reportFilePath)
    
    def getReportFilePath(self):
        self.cleanReportFile()
        self.reportFilePath = os.path.join(tempfile._get_default_tempdir(), next(tempfile._get_candidate_names()))
        
    def compute(self):
        self.getReportFilePath()
        if self.firstTime:
            self.root.execute_command("VO */Satellite/Satellite1 SolarPanel Visualization AddGroup default")
            self.firstTime = False
        else:
            self.root.execute_command("VO */Satellite/Satellite1 SolarPanel DeleteData")
        self.root.execute_command("VO */Satellite/Satellite1 SolarPanel Visualization Radius On 25.00");				
        self.root.execute_command("VO */Satellite/Satellite1 SolarPanel Compute \"1 Jul 2007 12:00:00.000\" \"1 Jul 2007 18:00:00.000\" 300 Area " + "\"" + self.reportFilePath + "\"" )
        
        self.computeBtn['state'] = "disabled"
        self.reportBtn['state'] = "normal"
        
    def report(self):
        with open(self.reportFilePath, 'r') as file:
            self.report = file.read()
        self.reportWindow = tk.Toplevel(self.window)
        self.reportWindow.title("Solar Panel Report")
        self.reportText = tk.Text(self.reportWindow)
        self.reportText.insert("0.0", self.report)
        self.reportText.pack(fill=tk.BOTH, expand=tk.YES)
        self.reportText['state'] = "disabled"
        self.reportWindow.update()
        self.reportBtn['state'] = "disabled"
        
    def closeScenario(self):
        if not self.firstTime:
            self.firstTime = True
            self.root.execute_command("VO */Satellite/Satellite1 SolarPanel DeleteData")
        self.root.close_scenario()
        self.cleanReportFile()
        self.newScenarioBtn['state'] = "normal"
        self.newSatelliteBtn['state'] = "disabled"
        self.computeBtn['state'] = "disabled"
        self.reportBtn['state'] = "disabled"
        self.closeScenarioBtn['state'] = "disabled"
        
if __name__ == '__main__':
    solarPanelTool = SolarPanelTool()
    solarPanelTool.run()
