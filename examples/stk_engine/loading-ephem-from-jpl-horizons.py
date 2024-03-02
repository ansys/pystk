# # Downloading ephemeris data from JPL Horizons
#
# This example shows how to download ephemeris data from JPL Horizons and use it in STK. A custom function is used to connect to the [NASA JPL Horizons System](https://ssd.jpl.nasa.gov/horizons/app.html) by using its [API service](https://ssd-api.jpl.nasa.gov/doc/horizons.html). After downloading the ephemerides file from the server, the file is adapted to STK ephemerides format by adding custom headers.

# ## What are ephemerides?
#
# Ephemerides files, often simply called ephemerides, are datasets containing information about the positions and movements of celestial objects such as planets, moons, asteroids, and comets. These files provide detailed information about the positions of these celestial bodies at specific points in time, typically given in coordinates such as right ascension and declination for celestial objects or ecliptic coordinates for objects within the solar system.
#
# In this example, the ephemerides of ['Oumuamua](https://ssd.jpl.nasa.gov/tools/sbdb_lookup.html#/?sstr=1I) are the ones studied.

# ## Downloading ephemerides from JPL Horizons System
#
# The JPL Horizons System provides a public API deployed in https://ssd.jpl.nasa.gov/api/horizons.api. Users can perform a ``GET`` request to previous endpoint and include different parameters in the query. Parameters allow to request desired data or indicate the output format. A complete list of the supported parameters can be found in the [official JPL Horizons System API reference](https://ssd-api.jpl.nasa.gov/doc/horizons.html).

JPL_HORIZONS_API = "https://ssd.jpl.nasa.gov/api/horizons.api"

# ### Defining the parameters
#
# STK ephemerides support a variety of parameters, see the [official STK ephemerides specification](https://help.agi.com/stk/12.8.0/index.htm#stk/importfiles-02.htm).
#
# To match previous specification, the parameters required for the JPL Horizons query are:
#
# - A ``Vector Table`` containing the data
# - ``State Vector`` data
# - CSV format
#
# In addition to previous ones, users can request a custom time span and coordinates center.
#
# Since this tutorial focuses on 1I/ʻOumuamua interstellar object, the JPL query parameters are the following:

# +
common_parameters = {
    "format": "text",
    "COMMAND": "'DES=A/2017 U1;'",  # Official indicator for Oumuamua
    "OBJ_DATA": "NO",               # Do not include header data
    "MAKE_EPHEM": "YES",            # Generate ephemerides for the query
    "EPHEM_TYPE": "VECTOR",         # Request only vector data
}

ephemerides_parameters = {
    "CENTER": "500@10",             # Generate ephemerides w.r.t Sun's center
    "START_TIME": "2017-01-01",     # Start time for the ephemerides
    "STOP_TIME": "2018-01-01",      # Stop time for the ephemerides
    "STEP_SIZE": "1d",              # Step size is 1 day
    "REF_SYSTEM": "ICRF",           # Reference system is ICRF
    "VEC_TABLE": "2",               # Request only state vector
    "OUT_UNITS": "KM-S",            # Output units in Kilometers and seconds
    "CAL_FORMAT": "JD",             # Dates must be in Julian Date
    "CSV_FORMAT": "YES",            # Apply CSV formatting
}

parameters = common_parameters | ephemerides_parameters
# -

# ### Querying JPL Horizons System
#
# Once the query parameters are defined, an asynchronous function can be implemented for performing the query:

# +
import httpx


async def query_jpl_horizons(params: dict) -> str:
    """Query JPL Horizons System with desired parameters.

    Parameters
    ----------
    params : dict
        Dictionary relating parameters and their values.

    Returns
    -------
    str
        Ephemerides data in string format.

    Notes
    -----
    For a complete list of valid parameters refer to https://ssd-api.jpl.nasa.gov/doc/horizons.html.
    
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(JPL_HORIZONS_API, params=params)
        if response.status_code == 200:
            return response.text
        else:
            raise RuntimeError("Failed to retrieve data.")
# -

# Finally, it is possible to query the JPL Horizons System:

oumuamua_ephem = await query_jpl_horizons(parameters)

# Previous data can be stored in a file, similarly to what JPL Horizons web application allows:

with open("horizons_results.txt", "w") as file:
    file.write(oumuamua_ephem)

# ## Cleaning ephemerides data
#
# The ephemerides file downloaded contains the following data:

# # !heat -n 50 horizons_results.txt

# This format is not supported by STK. The ephemerides data lies between the ``$$SOE`` (Start Of Ephemeris) and ``$EOE`` (End Of Ephemeris) keywords. In addition, no commas or headers must be present. Finally, some STK metadata needs to be included in the file, following [STK Ephemerides specification](https://help.agi.com/stk/12.8.0/index.htm#stk/importfiles-02.htm).
#
# The function below converts JPL Horizons ephemerides results to STK format:

# +
import re


def jpl_to_stk_ephem(jplfile: str, stkfile: str, version: str, metadata: dict) -> str:
    """Convert from JPL Horizons Service ephemerides format into STK format.

    Parameters
    ----------
    jplfile : str
        Path string to JPL ephemerides file.
    stkfile: str
        Path string to STK ephemerides file.
    version: str
        STK version formatted as MAJOR.MINOR
    metadata: dict
        Desired metadata to be included in the STK ephemerides file.

    Raises
    ------
    ValueError
        If ``$$SEO`` and ``$$EOE`` guards are not found.

    """
    # Look for ephemerides from JPL Horizons results
    with open(jplfile, "r") as file:
        EPHEM_PATTERN = r'\$\$SOE(.*?)\$\$EOE'
        match = re.search(EPHEM_PATTERN, file.read(), re.DOTALL)
        if not match:
            raise ValueError("Could not find ephemerides guards $$SEO and $$EOE.")
    
    # Extract JPL ephemerides data, remove empty lines, and split by commas
    jpl_ephem_data = match.group(1).strip().split(",")

    # Drop calendar dates as they are not required in STK ephemerides
    ignore_indices = set(range(1, len(jpl_ephem_data), 8))
    desired_values = lambda value: jpl_ephem_data.index(value) not in ignore_indices
    stk_ephem_data = "".join(list(filter(desired_values, jpl_ephem_data)))

    # Save data in STK ephemerides format
    with open(stkfile, "w") as file:
        file.write(f"stk.v.{version}\nBEGIN Ephemeris\n")

        max_key_length = max(len(key) for key in metadata.keys())
        for key, value in metadata.items():
            file.write(f"\t{key.ljust(max_key_length)}\t\t{value}\n")
            
        file.write(f"{stk_ephem_data}\nEND Ephemeris")


# -

# Metadata needs to be consistent with the query. In this example, the following metadata applies:

metadata = {
    "InterpolationMethod": "Lagrange",
    "InterpolationOrder": "5",
    "DistanceUnit": "Kilometers",
    "CentralBody": "Sun",
    "CoordinateSystem": "ICRF",
    "TimeFormat": "JDate",
    "EphemerisTimePosVel": "",
}

# Finally, it is possible to convert the ``horizons_result.txt`` file to an ephemerides file named ``oumuamua.e``:

jpl_to_stk_ephem(
    jplfile="horizons_results.txt", 
    stkfile="oumuamua.e", 
    version="12.9",
    metadata=metadata,
)

# ## Using the ephemerides in STK
#
# Once the ephemerides have been downloaded, cleaned, and formatted as needed, it is possible to load them in STK.
#
# Start by launching an instance of STK by running:

# +
from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(noGraphics=False)
print(f"Using {stk.version}")
# -

# ### Create a new scenario
#
# Start by creating a new scenario in STK. The scenario for simulating Oumuamua is set to have a time period that matches the one requested during the ephemerides query. In addition, the central body of this new scenario must be the Sun:

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE


root = stk.new_object_root()
scenario = root.children.new_on_central_body(STK_OBJECT_TYPE.SCENARIO, "JPLHorizonsEphem", "Sun")
scenario.set_time_period("1 Jan 2017", "1 Jan 2018")
# -

# Make sure to rewind the scenario once created:

root.rewind()

# Next, you can display the scenario. Since the orbit of Oumuamua is very distant from the Sun, it is required to updated the far plane of the camera. This ensures that any object up to this distance is rendered on the scene:

# +
from ansys.stk.core.stkengine.experimental.jupyterwidgets import GlobeWidget


plotter = GlobeWidget(root, 640, 480)
plotter.camera.far_plane = 1E12
plotter.show()
# -

# ### Visualizing the inner planets
#
# To better understand the orbit of Oumuamua and its trajectory through the solar system, the orbits of inner planets can be simulated. The default ephemerides provided by STK are used in this case:

# +
from ansys.stk.core.stkobjects import STK_OBJECT_TYPE, PLANET_POSITION_SOURCE_TYPE, EPHEM_SOURCE_TYPE
from ansys.stk.core.utilities.colors import Colors


planets = ["Mercury", "Venus", "Earth", "Mars"]
colors = [Colors.Gray, Colors.Orange, Colors.RoyalBlue, Colors.Red]

for planet_name, color in zip(planets, colors):
    planet = scenario.children.new(STK_OBJECT_TYPE.PLANET, planet_name)
    planet.common_tasks.set_position_source_central_body(planet_name, EPHEM_SOURCE_TYPE.DEFAULT)
    planet.graphics.color = color
# -

# Ensure that the following configuration is declared to visualize the orbits and labels for vehicles and planets:

# +
# General graphics configuration
scenario.graphics.labels_visible = True

# Vehicle specific graphics
scenario.graphics.orbits_visible = True

# Planet specific graphics
scenario.graphics.planet_orbits_visible = True
scenario.graphics.inertial_position_labels_visible = True
scenario.graphics.inertial_position_visible = True
scenario.graphics.sub_planet_points_visible = False
scenario.graphics.sub_planet_labels_visible = False
# -

# Next, display the scene to visualize the inner planets. The camera position is updated to have a detailed view of the scene: 

plotter.camera.position = [-39909210.2975278, -717257963.8657558, -85235906.80896328]
plotter.show()

# ### Simulating Oumuamua's orbit
#
# A satellite object can be used to simulate Omumuamua's orbit. The central body for this new object must be the Sun:

oumuamua = scenario.children.new_on_central_body(STK_OBJECT_TYPE.SATELLITE, "Oumuamua", "Sun")

# The ephemerides file created in the early stages of this notebook is used together with an external STK propagator:

# +
from ansys.stk.core.stkobjects import VEHICLE_PROPAGATOR_TYPE, STK_EXTERNAL_EPHEMERIS_FORMAT


oumuamua.set_propagator_type(VEHICLE_PROPAGATOR_TYPE.PROPAGATOR_STK_EXTERNAL)
oumuamua.propagator.file_format = STK_EXTERNAL_EPHEMERIS_FORMAT.STK
oumuamua.propagator.filename = "oumuamua.e"
# -

# A yellow color is used for visualizing the orbit of Oumuamua. Make sure to increase the detail threshold up to the maximum so the orbit renders in the scene:

oumuamua.graphics.attributes.color = Colors.Yellow
oumuamua.graphics_3d.model.detail_threshold.all = 1E12

# Next, propagate the orbit by running:

oumuamua.propagator.propagate()

# Finally, visualize the complete scene:

plotter.show()
