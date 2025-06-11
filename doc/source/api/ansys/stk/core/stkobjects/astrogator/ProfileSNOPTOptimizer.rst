ProfileSNOPTOptimizer
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IProfile`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   SNOPT optimizer profile.

.. py:currentmodule:: ProfileSNOPTOptimizer

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.control_parameters`
              - Get the list of control parameters defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.results`
              - Get the list of results defined for the profile.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.targeter_graphs`
              - Graphs.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.scripting_tool`
              - Return the Scripting tool for the sequence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.reset_controls_before_run`
              - Reset controls before each run.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.max_major_iterations`
              - Get or set the maximum number of major iterations allowed.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.tolerance_on_major_feasibility`
              - Specify how accurately the nonlinear constraints should be satisfied.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.tolerance_on_major_optimality`
              - Specify the final accuracy of the dual variables.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.max_minor_iterations`
              - Get or set the maximum number of iterations for the QP subproblem allowed during a single major iteration.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.tolerance_on_minor_feasibility`
              - Get or set the tolerance which the QP subproblem must meet before being considered feasible.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.tolerance_on_minor_optimality`
              - Undocumented in the SNOPT literature, and included here for completeness in terms of tolerance options.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.options_filename`
              - If used, the associated SNOPT specifications file may define any of the various SNOPT options. Options in the file that conflict with options specified elsewhere will take precedence.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.allow_internal_primal_infeasibility_measure_normalization`
              - Whether to allow internal normalization of the primal infeasibility measure.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ProfileSNOPTOptimizer


Property detail
---------------

.. py:property:: control_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.control_parameters
    :type: SNOPTControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.results
    :type: SNOPTResultCollection

    Get the list of results defined for the profile.

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.targeter_graphs
    :type: TargeterGraphCollection

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.scripting_tool
    :type: ScriptingTool

    Return the Scripting tool for the sequence.

.. py:property:: reset_controls_before_run
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: max_major_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.max_major_iterations
    :type: int

    Get or set the maximum number of major iterations allowed.

.. py:property:: tolerance_on_major_feasibility
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.tolerance_on_major_feasibility
    :type: float

    Specify how accurately the nonlinear constraints should be satisfied.

.. py:property:: tolerance_on_major_optimality
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.tolerance_on_major_optimality
    :type: float

    Specify the final accuracy of the dual variables.

.. py:property:: max_minor_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.max_minor_iterations
    :type: int

    Get or set the maximum number of iterations for the QP subproblem allowed during a single major iteration.

.. py:property:: tolerance_on_minor_feasibility
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.tolerance_on_minor_feasibility
    :type: float

    Get or set the tolerance which the QP subproblem must meet before being considered feasible.

.. py:property:: tolerance_on_minor_optimality
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.tolerance_on_minor_optimality
    :type: float

    Undocumented in the SNOPT literature, and included here for completeness in terms of tolerance options.

.. py:property:: options_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.options_filename
    :type: str

    If used, the associated SNOPT specifications file may define any of the various SNOPT options. Options in the file that conflict with options specified elsewhere will take precedence.

.. py:property:: allow_internal_primal_infeasibility_measure_normalization
    :canonical: ansys.stk.core.stkobjects.astrogator.ProfileSNOPTOptimizer.allow_internal_primal_infeasibility_measure_normalization
    :type: bool

    Whether to allow internal normalization of the primal infeasibility measure.


