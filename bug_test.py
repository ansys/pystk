from ansys.stk.core.stkengine import STKEngine


stk = STKEngine.start_application(no_graphics=False)
root = stk.new_object_root()

from ansys.stk.core.stkobjects import *
from numpy import *
from pandas import *

def _get_unique_element_names(results: "DataProviderResultDataSetCollection"):
    """Return a unique set of element names as a set."""

    unique_element_names = set(results.element_names)

    return unique_element_names


def _map_element_types_to_pandas_dtypes(data_provider_elements: "DataProviderElements",
                                        index_element_name: str = None):
    """
    Return a mapping of STK data provider element names and their types to corresponding pandas dtypes.

    Notes
    -----
    This function requires ``numpy``.
    """
    import numpy

    dtype_element_name_mapping = dict()

    for element in data_provider_elements:
        element_type = element.type
        normalized_element_name = element.name.lower()
        element_dimensions_name = element.dimension_name.lower()

        # By default to avoid issues with possible leap seconds or other time precision related issues we map date
        # dimension elements as string dtypes in pandas. Future work plans to implement more robust datetime support
        # for pandas.
        if element_type == DataProviderElementType.REAL and element_dimensions_name not in "date":
            pd_dtype = numpy.float64
        elif element_type == DataProviderElementType.INTEGER:
            pd_dtype = numpy.int64
        else:
            # by default make everything else a str, strings like datatime strings can be handled/parsed
            # separately
            pd_dtype = str

        if not index_element_name or normalized_element_name != index_element_name.lower():
            dtype_element_name_mapping[normalized_element_name] = pd_dtype

    return dtype_element_name_mapping

def to_numpy_array(results: "DataProviderResultDataSetCollection") -> "ndarray":
    import numpy

    results_arr = numpy.array([])

    # create numpy array from row formatted dataset elements
    row_elements = results.to_array()
    unshaped_elements_arr = numpy.array(row_elements)

    # get unique element names and unique element count
    unique_element_names = _get_unique_element_names(results)
    num_unique_columns = len(unique_element_names)

    # reshape to flatten list while preserving the proper column dimensions
    if num_unique_columns:
        results_arr = unshaped_elements_arr.reshape(-1, num_unique_columns)

    return results_arr


def to_pandas_dataframe(results: "DataProviderResultDataSetCollection", index_element_name: str = None,
                 data_provider_elements: "DataProviderElements" = None) -> "DataFrame":
    import pandas

    results_df = pandas.DataFrame()
    results_arr = to_numpy_array(results)

    if results_arr.size > 0:
        unique_element_names = _get_unique_element_names(results)
        num_unique_elements = len(unique_element_names)

        # Slice element names list to get unique column names in the order that they appear in the DataSet. This
        # ensures that the order of the unique column names is maintained when they are used as columns in the
        # new DataFrame.
        unique_element_names = results.element_names[0:num_unique_elements]

        # normalize element names to mitigate errors working and comparing DataFrame column names as column names are
        # case sensitive
        normalized_unique_element_names = [name.lower() for name in unique_element_names]

        results_df = pandas.DataFrame(data=results_arr, columns=normalized_unique_element_names)

        # set DataFrame index column
        if index_element_name:
            normalized_index_column = None

            # check that element name to be used as the DataFrame index column is valid
            for name in normalized_unique_element_names:
                if index_element_name.lower() == name:
                    normalized_index_column = index_element_name.lower()
                    break

            if normalized_index_column:
                results_df = results_df.set_index(normalized_index_column)
            else:
                element_names_str = ",".join(normalized_unique_element_names)
                error_message = f"\"{index_element_name}\" is not a valid data provider element name. Valid " \
                                f"element names are: {element_names_str}"
                raise ValueError(error_message)

        # map data provider element types to pandas dtypes
        if data_provider_elements:
            dtypes_dict = _map_element_types_to_pandas_dtypes(data_provider_elements,
                                                              index_element_name=index_element_name)

            # Update DataFrame column dtypes with mapped types. If we encounter values that can not be
            # converted such as None or Nan ignore them and return the original object, this allows the caller to
            # determine how to they would like to handle Nan etc values.
            results_df = results_df.astype(dtypes_dict, errors="ignore")

    return results_df

root.new_scenario("GraphTest")
scenario = root.current_scenario
scenario.set_time_period("5 Jun 2022", "6 Jun 2022")

facility = scenario.children.new(STKObjectType.FACILITY, "Facility")
facility.position.assign_planetodetic(39.95, -75.16, 0)


satellite = scenario.children.new(STKObjectType.SATELLITE, "Satellite")
satellite.set_propagator_type(PropagatorType.SGP4)
propagator = satellite.propagator
propagator.common_tasks.add_segments_from_online_source("25544")
propagator.propagate()

lighting_constraint = satellite.access_constraints.add_constraint(
    AccessConstraintType.LIGHTING
)
lighting_constraint.condition = ConstraintLighting.DIRECT_SUN

access = facility.get_access_to_object(satellite)
access.compute_access()

start_time = root.current_scenario.start_time
stop_time = root.current_scenario.stop_time
to_pandas_dataframe(access.data_providers.item("Access Data").execute_elements(start_time, stop_time, ["Access Number", "Duration", "Stop Time"]).data_sets)
df = access.data_providers.item("Access Data").execute_elements(start_time, stop_time, ["Access Number", "Duration"]).data_sets.to_pandas_dataframe()