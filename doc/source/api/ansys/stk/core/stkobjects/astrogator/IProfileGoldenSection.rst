IProfileGoldenSection
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection

   IProfile
   
   Properties for a Golden Section profile.

.. py:currentmodule:: IProfileGoldenSection

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.targeter_graphs`
              - Graphs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.scripting_tool`
              - Returns the Scripting tool for the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.controls`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.max_iterations`
              - Gets or sets the number of complete iterations of the profile to try before stopping. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.log_file`
              - Name of the log file for this profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.enable_display_status`
              - If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileGoldenSection


Property detail
---------------

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.targeter_graphs
    :type: ITargeterGraphCollection

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.scripting_tool
    :type: IScriptingTool

    Returns the Scripting tool for the sequence.

.. py:property:: controls
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.controls
    :type: IGoldenSectionControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.results
    :type: IGoldenSectionResultCollection

    Get the list of results defined for the profile.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.max_iterations
    :type: int

    Gets or sets the number of complete iterations of the profile to try before stopping. Dimensionless.

.. py:property:: log_file
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.log_file
    :type: str

    Name of the log file for this profile.

.. py:property:: enable_display_status
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.enable_display_status
    :type: bool

    If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.


