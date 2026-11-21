# # Missile Interference Test

# This tutorial demonstrates how to use the STK software’s Communications capability to model interference to a communications link using PySTK. It is inspired by [this](https://help.agi.com/stk/Content/training/Missile_Test_XM_Interference.htm) tutorial.


# ## Problem statement

# Engineers and operators need to quickly model and analyze a telemetry link from a missile launch and to determine how various settings on a radar will affect its ability to track a missile. You are launching a test missile from a launch pad located on the Pacific Coast of the United States. The missile will transmit telemetry data to a communications system on board a ship anchored off the coast. The missile’s telemetry data will be transmitted on an S-band frequency, which is close to a frequency used by multiple high-power satellite digital audio radio service (SDARS) satellites. Phase one of your test will determine if the satellites, which provide XM radio service, will interfere with ship’s ability to receive the test missile telemetry data. Phase two of your test will determine for how long a shipborne radar system can detect and track the missile during its flight. A custom radar cross section and a radar antenna pattern file are required for your analysis.

# ## Launching a new STK application instance

# Start by launching a new instance of the STK application. In this example, the STK Engine technology platform is used.

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# ## Creating a new scenario

# Create an STK scenario using the STK Root object:

# +
root = stk.new_object_root()
root.new_scenario("CommRadar_MissileTest_Interference")
# -

# Once the scenario is created, you can view a 3D Graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


globe_widget = GlobeWidget(root, 640, 480)
globe_widget.camera.position = [0, 0, 0]
globe_widget.show()
# -

# Show a 2D Graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import MapWidget


map_widget = MapWidget(root, 640, 480)
map_widget.show()
# -

# ## Setting the scenario time period

# Using the newly created scenario, set the start and stop times. Rewind the scenario so that the graphics match the start and stop times of the scenario:

# +
scenario = root.current_scenario
scenario.set_time_period("10 June 2026 16:00:00.000", "10 June 2026 16:35:00.000")
root.rewind()
# -

# ## Modeling the test missile

# The missile is launched from Vandenberg Space Force Base in California and ditches in the ocean upon completion of the test.

# Insert a new Missile object:

# +
from ansys.stk.core.stkobjects import Missile, STKObjectType


test_missile = scenario.children.new(STKObjectType.MISSILE, "test_missile")
# -

# First, set the units properly. Setting units proactively is best practice!

# +
root.units_preferences.item("Latitude").set_current_unit("deg")
root.units_preferences.item("Longitude").set_current_unit("deg")
root.units_preferences.item("Distance").set_current_unit("km")
# -

# Next, design the missile’s trajectory:

# +
from ansys.stk.core.stkobjects import (
    IPropagator,
    PropagatorType,
    VehicleImpactLocationPoint,
    VehicleLaunchControl,
)


test_missile.set_trajectory_type(PropagatorType.BALLISTIC)
trajectory = test_missile.trajectory
root.units_preferences.set_current_unit("DateFormat", "EpSec")
trajectory.ephemeris_interval.set_explicit_interval(0, 0)
# -

# Set the launch parameters:

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

# Lastly, propagate the missile:

# +
trajectory.propagate()
# -

# You can now view the test missile’s trajectory:

# + tags=["nbsphinx-thumbnail"]
globe_widget.camera.position = [
    19252.274451116944,
    4639.005171788969,
    5592.340350242526,
]
globe_widget.show()
# -

# ## Generating an Altitude vs Ground Range report

# Use the “Ground Range” data provider to set up an Altitude vs Ground Range report:

# +
provider = test_missile.data_providers.item("Ground Range").group.item("Fixed")
# -

# Then, set the time step. This is set in seconds.

# +
time_step = 60
# -

# Generate the report:

# +
ground_range_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
ground_range_report[["time", "ground range", "alt"]]
# -

# ## Modeling the test missile’s transmitter

# Attach a Transmitter object to the missile:

# +
from ansys.stk.core.stkobjects import Transmitter


missile_transmitter = test_missile.children.new(STKObjectType.TRANSMITTER, "Missile_Tx")
# -

# Use a Medium Transmitter model, for which you specify gain and power separately instead of entering their product (EIRP) directly:

# +
missile_transmitter.model_component_linking.set_component("Medium Transmitter Model")
transmitter_model = missile_transmitter.model_component_linking.component
# -

# Set the transmitter’s properties:

# +
transmitter_model.frequency = 2.31
transmitter_model.power = 19.03
transmitter_model.antenna_gain = -0.57
transmitter_model.data_rate = 2.048
# -

# Set the transmitter modulation options:

# +
transmitter_model.set_modulator("BPSK")
transmitter_model.modulator.enable_signal_psd = True
# -

# ## Modeling the ship

# The ship is anchored off the coast of California, where it is serving as a test location for your communications and radar equipment.

# Insert a new Ship object

# +
from ansys.stk.core.stkobjects import Ship


ship = scenario.children.new(STKObjectType.SHIP, "Ship")
# -

## Defining the ship’s route options

# The ship remains stationary throughout the duration of the test. First, set the propogator type to Great Arc:

# +
from ansys.stk.core.stkobjects import (
    IGreatArcVehicle,
    PropagatorGreatArc,
    PropagatorType,
    VehicleWaypointComputationMethod,
)


IGreatArcVehicle(ship).set_route_type(PropagatorType.GREAT_ARC)
# -

# Second, set its altitude reference:

# +
from ansys.stk.core.stkobjects import VehicleAltitudeReference


ship.route.set_altitude_reference_type(VehicleAltitudeReference.WGS84)
# -

# Now, propagate the route. Set the latitude, longitude, and the start and stop times.

# +
PropagatorGreatArc(IGreatArcVehicle(ship).route).set_points_specify_time_and_propagate(
    [
        [scenario.start_time, 34.196, -120, 0, 0],
        [scenario.stop_time, 34.196, -120, 0, 0],
    ]
)
# -

# Inserting a Sensor object

# The receiver on the ship is steerable. To create a steering device representing a servo motor, attach a Sensor object to the ship:

# +
from ansys.stk.core.stkobjects import Sensor, SensorPattern, SensorSimpleConicPattern


antenna_motor = ship.children.new(STKObjectType.SENSOR, "Antenna_Motor")
# -

# Define the sensor’s cone half angle to model a 10-degree field of view:

# +
antenna_motor.set_pattern_type(SensorPattern.SIMPLE_CONIC)
SensorSimpleConicPattern(antenna_motor.pattern).cone_angle = 5
# -

# Set the antenna motor’s location type to fixed:

# +
from ansys.stk.core.stkobjects import SensorLocation


antenna_motor.set_location_type(SensorLocation.FIXED)
# -

# After the location type is set to fixed, the location is editable using cartesian coordinates:

# +
root.units_preferences.item("Distance").set_current_unit("ft")
antenna_motor.location_data.assign_cartesian(75, 0, 75)
# -

# Target the test missile using the Receive track mode. The Track Mode specifies how you want to orient the antenna. Setting it to Receive orients it slightly “behind” the current location of the other object. The STK application computes the appropriate amount by which to lead or trail based on the light time delay. Access computations including the computation of targeting times are performed based on the sensor being the receiver of the signal.

# +
from ansys.stk.core.stkobjects import BoresightType, TrackMode


antenna_motor.common_tasks.set_pointing_targeted_tracking(
    TrackMode.RECEIVE, BoresightType.ROTATE, "Missile/test_missile"
)
# -

# You can view the targeted antenna in the 3D Graphics window:

# +
globe_widget.camera.position = [
    16443720.539118323,
    5550468.64120438,
    11651969.751643106,
]
globe_widget.show()
# -

# ## Model the test ship’s receiver

# Attach a Receiver object to the “Antenna_Motor” sensor.

# +
from ansys.stk.core.stkobjects import Receiver


ship_receiver = antenna_motor.children.new(STKObjectType.RECEIVER, "Ship_Rx")
# -

# Use a Complex Receiver model, which allows you to set a variety of analytical and realistic antenna models and to define the characteristics of the selected antenna type.

# +
ship_receiver.model_component_linking.set_component("Complex Receiver Model")
receiver_model = ship_receiver.model_component_linking.component
# -

# One the type is set, you can edit its properties. Set the receiver track and lock onto the transmitter’s carrier frequency with the `track_frequency_automatically` property:

# +
receiver_model.track_frequency_automatically = True
# -

# Define the receiver’s antenna specifications. First, set the antenna model to Helix:

# +
from ansys.stk.core.stkobjects import AntennaModelHelix, IAntennaModel


receiver_model.antenna_control.embedded_model_component_linking.set_component("Helix")
helix_model = receiver_model.antenna_control.embedded_model_component_linking.component
# -

# Once the antenna model is set to `Helix`, you can edit its properties:

# +
IAntennaModel(helix_model).design_frequency = 2.5
helix_model.diameter = 0.9
helix_model.efficiency = 55
helix_model.turn_spacing = 0.001
helix_model.number_of_turns = 3
helix_model.backlobe_gain = -30
# -

# Visualize the receiver’s antenna pattern. First define a volume variable:

# +
from ansys.stk.core.stkobjects import AntennaVolumeGraphics


volume = ship_receiver.graphics_3d.volume
# -

# Before anything else, you must set the `volume.show property` to “true.” Once this is set, you can edit the rest of the graphic properties.

# +
volume.show = True
volume.gain_scale = 0.5
# -

# You are now able to edit the pattern properties. These can be set all together at once:

# +
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
# -

# Next, add levels to the shading:

# +
levels = volume.levels
levels.clear()

for gain in range(-70, 1, 10):
    level = levels.add(gain)
# -

# ## Analyzing the telemetry downlink’s link budget

# Create a simple link budget to calculate the bit error rate (BER), which reflects how often errors occur in the transmission of digital data. You can compute a Simple Link Budget using the Access tool. For the purposes of this analysis, a Bit Error Rate of 1.000000e-09 or lower is acceptable.

# First, create and compute access between the ship’s receiver and the missile’s transmitter:

# +
from pandas import DataFrame

from ansys.stk.core.stkobjects import Access, ISTKObject


access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()
# -

# After computing access, use the Link Information data provider to retrieve the data:

# +
provider = access.data_providers.item("Link Information")
# -

# Finally, create and generate the Link Budget report.

# +
link_budget_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
# -

# Focus on the ber column:

# +
link_budget_report[["ber"]]
# -

# ## Insert the interfering satellites

# Get the STK application’s Satellite database location using a Connect command:

# +
from pathlib import Path

from ansys.stk.core.stkobjects import ExecuteCommandResult


result = root.execute_command("GetDirectory / Database Satellite")
satellite_data_dir = result[0]
file_location = '"' + str(Path(satellite_data_dir) / Path(r"stkAllTLE.sd")) + '"'
# -

# Import the relevant Satellite objects from the database using Connect commands:

# +
command = f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-8"
root.execute_command(command)

command = f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-9"
root.execute_command(command)

command = f"ImportFromDB * Satellite {file_location} Propagate On CommonName SXM-10"
root.execute_command(command)
# -

# Assign the satellites to variables:

# +
from ansys.stk.core.stkobjects import Satellite


sxm_8 = scenario.children.item("SXM-8_48838")
sxm_9 = scenario.children.item("SXM-9_62259")
sxm_10 = scenario.children.item("SXM-10_64290")
# -

# ## Model the interfering satellites’ transmitters, which, like that on the test missile, use a Medium Transmitter model:

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

# Assign the satellite transmitters to the existing satellite variables:

# +
sxm_8_transmitter = transmitters[0]
sxm_9_transmitter = transmitters[1]
sxm_10_transmitter = transmitters[2]
# -

# ## Checking for interference

# There are several methods through which you can determine the impact of interference on a system. For less complex systems, like the one in this scenario, you can compute interference effects directly in a Receiver object.

# Create an interference variable. Use this to modify the interference on the receiver.

# +
from ansys.stk.core.stkobjects import ISTKObject, RFInterference


interference = RFInterference(
    ship_receiver.model_component_linking.component.interference
)
# -

# You have to enable interference in the Receiver object before you can add and edit the interference sources:

# +
interference.enabled = True
# -

# Only now are you able to add the interference sources.

# +
interference.emitters.add(sxm_8_transmitter.path)
interference.emitters.add(sxm_9_transmitter.path)
interference.emitters.add(sxm_10_transmitter.path)
# -

# Determine the impact of interference with a Link Budget - Interference report. First, compute access:

# +
access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()
# -

# Next, retrieve the Link Information data provider to generatea a Link Budget - Interference report:

# +
provider = access.data_providers.item("Link Information")
# -

# +
link_budget_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
# -

# Focus on the ber and ber+i columns. BER column shows the link performance without interference while the BER + I shows the link performance with interference.


# +
link_budget_report[["ber", "ber+i"]]
# -

# The difference between the BER values with and without interference shows that interference has a major impact on the quality of the communications link.

# ## Mitigating interference with a spectrum filter

# To use a spectrum filter, you must first enable it:

# +
receiver_model.enable_filter = True
# -

# You are now able to set the filter type. Use a Butterworth filter:

# +
receiver_model.filter_component_linking.set_component("Butterworth")
ship_receiver_filter = receiver_model.filter_component_linking.component
# -

# Then, set the Butterworth filter’s properties:

# +
ship_receiver_filter.upper_bandwidth_limit = 20
ship_receiver_filter.lower_bandwidth_limit = -20
ship_receiver_filter.cut_off_frequency = 5
ship_receiver_filter.order = 4
# -

# Recompute the Link Budget - Interference report. The access must be refreshed first.

# +
access = ISTKObject(ship_receiver).get_access_to_object(missile_transmitter)
access.compute_access()
# -

# Then retrieve the Link Information data provider:

# +
provider = access.data_providers.item("Link Information")
# -

# Generate the Link Budget - Interference report:

# +
link_budget_report = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
# -

# Focus on the ber and ber+i columns:

# +
link_budget_report[["ber", "ber+i"]]
# -

# ## Modeling the ship’s radar

# First, attach a Radar object to the ship:

# +
from ansys.stk.core.stkobjects import Radar


ship_radar = ship.children.new(STKObjectType.RADAR, "Ship_Radar")
# -

# Next, set the Radar object as a Monostatic radar system:

# +
ship_radar.model_component_linking.set_component("Monostatic")
monostatic_radar = ship_radar.model_component_linking.component
# -

# Once the radar system is set to Monostatic, you can specify the mode. Set a Search Track Radar Monostatic mode:

# +
monostatic_radar.mode_component_linking.set_component("Search Track")
monostatic_search_track_radar = monostatic_radar.mode_component_linking.component
# -

# Only after setting the mode to Search Track can you modify its properties. Set the pulse width, which is a waveform pulse definition property:

# +
monostatic_search_track_radar.waveform.pulse_definition.pulse_width = 8.8e-7
# -

# Then, set the goal signal-to-noise ratio, which is a wavform pulse integration property:

# +
monostatic_search_track_radar.waveform.pulse_integration.snr = 20
# -

# Configure the radar’s antenna model to use an External Antenna Pattern component:

# +
from ansys.stk.core.stkobjects import AntennaControl, AntennaModelExternal


antenna_control = ship_radar.model_component_linking.component.antenna_control
antenna_control.embedded_model_component_linking.set_component(
    "External Antenna Pattern"
)

external_model = AntennaModelExternal(
    antenna_control.embedded_model_component_linking.component
)
# -

# Once an external pattern is selected, set its design frequency:

# +
external_model.design_frequency = 2.8
# -

# Then, specify the file from which the pattern will be provided. The ASR9Low.pattern file is included with the STK software install and uses a Symmetric antenna pattern format.

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

# Next, set the radar antenna’s orientation properties:

# +
root.units_preferences.item("SmallDistance").set_current_unit("ft")

antenna_control.embedded_model_orientation.position_offset.set(37, 0, 120)
# -

# Configure the radar transmitter:

# +
from ansys.stk.core.stkobjects import RadarFrequencySpecificationType, RadarReceiver


radar_transmitter = ship_radar.model_component_linking.component.transmitter
# -

# Set the radar transmitter’s specifications. First, select frequency as the independent property. The radar's wavelength will depend on its frequency.

# +
radar_transmitter.frequency_specification = RadarFrequencySpecificationType.FREQUENCY

radar_transmitter.frequency = 2.8
# -

# Set the power of the radar transmitter. This does not depend on frequency or wavelength.

# +
radar_transmitter.power = 100.414
# -

# Configure the radar’s receiver:

# +
radar_receiver = ship_radar.model_component_linking.component.receiver
# -

# Adjust the value for the gain introduced by the receiver’s Low Noise Amplifier (LNA):

# +
radar_receiver.lna_gain = 25
# -

# ## Defining the missile’s radar cross section

# The Radar capability enables you to specify an important property of a potential radar target: its radar cross section (RCS). You can define the missile’s RCS using an external RCS file. External RCS files can contain real-valued pattern data or complex-valued pattern data.

# First, the missile must not inherit its cross section from the Scenario properties so you can specify its properties yourself:

# +
test_missile.radar_cross_section.inherit = False
# -

# Create a `rcs_band` variable to manage the radar cross section properties:

# +
from ansys.stk.core.stkobjects import (
    RadarCrossSectionComputeStrategyExternalFile,
    RadarCrossSectionFrequencyBand,
)


rcs_band = test_missile.radar_cross_section.model_component_linking.component.frequency_bands.item(
    0
)
# -

# Select an external file for the radar cross section.

# +
rcs_band.set_compute_strategy("External File")

external_file_compute_strategy = rcs_band.compute_strategy
external_file_compute_strategy.filename = str(
    pathlib.Path(install_dir)
    / "Data"
    / "Resources"
    / "stktraining"
    / "samples"
    / "Basic_missile_mono.rcs"
)
# -

# ## Computubg access

# Determine if the ship’s radar can track the test missile by computing access:

# +
access = ISTKObject(ship_radar).get_access_to_object(test_missile)
access.compute_access()
# -

# ## Creating a custom report

# Create a custom report style that shows azimuth-elevation-range (AER) and Radar Search/Track data. First, generate the AER Data portion of the report.

# +
provider = access.data_providers.item("AER Data").group.item("BodyFixed")
aer_and_search_track_data = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
print(aer_and_search_track_data[["time", "azimuth", "elevation", "range"]])
# -

# Second, generate the Radar SearchTrack portion of the report.

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

# Finally, generate the Radar RCS portion of the report.

# +
provider = access.data_providers.item("Radar RCS")
aer_and_search_track_data = provider.execute(
    scenario.start_time, scenario.stop_time, time_step
).data_sets.to_pandas_dataframe()
print(aer_and_search_track_data[["rcs"]])
# -
