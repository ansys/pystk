# # How To Create Pointing Sensors in STK

# STK provides several methods for defining sensors and sensor pointing. This example shows some of the most common methods, as described below.

# This example is based on [this](https://analyticalgraphics.my.salesforce-sites.com/faqs/articles/HowTo/How-do-I-create-a-scanning-sweeping-sensor) tutorial.

# ## Launch a new STK instance

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario

# +
root = stk.new_object_root()
root.new_scenario("create_pointing_sensors")
# -

# Once the scenario is created, you can view a 3D graphics window by running:

# +
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


globe_widget = GlobeWidget(root, 640, 480)
globe_widget.camera.position = [0, 0, 0]
globe_widget.show()
# -

# First, a sensor needs a satellite to attach to:

# +
from ansys.stk.core.stkobjects import STKObjectType


satellite_1 = root.current_scenario.children.new(STKObjectType.SATELLITE, "satellite_1")
# -

# ## Stationary Sensors

# Next, attach a sensor object to the satellite:

# +
stationary_sensor = satellite_1.children.new(STKObjectType.SENSOR, "stationary_sensor")
# -

# Now that a sensor is attached to the satellite, first define the sensor type and constraints:

# +

# -

# and then define the pointing type and orientation:

# +

# -

# ## Tracking Sensors

# ## Sweeping Sensors
