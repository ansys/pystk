# # Missile Interference Test

# ## Problem Statement

# Engineers and operators need to quickly model and analyze a telemetry link from a missile launch and to determine how various settings on a radar
# will affect its ability to track a missile. You are launching a test missile from a launch pad located on the Pacific Coast of the United States.
# The missile will transmit telemetry data to a communications system on board a ship anchored off the coast. The missile's telemetry data will be
# transmitted on an S-band frequency, which is close to a frequency used by multiple high-power satellite digital audio radio service (SDARS)
# satellites. Phase one of your test will determine if the satellites, which provide XM radio service, will interfere with ship's ability to receive
# the test missile telemetry data. Phase two of your test will determine for how long a shipborne radar system can detect and track the missile
# during its flight. A custom radar cross section and a radar antenna pattern file are required for your analysis.

# This example is based on [this](https://help.agi.com/stk/index.htm#training/Missile_Test_XM_Interference.htm?TocPath=Tutorials%2520and%2520Training%257CSTK%2520Level%25203%2520-%2520Focused%2520Tutorials%257CProblem%2520Specific%257C_____21) tutorial.

# ## Launch a new STK instance

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# # -

# ## Create a new scenario

# +
root = stk.new_object_root()
root.new_scenario("CommRadar_MissileTest_Interference")
# -

# Once the scenario is created, you can view a 3D graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


globe_widget = GlobeWidget(root, 640, 480)
globe_widget.camera.position = [0, 0, 0]
globe_widget.show()
# -

# Once the scenario is created, you can view a 2D graphics window by running:

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

# ## Modele the test missile

# Insert a new Missile object

# +
from ansys.stk.core.stkobjects import Missile, STKObjectType


Test_Missile = scenario.children.new(STKObjectType.MISSILE, "Test_Missile")
# -

# First, set the units properly. Setting units proactively is a great practice!

# +
root.units_preferences.item("Latitude").set_current_unit("deg")
root.units_preferences.item("Longitude").set_current_unit("deg")
root.units_preferences.item("Distance").set_current_unit("km")
# -

# Next, design the missile's trajectory:

# +
from ansys.stk.core.stkobjects import (
    IPropagator,
    PropagatorType,
    VehicleImpactLocationPoint,
    VehicleLaunchControl,
)


Test_Missile.set_trajectory_type(PropagatorType.BALLISTIC)
trajectory = Test_Missile.trajectory
root.units_preferences.set_current_unit("DateFormat", "EpSec")
trajectory.ephemeris_interval.set_explicit_interval(0, 0)
# -

# Next, set the launch parameters:

# +
trajectory.launch.latitude = 34.7556
trajectory.launch.longitude = -120.6223
trajectory.launch.altitude = 0.0024385
# -

# Then, set the impact parameters:

# +
impact_location = trajectory.impact_location

impact_location.impact.latitude = 10
impact_location.impact.longitude = 173
impact_location.set_launch_control_type(VehicleLaunchControl.FIXED_DELTA_V)
impact_location.launch_control.delta_v = 6.90194
impact_location.impact.altitude = 0.0024385
# -

# Lastly, propagate:

# +
trajectory.propagate()
# -

# We can now view the test missile at its launch site:

# +
globe_widget.camera.position = [34.7556, -120.662, 1]  # <----------
globe_widget.show()
# -

# ## Generate an Altitude vs Ground Range report

# +
provider = Test_Missile.data_providers.item("Ground Range").group.item("Fixed")
time_step = 60
ground_range_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
ground_range_report[["time", "ground range", "alt"]]
# -

# ## Model the test missile's transmitter

# Insert a Transmitter object

# +
from ansys.stk.core.stkobjects import Transmitter


missile_transmitter = Test_Missile.children.new(STKObjectType.TRANSMITTER, "Missile_Tx")
# -

# Use a Medium Transmitter model

# +
missile_transmitter.model_component_linking.set_component("Medium Transmitter Model")
transmitter_model = missile_transmitter.model_component_linking.component
# -

# Set the transmitter properties.abs

# +
transmitter_model.frequency = 2.31
transmitter_model.power = 19.03
transmitter_model.antenna_gain = -0.57
transmitter_model.data_rate = 2.048
# -

# Set the transmitter modulation options

# +
transmitter_model.set_modulator("BPSK")
transmitter_model.modulator.enable_signal_psd = True
# -

# ## Model the ship

# Insert a new Ship object

# +
from ansys.stk.core.stkobjects import Ship


ship = scenario.children.new(STKObjectType.SHIP, "Ship")
# -

## Define the ship's route options

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

# Insert a Sensor Object

# +
from ansys.stk.core.stkobjects import Sensor, SensorPattern, SensorSimpleConicPattern


antenna_motor = ship.children.new(STKObjectType.SENSOR, "Antenna_Motor")
# -

# Define the sensor's cone half angle

# +
antenna_motor.set_pattern_type(SensorPattern.SIMPLE_CONIC)
SensorSimpleConicPattern(antenna_motor.pattern).cone_angle = 5
# -

# Set the antenna motor's location

# +
from ansys.stk.core.stkobjects import SensorLocation


antenna_motor.set_location_type(SensorLocation.FIXED)

root.units_preferences.item("Distance").set_current_unit("ft")
antenna_motor.location_data.assign_cartesian(75, 0, 75)
# -

# Target the test missile

# +
from ansys.stk.core.stkobjects import BoresightType, TrackMode


antenna_motor.common_tasks.set_pointing_targeted_tracking(
    TrackMode.RECEIVE, BoresightType.ROTATE, "Missile/Test_Missile"
)
# -

# View the targeted antenna is the 3D graphics window

# + tags=["nbsphinx-thumbnail"]
globe_widget.camera.position = [34.196, -120, 1]
globe_widget.show()
# -

# ## Model the test ship's receiver

# Insert a Receiver object

# +
from ansys.stk.core.stkobjects import Receiver


ship_receiver = antenna_motor.children.new(STKObjectType.RECEIVER, "Ship_Rx")
# -

# Use a Complex Receiver model

# +
ship_receiver.model_component_linking.set_component("Complex Receiver Model")
receiver_model = ship_receiver.model_component_linking.component
receiver_model.track_frequency_automatically = True
# -

# Define the receiver's antenna specifications

# +
from ansys.stk.core.stkobjects import AntennaModelHelix, IAntennaModel


receiver_model.antenna_control.embedded_model_component_linking.set_component("Helix")
helixModel = receiver_model.antenna_control.embedded_model_component_linking.component
# -

# Set the antenna's properties:

# +
IAntennaModel(helixModel).design_frequency = 2.5  # GHz
helixModel.diameter = 0.9
helixModel.efficiency = 55
helixModel.turn_spacing = 0.001
helixModel.number_of_turns = 3
helixModel.backlobe_gain = -30
# -

# Visualize the receiver's antenna pattern

# +
from ansys.stk.core.stkobjects import AntennaVolumeGraphics


volume = ship_receiver.graphics_3d.volume
volume.show = True
volume.gain_scale = 0.5

volume.set_resolution(
    azimuth_start=-180,
    azimuth_stop=180,
    azimuth_resolution=1,
    elevation_start=0,
    elevation_stop=90,
    elevation_resolution=1,
)
# -

# Add gain coloring

# +
from ansys.stk.core.stkobjects import FigureOfMeritGraphics2DColorMethod


volume.color_method = FigureOfMeritGraphics2DColorMethod.EXPLICIT
volume.relative_to_maximum = True

levels = volume.levels
levels.clear()

for gain in range(-70, 1, 10):
    level = levels.add(gain)
# -

# View the antenna pattern in the 3D Graphics window

# +
globe_widget.camera.position = [34.196, -120, 3]
globe_widget.show()
# -

# ## Analyze the telemetry downlink's link budget

# The missile will transmit telemetry data to the ship during its flight. Create a simple link budget to calculate the
# bit error rate (BER), which reflects of how often errors occur in the transmission of digital data. You can compute a
# simple link budget using the Access tool. The Access tool's preinstalled Link Budget report includes all the basic link
# parameters associated with the selected receiver or transmitter. It gives you the signal strength and quality of the
# link received at the ship from the missile. Obviously, you want a low BER value, because that means you have fewer
# errors over time. For the purposes of this analysis, a Bit Error Rate of 1.000000e-09 or lower is acceptable.

# +
from pandas import DataFrame

from ansys.stk.core.stkobjects import Access, ISTKObject


access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()

provider = access.data_providers.item("Link Information")
link_budget_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
link_budget_report[["ber"]]
# -

# ## Insert the interfering satellites

# +
from pathlib import Path

from ansys.stk.core.stkobjects import ExecuteCommandResult


# Get STK database location using Connect

# +
result = root.execute_command("GetDirectory / Database Satellite")
satDataDir = result[0]
file_location = '"' + str(Path(satDataDir) / Path(r"stkAllTLE.sd")) + '"'
# -

# Import object from database using Connect

# +
command = f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-8"
root.execute_command(command)

command = f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-9"
root.execute_command(command)

command = f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-10"
root.execute_command(command)
# -

# Assign the satellites:

# +
from ansys.stk.core.stkobjects import Satellite


sxm_8 = scenario.children.item("SXM-8_48838")
sxm_9 = scenario.children.item("SXM-9_62259")
sxm_10 = scenario.children.item("SXM-10_64290")
# -

# ## Model the interfering satellites' transmitters

# +
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

    transmitter_model.frequency = 2.3347
    transmitter_model.power = 41.2385
    transmitter_model.data_rate = 0.048
    transmitter_model.antenna_gain = 40

    transmitter_model.set_modulator("QPSK")
    transmitter_model.modulator.scale_bandwidth_automatically = True

    transmitters.append(transmitter)
# -

# Assign the satellite transmitters:

# +
sxm_8_transmitter = transmitters[0]
sxm_9_transmitter = transmitters[1]
sxm_10_transmitter = transmitters[2]
# -

# ## Check for interference

# There are several methods through which you can determine the impact of interference on a system.
# For more complex systems, you can use a Comm System to model dynamically configured communications
# links between constellations of transmitters and receivers. However, for less complex systems, like
# the one in this scenario, you can compute interference effects directly in a Receiver object.

# Add interference sources to the receiver

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

# Determine the impact of interference with a Link Budget - Interference report

# +
access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()

provider = access.data_providers.item("Link Information")
link_budget_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
link_budget_report[["ber", "ber+i"]]
# -

# ## Mitigate interference with a spectrum filter

# Use a butterworth filter

# +
receiver_model.enable_filter = True
receiver_model.filter_component_linking.set_component("Butterworth")
ship_receiver_filter = receiver_model.filter_component_linking.component
# -

# Then, set the filter properties:

# +
ship_receiver_filter.upper_bandwidth_limit = 20
ship_receiver_filter.lower_bandwidth_limit = -20
ship_receiver_filter.cut_off_frequency = 5
ship_receiver_filter.order = 4
# -

# Recompute the Link Budget - Interference report

# +
access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()

provider = access.data_providers.item("Link Information")
link_budget_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
link_budget_report[["ber", "ber+i"]]
# -

# ## Model the ship's radar

# First, insert a radar object

# +
from ansys.stk.core.stkobjects import Radar


ship_radar = ship.children.new(STKObjectType.RADAR, "Ship_Radar")
# -

# Next, set the radar's mode

# +
ship_radar.model_component_linking.set_component("Monostatic")
monostatic_radar = ship_radar.model_component_linking.component
monostatic_radar.mode_component_linking.set_component("Search Track")
monostatic_search_track_radar = monostatic_radar.mode_component_linking.component
monostatic_search_track_radar.waveform.pulse_definition.pulse_width = 8.8e-7
# -

# Then, set the goal signal-to-noise ratio

# +
monostatic_search_track_radar.waveform.pulse_integration.snr = 20
# -

# Configure the radar's antenna

# +
from ansys.stk.core.stkobjects import AntennaControl, AntennaModelExternal


antenna_control = ship_radar.model_component_linking.component.antenna_control
antenna_control.embedded_model_component_linking.set_component(
    "External Antenna Pattern"
)

external_model = AntennaModelExternal(
    antenna_control.embedded_model_component_linking.component
)
external_model.design_frequency = 2.8
# -

# Select the external pattern file

# +
import pathlib


install_dir = root.execute_command("GetDirectory / STKHome")[0]
external_model.filename = str(
    pathlib.Path(install_dir)
    / "Data"
    / "Resources"
    / "stktraining"
    / "samples"
    / "ASR9Low.pattern"
)
# -

# Set the radar antenna's location

# +
root.units_preferences.item("SmallDistance").set_current_unit("ft")

antenna_control.embedded_model_orientation.position_offset.set(37, 0, 120)
# -

# Set the radar transmitter specifications

# +
from ansys.stk.core.stkobjects import RadarFrequencySpecificationType, RadarReceiver


radar_transmitter = ship_radar.model_component_linking.component.transmitter
radar_transmitter.frequency_specification = RadarFrequencySpecificationType.FREQUENCY

radar_transmitter.frequency = 2.8
radar_transmitter.power = 100.414
# -

# Change the radar receiver LNA gain

# +
radar_receiver = ship_radar.model_component_linking.component.receiver
radar_receiver.lna_gain = 25
# -

# ## Define the missile's radar cross section

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


rcs_band = Test_Missile.radar_cross_section.model_component_linking.component.frequency_bands.item(
    0
)
# -

# Use an external file for the radar cross section.

# +
rcs_band.set_compute_strategy("External File")

external_file_compute_strategy = rcs_band.compute_strategy
external_file_compute_strategy.filename = str(
    pathlib.Path(install_dir)
    / "Data"
    / "Resources"
    / "stktraining"
    / "samples"
    / "Basic_Missile_mono.rcs"
)
# -

# ## Compute access

# Determine if the ship's radar can track the test missile.

# +
access = ISTKObject(ship_radar).get_access_to_object(Test_Missile)
access.compute_access()
# -

# ## Create a custom report

# Create a custom report style that shows azimuth-elevation-range (AER) and Radar Search/Track data.

# First, we will generate the AER Data portion of the report.

# +
provider = access.data_providers.item("AER Data").group.item("BodyFixed")
aer_and_search_track_data = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
print(aer_and_search_track_data[["time", "azimuth", "elevation", "range"]])
# -

# Second, we will generate the Radar SearchTrack portion of the report.

# +
root.units_preferences.item("Distance").set_current_unit("km")

provider = access.data_providers.item("Radar SearchTrack")
aer_and_search_track_data = provider.execute(
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
aer_and_search_track_data = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
print(aer_and_search_track_data[["rcs"]])
# -
