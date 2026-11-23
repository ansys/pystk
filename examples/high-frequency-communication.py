# %% [markdown]
# # Evaluate high-frequency communication links
#
# This tutorial demonstrates how to predict high-frequency (HF) communication link performance. It is inspired by [this tutorial](https://help.agi.com/stk/Content/training/STK_Comms_VOACAP.htm).

# %% [markdown]
# ## How can HF radios communicate beyond line of sight?
#
# High-frequency radio can use more than a direct, straight path by sending a signal upward to the ionosphere, a layer of the upper atmosphere that can bend some radio signals back toward Earth. This returned signal is called a skywave. In this way, HF radio can reach a receiver behind mountains or beyond the horizon.
#
# A near-vertical incidence skywave (NVIS) goes up at a high angle and can serve an area up to about $650~\mathrm{km}$ from its transmitter. It is useful when local terrain blocks a direct ground-to-ground path. A low-angle skywave travels farther, as it can bounce between the ionosphere and Earth more than once, supporting communication over thousands of kilometers. Each cycle of a skywave traveling to the ionosphere and bouncing back to the surface of the Earth is called a hop. Additionally, the ionosphere has multiple layers, each absorbing different frequencies. Absorption is also dependent on time of day. Designing a high-frequency communication system requires taking into account these layers as well as optimizing the number of hops of the skywaves.
#
# To do so, engineers may use VOACAP (Voice of America Coverage Analysis Program), a propagation prediction software that estimates how an HF skywave will behave. It considers the time of day, season, solar activity, transmitter and receiver locations, and the ionosphere. It also has the ability to compute simulation results for multiple alternative frequencies other than those actually in use by a system, allow for optimization of frequency design choices. STK features built-in interoperability with VOACAP, enabled for the transmitter, receiver, antenna, access, and coverage models to estimate the quality of a communication system over time.

# %% [markdown]
# ## Problem statement
#
# Engineers are designing an HF communication site in Los Angeles, USA, which will feature both transmitters and receivers. They want to assess the site's equipment for three different use cases:
#
# 1. The Los Angeles site receives communications from Palmdale, California, approximately $60~\mathrm{km}$ away. Mountainous terrain blocks direct line of sight.
# 2. The Los Angeles site transmits to Landstuhl, Germany, approximately $9{,}480~\mathrm{km}$ away.
# 3. The Los Angeles site transmits to a large region covering parts of Europe, Asia, and Africa.
#
# For the short-range link from Palmdale to Los Angeles, use an NVIS link. Configure the transmitter for $10~\mathrm{MHz}$, $1~\mathrm{W}$, and $5~\mathrm{Mb/s}$. Use horizontal dipoles at both endpoints, with $23~\mathrm{m}$ dipoles, a $6.5~\mathrm{MHz}$ design frequency, and $80\%$ efficiency.
#
# For the long-range link from Los Angeles to Landstuhl, use low-angle, long-range transmission to evaluate multihop propagation. Configure the Los Angeles transmitter for $20~\mathrm{MHz}$, $100~\mathrm{W}$, and $1~\mathrm{Mb/s}$. Use a directional antenna with a $15~\mathrm{MHz}$ design frequency and $65^\circ$ azimuth. At Landstuhl, use a horizontal dipole receiver with a $20~\mathrm{MHz}$ design frequency, $9~\mathrm{m}$ length, and $80\%$ efficiency.
#
# For the regional service analysis, compute maximum received isotropic power from the long-range transmitter over a $4^\circ$ grid from $35^\circ$ south to $65^\circ$ north and from $20^\circ$ west to $90^\circ$ east.
#
# For each analysis, determine suitable transmission frequencies for the antenna ranges used and local-time conditions during the analysis. Then assess whether the long-range system can provide strong regional service for the area of interest.

# %% [markdown]
# ## Launch a new STK instance
#
# Start by launching a new STK instance. In this example, `STKEngine` is used.

# %%
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
root = stk.new_object_root()

# %% [markdown]
# ## Create a new scenario

# %% [markdown]
# Create an STK scenario using the STK root object:

# %%
root.new_scenario("HF_Analysis")
scenario = root.current_scenario

# %% [markdown]
# ## Set the scenario time period
#
# Using the newly created scenario, set the start and stop times. The scenario starts at noon local time in Los Angeles. Landstuhl is $9~\mathrm{h}$ ahead, so the same scenario time can represent daylight at one endpoint and nighttime at the other. This time difference is important when selecting long-range HF frequencies. Set the analysis interval from $15~\mathrm{Apr}~2024~19{:}00{:}00.000~\mathrm{UTCG}$ through $16~\mathrm{Apr}~2024~19{:}00{:}00.000~\mathrm{UTCG}$ and rewind:

# %%
scenario.set_time_period("15 Apr 2024 19:00:00.000", "16 Apr 2024 19:00:00.000")
root.rewind()

# %% [markdown]
# ## Configure the scenario units
#
# Set `DateFormat` to `UTCG`, `Frequency` to `GHz`, and `Power` to `dBW`:

# %%
root.units_preferences.set_current_unit("DateFormat", "UTCG")
root.units_preferences.set_current_unit("Frequency", "GHz")
root.units_preferences.set_current_unit("Power", "dBW")

# %% [markdown]
# ## Configure the VOACAP RF environment
#
# Enable the scenario atmospheric-absorption channel and select the VOACAP model.
#
# Use the default VOACAP settings except for the sunspot number and alternate-frequency option. The sunspot number used for this analysis is $79$, representing predicted solar activity levels.
#
# Configure the VOACAP model to compute alternative frequencies. It evaluates the transmission frequency plus $10$ frequencies logarithmically distributed from $2~\mathrm{MHz}$ to $30~\mathrm{MHz}$.

# %% [markdown]
#
# Set `enable_atmospheric_absorption` to `True` so the scenario propagation channel can use an HF propagation model:

# %%
propagation_channel = scenario.rf_environment.propagation_channel
propagation_channel.enable_atmospheric_absorption = True

# %% [markdown]
#
# Select the `VOACAP` atmospheric-absorption model:

# %%
voacap_linking = propagation_channel.atmospheric_absorption_model_component_linking
voacap_linking.set_component("VOACAP")
voacap = voacap_linking.component

# %% [markdown]
#
# Set the sunspot number to $79$:

# %%
voacap.solar_activity_configuration.sunspot_number = 79

# %% [markdown]
# Enable alternate-frequency computation:

# %%
voacap.compute_alternate_frequencies = True

# %% [markdown]
# ## Create the NVIS ground sites
#
# The two ground sites for the NVIS analysis are located in Los Angeles and in Palmdale. These sites are approximately $60~\mathrm{km}$ apart. Palmdale is in high desert, while Los Angeles lies in a basin near the ocean, with a mountain range separating the sites. Through NVIS radio waves, the HF path can travel up to the ionosphere and back down instead of being blocked by the mountainous terrain.
# %% [markdown]
#
# Create the Palmdale transmitter site at $34.5794^\circ$ latitude, $-118.1165^\circ$ longitude, and $0~\mathrm{km}$ of altitude:

# %%
from ansys.stk.core.stkobjects import STKObjectType


palmdale = scenario.children.new(STKObjectType.PLACE, "Palmdale")
palmdale.position.assign_geodetic(34.5794, -118.1165, 0.0)

# %% [markdown]
#
# Create the Los Angeles receiver site at $34.0522^\circ$ latitude, $-118.2437^\circ$ longitude, and $0~\mathrm{km}$ altitude:

# %%
los_angeles = scenario.children.new(STKObjectType.PLACE, "Los_Angeles")
los_angeles.position.assign_geodetic(34.0522, -118.2437, 0.0)

# %% [markdown]
# ## Configure the NVIS transmitter
#
# Add a complex transmitter at Palmdale. Configure transmission to occur at a frequency of $10~\mathrm{MHz}$, using $1~\mathrm{W}$ of power, and a data rate of $5~\mathrm{Mb/s}$. Then use a $23~\mathrm{m}$ horizontal dipole antenna that has a $6.5~\mathrm{MHz}$ design frequency and $80\%$ efficiency. The design and operating frequencies differ because the dipole represents a multiband antenna.

# %% [markdown]
#
# Create a transmitter at Palmdale and select the `Complex Transmitter Model`, which allows for selection between a variety of analytical and realistic antenna models.

# %%
near_vertical_skywave_transmitter = palmdale.children.new(
    STKObjectType.TRANSMITTER, "NVIS_HF_Tx"
)
near_vertical_skywave_transmitter.model_component_linking.set_component(
    "Complex Transmitter Model"
)
near_vertical_skywave_transmitter_model = (
    near_vertical_skywave_transmitter.model_component_linking.component
)

# %% [markdown]
#
# Set the NVIS transmitter to transmit at $0.010~\mathrm{GHz}$, $0~\mathrm{dBW}$, and $5~\mathrm{Mb/s}$:

# %%
near_vertical_skywave_transmitter_model.frequency = 0.010
near_vertical_skywave_transmitter_model.power = 0.0
near_vertical_skywave_transmitter_model.data_rate = 5.0

# %% [markdown]
#
# Select the `Dipole` antenna model for `NVIS_HF_Tx` to represent a multiband transmit antenna:

# %%
near_vertical_skywave_transmit_antenna = (
    near_vertical_skywave_transmitter_model.antenna_control
)
near_vertical_skywave_transmit_antenna.embedded_model_component_linking.set_component(
    "Dipole"
)
near_vertical_skywave_transmit_dipole = (
    near_vertical_skywave_transmit_antenna.embedded_model_component_linking.component
)

# %% [markdown]
#
# Set the NVIS transmitter dipole to $0.0065~\mathrm{GHz}$ design frequency, $23~\mathrm{m}$ length, and $80\%$ efficiency:

# %%
near_vertical_skywave_transmit_dipole.design_frequency = 0.0065
near_vertical_skywave_transmit_dipole.length = 23.0
near_vertical_skywave_transmit_dipole.efficiency = 80.0

# %% [markdown]
#
# The default dipole antenna orientation is vertical, so assign an elevation of $0^\circ$ and an azimuth of $0^\circ$ to the model orientation to make the antenna horizontal:

# %%
from ansys.stk.core.stkutil import AzElAboutBoresight


near_vertical_skywave_transmit_antenna.embedded_model_orientation.assign_az_el(
    0.0, 0.0, AzElAboutBoresight.ROTATE
)

# %% [markdown]
# ## Configure the NVIS receiver
#
# Add the matching complex receiver at Los Angeles. Its dipole uses the same design frequency, length, efficiency, and horizontal orientation as the transmit antenna. Use a Complex Receiver Model for the receiver-side antenna characteristics to participate in the link calculation.

# %% [markdown]
#
# Create a receiver at the Los Angeles site and select the `Complex Receiver Model` so its antenna characteristics participate in the link budget:

# %%
near_vertical_skywave_receiver = los_angeles.children.new(
    STKObjectType.RECEIVER, "NVIS_HF_Rx"
)
near_vertical_skywave_receiver.model_component_linking.set_component(
    "Complex Receiver Model"
)
near_vertical_skywave_receiver_model = (
    near_vertical_skywave_receiver.model_component_linking.component
)

# %% [markdown]
#
# Select the `Dipole` antenna model to match the transmit-side multiband antenna:

# %%
near_vertical_skywave_receive_antenna = (
    near_vertical_skywave_receiver_model.antenna_control
)
near_vertical_skywave_receive_antenna.embedded_model_component_linking.set_component(
    "Dipole"
)
near_vertical_skywave_receive_dipole = (
    near_vertical_skywave_receive_antenna.embedded_model_component_linking.component
)

# %% [markdown]
#
# Set the NVIS receiver dipole to $0.0065~\mathrm{GHz}$ design frequency, $23~\mathrm{m}$ length, and $80\%$ efficiency to match the transmitter antenna:

# %%
near_vertical_skywave_receive_dipole.design_frequency = 0.0065
near_vertical_skywave_receive_dipole.length = 23.0
near_vertical_skywave_receive_dipole.efficiency = 80.0

# %% [markdown]
#
# Orient the NVIS receiver dipole at $0^\circ$ azimuth and $0^\circ$ elevation to match the transmitter polarization:

# %%
near_vertical_skywave_receive_antenna.embedded_model_orientation.assign_az_el(
    0.0, 0.0, AzElAboutBoresight.ROTATE
)

# %% [markdown]
# ## Enable skywave access
#
# Because a skywave uses an over-the-horizon path, remove the default line-of-sight constraint from the transmitter and receiver. Otherwise, STK returns no access intervals for a path blocked by terrain or Earth, even when NVIS communication is possible.

# %% [markdown]
#
# Remove the `LINE_OF_SIGHT` constraint from the transmitter:

# %%
from ansys.stk.core.stkobjects import AccessConstraintType


near_vertical_skywave_transmitter.access_constraints.remove_constraint(
    AccessConstraintType.LINE_OF_SIGHT
)

# %% [markdown]
#
# Remove the `LINE_OF_SIGHT` constraint from the receiver so both endpoints permit the over-the-horizon path:

# %%
near_vertical_skywave_receiver.access_constraints.remove_constraint(
    AccessConstraintType.LINE_OF_SIGHT
)

# %% [markdown]
# ## Evaluate the NVIS link
#
# Compute the transmitter-to-receiver access to determine the performance of the communication link:

# %%
near_vertical_skywave_access = near_vertical_skywave_transmitter.get_access_to_object(
    near_vertical_skywave_receiver
)
near_vertical_skywave_access.compute_access()

# %% [markdown]
# Next, retrieve the access results through data providers. The `Link Information` provider gives link-budget values, and `Link Information - VOACAP` provides skywave mode, loss, and elevation information. Sample these providers every hour.

# %% [markdown]
#
# Request hourly NVIS link-budget data as a dataframe:

# %%
near_vertical_skywave_link_budget = (
    near_vertical_skywave_access.data_providers.item("Link Information")
    .execute_elements(
        scenario.start_time,
        scenario.stop_time,
        3600,
        ["Time", "Rcvd. Iso. Power", "C/N"],
    )
    .data_sets.to_pandas_dataframe()
)

# %% [markdown]
#
# Request hourly NVIS VOACAP data as a dataframe:

# %%
near_vertical_skywave_voacap_results = (
    near_vertical_skywave_access.data_providers.item("Link Information - VOACAP")
    .execute_elements(
        scenario.start_time,
        scenario.stop_time,
        3600,
        ["Time", "Skywave Mode", "Skywave Transmit Elevation", "VOACAP Loss"],
    )
    .data_sets.to_pandas_dataframe()
)

# %% [markdown]
# Join the two dataframes to view the complete data per time, then display the results:

# %%
import pandas as pd


near_vertical_skywave_link_results = pd.merge(
    near_vertical_skywave_link_budget,
    near_vertical_skywave_voacap_results,
    on="time",
)
near_vertical_skywave_link_results

# %% [markdown]
# The `skywave mode` column identifies the number of propagation hops and the ionospheric layer used. For example, 1F2 indicates one hop from the F2 layer. This analysis uses one-hop E- and F2-layer modes. The `skywave transmit elevation` column gives the skywave path angle.
#
# `rcvd. iso. power` is the received power before receiver gain. For this analysis, values above $-150~\mathrm{dBW}$ indicate useful signals, but the received power is often too low. The `c/n` column shows a mix of good and poor carrier-to-noise ratios.

# %% [markdown]
# ## Use alternative frequency computations to improve the link

# %% [markdown]
# Retrieve the alternative-frequency results as text from the `Output File` element of the `Comm VOACAP Files` data provider.

# %% [markdown]
# This provider selects its evaluation time through `pre_data`, not `execute_elements`. Use the analysis start time and do not save the files to the scenario:

# %%
near_vertical_skywave_voacap_files = near_vertical_skywave_access.data_providers.item(
    "Comm VOACAP Files"
)
near_vertical_skywave_voacap_files.pre_data = (
    "Time '15 Apr 2024 19:00:00.000' SaveFilesToScenario false"
)

# %% [markdown]
# Execute the text-valued `Output File` element and display its values:

# %%
near_vertical_skywave_alternative_frequency_results = (
    near_vertical_skywave_voacap_files.execute_elements(["Output File"])
)

near_vertical_skywave_alternative_frequency_results.data_sets.item(0).get_values()

# %% [markdown]
# The results provide options for alternative frequencies that could be used to improve the link. The `FREQ` row shows tested frequencies.
#
# The multiband antennas support $3$--$10~\mathrm{MHz}$. Within that range, $6.7~\mathrm{MHz}$ provides a useful combination of high `TANGLE`, short `DELAY`, and high SNR.

# %% [markdown]
# ## Test the improved NVIS frequency
#
# As a starting point, change the frequency to $6.7~\mathrm{MHz}$.

# %% [markdown]
#
# Set the NVIS transmitter frequency to $0.0067~\mathrm{GHz}$ ($6.7~\mathrm{MHz}$) and recompute access:

# %%
near_vertical_skywave_transmitter_model.frequency = 0.0067
near_vertical_skywave_access.compute_access()

# %% [markdown]
#
# Refresh both link information dataframes and merge them:

# %%
near_vertical_skywave_link_budget_6p7_mhz = (
    near_vertical_skywave_access.data_providers.item("Link Information")
    .execute_elements(
        scenario.start_time,
        scenario.stop_time,
        3600,
        ["Time", "Rcvd. Iso. Power", "C/N"],
    )
    .data_sets.to_pandas_dataframe()
)
near_vertical_skywave_voacap_results_6p7_mhz = (
    near_vertical_skywave_access.data_providers.item("Link Information - VOACAP")
    .execute_elements(
        scenario.start_time,
        scenario.stop_time,
        3600,
        ["Time", "Skywave Mode", "Skywave Transmit Elevation", "VOACAP Loss"],
    )
    .data_sets.to_pandas_dataframe()
)
near_vertical_skywave_link_results_6p7_mhz = pd.merge(
    near_vertical_skywave_link_budget_6p7_mhz,
    near_vertical_skywave_voacap_results_6p7_mhz,
    on="time",
)
near_vertical_skywave_link_results_6p7_mhz

# %% [markdown]
# Using a lower frequency changes the skywave mode: the E layer is no longer used. The frequency change improves received isotropic power, with values above $-150~\mathrm{dBW}$ at all sampled times. The C/N ratio also improves significantly. The fluctuations in values in this column over time are caused by changes in the properties of the layers of the ionosphere over the day. In this scenario, 19:00 UTCG is local noon at the NVIS sites and 07:00 UTCG is local midnight. C/N values are lowest during darkness and near local noon.

# %% [markdown]
# ## Investigate low-angle, long-range skywave performance

# %% [markdown]
# A low-angle high-frequency skywave can support communication over very long distances. The ionosphere bends a signal that enters at a low angle back toward Earth when the ionization level can support the selected frequency. The Earth can then reflect the descending signal upward again, allowing it to repeat this Earth–ionosphere path through two or more hops. When the transmit frequency is just below the maximum usable frequency, propagation losses can be low enough for signals of only a few watts to reach receivers thousands of kilometers away.
#
# In this way, switching from near-vertical skywaves to low-angle skywaves can allow the Los Angeles site to transmit information much further than Palmdale.

# %% [markdown]
# ## Create the long-range receiver site
#
# Create a site in Landstuhl, Germany, which is around $9{,}480~\mathrm{km}$ from Los Angeles. Create the site at $49.4138^\circ$ latitude, $7.5702^\circ$ longitude, and $0~\mathrm{km}$ altitude:

# %%
landstuhl = scenario.children.new(STKObjectType.PLACE, "Landstuhl")
landstuhl.position.assign_geodetic(49.4138, 7.5702, 0.0)

# %% [markdown]
# ## Configure the long-range transmitter

# %% [markdown]
#
# Add a new transmitter in Los Angeles and select the `Complex Transmitter Model` so its directional antenna and link budget can be modeled:

# %%
long_range_transmitter = los_angeles.children.new(STKObjectType.TRANSMITTER, "LR_HF_Tx")
long_range_transmitter.model_component_linking.set_component(
    "Complex Transmitter Model"
)
long_range_transmitter_model = long_range_transmitter.model_component_linking.component

# %% [markdown]
#
# Configure the long-range transmitter to transmit at $0.020~\mathrm{GHz}$, $20~\mathrm{dBW}$, and $1~\mathrm{Mb/s}$:

# %%
long_range_transmitter_model.frequency = 0.020
long_range_transmitter_model.power = 20.0
long_range_transmitter_model.data_rate = 1.0

# %% [markdown]
# Use a custom antenna pattern for this analysis. An external antenna pattern supplies user-defined directional data instead of an analytical antenna shape. The pattern here is a PhiTheta external antenna pattern installed with the STK training samples. Select the `External Antenna Pattern` model for `LR_HF_Tx` to use directional PhiTheta data:

# %%
long_range_transmit_antenna = long_range_transmitter_model.antenna_control
long_range_transmit_antenna.embedded_model_component_linking.set_component(
    "External Antenna Pattern"
)
long_range_transmit_pattern = (
    long_range_transmit_antenna.embedded_model_component_linking.component
)

# %% [markdown]
#
# Load the `VOACAP.pattern` from the STK training-samples directory and set its design frequency to $0.015~\mathrm{GHz}$:

# %%
from pathlib import Path


install_dir = root.execute_command("GetDirectory / STKHome")[0]
antenna_pattern_file_path = (
    Path(install_dir)
    / "Data"
    / "Resources"
    / "stktraining"
    / "samples"
    / "VOACAP.pattern"
)
long_range_transmit_pattern.filename = str(antenna_pattern_file_path)
long_range_transmit_pattern.design_frequency = 0.015

# %% [markdown]
#
# The desired orientation is $65^\circ$ azimuth and $0^\circ$ elevation. For this external pattern, the embedded-model API represents that orientation with a $90^\circ$ elevation argument:

# %%
long_range_transmit_antenna.embedded_model_orientation.assign_az_el(
    65.0, 90.0, AzElAboutBoresight.ROTATE
)

# %% [markdown]
#
# Remove the `LINE_OF_SIGHT` constraint from `LR_HF_Tx` so multihop skywave access is not prevented by terrain:

# %%
long_range_transmitter.access_constraints.remove_constraint(
    AccessConstraintType.LINE_OF_SIGHT
)

# %% [markdown]
# ## Configure the long-range receiver

# %% [markdown]
#
# Add a complex receiver at Landstuhl and use the `Complex Receiver Model`:

# %%
long_range_receiver = landstuhl.children.new(STKObjectType.RECEIVER, "LR_HF_Rx")
long_range_receiver.model_component_linking.set_component("Complex Receiver Model")
long_range_receiver_model = long_range_receiver.model_component_linking.component

# %% [markdown]
#
# Select the `Dipole` antenna model for the receiver to represent the $10$--$30~\mathrm{MHz}$ receiving antenna range used when screening alternative frequencies:

# %%
long_range_receive_antenna = long_range_receiver_model.antenna_control
long_range_receive_antenna.embedded_model_component_linking.set_component("Dipole")
long_range_receive_dipole = (
    long_range_receive_antenna.embedded_model_component_linking.component
)

# %% [markdown]
#
# Set the long-range receiver dipole to $0.020~\mathrm{GHz}$ design frequency, $9~\mathrm{m}$ length, and $80\%$ efficiency:

# %%
long_range_receive_dipole.design_frequency = 0.020
long_range_receive_dipole.length = 9.0
long_range_receive_dipole.efficiency = 80.0

# %% [markdown]
#
# Orient the long-range receiver dipole at $0^\circ$ azimuth and $0^\circ$ elevation. Its default orientation is vertical, so setting $0^\circ$ elevation makes it horizontal:

# %%
long_range_receive_antenna.embedded_model_orientation.assign_az_el(
    0.0, 0.0, AzElAboutBoresight.ROTATE
)

# %% [markdown]
#
# Remove the `LINE_OF_SIGHT` constraint from the receiver so it accepts the over-the-horizon skywave:

# %%
long_range_receiver.access_constraints.remove_constraint(
    AccessConstraintType.LINE_OF_SIGHT
)

# %% [markdown]
# ## Evaluate the long-range link
#
# Compute one-hour samples for the Los Angeles-to-Landstuhl link.

# %% [markdown]
#
# Create and compute access from the Los Angeles transmitter to the Landstuhl receiver to evaluate the long-range link:

# %%
long_range_access = long_range_transmitter.get_access_to_object(long_range_receiver)
long_range_access.compute_access()

# %% [markdown]
#
# Retrieve hourly long-range link-budget data and long-range VOACAP data as dataframes, then merge the results:

# %%
long_range_link_budget = (
    long_range_access.data_providers.item("Link Information")
    .execute_elements(
        scenario.start_time,
        scenario.stop_time,
        3600,
        ["Time", "Rcvd. Iso. Power", "C/N"],
    )
    .data_sets.to_pandas_dataframe()
)
long_range_voacap_results = (
    long_range_access.data_providers.item("Link Information - VOACAP")
    .execute_elements(
        scenario.start_time,
        scenario.stop_time,
        3600,
        ["Time", "Skywave Mode", "Skywave Transmit Elevation", "Reliable Frequency"],
    )
    .data_sets.to_pandas_dataframe()
)
long_range_results = pd.merge(
    long_range_link_budget, long_range_voacap_results, on="time"
)
long_range_results

# %% [markdown]
# As this analysis used long-range, low-angle waves, the skywave transmit elevation is much lower as expected. Additionally, the use of low-angle waves over a longer range results in multihop propagation in the ionosphere's F layer. However, at $20~\mathrm{MHz}$, the received isotropic power and C/N values are poor, with all received power values below the $-150~\mathrm{dBW}$ threshold.
#
# The performance of the link varies over time, as lower frequencies work better at night. The analysis period begins at $12{:}00~\mathrm{pm}$ local time in Los Angeles, which corresponds to $9{:}00~\mathrm{pm}$ local time in Landstuhl. C/N is highest when it is night in Germany.

# %% [markdown]
# ## Use alternative frequency computations to improve the link

# %% [markdown]
# Because lower frequencies work better at night, the alternate-frequency result must be examined at the intended transmission time. So, retrieve the alternative frequency computations data by using the `Output File` element of the `Comm VOACAP Files` data provider for $16~\mathrm{Apr}~2024~04{:}00{:}00~\mathrm{UTCG}$, when Germany is at $9{:}00~\mathrm{pm}$ local time:

# %%
long_range_voacap_files = long_range_access.data_providers.item("Comm VOACAP Files")
long_range_voacap_files.pre_data = (
    "Time '16 Apr 2024 04:00:00.000' SaveFilesToScenario false"
)

long_range_alternative_results = long_range_voacap_files.execute_elements(
    ["Output File"]
)

long_range_alternative_results.data_sets.item(0).get_values()

# %% [markdown]
# The multiband antennas support $10$--$30~\mathrm{MHz}$. Although $12.2~\mathrm{MHz}$ has the best in-range SNR, $9.0~\mathrm{MHz}$ is best overall, so test the nearest permitted frequency, $10~\mathrm{MHz}$.

# %% [markdown]
# ## Test the new long-range frequency

# %% [markdown]
#
# Set the long-range transmitter frequency to $0.010~\mathrm{GHz}$ ($10~\mathrm{MHz}$) and recompute access:

# %%
long_range_transmitter_model.frequency = 0.010
long_range_access.compute_access()

# %% [markdown]
#
# Retrieve the data for the $10~\mathrm{MHz}$ long-range analysis:

# %%
long_range_link_budget_10_mhz = (
    long_range_access.data_providers.item("Link Information")
    .execute_elements(
        scenario.start_time,
        scenario.stop_time,
        3600,
        ["Time", "Rcvd. Iso. Power", "C/N"],
    )
    .data_sets.to_pandas_dataframe()
)
long_range_voacap_results_10_mhz = (
    long_range_access.data_providers.item("Link Information - VOACAP")
    .execute_elements(
        scenario.start_time,
        scenario.stop_time,
        3600,
        [
            "Time",
            "Skywave Mode",
            "Skywave Transmit Elevation",
            "VOACAP Loss",
            "Skywave Loss",
            "Skywave Free Space Loss",
        ],
    )
    .data_sets.to_pandas_dataframe()
)
long_range_link_results_10_mhz = pd.merge(
    long_range_link_budget_10_mhz,
    long_range_voacap_results_10_mhz,
    on="time",
)
long_range_link_results_10_mhz

# %% [markdown]
# The daylight transmission angles of the skywaves have increased. After the frequency change, more received-power values exceed $-150~\mathrm{dBW}$ and C/N improves. This indicates that there are times in which transmission would be successful. However, skywave loss and free-space loss greatly degrade the link.

# %% [markdown]
# ## Define the coverage grid
#
# Now, analyze the potential performance of this long-range communications system over a large geographic area covering much of Europe, Asia, and Africa.
# %% [markdown]
#
# Create a coverage definition to represent the area and define it through a `LATITUDE_LONGITUDE_REGION`:

# %%
from ansys.stk.core.stkobjects import CoverageBounds


coverage_definition = scenario.children.new(
    STKObjectType.COVERAGE_DEFINITION, "HF_VOACAP_Cov"
)
coverage_definition.grid.bounds_type = CoverageBounds.LATITUDE_LONGITUDE_REGION
coverage_bounds = coverage_definition.grid.bounds

# %% [markdown]
#
# Set the coverage region from $-35^\circ$ to $65^\circ$ latitude and from $-20^\circ$ to $90^\circ$ longitude:

# %%
coverage_bounds.minimum_latitude = -35.0
coverage_bounds.minimum_longitude = -20.0
coverage_bounds.maximum_latitude = 65.0
coverage_bounds.maximum_longitude = 90.0

# %% [markdown]
#
# Set latitude-longitude spacing to $4^\circ$ and point altitude to `ABOVE_TERRAIN` to sample the region every $4^\circ$ above the terrain during computations:

# %%
from ansys.stk.core.stkobjects import CoverageAltitudeMethod


coverage_definition.grid.resolution.latitude_longitude = 4.0
coverage_definition.point_definition.altitude_method = (
    CoverageAltitudeMethod.ABOVE_TERRAIN
)

# %% [markdown]
#
# Set the grid class to `RECEIVER` and seed instance to `Place/Landstuhl/Receiver/LR_HF_Rx` so that each coverage point inherits the link criteria for the long range receiver. This allows for computing the performance of a sample receiver at each coverage point:

# %%
from ansys.stk.core.stkobjects import CoverageGridClass


coverage_definition.point_definition.grid_class = CoverageGridClass.RECEIVER
coverage_definition.point_definition.seed_instance = "Place/Landstuhl/Receiver/LR_HF_Rx"

# %% [markdown]
#
# Assign `Place/Los_Angeles/Transmitter/LR_HF_Tx` as the coverage asset, so that the long range transmitter supplies the signal evaluated at each grid point:

# %%
coverage_definition.asset_list.add("Place/Los_Angeles/Transmitter/LR_HF_Tx")

# %% [markdown]
#
# Set automatic recomputation and static grid-point display to `False` to reduce the cost of the calculation:

# %%
coverage_definition.advanced.recompute_automatically = False
coverage_definition.graphics.static.show_points = False

# %% [markdown]
# ## Measure maximum received isotropic power
#
# In order to evaluate the performance of the communications system, create a Figure of Merit, which defines how coverage quality is measured. Here, measure quality based on the receiver's `RcvdIsotropicPower` access constraint, which calculates the received power from the transmission at each grid point. For each point, retain the maximum value in order to evaluate at which grid points transmission could be successful at any point over the analysis period.

# %% [markdown]
#
# Create a figure of merit with the `RcvdIsotropicPower` access constraint:

# %%
figure_of_merit = coverage_definition.children.new(
    STKObjectType.FIGURE_OF_MERIT, "Rcvd_Iso_Pwr"
)
figure_of_merit_definition = figure_of_merit.set_access_constraint_definition_name(
    "RcvdIsotropicPower"
)

# %% [markdown]
#
# Set the Figure of Merit time step to $3600~\mathrm{s}$ and compute type to `MAXIMUM` in order to retain each point's best hourly value:

# %%
from ansys.stk.core.stkobjects import FigureOfMeritCompute


figure_of_merit_definition.time_step = 3600.0
figure_of_merit_definition.set_compute_type(FigureOfMeritCompute.MAXIMUM)

# %% [markdown]
#
# Compute accesses for the configured coverage definition:

# %%
coverage_definition.compute_accesses()

# %% [markdown]
# ## Plot grid statistics over time
#
# Use the `Overall Value by Time` data provider for grid statistics. This data provider reports the grid minimum, maximum, average, standard deviation, and sum of the figure of merit values at each sampled time.
#
# Use these statistics to find the lowest minimum and highest maximum values during the $24~\mathrm{h}$ analysis:

# %%
grid_statistics = (
    figure_of_merit.data_providers.item("Overall Value by Time")
    .execute_elements(
        scenario.start_time, scenario.stop_time, 3600, ["Time", "Minimum", "Maximum"]
    )
    .data_sets.to_pandas_dataframe()
)
grid_statistics

# %% [markdown]
# The highest maximum is around $-124~\mathrm{dBW}$, while the lowest minimum is around $-448~\mathrm{dBW}$, indicating a wide range in coverage quality.

# %% [markdown]
#
# Plot the coverage minimum, maximum, and average values over time:

# %%
from ansys.stk.extensions.data_analysis.graphs.figure_of_merit_graphs import (
    grid_stats_over_time_line_chart,
)


fig, axes = grid_stats_over_time_line_chart(
    figure_of_merit,
    start_time=scenario.start_time,
    stop_time=scenario.stop_time,
    step=3600,
)
axes.set_xticks(range(0, 24 * 3600 + 1, 3 * 3600))
axes.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
fig.subplots_adjust(bottom=0.25)

# %% [markdown]
# ## Visualize the figure of merit results through 2D graphics
#
# To visualize the results of the link performance analysis, use contours over the coverage definition area. The contours will represent the received isotropic power in each grid location over the analysis period.

# %% [markdown]
#
# Set Figure of Merit animation translucency to $50\%$. This lets coverage colors remain visible without obscuring the map:

# %%
figure_of_merit_animation = figure_of_merit.graphics.animation_settings
figure_of_merit_animation.fill_translucency = 50.0

# %% [markdown]
#
# Set the contour display to `True` so that the contours appear, and set the color method to `COLOR_RAMP` so that the different values are plotted using a varying color scale:

# %%
from ansys.stk.core.stkobjects import FigureOfMeritGraphics2DColorMethod


figure_of_merit_contours = figure_of_merit_animation.contours
figure_of_merit_contours.show_graphics = True
figure_of_merit_contours.color_method = FigureOfMeritGraphics2DColorMethod.COLOR_RAMP

# %% [markdown]
#
# Add contour levels from $-450~\mathrm{dBW}$ to $-130~\mathrm{dBW}$ in $40~\mathrm{dB}$ steps to cover the range of values seen in the analysis:

# %%
contour_levels = figure_of_merit_contours.level_attributes
contour_levels.remove_all()
contour_levels.add_level_range(-450.0, -130.0, 40.0)

# %% [markdown]
#
# Set the contour-ramp start color to red and end color to blue, so that lower received values appear in red, and the highest values in blue.

# %%
from ansys.stk.core.utilities.colors import Colors


figure_of_merit_contours.ramp_color.start_color = Colors.Red
figure_of_merit_contours.ramp_color.end_color = Colors.Blue

# %% [markdown]
#
# Show the embedded legend in both 2D and 3D, title it `Received Isotropic Power (dBW)`, use zero decimal digits, and set $60~\mathrm{px}$ color squares:

# %%
contour_legend = figure_of_merit_contours.legend
contour_legend.graphics_2d_window.show_on_map = True
contour_legend.graphics_3d_window.show_on_map = True
contour_legend.text_options.title = "Received Isotropic Power (dBW)"
contour_legend.text_options.number_of_decimal_digits = 0
contour_legend.range_color_options.color_square_width = 60

# %% [markdown]
# Create a 2D graphics window to view the results:

# %%
from ansys.stk.core.experimental.jupyterwidgets import MapWidget


map_widget = MapWidget(root, 640, 640)
map_widget.show()

# %% [markdown]
# View the results for $16~\mathrm{Apr}~2024~00{:}00{:}00.000~\mathrm{UTCG}$, when it is night over much of the coverage definition:

# %%
root.current_time = float(
    root.conversion_utility.convert_date(
        "UTCG",
        "EpSec",
        "16 Apr 2024 00:00:00.000",
    )
)

map_widget.show()

# %% [markdown]
# The link quality is high over much of the area, as low frequencies transmit better at night.

# %% [markdown]
# Now, view the result for $16~\mathrm{Apr}~2024~13{:}00{:}00.000~\mathrm{UTCG}$, when it is daytime for most of the covered area:

# %%
root.current_time = float(
    root.conversion_utility.convert_date(
        "UTCG",
        "EpSec",
        "16 Apr 2024 13:00:00.000",
    )
)

map_widget.show()

# %% [markdown]
# As expected, the transmission quality is lower during the daytime.
