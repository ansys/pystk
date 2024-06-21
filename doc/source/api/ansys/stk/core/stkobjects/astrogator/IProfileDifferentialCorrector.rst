IProfileDifferentialCorrector
=============================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector

   IProfile
   
   Properties for a Differential Corrector profile.

.. py:currentmodule:: IProfileDifferentialCorrector

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.control_parameters`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.results`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.max_iterations`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_display_status`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.convergence_criteria`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_line_search`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.max_line_search_iterations`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.line_search_lower_bound`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.line_search_upper_bound`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.line_search_tolerance`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_homotopy`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.homotopy_steps`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.derivative_calc_method`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.clear_corrections_before_run`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_b_plane_nominal`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_b_plane_perturbations`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.draw_perturbation`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.scripting_tool`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.root_finding_algorithm`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.num_iterations`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.targeter_graphs`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.stop_on_limit_cycle_detection`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileDifferentialCorrector


Property detail
---------------

.. py:property:: control_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.control_parameters
    :type: IDifferentialCorrectorControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.results
    :type: IDifferentialCorrectorResultCollection

    Get the list of results defined for the profile.

.. py:property:: max_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.max_iterations
    :type: int

    Gets or sets the number of complete iterations of the profile to try before stopping. Dimensionless.

.. py:property:: enable_display_status
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_display_status
    :type: bool

    If true, a page will appear during the targeting run to report the status of the targeting effort in terms of proximity to the desired value for each dependent variable in the profile.

.. py:property:: convergence_criteria
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.convergence_criteria
    :type: CONVERGENCE_CRITERIA

    Gets or sets the convergence criteria.

.. py:property:: enable_line_search
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_line_search
    :type: bool

    If true, the profile will perform a line search.

.. py:property:: max_line_search_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.max_line_search_iterations
    :type: int

    Gets or sets the number of line search iterations to try before stopping. Dimensionless.

.. py:property:: line_search_lower_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.line_search_lower_bound
    :type: float

    Gets or sets the low boundary for the line search. Dimensionless.

.. py:property:: line_search_upper_bound
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.line_search_upper_bound
    :type: float

    Gets or sets the high boundary for the line search. Dimensionless.

.. py:property:: line_search_tolerance
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.line_search_tolerance
    :type: float

    Gets or sets the tolerance for the line search. Dimensionless.

.. py:property:: enable_homotopy
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_homotopy
    :type: bool

    If true, the profile will divide the problem into steps to solve it.

.. py:property:: homotopy_steps
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.homotopy_steps
    :type: int

    Gets or sets the number of steps to divide a problem into for a homotopic calculation. Dimensionless - .

.. py:property:: derivative_calc_method
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.derivative_calc_method
    :type: DERIVE_CALC_METHOD

    Gets or sets the derivative calculation method.

.. py:property:: clear_corrections_before_run
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.clear_corrections_before_run
    :type: bool

    Clear Corrections Before Each Run - if true, the differential corrector is automatically reset each time that it is run, discarding information that was computed the last time it was run.

.. py:property:: enable_b_plane_nominal
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_b_plane_nominal
    :type: bool

    If true, Astrogator will update the display of B-Planes for the nominal run of each iteration during the targeting process.

.. py:property:: enable_b_plane_perturbations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.enable_b_plane_perturbations
    :type: bool

    If true, Astrogator will update the display of B-Planes for both of the perturbations of each iteration during the targeting process.

.. py:property:: draw_perturbation
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.draw_perturbation
    :type: DRAW_PERTURBATION

    Defines the display of perturbations in the 2D and 3D Graphics windows, if you have set Astrogator to draw while calculating.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.scripting_tool
    :type: IScriptingTool

    Returns the Scripting tool for the sequence.

.. py:property:: root_finding_algorithm
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.root_finding_algorithm
    :type: ROOT_FINDING_ALGORITHM

    Gets or sets the root-finding algorithm to use.

.. py:property:: num_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.num_iterations
    :type: int

    Get the number of iterations of the last run.

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.targeter_graphs
    :type: ITargeterGraphCollection

    Graphs.

.. py:property:: stop_on_limit_cycle_detection
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileDifferentialCorrector.stop_on_limit_cycle_detection
    :type: bool

    If true, Astrogator will stop targeting if a limit cycle is detected.


