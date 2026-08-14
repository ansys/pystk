# # How To Create Pointing Sensors in STK

# STK provides several methods for defining sensors and sensor pointing. This example shows some of the most common methods, as described below.

# This example is based on [this](https://analyticalgraphics.my.salesforce-sites.com/faqs/articles/HowTo/How-do-I-create-a-scanning-sweeping-sensor) tutorial.

# ## Launch a new STK instance:

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario:

# +
root = stk.new_object_root()
root.new_scenario("sensor_pointing_demo")
scenario = root.current_scenario
# -

# Add a satellite and a target to the scenario:

# +
from ansys.stk.core.stkobjects import STKObjectType


satellite = scenario.children.new(STKObjectType.SATELLITE, "satellite")

target = scenario.children.new(STKObjectType.TARGET, "target")
# -

# ## Fixed Sensor

# Create a sensor and attach it to the satellite:

# +
fixed_sensor = satellite.children.new(STKObjectType.SENSOR, "fixed_sensor")
# -

# Set the fixed sensor's rectangular field of view:

# +
fixed_pattern = fixed_sensor.common_tasks.set_pattern_rectangular(
    vertical_half_angle=5.0, horizontal_half_angle=15.0
)
# -

# Set fixed pointing:

# +
from ansys.stk.core.stkutil import YPRAnglesSequence


fixed_pointing = fixed_sensor.common_tasks.set_pointing_fixed_ypr(
    sequence=YPRAnglesSequence.YPR, yaw=0.0, pitch=0.0, roll=30.0
)
# -

# ## Targeted Sensor

# Create a sensor and attach it to the satellite:

# +
targeted_sensor = satellite.children.new(STKObjectType.SENSOR, "targeted_sensor")
# -

# Set target-tracking pointing towards the target:

# +
from ansys.stk.core.stkobjects import BoresightType, TrackMode


targeted_pointing = targeted_sensor.common_tasks.set_pointing_targeted_tracking(
    TrackMode.RECEIVE, BoresightType.HOLD, "Target/target"
)
# -

# ## Spinning Sensor

# Create a sensor and attach it to the satellite:

# +
spinning_sensor = satellite.children.new(STKObjectType.SENSOR, "spinning_sensor")
# -

# Set the same FOV as the fixed sensor:

# +
spinning_sensor.common_tasks.set_pattern_rectangular(
    vertical_half_angle=5.0, horizontal_half_angle=15.0
)
# -

# Configure the spinning pointing properties:

# +
from ansys.stk.core.stkobjects import SensorScanMode


spinning_pointing = spinning_sensor.common_tasks.set_pointing_spinning(
    spin_axis_azimuth=0,
    spin_axis_elevation=0,
    spin_axis_cone_angle=90,
    scan_mode=SensorScanMode.BIDIRECTIONAL,
    spin_rate=0.5,
    offset_angle=0,
    clock_angle_start=200,
    clock_angle_stop=230,
)
# -

# ## External Pointing Pattern Sensor

# Create a sensor and attach it to the satellite:

# +
external_pattern_sensor = satellite.children.new(
    STKObjectType.SENSOR, "external_sensor"
)
# -

# Set the pointing type to "external" and choose a file:

# +
external_pattern_sensor.set_pointing_external_file(
    sensor_pointing_file="insert_external_file_path"
)
# -

# ## More Complex Sweeping Patterns

# Create a new satellite representing the oriented frame:

# +
point_sensor_satellite = scenario.children.new(
    STKObjectType.SATELLITE, "point_sensor_satellite"
)
# -

# Set the attitude category to standard in order to use the basic menu:

# +
point_sensor_satellite.set_attitude_type(attitude=STANDARD)
# -

# Next, set the attitude "type" to fixed in axes:

# +
