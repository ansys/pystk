IStkPreferencesVDF
==================

.. py:class:: IStkPreferencesVDF

   object
   
   VDF Load/Save settings.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~save_scenario_as_vdf`
            * - :py:meth:`~base_directory`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkPreferencesVDF


Property detail
---------------

.. py:property:: save_scenario_as_vdf
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesVDF.save_scenario_as_vdf
    :type: bool

    Gets or sets the SaveScenarioAsVDF property determines whether a scenario will be saved as a scenario file or as a VDF file when the Save method is called. If a VDF file is loaded, then the SaveScenarioAsVDF property has no effect when Save is called.

.. py:property:: base_directory
    :canonical: ansys.stk.core.stkobjects.IStkPreferencesVDF.base_directory
    :type: str

    Gets or sets the Base Directory where VDF file is extracted.


