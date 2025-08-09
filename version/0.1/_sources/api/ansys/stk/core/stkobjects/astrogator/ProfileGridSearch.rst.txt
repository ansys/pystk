ProfileGridSearch
=================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileGridSearch

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Grid Search profile.

.. py:currentmodule:: ProfileGridSearch

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.targeter_graphs`
              - Graphs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.scripting_tool`
              - Return the Scripting tool for the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.controls`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.log_file`
              - Name of the log file for this profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.enable_display_status`
              - If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.should_generate_graph`
              - If true, a plot is automatically generate the selected result value versus the control value for the grid search when the profile runs.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileGridSearch


Property detail
---------------

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.targeter_graphs
    :type: TargeterGraphCollection

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.scripting_tool
    :type: ScriptingTool

    Return the Scripting tool for the sequence.

.. py:property:: controls
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.controls
    :type: GridSearchControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.results
    :type: GridSearchResultCollection

    Get the list of results defined for the profile.

.. py:property:: log_file
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.log_file
    :type: str

    Name of the log file for this profile.

.. py:property:: enable_display_status
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.enable_display_status
    :type: bool

    If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.

.. py:property:: should_generate_graph
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileGridSearch.should_generate_graph
    :type: bool

    If true, a plot is automatically generate the selected result value versus the control value for the grid search when the profile runs.


