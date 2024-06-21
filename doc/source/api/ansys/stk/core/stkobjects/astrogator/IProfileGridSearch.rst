IProfileGridSearch
==================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileGridSearch

   IProfile
   
   Properties for a Grid Search profile.

.. py:currentmodule:: IProfileGridSearch

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.targeter_graphs`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.scripting_tool`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.controls`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.results`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.log_file`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.enable_display_status`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.should_generate_graph`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileGridSearch


Property detail
---------------

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.targeter_graphs
    :type: ITargeterGraphCollection

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.scripting_tool
    :type: IScriptingTool

    Returns the Scripting tool for the sequence.

.. py:property:: controls
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.controls
    :type: IGridSearchControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.results
    :type: IGridSearchResultCollection

    Get the list of results defined for the profile.

.. py:property:: log_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.log_file
    :type: str

    Name of the log file for this profile.

.. py:property:: enable_display_status
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.enable_display_status
    :type: bool

    If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.

.. py:property:: should_generate_graph
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGridSearch.should_generate_graph
    :type: bool

    If true, a plot is automatically generate the selected result value versus the control value for the grid search when the profile runs.


