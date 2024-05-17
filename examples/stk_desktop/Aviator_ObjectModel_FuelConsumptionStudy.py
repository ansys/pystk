import sys
import os
try:
    if os.name == "nt":
        from ansys.stk.core.stkdesktop import STKDesktop
    from ansys.stk.core.stkobjects import *
    from ansys.stk.core.stkobjects.aviator import *
    from ansys.stk.core.utilities.colors import *
except:
    print("Failed to import stk modules. Make sure you have installed the STK Python API wheel (agi.stk<..ver..>-py3-none-any.whl) from the STK Install bin directory")
try:
    import matplotlib.pyplot as plt
except:
    print("**** Error: Failed to import one of the required modules (mpl_toolkits, matplotlib, numpy). Make sure you have them installed. If you are using anaconda python, make sure you are running the sample from an anaconda command prompt.")
    sys.exit(1)

if os.name == "nt":
    try:
        uiApp = STKDesktop.attach_to_application()

        stkRoot = uiApp.root
        checkEmpty = stkRoot.children.count

        if checkEmpty == 0:
            uiApp.visible = True
            uiApp.userControl = True
        else:
            # If a Scenario is open and has objects in it, launch new instance of STK 12
            uiApp = STKDesktop.start_application(visible=True, userControl=True)
            stkRoot = uiApp.root
    except:
        uiApp = STKDesktop.start_application(visible=True, userControl=True)
        stkRoot = uiApp.root
else:
    print("Automation samples only work on windows with the desktop application, see Custom Applications for STK Engine examples.")
    quit()

stkRoot.new_scenario('AviatorParametricDemo')
scenario = Scenario(stkRoot.current_scenario)
stkRoot.unit_preferences.set_current_unit('DateFormat', 'EpHr')

aircraft = Aircraft(stkRoot.current_scenario.children.new(STK_OBJECT_TYPE.eAircraft, 'AvtrAircraft'))
aircraft.SetRouteType(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_AVIATOR)
avtrProp = AviatorPropagator(VehiclePropagatorAviator(aircraft.Route).AvtrPropagator)

avtrMission = avtrProp.AvtrMission
phases = avtrMission.Phases
phase = phases[0]
procedures = phase.Procedures

## Get the runways from the catalog
runwayCategory = avtrProp.AvtrCatalog.RunwayCategory
installDir = stkRoot.execute_command('GetDirectory / STKHome')[0]
runwayCategory.ARINC424Runways.MasterDataFilepath = os.path.join(installDir, 'Data', 'Resources', 'stktraining', 'samples', 'FAANFD18')
JFK = runwayCategory.ARINC424Runways.GetARINC424Item('JOHN F KENNEDY INTL 04L 22R')
LAX = runwayCategory.ARINC424Runways.GetARINC424Item('LOS ANGELES INTL 06L 24R')

ac = avtrProp.AvtrCatalog.AircraftCategory

if ac.AircraftModels.Contains('Advanced Airliner') > 0:
    ac.AircraftModels.RemoveChild('Advanced Airliner')

basicAirliner = ac.AircraftModels.GetAircraft('Basic Airliner')
advAirliner = basicAirliner.Duplicate();
advAirliner.Name = 'Advanced Airliner'
advTool = advAirliner.AdvFixedWingTool
advTool.MaxMach = 0.88
advTool.AeroStrategy = ADVANCED_FIXED_WING_AERO_STRATEGY.SUBSONIC_AERO
advTool.PowerplantStrategy = ADVANCED_FIXED_WING_POWERPLANT_STRATEGY.TURBOFAN_HIGH_BYPASS
engine = advTool.PowerplantModeAsEmpiricalJetEngine
engine.MaxSeaLevelStaticThrust = 200000
engine.DesignPointAltitude = 39000;
advTool.CreateAllPerfModels('AdvancedModel', 1, 1)

avtrMission.Vehicle = advAirliner

takeoff = procedures.Add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_TAKEOFF)
jfkRunway = takeoff.Site
SiteRunway(jfkRunway).CopyFromCatalog(JFK)


enroute = procedures.Add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_ENROUTE)
laxRunway = enroute.Site
SiteRunway(laxRunway).CopyFromCatalog(LAX)
laxRunway.LowEndHeading = 35
laxRunway.Name = 'LAX Alternate Runway'
SiteRunway(laxRunway).AddToCatalog(1)
ProcedureEnroute(enroute).AltitudeMSLOptions.UseDefaultCruiseAltitude = 0

landing = procedures.Add(SITE_TYPE.SITE_RUNWAY, PROCEDURE_TYPE.PROC_LANDING)
landing.Name = 'Landing'
landingRunway = landing.Site
laxAlternate = runwayCategory.UserRunways.GetUserRunway('LAX Alternate Runway')
SiteRunway(landingRunway).CopyFromCatalog(laxAlternate)

altitudes = [20000, 25000, 30000, 35000, 40000, 45000]
totalFuel = []
totalTime = []

for altitude in altitudes:
    print(f'Setting Altitude to {altitude} ft')
    ProcedureEnroute(enroute).AltitudeMSLOptions.MSLAltitude = altitude
    avtrProp.Propagate()
    flightDP = DataProviderTimeVarying(aircraft.DataProviders['Flight Profile By Time']).Exec(4.5, 6.5, 3600)
    fuelUsed = flightDP.DataSets.GetDataSetByName('Fuel Consumed').GetValues()
    totalFuel.append(fuelUsed[-1])
    time = flightDP.DataSets.GetDataSetByName('Time').GetValues()
    totalTime.append(time[-1])

fig = plt.subplots(figsize = (12, 8))
gridsize = (3,2)
ax1 = plt.subplot2grid(gridsize, (0,0), colspan = 2, rowspan = 2, projection='3d')
ax2 = plt.subplot2grid(gridsize, (2,0))
ax3 = plt.subplot2grid(gridsize, (2,1))

ax1.plot3D(altitudes, totalTime, totalFuel)
ax1.set_title('Fuel Consumed and Time of Flight at Varying Altitudes')
ax1.set_xlabel('Altitude (ft)')
ax1.set_ylabel('Time of Flight (hrs)')
ax1.set_zlabel('Fuel Consumed (lbs)')

ax2.plot(altitudes, totalFuel)
ax2.set_title('Fuel Consumed at Each Altitude')
ax2.set_xlabel('Altitude (ft)')
ax2.set_ylabel('Fuel Consumed (lbs)')

ax3.plot(altitudes, totalTime)
ax3.set_title('Total Time of Flight at Each Altidue')
ax3.set_xlabel('Altitude (ft)')
ax3.set_ylabel('Time of Flight (hrs)')

plt.show()
