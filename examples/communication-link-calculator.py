# # Communication link budget calculator

# This tutorial demonstrates how to model a communications system including transmitters and receivers, and calculate link budgets considering factors like terrain, rain models, and atmospheric losses using Python and PySTK. It is inspired by [this](https://help.agi.com/stk/Content/training/StartCommunications.htm) tutorial.

# ## What are communications links, and how are they evaluated?

# Communication links define the ways that a transmitter and a receiver access each other. STK allows the modeling of two kinds of links: basic and multi-hop. A basic communications link is access between just a single transmitter and a single receiver. A multi-hop communications link is defined by a group of communication objects consisting of a transmitter, receiver, re-transmitter, and another receiver. STK also allows setting constraints on communication links, including terrain masking constraints.
#
# Communications links in STK can be analyzed using link budget reports, which include all the link parameters associated with the selected receiver or transmitter. Link budget reports take light speed delay into account. They also take computed refraction into account if enabled on the transmitter or receiver objects. Link budget reports include many communications-specific fields, including EIRP (effective isotropic radiated power in the link direction), C/N (Carrier-to-Noise ratio at the receiver input), Eb/No (Signal-to-Noise ratio at the receiver), and BER (Bit Error Rate). Link budget reports can also include access-specific information, such as the loss calculated by different selected models, including atmospheric, rain, cloud/fog, and terrain models. 

# ## Problem statement

# A team of scientists is monitoring glacial meltwater in a remote, mountainous location (latitude $47.5605^\circ$, longitude $11.5027^\circ$). They need to determine how their location impacts a link budget between them and a low earth orbit (LEO), Earth observation satellite which is downloading data to the team. The satellite has a simple transmitter with an isotropic antenna pattern, a frequency of $1.7045$ GHz, an EIRP of $10$ dBW, a data rate of $4.2$ Mb/sec, and a right-hand circular polarization. The camp's receiver is steerable, points at the satellite, and is placed on a half power sensor located $6$ ft above the ground, with a frequency of $1.7045$ GHz and $1.6$ m. The receiver has a parabolic antenna with a design frequency of $1.7$ GHz, a $1.6$ m diameter, and right-hand circular polarization.
#
# Model and analyze a link budget between the ground site and the Earth observation satellite, taking into account different factors such as terrain, rain and atmospheric absorption, and system noise temperature from sun, atmosphere, rain, and cosmic background.

# ## Launch a new STK instance

# Start by launching a new STK instance. In this example, STKEngine is used.

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(noGraphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario

# Create a new scenario in STK by running:

root = stk.new_object_root()
root.new_scenario("Communications")

# Once the scenario is created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


globe = GlobeWidget(root, 640, 480)
globe.show()
# -

# ## Set the scenario time period

# Using the newly created scenario, set the start and stop times. Rewind the scenario so that the graphics match the start and stop times of the scenario:

scenario = root.current_scenario
scenario.set_time_period("15 Mar 2024 06:00:00.000", "16 Mar 2024 06:00:00.000")
root.rewind()

# ## Add analytical and visual terrain

# Use an STK terrain file (file extension .pdtt) included with the STK install to add analytical terrain to the scenario. The file contains information on the terrain around the scientists' camp site. Use a Connect command to find the path to the RaistingStation.pdtt file:

# +
import pathlib
from ansys.stk.core.stkobjects import TERRAIN_FILE_TYPE


install_dir = root.execute_command("GetDirectory / STKHome")[0]
terrain_path = str(pathlib.Path(install_dir) / "Data" / "Resources" / "stktraining" / "imagery" / "RaistingStation.pdtt")
# -

# Then, add the file to the Earth central body's terrain collection:

terrain = scenario.terrain.item('Earth').terrain_collection.add(terrain_path, TERRAIN_FILE_TYPE.PDTT_TERRAIN_FILE)

# This file is used for analysis by default after it is inserted.

# ## Add a satellite

# The Earth observation satellite is in a sun-synchronous orbit. It can thus be modelled by an SGP4 propagator, which is used for LEO satellites. The satellite communicating with the camp has a common name of TerraSarX, which corresponds to a space surveillance catalog number of 31698.

# To add the satellite, first insert a satellite object:

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE, VEHICLE_PROPAGATOR_TYPE


satellite = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "TerraSarX_31698")
# -

# Then, set the satellite's propagator to the SGP4 propagator:

satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_SGP4)
propagator = satellite.propagator

# Finally, use the propagator's `common_tasks` property to add the satellite's orbit from an online source, and propagate the satellite:

propagator.common_tasks.add_segs_from_online_source("31698")
propagator.propagate()

# ## Add the camp site

# Add a place object to represent the camp site:

camp_site = root.current_scenario.children.new(STK_OBJECT_TYPE.PLACE, "CampSite")

# Assign the site's position to latitude $47.5605^\circ$ and longitude $11.5027^\circ$, with an elevation of $6$ ft ($0.0018288$ km) to simulate the height of the equipment at the site:

camp_site.position.assign_planetodetic(47.5605, 11.5027, 0.0018288)

# ## Model a simple transmitter

# The satellite has a simple transmitter model, a model type which uses an isotropic, omnidirectional antenna, which is an ideal spherical pattern antenna with constant gain. Insert the transmitter on the satellite:

transmitter = satellite.children.new(STK_OBJECT_TYPE.TRANSMITTER, "DownloadTransmitter")

# The transmitter's `model` property now contains a `TransmitterModelSimple` object. Set the model's frequency to $1.7045$ GHz:

transmitter.model.frequency = 1.7045

# Then, set the model's EIRP, which is the effective isotropic radiated power at the output of the transmit antenna. Set the EIRP to $10$ dBW:

transmitter.model.eirp = 10

# Next, set the model's data rate to $4.2$ Mb/sec:

transmitter.model.data_rate = 4.2

# Then, enable polarization on the model:

transmitter.model.enable_polarization = True

# Finally, set the model's polarization type to right-hand circular:

# +
from ansys.stk.core.stkobjects import POLARIZATION_TYPE


transmitter.model.set_polarization_type(POLARIZATION_TYPE.RHC)
# -

# ## Add a steerable sensor

# The receiver antenna at the camp site is steerable. To create a steering device, add a sensor object:

sensor = camp_site.children.new(STK_OBJECT_TYPE.SENSOR, "ServoMotor")

# Then, set the sensor's pattern to a half power pattern, which is designed to visually model parabolic antennas. The sensor half angle is determined by frequency and antenna diameter.

# +
from ansys.stk.core.stkobjects import SENSOR_PATTERN


sensor.set_pattern_type(SENSOR_PATTERN.HALF_POWER)
# -

# The sensor's `pattern` property now holds a `SensorHalfPowerPattern` object, through which it is possible to configure the half power model. First, set the sensor's frequency to $1.7045$ GHz:

sensor.pattern.frequency = 1.7045 

# Then, set the sensor's antenna diameter to $1.6$ m:

sensor.pattern.antenna_diameter = 1.6

# The sensor is steerable and tracks the satellite, so set the sensor's pointing type to targeted:

# +
from ansys.stk.core.stkobjects import SENSOR_POINTING


sensor.set_pointing_type(SENSOR_POINTING.POINT_TARGETED)
# -

# The sensor's `pointing` property now holds a `SensorPointingTargeted` object, through which it is possible to set the satellite as the sensor's target:

sensor.pointing.targets.add('Satellite/TerraSarX_31698')

# ## Calculate access

# Get and compute the access between the camp site's sensor and the satellite:

sensor_to_satellite_access = sensor.get_access_to_object(satellite)
sensor_to_satellite_access.compute_access()

# Then, get the access data during the entire scenario as a dataframe:

sensor_to_satellite_access_df = sensor_to_satellite_access.data_providers.item("Access Data").exec(scenario.start_time, scenario.stop_time).data_sets.to_pandas_dataframe()
sensor_to_satellite_access_df

# The sensor is able to access the satellite six times throughout the duration of the scenario.

# The access between the sensor and the satellite can be seen in the 3D graphics window approximately 1389 seconds after the scenario begins:

root.current_time = 1389.458394
globe.camera.position = [2703.568833967754, -5862.711497073381, 9424.82507431983]
globe.show()

# ## Model the receiver

# The sensor's receiver is modelled using a complex receiver model, which allows selecting among a variety of analytical and realistic antenna models and defining the characteristics of the selected antenna type.

# First, add the receiver on the sensor:

receiver = sensor.children.new(STK_OBJECT_TYPE.RECEIVER, "DownloadReceiver")

# Then, set the receiver's model type to the complex receiver model:

receiver.set_model("Complex Receiver Model")

# Next, use the model's `antenna_control` property to set the receiver's embedded model to a parabolic antenna:

receiver.model.antenna_control.set_embedded_model("Parabolic")

# The receiver model's antenna control's `embedded_model` property now holds an `AntennaModelParabolic` object, through which it is possible to configure the antenna model. First, configure the antenna model to use diameter as its input type: 

# +
from ansys.stk.core.stkobjects import ANTENNA_MODEL_INPUT_TYPE


receiver.model.antenna_control.embedded_model.input_type = ANTENNA_MODEL_INPUT_TYPE.DIAMETER
# -

# Then, set the diameter to $1.6$ m:

receiver.model.antenna_control.embedded_model.diameter = 1.6

# Set the design frequency to $1.7$ GHz:

receiver.model.antenna_control.embedded_model.design_frequency = 1.7

# Next, enable the use of polarization on the receiver model:

receiver.model.enable_polarization = True

# The receiver's polarization type is the same as the transmitter's polarization, so set the model's polarization type to right-hand circular:

receiver.model.set_polarization_type(POLARIZATION_TYPE.RHC)

# ## Calculate access

# Get and calculate the access between the receiver and transmitter:

receiver_basic_access = receiver.get_access_to_object(transmitter)
receiver_basic_access.compute_access()

# Then, get the link information for the access for the entire scenario, using a time step of $30$ s:

receiver_basic_link_df = receiver_basic_access.data_providers.item("Link Information").exec(scenario.start_time, scenario.stop_time, 30).data_sets.to_pandas_dataframe()

# Get the columns corresponding to time, atmospheric loss (atmos loss), rain loss, EIRP in the link direction (eirp), received isotropic power at the receiver antenna (rcvd. iso. power), power flux density at the receiver antenna (flux density), receiver gain over equivalent noise temperature (g/T), carrier-to-noise density at the receiver input (c/no), bandwidth, carrier-to-noise ratio at the receiver input (c/n), signal-to-noise ratio at the receiver (eb/no), bit error rate (ber), and calculated system noise temperatures (tatmos, train, tsun, tearth, tcosmic, tantenna, tequivalent):

link_budget_columns = ['time', 'atmos loss', 'rain loss','eirp', 'rcvd. frequency', 'rcvd. iso. power', 'flux density', 'g/t', 'c/no', 
                       'bandwidth', 'c/n', 'eb/no', 'ber', 'tatmos', 'train', 'tsun', 'tearth', 'tcosmic', 'tantenna', 'tequivalent']
receiver_basic_link_df.head(10)[link_budget_columns]

# The dataframe now shows information corresponding to an STK link budget report. From the data, it is possible to see that as the satellite rises over the horizon of the central body, the site receives transmissions. When the satellite falls below the horizon, the site loses transmissions. Additionally, because the access calculation does not include any environmental factor models or system noise temperature considerations, the columns corresponding to the losses/noise all have values of 0.

# ## Add terrain to the analysis

# Next, add a terrain mask to the receiver to add terrain into the access analysis. A terrain mask causes STK to constrain access to an object by any terrain data in the line of sight to which access is being calculated. Add a terrain mask access constraint:

# +
from ansys.stk.core.stkobjects import ACCESS_CONSTRAINTS


terrain_constraint = receiver.access_constraints.add_constraint(ACCESS_CONSTRAINTS.TERRAIN_MASK)
# -

# Recalculate the access between the receiver and transmitter, then get the data corresponding to a link budget report:

receiver_basic_access.compute_access()
receiver_terrain_link_df = receiver_basic_access.data_providers.item("Link Information").exec(scenario.start_time, scenario.stop_time, 30).data_sets.to_pandas_dataframe()
receiver_terrain_link_df.head(10)[link_budget_columns]

# Next, get the access data for the updated access:

receiver_basic_access.data_providers.item("Access Data").exec(scenario.start_time, scenario.stop_time).data_sets.to_pandas_dataframe()

# Before adding a terrain mask, there were 6 accesses between the receiver and transmitter. By adding a terrain mask, the accesses blocked by terrain have been removed from the report, and there are now only 4 accesses between the receiver and transmitter.

# ## Model environmental factors

# Environmental factors can affect the performance of a communications link. In STK, it is possible to enable or disable the use of different environmental factors at three levels: scenario, platform (facilities, places, targets, and all vehicles except satellites), and subobject (transmitter, receiver, radar, and antenna). In this case, since the scenario only includes a single receiver/transmitter pair, set the environmental factors at the scenario level.

# First, add a rain model, which is used to estimate the amount of degradation (or fading) of signal when passing through rain. The degradation is primarily due to absorption by water molecules and is a function of frequency and elevation angle. Generally speaking, the rain loss increases with increasing frequency. The loss also increases with decreasing ground elevation angle due to a greater path distance through the portion of the atmosphere where rain occurs. Rain also causes an increase in the antenna noise temperature. Set the `enable_rain_loss` property to `True` on the scenario's RF environment's propagation channel:

scenario.rf_environment.propagation_channel.enable_rain_loss = True

# Then, enable the use of the atmospheric absorption model:

scenario.rf_environment.propagation_channel.enable_atmos_absorption = True

# It is possible to configure which specific model is used for the different environmental factors. However, in this case, the default models are sufficient.

# Next, recalculate the access between the receiver and transmitter:

receiver_basic_access.compute_access()
receiver_environmental_link_df = receiver_basic_access.data_providers.item("Link Information").exec(scenario.start_time, scenario.stop_time, 30).data_sets.to_pandas_dataframe()
receiver_environmental_link_df.head(10)[link_budget_columns]

# After adding environmental factor models, the atmospheric and rain losses are now greater than 0. However, the losses are minimal, so the losses in C/N and Eb/No are also minimal.

# ## Model system noise temperature

# The receiver's system noise temperature enables specifying the system's inherent noise characteristics, which can help simulate real-world RF situations more accurately. STK can use either a constant system noise temperature value, or can calculate it based off of different noise sources. In this case, configure the receiver model's system noise temperature to use calculated values:

# +
from ansys.stk.core.stkobjects import NOISE_TEMP_COMPUTE_TYPE


receiver.model.system_noise_temperature.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE
# -

# Do the same for the model's antenna noise temperature:

receiver.model.system_noise_temperature.antenna_noise_temperature.compute_type = NOISE_TEMP_COMPUTE_TYPE.CALCULATE

# Then, enable the use of sun, atmosphere, rain, and cosmic background in computations:

receiver.model.system_noise_temperature.antenna_noise_temperature.use_sun = True
receiver.model.system_noise_temperature.antenna_noise_temperature.use_atmosphere = True
receiver.model.system_noise_temperature.antenna_noise_temperature.use_rain = True
receiver.model.system_noise_temperature.antenna_noise_temperature.use_cosmic_background = True

# Finally, recompute the access and get the updated link information:

receiver_basic_access.compute_access()
receiver_noise_link_df = receiver_basic_access.data_providers.item("Link Information").exec(scenario.start_time, scenario.stop_time, 30).data_sets.to_pandas_dataframe()
receiver_noise_link_df.head(10)[link_budget_columns]

# There are now non-zero values in the tatmos, train, tsun, tcosmic, tantenna, and tequivalent columns. Calculating system noise temperature improved the report and extended the time available for downloading data.

# ## Plot the different link budgets

# Visualize the calculated link budgets under the different modeling factors:

# +
import matplotlib.dates as md
import matplotlib.pyplot as plt
import pandas as pd


# Create plot
fig, ax = plt.subplots()

# Format data
receiver_environmental_link_df['time'] = pd.to_datetime(receiver_environmental_link_df['time'])
receiver_environmental_link_df.sort_values(by='time', inplace=True)
receiver_terrain_link_df['time'] = pd.to_datetime(receiver_terrain_link_df['time'])
receiver_terrain_link_df.sort_values(by='time', inplace=True)
receiver_noise_link_df['time'] = pd.to_datetime(receiver_noise_link_df['time'])
receiver_noise_link_df.sort_values(by='time', inplace=True)

# Plot dataframes
receiver_environmental_link_df.plot(x='time', y='c/no', ax=ax, label='terrain, environmental', color='darkblue')
receiver_terrain_link_df.plot(x='time', y='c/no', ax=ax, label='terrain', color='deeppink')
receiver_noise_link_df.plot(x='time', y='c/no', ax=ax, label='terrain, environmental, system noise', color='palegreen')

# Configure plot style
ax.set_facecolor("whitesmoke")
ax.grid(visible=True, which="both")

# Set title and labels
ax.set_title("Carrier to Noise Ratio Over Time Under Different Models")
ax.set_xlabel("Time")
ax.set_ylabel("C/N (dB)")

# Improve x-axis formatting
formatter = md.DateFormatter("%H:%M:%S")
ax.xaxis.set_major_formatter(formatter)

# Set figure size
fig.set_size_inches(15, 8)

# Show figure
plt.show()
# -

# The model accounting for only terrain has similar C/N values to the model accounting for terrain and environmental factors, as the losses from environmental factors were minimal in this analysis. The model accounting for terrain, environmental factors, and system noise consistently had the highest C/N values, as calculating system noise temperature improved the link budget.
