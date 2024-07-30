StkPreferencesVDF
=================

.. py:class:: ansys.stk.core.stkobjects.StkPreferencesVDF

   Bases: 

   Allow configuring VDF preferences.

.. py:currentmodule:: StkPreferencesVDF

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesVDF.save_scenario_as_vdf`
              - Gets or sets the SaveScenarioAsVDF property determines whether a scenario will be saved as a scenario file or as a VDF file when the Save method is called. If a VDF file is loaded, then the SaveScenarioAsVDF property has no effect when Save is called.
            * - :py:attr:`~ansys.stk.core.stkobjects.StkPreferencesVDF.base_directory`
              - Gets or sets the Base Directory where VDF file is extracted.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import StkPreferencesVDF


Property detail
---------------

.. py:property:: save_scenario_as_vdf
    :canonical: ansys.stk.core.stkobjects.StkPreferencesVDF.save_scenario_as_vdf
    :type: bool

    Gets or sets the SaveScenarioAsVDF property determines whether a scenario will be saved as a scenario file or as a VDF file when the Save method is called. If a VDF file is loaded, then the SaveScenarioAsVDF property has no effect when Save is called.

.. py:property:: base_directory
    :canonical: ansys.stk.core.stkobjects.StkPreferencesVDF.base_directory
    :type: str

    Gets or sets the Base Directory where VDF file is extracted.


