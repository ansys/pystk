IProfileGoldenSection
=====================

.. py:class:: IProfileGoldenSection

   IProfile
   
   Properties for a Golden Section profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~targeter_graphs`
            * - :py:meth:`~scripting_tool`
            * - :py:meth:`~controls`
            * - :py:meth:`~results`
            * - :py:meth:`~max_iterations`
            * - :py:meth:`~log_file`
            * - :py:meth:`~enable_display_status`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileGoldenSection


Property detail
---------------

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.targeter_graphs
    :type: "IAgVATargeterGraphCollection"

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.scripting_tool
    :type: "IAgVAScriptingTool"

    Returns the Scripting tool for the sequence.

.. py:property:: controls
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.controls
    :type: "IAgVAGoldenSectionControlCollection"

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileGoldenSection.results
    :type: "IAgVAGoldenSectionResultCollection"

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


