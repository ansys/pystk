Create and load scenarios
#########################

This section explains how to use PySTK to create and load STK scenarios. By leveraging PySTK, you can automate the setup of complex scenarios, load existing scenarios, and interact with various objects within STK, such as satellites, aircraft, and ground stations. This enables you to configure and analyze scenarios without needing to manually input data or interact with the STK graphical user interface.

Create a new STK scenario
=========================

To create new scenario, you first need to connect to STK. 

.. code-block::
    # Connect to the STK Application object
    stk_app = win32com.client.Dispatch("STK12.Application")
    stk_app.Visible = True  # This will make the STK UI visible

This creates an instance of the STK application, and setting Visible to True opens the STK window.

Next, it's time to create a scenario.

.. code-block::
    # Create a new scenario
    stk_scenario = stk_app.NewScenario("MyScenario")

This creates a new scenario in STK named "MyScenario."


Load an existing scenario
=========================

You can load an existing scenario by opening the .sc (scenario) file:

.. code-block::
    # Open an existing scenario
    existing_scenario_path = "C:\\Path\\To\\Your\\Scenario.sc"
    stk_scenario = stk_app.LoadScenario(existing_scenario_path)

Create objects in a scenario
============================

After creating or loading the scenario, you can create and manipulate objects like satellites, aircraft, or ground stations. For example, to add a satellite:

.. code-block::
    # Create a satellite in the scenario
    satellite = stk_scenario.Children.New("Satellite", "MySatellite")

To set the satellite's orbit and to set a propagator type:

.. code-block::
    # Set the satellite's orbit (assuming you want a basic orbit definition)
    satellite.SetPropagatorType("ePropagatorSGP4")  # Using SGP4 propagator
    propagator = satellite.Propagator
    propagator.InitialState = "InitialState"
    satellite.Propagate()  # To propagate the orbit

Save a scenario
===============

Once you've created your scenario and added the necessary objects, save the scenario using PySTK:

.. code-block::
    # Save the scenario
    stk_scenario.SaveAs("C:\\Path\\To\\Save\\NewScenario.sc")

Close the STK application
=========================

After you're done, you can close the STK application:

.. code-block::
    # Close the STK application
    stk_app.Quit()
