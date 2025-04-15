StkObjectRoot
=============

.. py:class:: ansys.stk.core.stkobjects.StkObjectRoot

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`, :py:class:`~ansys.stk.core.stkobjects.IAnimation`

   Top-level object in the Object Model Hierarchy.

.. py:currentmodule:: StkObjectRoot

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.execute_command`
              - Execute a custom CONNECT action. The method throws an exception if the command has failed.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.load_scenario`
              - Use Load method. Loads a scenario using the specified path. The method throws an exception if there is a scenario already loaded.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.close_scenario`
              - Close the scenario. The method throws an exception if no scenario has been loaded.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.new_scenario`
              - Create a new scenario. User must close a scenario before creating a new one; otherwise an exception will occur.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.save_scenario`
              - Use Save method. Saves the changes made to the scenario.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.save_scenario_as`
              - Use SaveAs method. Saves the changes made to the scenario to a specified path and file name.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.load_custom_marker`
              - Add a custom marker to Application.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.get_object_from_path`
              - Get the object instance that matches the path provided.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.all_instance_names_in_xml`
              - Return an XML representation of AllInstanceNames.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.begin_update`
              - Signals the object that the batch update is starting.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.end_update`
              - Signals the object that the batch update is complete.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.execute_multiple_commands`
              - Execute multiple CONNECT actions.  The behavior of the method when encountering an exception varies depending on the setting of the Action parameter. See the help for AgEExecMultiCmdResultAction.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.isolate`
              - Make the unit preferences of the current instance isolated.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.load_vdf`
              - Load a vdf using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.object_exists`
              - Check whether a currently loaded scenario contains an object with the given path.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.get_licensing_report`
              - Return a formatted string that contains the license names and their states. The string is formatted as an XML document.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.save_vdf_as`
              - Save the changes made to the scenario to a specified path and file name as a vdf file.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.load`
              - Load a scenario/vdf using the specified path. The method throws an exception if there is a scenario already loaded.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.save`
              - Save the changes made to the scenario/vdf.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.save_as`
              - Save the changes made to the scenario/vdf to a specified path and file name.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.load_vdf_from_sdf`
              - Do not use this method, as it is deprecated. SDF functionality has been removed and this will be removed in the next major release. Loads a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.load_vdf_from_sdf_with_version`
              - Do not use this method, as it is deprecated. SDF functionality has been removed and this will be removed in the next major release. Loads a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.save_vdf_to_sdf`
              - Do not use this method, as it is deprecated. SDF functionality has been removed and this will be removed in the next major release. Saves a vdf to SDF at the specified location. The method throws an exception if the VDF creation or upload fails.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.subscribe`
              - """Return an IStkObjectRootEventHandler that is subscribed to handle events associated with this instance of StkObjectRoot."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.units_preferences`
              - Provide access to the Global Unit table.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.current_scenario`
              - Return a Scenario object or null if no scenario has been loaded yet.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.isolated`
              - Return whether the instance is isolated.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.conversion_utility`
              - Return the conversion utility interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.military_standard_2525b_symbols`
              - Return the interface that enables creating 2525b symbols.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.available_features`
              - Allow the user to inquiry about the available features.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.analysis_workbench_components_root`
              - Return an instance of VGT root object.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.central_bodies`
              - Return a collection of available central bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.notification_filter`
              - Temporarily disable only the root events to prevent them from being raised. The event filtering can be used to improve client application performance.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.preferences`
              - Configures STK preferences.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.rf_channel_modeler`
              - Return an RF Channel Modeler object.



Examples
--------

Extract data from Connect result

.. code-block:: python

    result = root.execute_command('Report_RM */Place/MyPlace Style "Cartesian Position"')

    for i in range(0, result.count):
        cmdRes = result.item(i)
        print(cmdRes)


Use arrays to send and retrieve data with Connect

.. code-block:: python

    from ansys.stk.core.stkutil import ExecuteMultipleCommandsMode

    connect_commands = ['GetStkVersion /', 'New / Scenario ExampleScenario']
    command_results = root.execute_multiple_commands(connect_commands, ExecuteMultipleCommandsMode.CONTINUE_ON_ERROR)

    first_message = command_results.item(0)
    also_first_message = command_results[0]

    for message in command_results:
        print(message.count)


Execute multiple Connect commands

.. code-block:: python

    commandList = [["New / */Place MyPlace"], ["SetPosition */Place/MyPlace Geodetic 37.9 -75.5 0.0"]]
    root.execute_multiple_commands(commandList, ExecuteMultipleCommandsMode.EXCEPTION_ON_ERROR)


Execute Connect command

.. code-block:: python

    root.execute_command("New / */Target MyTarget")


Attach to an already running STK Runtime and get a reference to STK Object Root

.. code-block:: python

    # Attach to already running instance of STK Runtime
    from ansys.stk.core.stkruntime import STKRuntime

    stk = STKRuntime.attach_to_application()

    # Get the STK Object Root interface
    root = stk.new_object_root()


Start STK Runtime and get a reference to STK Object Root

.. code-block:: python

    # Start new instance of STK Runtime
    from ansys.stk.core.stkruntime import STKRuntime

    stk = STKRuntime.start_application()

    # Get the STK Object Root interface
    root = stk.new_object_root()


Start STK Desktop and get a reference to STK Object Root

.. code-block:: python

    # Start new instance of STK Desktop
    from ansys.stk.core.stkdesktop import STKDesktop

    stk = STKDesktop.start_application(visible=True)  # using optional visible argument

    # Get the STK Object Root interface
    root = stk.root

    # ...

    # Clean-up when done
    stk.shutdown()


Get a reference to STK Object Root using a running STK Desktop instance

.. code-block:: python

    # Get reference to running STK Desktop instance
    from ansys.stk.core.stkdesktop import STKDesktop

    stk = STKDesktop.attach_to_application()

    # Get the STK Object Root interface
    root = stk.root


Initialize STK Engine in no graphics mode and get a reference to STK Object Root

.. code-block:: python

    # Initialize STK Engine without graphics in the current process
    from ansys.stk.core.stkengine import STKEngine

    stk = STKEngine.start_application(no_graphics=True)

    # Get the STK Object Root interface
    root = stk.new_object_root()


Initialize STK Engine with graphics and get a reference to STK Object Root

.. code-block:: python

    # Initialize STK Engine with graphics in the current process
    from ansys.stk.core.stkengine import STKEngine

    stk = STKEngine.start_application(no_graphics=False)

    # Get the STK Object Root interface
    root = stk.new_object_root()


Set unit preferences for Object Model

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    root.units_preferences.item("DateFormat").set_current_unit("UTCG")
    root.units_preferences.item("Distance").set_current_unit("km")


Create a new Scenario

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    root.new_scenario("Example_Scenario")


Manage STK Desktop events

.. code-block:: python

    from ansys.stk.core.stkdesktop import STKDesktop
    from ansys.stk.core.stkobjects import STKObjectType

    def on_stk_object_added_custom_callback(path:str):
        print(f'{path} has been added.')

    stk = STKDesktop.start_application(visible=True)
    root = stk.root
    root.new_scenario('ExampleScenario')
    skt_object_root_events = root.subscribe()
    skt_object_root_events.on_stk_object_added += on_stk_object_added_custom_callback
    scenario = root.current_scenario

    # on_stk_object_added_custom_callback is successfully called when the next line is executed
    facility = scenario.children.new(STKObjectType.FACILITY, 'AGI_HQ')

    # Now switch control to the desktop application and create another facility.
    # The user interface becomes unresponsive.

    # Now open a tkinter window that processing COM messages.
    from tkinter import Tk

    window = Tk()
    window.mainloop()


Manage STK Engine events

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    def on_scenario_new_custom_callback(path: str):
        print(f'Scenario {path} has been created.')

    skt_object_root_events = root.subscribe()
    skt_object_root_events.on_scenario_new += on_scenario_new_custom_callback

    root.new_scenario('ExampleScenario')
    # callback should be executed now

    # remove the callback from the handler
    skt_object_root_events.on_scenario_new -= on_scenario_new_custom_callback

    # all finished with events, unsubscribe
    skt_object_root_events.unsubscribe()


Close an open Scenario

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    root.close_scenario()


Open a Viewer Data File

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    root.load_vdf(os.path.join(installPath, "Data", "ExampleScenarios", "Intro_STK_Space_Systems.vdf"), "")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkObjectRoot


Property detail
---------------

.. py:property:: units_preferences
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.units_preferences
    :type: IUnitPreferencesDimensionCollection

    Provide access to the Global Unit table.

    Examples
    --------

    Set unit preferences for Object Model

    .. code-block:: python

        # StkObjectRoot root: STK Object Model Root
        root.units_preferences.item("DateFormat").set_current_unit("UTCG")
        root.units_preferences.item("Distance").set_current_unit("km")


.. py:property:: current_scenario
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.current_scenario
    :type: IStkObject

    Return a Scenario object or null if no scenario has been loaded yet.

.. py:property:: isolated
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.isolated
    :type: bool

    Return whether the instance is isolated.

.. py:property:: conversion_utility
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.conversion_utility
    :type: ConversionUtility

    Return the conversion utility interface.

.. py:property:: military_standard_2525b_symbols
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.military_standard_2525b_symbols
    :type: MilitaryStandard2525bSymbols

    Return the interface that enables creating 2525b symbols.

.. py:property:: available_features
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.available_features
    :type: AvailableFeatures

    Allow the user to inquiry about the available features.

.. py:property:: analysis_workbench_components_root
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.analysis_workbench_components_root
    :type: IAnalysisWorkbenchRoot

    Return an instance of VGT root object.

.. py:property:: central_bodies
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.central_bodies
    :type: CentralBodyCollection

    Return a collection of available central bodies.

.. py:property:: notification_filter
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.notification_filter
    :type: None

    Temporarily disable only the root events to prevent them from being raised. The event filtering can be used to improve client application performance.

.. py:property:: preferences
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.preferences
    :type: Preferences

    Configures STK preferences.

.. py:property:: rf_channel_modeler
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.rf_channel_modeler
    :type: typing.Any

    Return an RF Channel Modeler object.


Method detail
-------------

.. py:method:: execute_command(self, connect_command: str) -> ExecuteCommandResult
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.execute_command

    Execute a custom CONNECT action. The method throws an exception if the command has failed.

    :Parameters:

    **connect_command** : :obj:`~str`

    :Returns:

        :obj:`~ExecuteCommandResult`

.. py:method:: load_scenario(self, path: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load_scenario

    Use Load method. Loads a scenario using the specified path. The method throws an exception if there is a scenario already loaded.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: close_scenario(self) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.close_scenario

    Close the scenario. The method throws an exception if no scenario has been loaded.

    :Returns:

        :obj:`~None`

    Examples
    --------

    Close an open Scenario

    .. code-block:: python

        # StkObjectRoot root: STK Object Model Root
        root.close_scenario()


.. py:method:: new_scenario(self, scenario_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.new_scenario

    Create a new scenario. User must close a scenario before creating a new one; otherwise an exception will occur.

    :Parameters:

    **scenario_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

    Examples
    --------

    Create a new Scenario

    .. code-block:: python

        # StkObjectRoot root: STK Object Model Root
        root.new_scenario("Example_Scenario")


.. py:method:: save_scenario(self) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_scenario

    Use Save method. Saves the changes made to the scenario.

    :Returns:

        :obj:`~None`

.. py:method:: save_scenario_as(self, sc_file_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_scenario_as

    Use SaveAs method. Saves the changes made to the scenario to a specified path and file name.

    :Parameters:

    **sc_file_name** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: load_custom_marker(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load_custom_marker

    Add a custom marker to Application.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_object_from_path(self, object_path: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.get_object_from_path

    Get the object instance that matches the path provided.

    :Parameters:

    **object_path** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: all_instance_names_in_xml(self) -> str
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.all_instance_names_in_xml

    Return an XML representation of AllInstanceNames.

    :Returns:

        :obj:`~str`

.. py:method:: begin_update(self) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.begin_update

    Signals the object that the batch update is starting.

    :Returns:

        :obj:`~None`

.. py:method:: end_update(self) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.end_update

    Signals the object that the batch update is complete.

    :Returns:

        :obj:`~None`

.. py:method:: execute_multiple_commands(self, connect_commands: list, action: ExecuteMultipleCommandsMode) -> ExecuteMultipleCommandsResult
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.execute_multiple_commands

    Execute multiple CONNECT actions.  The behavior of the method when encountering an exception varies depending on the setting of the Action parameter. See the help for AgEExecMultiCmdResultAction.

    :Parameters:

    **connect_commands** : :obj:`~list`
    **action** : :obj:`~ExecuteMultipleCommandsMode`

    :Returns:

        :obj:`~ExecuteMultipleCommandsResult`

.. py:method:: isolate(self) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.isolate

    Make the unit preferences of the current instance isolated.

    :Returns:

        :obj:`~None`




.. py:method:: load_vdf(self, path: str, password: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load_vdf

    Load a vdf using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.

    :Parameters:

    **path** : :obj:`~str`
    **password** : :obj:`~str`

    :Returns:

        :obj:`~None`


    Examples
    --------

    Open a Viewer Data File

    .. code-block:: python

        # StkObjectRoot root: STK Object Model Root
        installPath = r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
        root.load_vdf(os.path.join(installPath, "Data", "ExampleScenarios", "Intro_STK_Space_Systems.vdf"), "")


.. py:method:: object_exists(self, object_path: str) -> bool
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.object_exists

    Check whether a currently loaded scenario contains an object with the given path.

    :Parameters:

    **object_path** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: get_licensing_report(self) -> str
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.get_licensing_report

    Return a formatted string that contains the license names and their states. The string is formatted as an XML document.

    :Returns:

        :obj:`~str`



.. py:method:: save_vdf_as(self, vdf_file_name: str, password: str, description: str, window_id: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_vdf_as

    Save the changes made to the scenario to a specified path and file name as a vdf file.

    :Parameters:

    **vdf_file_name** : :obj:`~str`
    **password** : :obj:`~str`
    **description** : :obj:`~str`
    **window_id** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: load(self, path: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load

    Load a scenario/vdf using the specified path. The method throws an exception if there is a scenario already loaded.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: save(self) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save

    Save the changes made to the scenario/vdf.

    :Returns:

        :obj:`~None`

.. py:method:: save_as(self, file_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_as

    Save the changes made to the scenario/vdf to a specified path and file name.

    :Parameters:

    **file_name** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_vdf_from_sdf(self, vdf_path: str, password: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load_vdf_from_sdf

    Do not use this method, as it is deprecated. SDF functionality has been removed and this will be removed in the next major release. Loads a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded.

    :Parameters:

    **vdf_path** : :obj:`~str`
    **password** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_vdf_from_sdf_with_version(self, vdf_path: str, password: str, version: float) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load_vdf_from_sdf_with_version

    Do not use this method, as it is deprecated. SDF functionality has been removed and this will be removed in the next major release. Loads a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded.

    :Parameters:

    **vdf_path** : :obj:`~str`
    **password** : :obj:`~str`
    **version** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: save_vdf_to_sdf(self, sdf_path: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_vdf_to_sdf

    Do not use this method, as it is deprecated. SDF functionality has been removed and this will be removed in the next major release. Saves a vdf to SDF at the specified location. The method throws an exception if the VDF creation or upload fails.

    :Parameters:

    **sdf_path** : :obj:`~str`

    :Returns:

        :obj:`~None`


