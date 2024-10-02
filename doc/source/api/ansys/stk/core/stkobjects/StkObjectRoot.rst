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
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.all_instance_names_to_xml`
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
              - Load a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.load_vdf_from_sdf_with_version`
              - Load a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.save_vdf_to_sdf`
              - Save a vdf to SDF at the specified location. The method throws an exception if the VDF creation or upload fails.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.Subscribe`
              - """Return an IStkObjectRootEventHandler that is subscribed to handle events associated with this instance of StkObjectRoot."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.unit_preferences`
              - Provides access to the Global Unit table.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.current_scenario`
              - Returns a Scenario object or null if no scenario has been loaded yet.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.isolated`
              - Returns whether the instance is isolated.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.conversion_utility`
              - Returns the conversion utility interface.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.std_military2525_b_symbols`
              - Returns the interface that enables creating 2525b symbols.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.available_features`
              - Allows the user to inquiry about the available features.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.vgt_root`
              - Returns an instance of VGT root object.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.central_bodies`
              - Returns a collection of available central bodies.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.notification_filter`
              - Temporarily disable only the root events to prevent them from being raised. The event filtering can be used to improve client application performance.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkObjectRoot.stk_preferences`
              - Configures STK preferences.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkObjectRoot


Property detail
---------------

.. py:property:: unit_preferences
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.unit_preferences
    :type: IUnitPreferencesDimensionCollection

    Provides access to the Global Unit table.

.. py:property:: current_scenario
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.current_scenario
    :type: IStkObject

    Returns a Scenario object or null if no scenario has been loaded yet.

.. py:property:: isolated
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.isolated
    :type: bool

    Returns whether the instance is isolated.

.. py:property:: conversion_utility
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.conversion_utility
    :type: IConversionUtility

    Returns the conversion utility interface.

.. py:property:: std_military2525_b_symbols
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.std_military2525_b_symbols
    :type: StdMilitary2525bSymbols

    Returns the interface that enables creating 2525b symbols.

.. py:property:: available_features
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.available_features
    :type: AvailableFeatures

    Allows the user to inquiry about the available features.

.. py:property:: vgt_root
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.vgt_root
    :type: IAnalysisWorkbenchProviderRoot

    Returns an instance of VGT root object.

.. py:property:: central_bodies
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.central_bodies
    :type: StkCentralBodyCollection

    Returns a collection of available central bodies.

.. py:property:: notification_filter
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.notification_filter
    :type: None

    Temporarily disable only the root events to prevent them from being raised. The event filtering can be used to improve client application performance.

.. py:property:: stk_preferences
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.stk_preferences
    :type: StkPreferences

    Configures STK preferences.


Method detail
-------------

.. py:method:: execute_command(self, connectCommand: str) -> ExecuteCommandResult
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.execute_command

    Execute a custom CONNECT action. The method throws an exception if the command has failed.

    :Parameters:

    **connectCommand** : :obj:`~str`

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

.. py:method:: new_scenario(self, scenarioName: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.new_scenario

    Create a new scenario. User must close a scenario before creating a new one; otherwise an exception will occur.

    :Parameters:

    **scenarioName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: save_scenario(self) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_scenario

    Use Save method. Saves the changes made to the scenario.

    :Returns:

        :obj:`~None`

.. py:method:: save_scenario_as(self, scFileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_scenario_as

    Use SaveAs method. Saves the changes made to the scenario to a specified path and file name.

    :Parameters:

    **scFileName** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: load_custom_marker(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load_custom_marker

    Add a custom marker to Application.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_object_from_path(self, objectPath: str) -> IStkObject
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.get_object_from_path

    Get the object instance that matches the path provided.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~IStkObject`

.. py:method:: all_instance_names_to_xml(self) -> str
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.all_instance_names_to_xml

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

.. py:method:: execute_multiple_commands(self, connectCommands: list, action: EXECUTE_MULTIPLE_COMMANDS_MODE) -> ExecuteMultipleCommandResult
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.execute_multiple_commands

    Execute multiple CONNECT actions.  The behavior of the method when encountering an exception varies depending on the setting of the Action parameter. See the help for AgEExecMultiCmdResultAction.

    :Parameters:

    **connectCommands** : :obj:`~list`
    **action** : :obj:`~EXECUTE_MULTIPLE_COMMANDS_MODE`

    :Returns:

        :obj:`~ExecuteMultipleCommandResult`

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


.. py:method:: object_exists(self, objectPath: str) -> bool
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.object_exists

    Check whether a currently loaded scenario contains an object with the given path.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: get_licensing_report(self) -> str
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.get_licensing_report

    Return a formatted string that contains the license names and their states. The string is formatted as an XML document.

    :Returns:

        :obj:`~str`



.. py:method:: save_vdf_as(self, vdfFileName: str, password: str, description: str, windowID: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_vdf_as

    Save the changes made to the scenario to a specified path and file name as a vdf file.

    :Parameters:

    **vdfFileName** : :obj:`~str`
    **password** : :obj:`~str`
    **description** : :obj:`~str`
    **windowID** : :obj:`~str`

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

.. py:method:: save_as(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_as

    Save the changes made to the scenario/vdf to a specified path and file name.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_vdf_from_sdf(self, vDFPath: str, password: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load_vdf_from_sdf

    Load a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.

    :Parameters:

    **vDFPath** : :obj:`~str`
    **password** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_vdf_from_sdf_with_version(self, vDFPath: str, password: str, version: float) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.load_vdf_from_sdf_with_version

    Load a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.

    :Parameters:

    **vDFPath** : :obj:`~str`
    **password** : :obj:`~str`
    **version** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: save_vdf_to_sdf(self, sDFPath: str) -> None
    :canonical: ansys.stk.core.stkobjects.StkObjectRoot.save_vdf_to_sdf

    Save a vdf to SDF at the specified location. The method throws an exception if the VDF creation or upload fails.

    :Parameters:

    **sDFPath** : :obj:`~str`

    :Returns:

        :obj:`~None`

