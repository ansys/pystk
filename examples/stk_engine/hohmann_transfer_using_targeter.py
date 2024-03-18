# # Hohmann transfer using targeter
#
# This example provides a practical example of how to use PySTK to solve for a Hohmann transfer problem. The satellite presents an circular and equatorial orbit with a periapsis radius of 6700 kilometers. Its desired final orbit has an apoapsis radius of 42238 kilometers.
#
# ## What is a Hohmann transfer?
#
# A Hohmann transfer is a fuel-efficient orbital maneuver used in spaceflight to transfer a spacecraft from one circular orbit to another circular orbit at a different altitude or around a different celestial body. It was developed by German engineer Walter Hohmann in 1925 and is often referred to as the Hohmann transfer orbit or Hohmann ellipse. This maneuver is commonly used for missions within our solar system, including transfers between planets or moons.
#
# The transfer is typically modeled under the two-body assumption. This means that it assumes a simplified scenario where only two significant gravitational bodies are considered: the spacecraft and the central body (e.g., a planet or a moon).
#
# ## Launch a new STK instance
#
# Start by launching a new STK instance. In this example, STKEngine is used in noGraphics mode. This means that the graphic user interface (GUI) of the product is not launched:


# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(noGraphics=False)
print(f"Using {stk.version}")
# -

# ## Create a new scenario
#
# Start by creating a new scenario in STK by running:

root = stk.new_object_root()
root.new_scenario("HohmannTransfer")

# Once created, it is possible to show a 3D graphics window by running:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.show()
# -

# ## Adding a satellite to the scenario
#
# Now that a new scenario is available, add a new satellite:

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE

satellite = root.current_scenario.children.new(STK_OBJECT_TYPE.SATELLITE, "Satellite")
# -

# Then, declare the type of propagator used for the satellite:

# +
from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE

satellite.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_ASTROGATOR)
# -

# Initialize the propagator by making sure that no previous sequence is present. Add any additional configurations for the propagator. For this example, its is requested to draw the maneuver in 3D.

satellite.propagator.main_sequence.remove_all()
satellite.propagator.options.draw_trajectory_in_3d = True

# ## Set up the initial state of the satellite
#
# To declare the initial state of a satellite, a total of six elements are required. STK supports multiple sets of elements. List them by running:

# +
from ansys.stk.core.stkobjects.astrogator import ELEMENT_TYPE

element_types = [element_type for element_type, _ in ELEMENT_TYPE.__members__.items()]
print(element_types)
# -

# An initial state segment is required to specify the initial state of the satellite. To see the list of different segment types, run:

# +
from ansys.stk.core.stkobjects.astrogator import SEGMENT_TYPE

initial_state = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.INITIAL_STATE, "Initial State", "-")
initial_state.set_element_type(ELEMENT_TYPE.KEPLERIAN)
# -

# A total of six orbital parameters are required to specify the initial state of the satellite. Considering the data provided in this example, it is possible to assign the following parameters:

initial_state.element.periapsis_radius_size = 6700.00
initial_state.element.eccentricity = 0.00
initial_state.element.inclination = 0.00
initial_state.element.raan = 0.00
initial_state.element.arg_of_periapsis = 0.00
initial_state.element.true_anomaly = 0.00

# ## Set up the parking orbit of the satellite
#
# The parking orbit is the temporary orbit that the satellite follows before starting any maneuver. Modelling a parking orbit requires creating a new segment in the main sequence. This segment must be of the propagate type. To be consistent with the assumptions of the Hohmann transfer, the segment should be propagated using an Earth Point Mass propagator. The total duration of the propagation is set in this example for 7200 seconds. 

parking_orbit_propagate = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Parking Orbit Propagate", "-")
parking_orbit_propagate.propagator_name = "Earth point mass"
parking_orbit_propagate.stopping_conditions["Duration"].properties.trip = 7200

# Additional configurations, like the color used to visualize the orbit of the satellite, can also be declared by running:

# +
from ansys.stk.core.utilities.colors import Colors


parking_orbit_propagate.properties.color = Colors.Blue
# -

# ## Define the target sequence for solving transfer orbit
#
# The target sequence is used to find the magnitude of each $\Delta v$ so that the satellite can achieve its desired altitude.

start_transfer_sequence = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "Start Transfer", "-")

# ### First impulse to transfer the satellite to the final orbit
#
# Hohmann maneuver is an impulsive maneuver. Thus, define a maneuver of impulsive type in the target sequence:

# +
from ansys.stk.core.stkobjects.astrogator import MANEUVER_TYPE


delta_v1 = start_transfer_sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "First Impulse", "-")
delta_v1.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)
# -

# This first impulse takes place in the direction of the velocity vector at the periapsis. For this reason, it is convenient to define the thrust impulse in the Velocity-Normal-CoNormal (VNC) frame. By selecting the VNC frame, the velocity vector is now aligned with the X-axis. The magnitude of the burn will be determined using the radius of apoapsis after the maneuver, so radius of apoapsis is added as a result to the maneuver segment:

# +
from ansys.stk.core.stkobjects.astrogator import ATTITUDE_CONTROL, CONTROL_MANEUVER, PROFILE_MODE, TARGET_SEQ_ACTION

delta_v1.maneuver.set_attitude_control_type(ATTITUDE_CONTROL.THRUST_VECTOR)
delta_v1.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
delta_v1.results.add('Keplerian Elems/Radius of Apoapsis');
# -

# Now, configure the solver for this target sequence. A differential corrector can be used to solve for the desired final radius at apoapsis. Retrieve the differential corrector for the target sequence:

first_impulse_differential_corrector = start_transfer_sequence.profiles["Differential Corrector"]

# Configure the differential corrector for the first impulse:

control_delta_v1_x = first_impulse_differential_corrector.control_parameters.get_control_by_paths("First Impulse", "ImpulsiveMnvr.Cartesian.X")
control_delta_v1_x.enable = True
control_delta_v1_x.max_step = 0.30

# Impose the numerical conditions to be met by the impulse along its X axis:

desired_radius_of_apoapsis = first_impulse_differential_corrector.results.get_result_by_paths("First Impulse", "Radius Of Apoapsis")
desired_radius_of_apoapsis.enable = True
desired_radius_of_apoapsis.desired_value = 42238.00
desired_radius_of_apoapsis.tolerance = 0.10

# Establish the maximum number of iterations and an iterative profile search:

first_impulse_differential_corrector.max_iterations = 50
first_impulse_differential_corrector.mode = PROFILE_MODE.ITERATE

# Finally, set the mode of the target sequence to run all active profiles:

start_transfer_sequence.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES

# ### Propagate the satellite to the end of the transfer orbit

# After the first maneuver, the next step is to propagate the satellite to the end of the transfer orbit. This is done by adding a new propagation segment to the main sequence:

propagate_transfer = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Transfer Orbit", "-")
propagate_transfer.propagator_name = "Earth point mass"
propagate_transfer.stopping_conditions.add("Apoapsis")
propagate_transfer.stopping_conditions.remove("Duration")

# This segment is colored using red to differentiate it from the parking segment:

propagate_transfer.properties.color = Colors.Red

# ### Final impulse to circularize the orbit
#
# For the final impulse, create a new target sequence:

end_transfer_sequence = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.TARGET_SEQUENCE, "End Transfer", "-")

# Next, add a new impulsive maneuver to model the burn to adapt the transfer orbit to the final desired one:

delta_v2 = end_transfer_sequence.segments.insert(SEGMENT_TYPE.MANEUVER, "Last Impulse", "-")
delta_v2.set_maneuver_type(MANEUVER_TYPE.IMPULSIVE)

# Again, define the thrust in the direction of the local velocity vector. This time, eccentricity is used as a result since the desired orbit at the end of the transfer is circular:

delta_v2.maneuver.set_attitude_control_type(ATTITUDE_CONTROL.THRUST_VECTOR)
delta_v2.enable_control_parameter(CONTROL_MANEUVER.IMPULSIVE_CARTESIAN_X)
delta_v2.results.add("Keplerian Elems/Eccentricity");

# Configure the differential corrector for this target sequence:

last_impulse_differential_corrector = end_transfer_sequence.profiles["Differential Corrector"]

# Configure the differential corrector for the last impulse:

control_delta_v2_x = last_impulse_differential_corrector.control_parameters.get_control_by_paths("Last Impulse", "ImpulsiveMnvr.Cartesian.X")
control_delta_v2_x.enable = True
control_delta_v2_x.max_step = 0.30

# Impose the numerical conditions to be met by the impulse along its X axis:

desired_eccentricity = last_impulse_differential_corrector.results.get_result_by_paths("Last Impulse", "Eccentricity")
desired_eccentricity.enable = True
desired_eccentricity.desired_value = 0
desired_eccentricity.tolerance = 0.01

# Again, establish the maximum number of iterations and an iterative profile search:

last_impulse_differential_corrector.enable_display_status = True
last_impulse_differential_corrector.mode = PROFILE_MODE.ITERATE

# Finally, set the mode of the target sequence to run all active profiles:

end_transfer_sequence.action = TARGET_SEQ_ACTION.RUN_ACTIVE_PROFILES

# ## Propagation along the final orbit
#
# Once the last impulse has been applied, it is possible to propagate the satellite along its final orbit. Start by creating a new propagation segment in the main sequence. Propagate the satellite for a total of 86400 seconds.

propagate_final_orbit = satellite.propagator.main_sequence.insert(SEGMENT_TYPE.PROPAGATE, "Final State Propagate", "-")
propagate_final_orbit.properties.color = Colors.Green
propagate_final_orbit.propagator_name = "Earth Point Mass"
propagate_final_orbit.stopping_conditions["Duration"].properties.trip = 86400.00

# ## Running the main control sequence
#
# Once that all the segments for the main sequence are defined, the main control sequence can be executed to solve for the desired values in each sequence:

satellite.propagator.run_mission_control_sequence()

# ## Retrieve the results
#
# Once the analysis has been performed, analytical results can be retrieved for a desired segment.

# ### Results for the first impulse

# +
start_transfer_sequence = satellite.propagator.main_sequence["Start Transfer"]
start_differential_corrector = start_transfer_sequence.profiles["Differential Corrector"]

delta_v1_x = start_differential_corrector.control_parameters.get_control_by_paths("First Impulse", "ImpulsiveMnvr.Cartesian.X").final_value
print(f"\N{GREEK CAPITAL LETTER DELTA}V1 along X direction: {delta_v1_x:.5f} [km/s]")

thrust_v1_x = start_transfer_sequence.segments["First Impulse"].maneuver.attitude_control.x
print(f"Thrust along X direction: {thrust_v1_x:.5f} [??]")
# -

# ### Results for the last impulse

# +
end_transfer_sequence = satellite.propagator.main_sequence["End Transfer"]
end_differential_corrector = end_transfer_sequence.profiles["Differential Corrector"]

delta_v2_x = end_differential_corrector.control_parameters.get_control_by_paths("Last Impulse", "ImpulsiveMnvr.Cartesian.X").final_value
print(f"\N{GREEK CAPITAL LETTER DELTA}V2 along X direction: {delta_v2_x:.5f} [km/s]")

thrust_v2_x = end_transfer_sequence.segments["Last Impulse"].maneuver.attitude_control.x
print(f"Thrust along X direction: {thrust_v2_x:.5f} [??]")
# -

# ## Apply the results
#
# Previously computed results need to be applied to the main sequence. This can be done by running:

start_transfer_sequence.apply_profiles()
end_transfer_sequence.apply_profiles()

# ## Plot the trajectory
#
# Finally, it is possible to visualize the complete sequence of maneuvers by showing the plotter again. Since the maneuver gets out of the field of view of the plotter's camera, the position of the camera is updated:

plotter.camera.position = [57000, 85000, 55000]
plotter.show()
