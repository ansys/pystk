# # CommRadar_MissileTest_Interference

# ## Problem Statement

# Engineers and operators need to quickly model and analyze a telemetry link from a missile launch and to determine how various settings on a radar
# will affect its ability to track a missile. You are launching a test missile from a launch pad located on the Pacific Coast of the United States.
# The missile will transmit telemetry data to a communications system on board a ship anchored off the coast. The missile's telemetry data will be
# transmitted on an S-band frequency, which is close to a frequency used by multiple high-power satellite digital audio radio service (SDARS)
# satellites. Phase one of your test will determine if the satellites, which provide XM radio service, will interfere with ship's ability to receive
# the test missile telemetry data. Phase two of your test will determine for how long a shipborne radar system can detect and track the missile
# during its flight. A custom radar cross section and a radar antenna pattern file are required for your analysis.

# ## Launch a new STK instance

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# # -

# # ## Creating a new scenario

# # +
root = stk.new_object_root()
root.new_scenario("CommRadar_MissileTest_Interference_SCRIPT")
# from ansys.stk.core.stkdesktop import STKDesktop
# stk = STKDesktop.start_application(visible=True)
# -

# ## Creating a new scenario

# +
# root = stk.root
# root.new_scenario("CommRadar_MissileTest_Interference_SCRIPT")

# -

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


globe_widget = GlobeWidget(root, 640, 480)
globe_widget.camera.position = [0, 0, 0]
globe_widget.show()
# -

# +
from ansys.stk.core.experimental.jupyterwidgets import MapWidget


map_widget = MapWidget(root, 640, 480)
map_widget.show()
# -

# ## Set the scenario time period

# +
scenario = root.current_scenario
scenario.set_time_period("10 June 2026 16:00:00.000", "10 June 2026 16:35:00.000")
root.rewind()
# -

# ## Modeling the test missile

# Inserting a new Missile object

# +
from ansys.stk.core.stkobjects import Missile, STKObjectType


Test_Missile: Missile = scenario.children.new(STKObjectType.MISSILE, "Test_Missile")
# -

# Designing the Missile object's trajectory

# +
from ansys.stk.core.stkobjects import (
    IPropagator,
    PropagatorType,
    VehicleImpactLocationPoint,
    VehicleLaunchControl,
)


root.units_preferences.item("Latitude").set_current_unit("deg")
root.units_preferences.item("Longitude").set_current_unit("deg")
root.units_preferences.item("Distance").set_current_unit("km")

Test_Missile.set_trajectory_type(PropagatorType.BALLISTIC)
trajectory: IPropagator = Test_Missile.trajectory
root.units_preferences.set_current_unit("DateFormat", "EpSec")
trajectory.ephemeris_interval.set_explicit_interval(
    0, 0
)  # stop time later computed based on propagation
trajectory.launch.latitude = 34.7556
trajectory.launch.longitude = -120.6223
trajectory.launch.altitude = 0.0024385  # km --> 8 ft = 0.0024384 km

impact_location: VehicleImpactLocationPoint = trajectory.impact_location

impact_location.impact.latitude = 10
impact_location.impact.longitude = 173
impact_location.set_launch_control_type(VehicleLaunchControl.FIXED_DELTA_V)
impact_location.launch_control.delta_v = 6.90194  # km/secs
impact_location.impact.altitude = 0.0024385  # km --> 8 ft = 0.0024384 km

trajectory.propagate()
# -

# Viewing the test missile

# +
globe_widget.camera.position = [34.7556, -120.662, 1]
globe_widget.show()
# -

# Generate an Altitude vs Ground Range report (1)

# +
provider = Test_Missile.data_providers.item("Ground Range").group.item("Fixed")
time_step = 60  # Time step for Altitude vs Ground Range Report in seconds.
ground_range_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
ground_range_report[["time", "ground range", "alt"]]
# -

# ## Modeling the test missile's transmitter

# Inserting a Transmitter object

# +
from ansys.stk.core.stkobjects import Transmitter


missile_transmitter: Transmitter = Test_Missile.children.new(
    STKObjectType.TRANSMITTER, "Missile_Tx"
)
# -

# Using a Medium Transmitter model

# +
missile_transmitter.model_component_linking.set_component("Medium Transmitter Model")
transmitter_model = missile_transmitter.model_component_linking.component
transmitter_model.frequency = 2.31  # GHz
transmitter_model.power = 19.03  # dBW <--- 80 W = 19.03 dBW... 10log(80) = 19.03
transmitter_model.antenna_gain = -0.57  # dB
transmitter_model.data_rate = 2.048  # Mb/sec
# -

# Setting the transmitter modulation options

# +
transmitter_model.set_modulator("BPSK")
transmitter_model.modulator.enable_signal_psd = True
# -

# ## Modeling the ship

# Inserting a new Ship object

# +
from ansys.stk.core.stkobjects import Ship


ship: Ship = scenario.children.new(STKObjectType.SHIP, "Ship")
# -

## Defining the ship's route options

# In the tutorial, the ship is defined to be stationary.

# +
from ansys.stk.core.stkobjects import (
    IGreatArcVehicle,
    PropagatorGreatArc,
    PropagatorType,
    VehicleWaypointComputationMethod,
)


IGreatArcVehicle(ship).set_route_type(PropagatorType.GREAT_ARC)

from ansys.stk.core.stkobjects import VehicleAltitudeReference


ship.route.set_altitude_reference_type(VehicleAltitudeReference.WGS84)

PropagatorGreatArc(IGreatArcVehicle(ship).route).set_points_specify_time_and_propagate(
    [
        [scenario.start_time, 34.196, -120, 0, 0],
        [scenario.stop_time, 34.196, -120, 0, 0],
    ]
)
# -

# Inserting a Sensor Object

# +
from ansys.stk.core.stkobjects import Sensor, SensorPattern, SensorSimpleConicPattern


antenna_motor: Sensor = ship.children.new(STKObjectType.SENSOR, "Antenna_Motor")
# -

# Defining the sensor's cone half angle

# +
antenna_motor.set_pattern_type(SensorPattern.SIMPLE_CONIC)
SensorSimpleConicPattern(antenna_motor.pattern).cone_angle = 5
# -

# Setting the antenna motor's location

# +
from ansys.stk.core.stkobjects import SensorLocation


antenna_motor.set_location_type(SensorLocation.FIXED)

root.units_preferences.item("Distance").set_current_unit("ft")
antenna_motor.location_data.assign_cartesian(75, 0, 75)  # ft
# -

# Targeting the test missile

# +
from ansys.stk.core.stkobjects import BoresightType, TrackMode


antenna_motor.common_tasks.set_pointing_targeted_tracking(
    TrackMode.RECEIVE, BoresightType.ROTATE, "Missile/Test_Missile"
)
# -

# Viewing the targeted antenna is the 3D graphics window

# +
globe_widget.camera.position = [34.196, -120, 1]  # Deg Latitude & Longitude
globe_widget.show()
# -

# ## Modeling the test ship's receiver

# Inserting a Receiver object

# +
from ansys.stk.core.stkobjects import Receiver


ship_receiver: Receiver = antenna_motor.children.new(STKObjectType.RECEIVER, "Ship_Rx")
# -

# Using a Complex Receiver model

# +
ship_receiver.model_component_linking.set_component("Complex Receiver Model")
receiver_model = ship_receiver.model_component_linking.component
receiver_model.track_frequency_automatically = True
# -

# Defining the receiver's antenna specifications

# +
from ansys.stk.core.stkobjects import AntennaModelHelix, IAntennaModel


receiver_model.antenna_control.embedded_model_component_linking.set_component("Helix")
helixModel: AntennaModelHelix = (
    receiver_model.antenna_control.embedded_model_component_linking.component
)

IAntennaModel(helixModel).design_frequency = 2.5  # GHz
helixModel.diameter = 0.9  # m
helixModel.efficiency = 55  # %
helixModel.turn_spacing = 0.001  # m
helixModel.number_of_turns = 3  # integer value
helixModel.backlobe_gain = -30  # dB
# -

# Visualizing the receiver's antenna pattern

# +
from ansys.stk.core.stkobjects import AntennaVolumeGraphics


volume: AntennaVolumeGraphics = ship_receiver.graphics_3d.volume
volume.show = True
volume.gain_scale = 0.5  # km

volume.set_resolution(
    azimuth_start=-180,
    azimuth_stop=180,  # deg
    azimuth_resolution=1,
    elevation_start=0,
    elevation_stop=90,
    elevation_resolution=1,
)
# -

# Adding gain coloring

# +
from ansys.stk.core.stkobjects import FigureOfMeritGraphics2DColorMethod


volume.color_method = FigureOfMeritGraphics2DColorMethod.EXPLICIT
volume.relative_to_maximum = True

levels = volume.levels
levels.clear()

for gain in range(-70, 1, 10):
    level = levels.add(gain)
# -

# Viewing the antenna pattern in the 3D Graphics window

# +
globe_widget.camera.position = [34.196, -120, 3]  # Deg Latitude & Longitude
globe_widget.show()
# -

# ## Analyzing the telemetry downlink's link budget (2)

# The missile will transmit telemetry data to the ship during its flight. Create a simple link budget to calculate the
# bit error rate (BER), which reflects of how often errors occur in the transmission of digital data. You can compute a
# simple link budget using the Access tool. The Access tool's preinstalled Link Budget report includes all the basic link
# parameters associated with the selected receiver or transmitter. It gives you the signal strength and quality of the
# link received at the ship from the missile. Obviously, you want a low BER value, because that means you have fewer
# errors over time. For the purposes of this analysis, a Bit Error Rate of 1.000000e-09 or lower is acceptable.

# +
from pandas import DataFrame

from ansys.stk.core.stkobjects import Access, ISTKObject


access: Access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()

provider = access.data_providers.item("Link Information")
link_budget_report: DataFrame = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
link_budget_report[["ber"]]
root.save_scenario()
# -

# ## Inserting the interfering satellites

# +
from pathlib import Path

from ansys.stk.core.stkobjects import ExecuteCommandResult


# Get STK database location using Connect
result: ExecuteCommandResult = root.execute_command("GetDirectory / Database Satellite")
satDataDir: str = result[0]
file_location: str = '"' + str(Path(satDataDir) / Path(r"stkAllTLE.sd")) + '"'

# Import object from database using Connect
command: str = f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-8"
root.execute_command(command)  # Import SXM-8

command: str = f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-9"
root.execute_command(command)  # Import SXM-9

command: str = (
    f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-10"
)
root.execute_command(command)  # Import SXM-10

from ansys.stk.core.stkobjects import Satellite


sxm_8: Satellite = scenario.children.item("SXM-8_48838")
sxm_9: Satellite = scenario.children.item("SXM-9_62259")
sxm_10: Satellite = scenario.children.item("SXM-10_64290")
# -

# ## Modeling the interfering satellites' transmitters

from ansys.stk.core.stkobjects import TransmitterModelMedium


transmitters = []

for satellite in [sxm_8, sxm_9, sxm_10]:
    transmitter = ISTKObject(satellite).children.new(
        STKObjectType.TRANSMITTER, "Transmitter"
    )

    transmitter.model_component_linking.set_component("Medium Transmitter Model")

    transmitter_model = TransmitterModelMedium(
        transmitter.model_component_linking.component
    )

    transmitter_model.frequency = 2.3347  # GHz
    transmitter_model.power = 41.2385  # dBW
    transmitter_model.data_rate = 0.048
    transmitter_model.antenna_gain = 40  # dB

    transmitter_model.set_modulator("QPSK")
    transmitter_model.modulator.scale_bandwidth_automatically = True

    transmitters.append(transmitter)

sxm_8_transmitter = transmitters[0]
sxm_9_transmitter = transmitters[1]
sxm_10_transmitter = transmitters[2]

# ## Checking for interference

# There are several methods through which you can determine the impact of interference on a system.
# For more complex systems, you can use a Comm System to model dynamically configured communications
# links between constellations of transmitters and receivers. However, for less complex systems, like
# the one in this scenario, you can compute interference effects directly in a Receiver object.

# Adding interference sources to the receiver

# +
from ansys.stk.core.stkobjects import ISTKObject, RFInterference


interference = RFInterference(
    ship_receiver.model_component_linking.component.interference
)
interference.enabled = True
interference.emitters.add(sxm_8_transmitter.path)
interference.emitters.add(sxm_9_transmitter.path)
interference.emitters.add(sxm_10_transmitter.path)
# -

# Determining the impact of interference with a Link Budget - Interference report (3)

# +
access: Access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()

provider = access.data_providers.item("Link Information")
link_budget_report: DataFrame = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
link_budget_report[["ber", "ber+i"]]
root.save_scenario()
# -

# ## Mitigating interference with a spectrum filter

# Using a butterworth filter

# +
from ansys.stk.core.stkobjects import RFFilterModelButterworth


receiver_model.enable_filter = True
receiver_model.filter_component_linking.set_component("Butterworth")
ship_receiver_filter: RFFilterModelButterworth = (
    receiver_model.filter_component_linking.component
)
ship_receiver_filter.upper_bandwidth_limit = 20  # MHz
ship_receiver_filter.lower_bandwidth_limit = -20  # MHz
ship_receiver_filter.cut_off_frequency = 5  # MHz
ship_receiver_filter.order = 4  # Unit
# -

# Recomputing the Link Budget - Interference report (4)

# +
access: Access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()

provider = access.data_providers.item("Link Information")
link_budget_report: DataFrame = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
link_budget_report[["ber", "ber+i"]]
root.save_scenario()
# -

# ## Modeling the ship's radar

# Inserting a Radar object

# +
from ansys.stk.core.stkobjects import Radar


ship_radar: Radar = ship.children.new(STKObjectType.RADAR, "Ship_Radar")
# -

# Setting the radar's mode

# +
ship_radar.model_component_linking.set_component("Monostatic")
monostatic_radar = ship_radar.model_component_linking.component
monostatic_radar.mode_component_linking.set_component("Search Track")
monostatic_search_track_radar = monostatic_radar.mode_component_linking.component
monostatic_search_track_radar.waveform.pulse_definition.pulse_width = 8.8e-7
# -

# Setting the goal signal-to-noise ratio

# +
monostatic_search_track_radar.waveform.pulse_integration.snr = 20  # dB
# -

# Configuring the radar's antenna

# +
from ansys.stk.core.stkobjects import AntennaControl, AntennaModelExternal


antenna_control: AntennaControl = (
    ship_radar.model_component_linking.component.antenna_control
)
antenna_control.embedded_model_component_linking.set_component(
    "External Antenna Pattern"
)

external_model = AntennaModelExternal(
    antenna_control.embedded_model_component_linking.component
)
external_model.design_frequency = 2.8  # GHz
# -

# Selecting the external pattern file

# +
external_model.filename = str(
    Path(
        r"C:\Program Files\AGI\STK_ODTK 13\Data\Resources\stktraining\samples\ASR9Low.pattern"
    )
)
# -

# Setting the radar antenna's location

# +
root.units_preferences.item("SmallDistance").set_current_unit("ft")

antenna_control.embedded_model_orientation.position_offset.set(37, 0, 120)
# -

# Setting the radar transmitter specifications

# +
from ansys.stk.core.stkobjects import RadarFrequencySpecificationType, RadarReceiver


radar_transmitter = ship_radar.model_component_linking.component.transmitter
radar_transmitter.frequency_specification = RadarFrequencySpecificationType.FREQUENCY

radar_transmitter.frequency = 2.8  # GHz
radar_transmitter.power = 100.414  # dBW (11 GW = 100.414 dBW)
# -

# Changing the radar receiver LNA gain

# +
radar_receiver: RadarReceiver = ship_radar.model_component_linking.component.receiver
radar_receiver.lna_gain = 25  # dB
# -

# ## Defining the missile's radar cross section

# The Radar capability enables you to specify an important property of a potential radar target: its radar cross
# section (RCS). To design a radar system, it is essential to be able to describe the target's echo, which is a
# function of its size, shape, and orientation. RCS is the projected area of a metal sphere that would return the
# same echo signal as the target if it were substituted for the target. The signal return from a point target is
# inversely proportional to the fourth power of target range and directly proportional to the target's radar cross
# section. Real targets have widely differing radar cross sections from different aspect angles.

# You can define the missile's RCS using an external RCS file. External RCS files can contain real-valued pattern
# data or complex-valued pattern data.

# +
Test_Missile.radar_cross_section.inherit = False

from ansys.stk.core.stkobjects import (
    RadarCrossSectionComputeStrategyExternalFile,
    RadarCrossSectionFrequencyBand,
)


rcs_band: RadarCrossSectionFrequencyBand = Test_Missile.radar_cross_section.model_component_linking.component.frequency_bands.item(
    0
)
rcs_band.set_compute_strategy("External File")

external_file_compute_strategy: RadarCrossSectionComputeStrategyExternalFile = (
    rcs_band.compute_strategy
)

external_file_compute_strategy.filename = str(
    Path(
        r"C:\Program Files\AGI\STK_ODTK 13\Data\Resources\stktraining\samples\Basic_Missile_mono.rcs"
    )
)
root.save_scenario()
# -

# ## Computing access

# Determine if the ship's radar can track the test missile.

# +
access: Access = ISTKObject(ship_radar).get_access_to_object(Test_Missile)
access.compute_access()
# -

# ## Creating a custom report (5)

# Create a custom report style that shows azimuth-elevation-range (AER) and Radar Search/Track data.

# First, we will generate the AER Data portion of the report.

# +
provider = access.data_providers.item("AER Data").group.item("BodyFixed")
aer_and_search_track_data: DataFrame = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
print(aer_and_search_track_data[["time", "azimuth", "elevation", "range"]])
# -

# Second, we will generate the Radar SearchTrack portion of the report.

# +
root.units_preferences.item("Distance").set_current_unit(
    "km"
)  # The script report is now using the same units as the scenario report.

provider = access.data_providers.item("Radar SearchTrack")
aer_and_search_track_data: DataFrame = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
print(
    aer_and_search_track_data[
        ["s/t integrated snr", "s/t integrated pdet", "s/t pulses integrated"]
    ]
)
# -

# Third, we will generate the Radar RCS portion of the report.

# +
provider = access.data_providers.item("Radar RCS")
aer_and_search_track_data: DataFrame = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
print(aer_and_search_track_data[["rcs"]])
# -
