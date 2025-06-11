DataProviderCollection
======================

.. py:class:: ansys.stk.core.stkobjects.DataProviderCollection

   Collection of data providers attached to the current STK object.

.. py:currentmodule:: DataProviderCollection

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_schema`
              - Return a string containing the XML representation of the available data providers.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.item`
              - Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_information_from_path`
              - Return the data provider information specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_time_varying_from_path`
              - Return the time variable data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_interval_from_path`
              - Return the interval data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_fixed_from_path`
              - Return the fixed data provider specified by the data provider path.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_item_by_index`
              - Retrieve a data provider from the collection by index.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.get_item_by_name`
              - Retrieve a data provider from the collection by name.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection.count`
              - Return number of elements in the collection.
            * - :py:attr:`~ansys.stk.core.stkobjects.DataProviderCollection._new_enum`
              - Return the enumerator for the collection.



Examples
--------

Get Data for Specific Points and Elements

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    times = [[0], [15000], [20000], [55000]]
    elems = [["Time"], ["Precision Pass Number"]]
    satPassesDP = satellite.data_providers.item(
        "Precision Passes"
    ).execute_single_elements_array(times, elems)
    passes = satPassesDP.get_array(1)


Get Data for a Single Point in Time

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    satPassDP = satellite.data_providers.item("Precision Passes").execute_single(2600)
    passes = satPassDP.data_sets.get_data_set_by_name("Precision Pass Number").get_values()


Extract Elements from Data Providers with pre-data

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    # Facility facility: Facility object
    # Scenario scenario: Scenario object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    facChooseDP = facility.data_providers.item("Points Choose System")
    dataProvCenter = facChooseDP.group.item("Center")
    # Choose the reference system you want to report the Center point in
    dataProvCenter.pre_data = "CentralBody/Earth TOD"
    rptElems = [["Time"], ["x"], ["y"], ["z"]]
    results = dataProvCenter.execute_elements(
        scenario.start_time, scenario.stop_time, 60, rptElems
    )
    datasets = results.data_sets
    Time = datasets.get_data_set_by_name("Time").get_values()
    facTODx = datasets.get_data_set_by_name("x").get_values()
    facTODy = datasets.get_data_set_by_name("y").get_values()
    facTODz = datasets.get_data_set_by_name("z").get_values()


Extract Elements from Data Providers with Groups

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Scenario scenario: Scenario object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    satPosDP = (
        satellite.data_providers.item("Cartesian Position")
        .group.item("ICRF")
        .execute(scenario.start_time, scenario.stop_time, 60)
    )
    satx = satPosDP.data_sets.get_data_set_by_name("x").get_values()
    saty = satPosDP.data_sets.get_data_set_by_name("y").get_values()
    satz = satPosDP.data_sets.get_data_set_by_name("z").get_values()

    satVelDP = satellite.data_providers.get_data_provider_time_varying_from_path(
        "Cartesian Velocity/ICRF"
    ).execute(scenario.start_time, scenario.stop_time, 60)
    # There are 4 Methods to get DP From a Path depending on the kind of DP:
    #   GetDataPrvTimeVarFromPath
    #   GetDataPrvIntervalFromPath
    #   GetDataPrvInfoFromPath
    #   GetDataPrvFixedFromPath
    satvx = satVelDP.data_sets.get_data_set_by_name("x").get_values()
    satvy = satVelDP.data_sets.get_data_set_by_name("y").get_values()
    satvz = satVelDP.data_sets.get_data_set_by_name("z").get_values()


Use a Time Dependent Data Provider and requesting only specified elements

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Scenario scenario: Scenario object
    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    elems = [["Time"], ["q1"], ["q2"], ["q3"], ["q4"]]
    satDP = satellite.data_providers.item("Attitude Quaternions").execute_elements(
        scenario.start_time, scenario.stop_time, 60, elems
    )
    # Whenever you pass an index to an array, you need to cast it to a long
    # equivalent (int32)
    satTime = satDP.data_sets.item(0).get_values()
    satq1 = satDP.data_sets.item(1).get_values()
    satq2 = satDP.data_sets.item(2).get_values()
    satq3 = satDP.data_sets.item(3).get_values()
    satq4 = satDP.data_sets.item(4).get_values()


Use an interval Data Provider

.. code-block:: python

    # STKObjectRoot root: STK Object Model root
    # Satellite satellite: Satellite object
    # Facility facility: Facility object

    # Change DateFormat dimension to epoch seconds to make the data easier to handle in
    # Python
    root.units_preferences.item("DateFormat").set_current_unit("EpSec")
    # Get the current scenario
    scenario = root.current_scenario
    # Set up the access object
    access = satellite.get_access_to_object(facility)
    access.compute_access()
    # Get the Access AER Data Provider
    accessDP = access.data_providers.item("Access Data").execute(
        scenario.start_time, scenario.stop_time
    )

    accessStartTimes = accessDP.data_sets.get_data_set_by_name("Start Time").get_values()
    accessStopTimes = accessDP.data_sets.get_data_set_by_name("Stop Time").get_values()


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DataProviderCollection


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.count
    :type: int

    Return number of elements in the collection.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection._new_enum
    :type: EnumeratorProxy

    Return the enumerator for the collection.


Method detail
-------------

.. py:method:: get_schema(self) -> str
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_schema

    Return a string containing the XML representation of the available data providers.

    :Returns:

        :obj:`~str`

.. py:method:: item(self, index_or_name: typing.Any) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.item

    Given an index, returns the element in the collection. If the index is an integer, then method returns the element in the collection at the given position. If the index is a string, then the method returns the element with the specified name.

    :Parameters:

        **index_or_name** : :obj:`~typing.Any`


    :Returns:

        :obj:`~IDataProviderInfo`



.. py:method:: get_data_provider_information_from_path(self, data_provider_path: str) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_information_from_path

    Return the data provider information specified by the data provider path.

    :Parameters:

        **data_provider_path** : :obj:`~str`


    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_data_provider_time_varying_from_path(self, data_provider_path: str) -> DataProviderTimeVarying
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_time_varying_from_path

    Return the time variable data provider specified by the data provider path.

    :Parameters:

        **data_provider_path** : :obj:`~str`


    :Returns:

        :obj:`~DataProviderTimeVarying`

.. py:method:: get_data_provider_interval_from_path(self, data_provider_path: str) -> DataProviderInterval
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_interval_from_path

    Return the interval data provider specified by the data provider path.

    :Parameters:

        **data_provider_path** : :obj:`~str`


    :Returns:

        :obj:`~DataProviderInterval`

.. py:method:: get_data_provider_fixed_from_path(self, data_provider_path: str) -> DataProviderFixed
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_data_provider_fixed_from_path

    Return the fixed data provider specified by the data provider path.

    :Parameters:

        **data_provider_path** : :obj:`~str`


    :Returns:

        :obj:`~DataProviderFixed`

.. py:method:: get_item_by_index(self, index: int) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_item_by_index

    Retrieve a data provider from the collection by index.

    :Parameters:

        **index** : :obj:`~int`


    :Returns:

        :obj:`~IDataProviderInfo`

.. py:method:: get_item_by_name(self, name: str) -> IDataProviderInfo
    :canonical: ansys.stk.core.stkobjects.DataProviderCollection.get_item_by_name

    Retrieve a data provider from the collection by name.

    :Parameters:

        **name** : :obj:`~str`


    :Returns:

        :obj:`~IDataProviderInfo`

