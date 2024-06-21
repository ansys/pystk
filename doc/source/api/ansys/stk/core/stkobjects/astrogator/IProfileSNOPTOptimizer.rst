IProfileSNOPTOptimizer
======================

.. py:class:: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer

   IProfile
   
   Properties of SNOPT Optimizer profile.

.. py:currentmodule:: IProfileSNOPTOptimizer

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.control_parameters`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.results`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.targeter_graphs`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.scripting_tool`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.reset_controls_before_run`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.max_major_iterations`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.tolerance_on_major_feasibility`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.tolerance_on_major_optimality`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.max_minor_iterations`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.tolerance_on_minor_feasibility`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.tolerance_on_minor_optimality`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.options_filename`
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.allow_internal_primal_infeasibility_measure_normalization`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileSNOPTOptimizer


Property detail
---------------

.. py:property:: control_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.control_parameters
    :type: ISNOPTControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.results
    :type: ISNOPTResultCollection

    Get the list of results defined for the profile.

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.targeter_graphs
    :type: ITargeterGraphCollection

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.scripting_tool
    :type: IScriptingTool

    Returns the Scripting tool for the sequence.

.. py:property:: reset_controls_before_run
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: max_major_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.max_major_iterations
    :type: int

    Gets or sets the maximum number of major iterations allowed.

.. py:property:: tolerance_on_major_feasibility
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.tolerance_on_major_feasibility
    :type: float

    Specifies how accurately the nonlinear constraints should be satisfied.

.. py:property:: tolerance_on_major_optimality
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.tolerance_on_major_optimality
    :type: float

    Specifies the final accuracy of the dual variables.

.. py:property:: max_minor_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.max_minor_iterations
    :type: int

    Gets or sets the maximum number of iterations for the QP subproblem allowed during a single major iteration.

.. py:property:: tolerance_on_minor_feasibility
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.tolerance_on_minor_feasibility
    :type: float

    Gets or sets the tolerance which the QP subproblem must meet before being considered feasible.

.. py:property:: tolerance_on_minor_optimality
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.tolerance_on_minor_optimality
    :type: float

    Undocumented in the SNOPT literature, and included here for completeness in terms of tolerance options.

.. py:property:: options_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.options_filename
    :type: str

    If used, the associated SNOPT specifications file may define any of the various SNOPT options. Options in the file that conflict with options specified elsewhere will take precedence.

.. py:property:: allow_internal_primal_infeasibility_measure_normalization
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileSNOPTOptimizer.allow_internal_primal_infeasibility_measure_normalization
    :type: bool

    Whether to allow internal normalization of the primal infeasibility measure.


