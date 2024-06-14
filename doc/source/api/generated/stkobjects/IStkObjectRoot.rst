IStkObjectRoot
==============

.. py:class:: IStkObjectRoot

   object
   
   Represents the automation interface supported by the root object of the Automation Object Model.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~execute_command`
              - Execute a custom CONNECT action. The method throws an exception if the command has failed.
            * - :py:meth:`~load_scenario`
              - Use Load method. Loads a scenario using the specified path. The method throws an exception if there is a scenario already loaded.
            * - :py:meth:`~close_scenario`
              - Close the scenario. The method throws an exception if no scenario has been loaded.
            * - :py:meth:`~new_scenario`
              - Create a new scenario. User must close a scenario before creating a new one; otherwise an exception will occur.
            * - :py:meth:`~save_scenario`
              - Use Save method. Saves the changes made to the scenario.
            * - :py:meth:`~save_scenario_as`
              - Use SaveAs method. Saves the changes made to the scenario to a specified path and file name.
            * - :py:meth:`~load_custom_marker`
              - Add a custom marker to Application.
            * - :py:meth:`~get_object_from_path`
              - Get the object instance that matches the path provided.
            * - :py:meth:`~all_instance_names_to_xml`
              - Return an XML representation of AllInstanceNames.
            * - :py:meth:`~begin_update`
              - Signals the object that the batch update is starting.
            * - :py:meth:`~end_update`
              - Signals the object that the batch update is complete.
            * - :py:meth:`~execute_multiple_commands`
              - Execute multiple CONNECT actions.  The behavior of the method when encountering an exception varies depending on the setting of the Action parameter. See the help for AgEExecMultiCmdResultAction.
            * - :py:meth:`~isolate`
              - Make the unit preferences of the current instance isolated.
            * - :py:meth:`~load_vdf`
              - Load a vdf using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.
            * - :py:meth:`~object_exists`
              - Check whether a currently loaded scenario contains an object with the given path.
            * - :py:meth:`~get_licensing_report`
              - Return a formatted string that contains the license names and their states. The string is formatted as an XML document.
            * - :py:meth:`~save_vdf_as`
              - Save the changes made to the scenario to a specified path and file name as a vdf file.
            * - :py:meth:`~load`
              - Load a scenario/vdf using the specified path. The method throws an exception if there is a scenario already loaded.
            * - :py:meth:`~save`
              - Save the changes made to the scenario/vdf.
            * - :py:meth:`~save_as`
              - Save the changes made to the scenario/vdf to a specified path and file name.
            * - :py:meth:`~load_vdf_from_sdf`
              - Load a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.
            * - :py:meth:`~load_vdf_from_sdf_with_version`
              - Load a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.
            * - :py:meth:`~save_vdf_to_sdf`
              - Save a vdf to SDF at the specified location. The method throws an exception if the VDF creation or upload fails.
            * - :py:meth:`~Subscribe`
              - """Return an IStkObjectRootEventHandler that is subscribed to handle events associated with this instance of IStkObjectRoot."""

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~unit_preferences`
            * - :py:meth:`~current_scenario`
            * - :py:meth:`~isolated`
            * - :py:meth:`~conversion_utility`
            * - :py:meth:`~std_military2525_b_symbols`
            * - :py:meth:`~available_features`
            * - :py:meth:`~vgt_root`
            * - :py:meth:`~central_bodies`
            * - :py:meth:`~notification_filter`
            * - :py:meth:`~stk_preferences`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObjectRoot


Property detail
---------------

.. py:property:: unit_preferences
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.unit_preferences
    :type: "IAgUnitPrefsDimCollection"

    Provides access to the Global Unit table.

.. py:property:: current_scenario
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.current_scenario
    :type: "IAgStkObject"

    Returns a Scenario object or null if no scenario has been loaded yet.

.. py:property:: isolated
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.isolated
    :type: bool

    Returns whether the instance is isolated.

.. py:property:: conversion_utility
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.conversion_utility
    :type: "IAgConversionUtility"

    Returns the conversion utility interface.

.. py:property:: std_military2525_b_symbols
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.std_military2525_b_symbols
    :type: "IAgStdMil2525bSymbols"

    Returns the interface that enables creating 2525b symbols.

.. py:property:: available_features
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.available_features
    :type: "IAgAvailableFeatures"

    Allows the user to inquiry about the available features.

.. py:property:: vgt_root
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.vgt_root
    :type: "IAgCrdnRoot"

    Returns an instance of VGT root object.

.. py:property:: central_bodies
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.central_bodies
    :type: "IAgStkCentralBodyCollection"

    Returns a collection of available central bodies.

.. py:property:: notification_filter
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.notification_filter
    :type: None

    Temporarily disable only the root events to prevent them from being raised. The event filtering can be used to improve client application performance.

.. py:property:: stk_preferences
    :canonical: ansys.stk.core.stkobjects.IStkObjectRoot.stk_preferences
    :type: "IAgStkPreferences"

    Configures STK preferences.


Method detail
-------------

.. py:method:: execute_command(self, connectCommand:str) -> "IExecCmdResult"

    Execute a custom CONNECT action. The method throws an exception if the command has failed.

    :Parameters:

    **connectCommand** : :obj:`~str`

    :Returns:

        :obj:`~"IExecCmdResult"`

.. py:method:: load_scenario(self, path:str) -> None

    Use Load method. Loads a scenario using the specified path. The method throws an exception if there is a scenario already loaded.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: close_scenario(self) -> None

    Close the scenario. The method throws an exception if no scenario has been loaded.

    :Returns:

        :obj:`~None`

.. py:method:: new_scenario(self, scenarioName:str) -> None

    Create a new scenario. User must close a scenario before creating a new one; otherwise an exception will occur.

    :Parameters:

    **scenarioName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: save_scenario(self) -> None

    Use Save method. Saves the changes made to the scenario.

    :Returns:

        :obj:`~None`

.. py:method:: save_scenario_as(self, scFileName:str) -> None

    Use SaveAs method. Saves the changes made to the scenario to a specified path and file name.

    :Parameters:

    **scFileName** : :obj:`~str`

    :Returns:

        :obj:`~None`



.. py:method:: load_custom_marker(self, filename:str) -> None

    Add a custom marker to Application.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: get_object_from_path(self, objectPath:str) -> "IStkObject"

    Get the object instance that matches the path provided.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~"IStkObject"`

.. py:method:: all_instance_names_to_xml(self) -> str

    Return an XML representation of AllInstanceNames.

    :Returns:

        :obj:`~str`

.. py:method:: begin_update(self) -> None

    Signals the object that the batch update is starting.

    :Returns:

        :obj:`~None`

.. py:method:: end_update(self) -> None

    Signals the object that the batch update is complete.

    :Returns:

        :obj:`~None`

.. py:method:: execute_multiple_commands(self, connectCommands:list, action:"EXEC_MULTI_CMD_RESULT_ACTION") -> "IExecMultiCmdResult"

    Execute multiple CONNECT actions.  The behavior of the method when encountering an exception varies depending on the setting of the Action parameter. See the help for AgEExecMultiCmdResultAction.

    :Parameters:

    **connectCommands** : :obj:`~list`
    **action** : :obj:`~"EXEC_MULTI_CMD_RESULT_ACTION"`

    :Returns:

        :obj:`~"IExecMultiCmdResult"`

.. py:method:: isolate(self) -> None

    Make the unit preferences of the current instance isolated.

    :Returns:

        :obj:`~None`




.. py:method:: load_vdf(self, path:str, password:str) -> None

    Load a vdf using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.

    :Parameters:

    **path** : :obj:`~str`
    **password** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: object_exists(self, objectPath:str) -> bool

    Check whether a currently loaded scenario contains an object with the given path.

    :Parameters:

    **objectPath** : :obj:`~str`

    :Returns:

        :obj:`~bool`



.. py:method:: get_licensing_report(self) -> str

    Return a formatted string that contains the license names and their states. The string is formatted as an XML document.

    :Returns:

        :obj:`~str`



.. py:method:: save_vdf_as(self, vdfFileName:str, password:str, description:str, windowID:str) -> None

    Save the changes made to the scenario to a specified path and file name as a vdf file.

    :Parameters:

    **vdfFileName** : :obj:`~str`
    **password** : :obj:`~str`
    **description** : :obj:`~str`
    **windowID** : :obj:`~str`

    :Returns:

        :obj:`~None`


.. py:method:: load(self, path:str) -> None

    Load a scenario/vdf using the specified path. The method throws an exception if there is a scenario already loaded.

    :Parameters:

    **path** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: save(self) -> None

    Save the changes made to the scenario/vdf.

    :Returns:

        :obj:`~None`

.. py:method:: save_as(self, fileName:str) -> None

    Save the changes made to the scenario/vdf to a specified path and file name.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_vdf_from_sdf(self, vDFPath:str, password:str) -> None

    Load a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.

    :Parameters:

    **vDFPath** : :obj:`~str`
    **password** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: load_vdf_from_sdf_with_version(self, vDFPath:str, password:str, version:float) -> None

    Load a vdf from SDF using the specified path. The method throws an exception if there is a scenario already loaded. If the password isn't needed, enter an empty string.

    :Parameters:

    **vDFPath** : :obj:`~str`
    **password** : :obj:`~str`
    **version** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: save_vdf_to_sdf(self, sDFPath:str) -> None

    Save a vdf to SDF at the specified location. The method throws an exception if the VDF creation or upload fails.

    :Parameters:

    **sDFPath** : :obj:`~str`

    :Returns:

        :obj:`~None`

