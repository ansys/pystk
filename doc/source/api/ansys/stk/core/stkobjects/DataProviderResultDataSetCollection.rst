DataProviderResultDataSetCollection
===================================

.. py:class:: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection

   Represents a collection of datasets in the interval returned by the data providers.

.. py:currentmodule:: DataProviderResultDataSetCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.item`
              - Given an index, returns an element in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.get_data_set_by_name`
              - Return the element, given the name.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.get_row`
              - Return the specified row.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_array`
              - Return the entire dataset collection in row format.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_numpy_array`
              - Return a row formatted dataset collection as a numpy array. This function requires ``numpy``.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_pandas_dataframe`
              - Return a row formatted dataset collection as a pandas DataFrame. This function requires ``pandas``.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.count`
              - Return a number of elements in collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection._new_enum`
              - Return an enumerator for the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.row_count`
              - Return the number of rows in the dataset collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.element_names`
              - Return the element names.



Examples
--------

Create a heat map of coverage definition results graphing duration by asset using a Pandas DataFrame

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    from matplotlib import pyplot as plt
    import numpy as np

    # compute data provider results for All Regions by Pass coverage
    coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
    coverage_data = coverage_data_provider.execute()

    # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
    coverage_all_regions_elements = coverage_data_provider.elements
    all_regions_coverage_df = coverage_data.data_sets.to_pandas_dataframe(data_provider_elements=coverage_all_regions_elements)

    # reshape the DataFrame based on column values
    pivot = all_regions_coverage_df.pivot_table(index='region name', columns='asset name', values='duration')

    # plot heat map that shows duration by asset name by region
    plt.xlabel('Duration by Asset', fontsize=20)
    plt.xticks(ticks=range(len(pivot.columns.values)), labels=pivot.columns.values)

    plt.ylabel('Region Name', fontsize=20)
    plt.yticks(ticks=np.arange(len(pivot.index), step=10), labels=pivot.index[::10])

    im = plt.imshow(pivot, cmap="YlGnBu", aspect='auto', interpolation='none')
    plt.colorbar(orientation='vertical')


Compute descriptive statistics for access measurements using a Pandas DataFrame

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    import pandas as pd

    # compute data provider results for All Regions by Pass coverage
    coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
    coverage_data = coverage_data_provider.execute()

    # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
    all_regions_coverage_df = coverage_data.data_sets.to_pandas_dataframe()

    # compute descriptive statistics of Duration, Percent Coverage, Area Coverage
    all_regions_coverage_df[['duration', 'percent coverage', 'area coverage']].apply(pd.to_numeric).describe()


Convert access data provider results to a Pandas DataFrame

.. code-block:: python

    # Access facility_sensor_satellite_access: Access calculation
    # compute data provider results for basic Access
    field_names = ['Access Number', 'Start Time', 'Stop Time', 'Duration']

    access_data = facility_sensor_satellite_access.data_providers['Access Data'].execute_elements(
        self.get_scenario().start_time, self.get_scenario().stop_time, field_names
    )

    # convert dataset collection in a row format as a Pandas DataFrame
    index_column = 'Access Number'
    access_data_df = access_data.data_sets.to_pandas_dataframe(index_element_name=index_column)


Convert coverage definition data provider results to a Pandas DataFrame

.. code-block:: python

    # CoverageDefinition coverage: Coverage object
    # compute data provider results for All Regions by Pass coverage
    coverage_data_provider = coverage.data_providers.item('All Regions By Pass')
    coverage_data = coverage_data_provider.execute()

    # convert dataset collection in a row format as a Pandas DataFrame with default numeric row index
    coverage_arr = coverage_data.data_sets.to_pandas_dataframe()


Load a Numpy array with flight profile data

.. code-block:: python

    # Aircraft aircraft: Aircraft object
    from scipy.spatial import ConvexHull
    import matplotlib.pyplot as plt

    # compute data provider results for an aircraft's Flight Profile By Time
    field_names = ['Mach #', 'Altitude']
    time_step_sec = 1.0

    flight_profile_data_provider = aircraft.data_providers.item('Flight Profile By Time')
    flight_profile_data = flight_profile_data_provider.execute_elements(self.get_scenario().start_time, self.get_scenario().stop_time, time_step_sec, field_names)

    # convert dataset collection in a row format as a Numpy array
    flight_profile_data_arr = flight_profile_data.data_sets.to_numpy_array()

    # plot estimated fligth envelope as a convex hull
    hull = ConvexHull(flight_profile_data_arr)

    plt.figure(figsize=(15,10))
    for simplex in hull.simplices:
        plt.plot(flight_profile_data_arr[simplex, 1], flight_profile_data_arr[simplex, 0], color="darkblue")

    plt.title('Estimated Flight Envelope', fontsize=15)
    plt.xlabel('Mach Number', fontsize=15)
    plt.ylabel('Altitude', fontsize=15)

    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=15)
    plt.grid(visible=True)


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderResultDataSetCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.count
    :type: int

    Return a number of elements in collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection._new_enum
    :type: EnumeratorProxy

    Return an enumerator for the collection.

.. py:property:: row_count
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.row_count
    :type: int

    Return the number of rows in the dataset collection.

.. py:property:: element_names
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.element_names
    :type: list

    Return the element names.


Method detail
-------------


.. py:method:: item(self, index: int) -> DataProviderResultDataSet
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.item

    Given an index, returns an element in the collection.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~DataProviderResultDataSet`


.. py:method:: get_data_set_by_name(self, data_set_name: str) -> DataProviderResultDataSet
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.get_data_set_by_name

    Return the element, given the name.

    :Parameters:

    **data_set_name** : :obj:`~str`

    :Returns:

        :obj:`~DataProviderResultDataSet`


.. py:method:: get_row(self, index: int) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.get_row

    Return the specified row.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~list`

.. py:method:: to_array(self) -> list
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_array

    Return the entire dataset collection in row format.

    :Returns:

        :obj:`~list`

.. py:method:: to_numpy_array(self) -> ndarray
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_numpy_array

    Return a row formatted dataset collection as a numpy array. This function requires ``numpy``.

    :Returns:

        :obj:`~ndarray`

.. py:method:: to_pandas_dataframe(self, index_element_name: str, data_provider_elements: DataProviderElements) -> DataFrame:
    :canonical: ansys.stk.core.stkobjects.DataProviderResultDataSetCollection.to_pandas_dataframe

    Return a row formatted dataset collection as a pandas DataFrame. This function requires ``pandas``.

    This function optionally maps data provider element types to pandas DataFrame column dtypes and optionally sets the
    column to be used as the DataFrame index.

    :Parameters:

    **index_element_name** : :obj:`~str`
    **data_provider_elements** : :obj:`~DataProviderElements`

    :Returns:

        :obj:`~DataFrame`

