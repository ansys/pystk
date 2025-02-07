PreferencesVDF
==============

.. py:class:: ansys.stk.core.stkobjects.PreferencesVDF

   Allow configuring VDF preferences.

.. py:currentmodule:: PreferencesVDF

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesVDF.save_scenario_as_vdf`
              - Get or set the SaveScenarioAsVDF property determines whether a scenario will be saved as a scenario file or as a VDF file when the Save method is called. If a VDF file is loaded, then the SaveScenarioAsVDF property has no effect when Save is called.
            * - :py:attr:`~ansys.stk.core.stkobjects.PreferencesVDF.base_directory`
              - Get or set the Base Directory where VDF file is extracted.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import PreferencesVDF


Property detail
---------------

.. py:property:: save_scenario_as_vdf
    :canonical: ansys.stk.core.stkobjects.PreferencesVDF.save_scenario_as_vdf
    :type: bool

    Get or set the SaveScenarioAsVDF property determines whether a scenario will be saved as a scenario file or as a VDF file when the Save method is called. If a VDF file is loaded, then the SaveScenarioAsVDF property has no effect when Save is called.

.. py:property:: base_directory
    :canonical: ansys.stk.core.stkobjects.PreferencesVDF.base_directory
    :type: str

    Get or set the Base Directory where VDF file is extracted.


