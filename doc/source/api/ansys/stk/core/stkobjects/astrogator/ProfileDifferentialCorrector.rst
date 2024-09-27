ProfileDifferentialCorrector
============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Differential Corrector profile.

.. py:currentmodule:: ProfileDifferentialCorrector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.control_parameters`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.max_iterations`
              - Gets or sets the number of complete iterations of the profile to try before stopping. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_display_status`
              - If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.convergence_criteria`
              - Gets or sets the convergence criteria.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_line_search`
              - If true, the profile will perform a line search.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.max_line_search_iterations`
              - Gets or sets the number of line search iterations to try before stopping. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.line_search_lower_bound`
              - Gets or sets the low boundary for the line search. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.line_search_upper_bound`
              - Gets or sets the high boundary for the line search. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.line_search_tolerance`
              - Gets or sets the tolerance for the line search. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_homotopy`
              - If true, the profile will divide the problem into steps to solve it.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.homotopy_steps`
              - Gets or sets the number of steps to divide a problem into for a homotopic calculation. Dimensionless - .
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.derivative_calc_method`
              - Gets or sets the derivative calculation method.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.clear_corrections_before_run`
              - Clear Corrections Before Each Run - if true, the differential corrector is automatically reset each time that it is run, discarding information that was computed the last time it was run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_b_plane_nominal`
              - If true, Astrogator will update the display of B-Planes for the nominal run of each iteration during the targeting process.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_b_plane_perturbations`
              - If true, Astrogator will update the display of B-Planes for both of the perturbations of each iteration during the targeting process.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.draw_perturbation`
              - Defines the display of perturbations in the 2D and 3D Graphics windows, if you have set Astrogator to draw while calculating.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.scripting_tool`
              - Returns the Scripting tool for the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.root_finding_algorithm`
              - Gets or sets the root-finding algorithm to use.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.number_of_iterations`
              - Get the number of iterations of the last run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.targeter_graphs`
              - Graphs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.stop_on_limit_cycle_detection`
              - If true, Astrogator will stop targeting if a limit cycle is detected.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileDifferentialCorrector


Property detail
---------------

.. py:property:: control_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.control_parameters
    :type: DifferentialCorrectorControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.results
    :type: DifferentialCorrectorResultCollection

    Get the list of results defined for the profile.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.max_iterations
    :type: int

    Gets or sets the number of complete iterations of the profile to try before stopping. Dimensionless.

.. py:property:: enable_display_status
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_display_status
    :type: bool

    If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.

.. py:property:: convergence_criteria
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.convergence_criteria
    :type: CONVERGENCE_CRITERIA

    Gets or sets the convergence criteria.

.. py:property:: enable_line_search
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_line_search
    :type: bool

    If true, the profile will perform a line search.

.. py:property:: max_line_search_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.max_line_search_iterations
    :type: int

    Gets or sets the number of line search iterations to try before stopping. Dimensionless.

.. py:property:: line_search_lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.line_search_lower_bound
    :type: float

    Gets or sets the low boundary for the line search. Dimensionless.

.. py:property:: line_search_upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.line_search_upper_bound
    :type: float

    Gets or sets the high boundary for the line search. Dimensionless.

.. py:property:: line_search_tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.line_search_tolerance
    :type: float

    Gets or sets the tolerance for the line search. Dimensionless.

.. py:property:: enable_homotopy
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_homotopy
    :type: bool

    If true, the profile will divide the problem into steps to solve it.

.. py:property:: homotopy_steps
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.homotopy_steps
    :type: int

    Gets or sets the number of steps to divide a problem into for a homotopic calculation. Dimensionless - .

.. py:property:: derivative_calc_method
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.derivative_calc_method
    :type: DERIVATIVE_CALCULATION_METHOD

    Gets or sets the derivative calculation method.

.. py:property:: clear_corrections_before_run
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.clear_corrections_before_run
    :type: bool

    Clear Corrections Before Each Run - if true, the differential corrector is automatically reset each time that it is run, discarding information that was computed the last time it was run.

.. py:property:: enable_b_plane_nominal
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_b_plane_nominal
    :type: bool

    If true, Astrogator will update the display of B-Planes for the nominal run of each iteration during the targeting process.

.. py:property:: enable_b_plane_perturbations
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.enable_b_plane_perturbations
    :type: bool

    If true, Astrogator will update the display of B-Planes for both of the perturbations of each iteration during the targeting process.

.. py:property:: draw_perturbation
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.draw_perturbation
    :type: DRAW_PERTURBATION

    Defines the display of perturbations in the 2D and 3D Graphics windows, if you have set Astrogator to draw while calculating.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.scripting_tool
    :type: ScriptingTool

    Returns the Scripting tool for the sequence.

.. py:property:: root_finding_algorithm
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.root_finding_algorithm
    :type: ROOT_FINDING_ALGORITHM

    Gets or sets the root-finding algorithm to use.

.. py:property:: number_of_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.number_of_iterations
    :type: int

    Get the number of iterations of the last run.

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.targeter_graphs
    :type: TargeterGraphCollection

    Graphs.

.. py:property:: stop_on_limit_cycle_detection
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileDifferentialCorrector.stop_on_limit_cycle_detection
    :type: bool

    If true, Astrogator will stop targeting if a limit cycle is detected.


