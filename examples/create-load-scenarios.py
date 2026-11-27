# # Creating and Loading Scenarios

# This tutorial explains how to use the PySTK pythonic access tool to create and load STK scenarios. PySTK can automate the setup of complex scenarios, load existing scenarios, and interact with various objects within theSTK application, such as satellites, aircraft, and ground stations. Configure and analyze scenarios without needing to manually input data or interact with the STK graphical user interface.

# ## Creating a new STK scenario

# To create a new scenario, first connect to the STK application. This tutorial uses the STK Engine technology platform.

# +
from ansys.stk.core.stkengine import STKEngine


# Connect to the STK Application object
stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# This creates an instance of STK Engine. Setting `no_graphics` to `False` enables graphics support, but it does not open an STK application window on your desktop.
# For details on `no_graphics`, see the `STK Programming Help <https://help.agi.com/stkdevkit/index.htm#stkEngine/NoGraphics.htm>`_.

# Next, create a new scenario.

# Create a new scenario
root = stk.new_object_root()
root.new_scenario("MyScenario")

# This creates a new scenario in the STK application named "MyScenario."

scenario = root.current_scenario
print(scenario.path)

# ## Creating objects in a scenario
# After creating (or loading) a scenario, PySTK enables the creation and manipulation of STK objects like Satellites, Aircraft, and Facilities. For example, to add a Satellite object:

# +
from ansys.stk.core.stkobjects import STKObjectType


# Create a satellite in the scenario
satellite = scenario.children.new(STKObjectType.SATELLITE, "MySatellite")
# -

# To set the satellite’s orbit and to set a propagator type:

# +
from ansys.stk.core.stkobjects import PropagatorType


# Set the satellite’s orbit (assuming you want a basic orbit definition)
satellite.set_propagator_type(PropagatorType.SGP4)  # Using SGP4 propagator
propagator = satellite.propagator
propagator.propagate()  # To propagate the orbit
# -

# ## Displaying the scenario in a widget
#
# It is possible to display the created scenario by using map and globe widgets for Jupyter Notebooks using Remote Frame Buffer. For example, you can display the 3D Globe widget:


# + tags=["nbsphinx-thumbnail"]
from ansys.stk.core.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Saving a scenario

# Save the scenario along with all added objects using PySTK.

# +
from pathlib import Path


# Create directory for scenario files
scenario_directory = Path.cwd() / "scenario" / "MyScenario"
scenario_directory.mkdir(parents=True, exist_ok=True)

# Save the scenario
scenario_path = scenario_directory / "MyScenario.sc"
root.save_as(str(scenario_path))
root.close_scenario()
# -

# ## Loading an existing scenario

# Load an existing scenario by opening the SC (scenario) file:

# Open an existing scenario
scenario = root.load_scenario(str(scenario_path))

# ## Closing the STK application

# After you’re done, you can close the STK application:

# +
# Close the Jupyter widget to ensure graceful exit
plotter.close()

# Close the STK application
stk.shutdown()
# -
