IProfileIPOPTOptimizer
======================

.. py:class:: IProfileIPOPTOptimizer

   IProfile
   
   Properties of IPOPT Optimizer profile.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~control_parameters`
            * - :py:meth:`~results`
            * - :py:meth:`~targeter_graphs`
            * - :py:meth:`~scripting_tool`
            * - :py:meth:`~reset_controls_before_run`
            * - :py:meth:`~tolerance_on_convergence`
            * - :py:meth:`~maximum_iterations`
            * - :py:meth:`~tolerance_on_constraint_violation`
            * - :py:meth:`~tolerance_on_dual_infeasibility`
            * - :py:meth:`~tolerance_on_complementary_infeasibility`
            * - :py:meth:`~options_filename`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IProfileIPOPTOptimizer


Property detail
---------------

.. py:property:: control_parameters
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.control_parameters
    :type: IAgVAIPOPTControlCollection

    Get the list of control parameters defined for the profile.

.. py:property:: results
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.results
    :type: IAgVAIPOPTResultCollection

    Get the list of results defined for the profile.

.. py:property:: targeter_graphs
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.targeter_graphs
    :type: IAgVATargeterGraphCollection

    Graphs.

.. py:property:: scripting_tool
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.scripting_tool
    :type: IAgVAScriptingTool

    Returns the Scripting tool for the sequence.

.. py:property:: reset_controls_before_run
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.reset_controls_before_run
    :type: bool

    Reset controls before each run.

.. py:property:: tolerance_on_convergence
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.tolerance_on_convergence
    :type: float

    Gets or sets the tolerance by which the optimality conditions must be satisfied for the problem to be considered converged. The default value is 1E-8.

.. py:property:: maximum_iterations
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.maximum_iterations
    :type: int

    Gets or sets the maximum number of iterations before IPOPT should give up if it hasn't yet converged on a solution. The default value is 3000.

.. py:property:: tolerance_on_constraint_violation
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.tolerance_on_constraint_violation
    :type: float

    Gets or sets the tolerance by which user-specified constraints are allowed to be violated with the solution still considered feasible. The default value is 1.0E-4.

.. py:property:: tolerance_on_dual_infeasibility
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.tolerance_on_dual_infeasibility
    :type: float

    Gets or sets the desired absolute tolerance on the maximum norm of the dual infeasibility. The default value is 1.

.. py:property:: tolerance_on_complementary_infeasibility
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.tolerance_on_complementary_infeasibility
    :type: float

    Gets or sets the desired absolute tolerance on the maximum norm of the complementarity conditions. The default value is 1.0E-4.

.. py:property:: options_filename
    :canonical: ansys.stk.core.stkobjects.astrogator.IProfileIPOPTOptimizer.options_filename
    :type: str

    If used, the associated IPOPT specifications file may define any of the various IPOPT options. Options in the file that conflict with options specified elsewhere will take precedence.


