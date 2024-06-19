IProfileSearchPlugin
====================

.. py:class:: IProfileSearchPlugin

   IProfile
   
   Properties of a plugin search profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~controls`
            * - :py:meth:`~results`
            * - :py:meth:`~plugin_config`
            * - :py:meth:`~plugin_identifier`
            * - :py:meth:`~scripting_tool`
            * - :py:meth:`~reset_controls_before_run`
            * - :py:meth:`~targeter_graphs`
            * - :py:meth:`~log_file`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileSearchPlugin


Property detail
---------------

.. py:property:: controls
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin.controls
    :type: IAgVASearchPluginControlCollection

    Get the selected control parameters.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin.results
    :type: IAgVASearchPluginResultCollection

    Get the selected equality constraints.

.. py:property:: plugin_config
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin.plugin_config
    :type: IAgVAPluginProperties

    Get the properties of the selected plugin.

.. py:property:: plugin_identifier
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin.plugin_identifier
    :type: str

    Get the plugin identifier.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin.scripting_tool
    :type: IAgVAScriptingTool

    Returns the Scripting tool for the sequence.

.. py:property:: reset_controls_before_run
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin.targeter_graphs
    :type: IAgVATargeterGraphCollection

    Graphs.

.. py:property:: log_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSearchPlugin.log_file
    :type: str

    Name of the log file for this profile.


