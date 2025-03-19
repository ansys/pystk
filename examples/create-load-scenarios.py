# # Create and load scenarios

# This tutorial explains how to use PySTK to create and load STK scenarios. PySTK can automate the setup of complex scenarios, load existing scenarios, and interact with various objects within STK, such as satellites, aircraft, and ground stations. Configure and analyze scenarios without needing to manually input data or interact with the STK graphical user interface.

# ## Create a new STK scenario

# To create a new scenario, first connect to STK. This tutorial uses STK Engine.

# +
from ansys.stk.core.stkengine import STKEngine


# Connect to the STK Application object
stk = STKEngine.start_application(no_graphics=False)
print(f"Using {stk.version}")
# -

# This creates an instance of the STK application. Setting `no_graphics` to `False` opens the STK window.

# Next, it's time to create a scenario.

# Create a new scenario
root = stk.new_object_root()
root.new_scenario("MyScenario")

# This creates a new scenario in STK named "MyScenario."

scenario = root.current_scenario
print(scenario.path)

# ## Create objects in a scenario
# After creating (or loading) the scenario, PySTK enables the creation and manipulation of objects like satellites, aircraft, or ground stations. For example, to add a satellite:

# +
from ansys.stk.core.stkobjects import Satellite, STKObjectType


# Create a satellite in the scenario
satellite = Satellite(scenario.children.new(STKObjectType.SATELLITE, "MySatellite"))
# -

# To set the satellite's orbit and to set a propagator type:

# +
from ansys.stk.core.stkobjects import PropagatorSGP4, PropagatorType


# Set the satellite's orbit (assuming you want a basic orbit definition)
satellite.set_propagator_type(PropagatorType.SGP4)  # Using SGP4 propagator
propagator = PropagatorSGP4(satellite.propagator)
propagator.propagate()  # To propagate the orbit
# -

# ## Save a scenario

# Now save the scenario along with all added objects using PySTK.

# +
import pathlib


# Create a directory for scenario files
scenario_directory = pathlib.Path(pathlib.Path.cwd() / "scenario" / "MyScenario")
pathlib.Path(scenario_directory).mkdir(parents=True, exist_ok=True)

# Save the scenario
scenario_path = pathlib.Path(scenario_directory / "MyScenario.sc")
root.save_as(str(scenario_path))
root.close_scenario()
# -

# ## Load an existing scenario

# Load an existing scenario by opening the .sc (scenario) file:

# Open an existing scenario
scenario = root.load_scenario(str(scenario_path))

# ## Close the STK application

# After you're done, you can close the STK application:

# Close the STK application
stk.shutdown()
