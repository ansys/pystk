IManeuverOptimalFinite
======================

.. py:class:: IManeuverOptimalFinite

   IManeuver
   
   Engine properties for a Optimal Finite Maneuver.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~run_seed`
              - Run seed.
            * - :py:meth:`~export_nodes`
              - Export the current set of collocation nodes to a file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~pressure_mode`
            * - :py:meth:`~thrust_efficiency`
            * - :py:meth:`~thrust_efficiency_mode`
            * - :py:meth:`~number_of_nodes`
            * - :py:meth:`~initial_guess_file_name`
            * - :py:meth:`~seed_method`
            * - :py:meth:`~node_status_message`
            * - :py:meth:`~run_mode`
            * - :py:meth:`~halt_mission_control_sequence_when_no_convergence`
            * - :py:meth:`~discretization_strategy`
            * - :py:meth:`~working_variables`
            * - :py:meth:`~scaling_options`
            * - :py:meth:`~enable_unit_vector_controls`
            * - :py:meth:`~thrust_axes`
            * - :py:meth:`~snopt_optimizer`
            * - :py:meth:`~initial_boundary_conditions`
            * - :py:meth:`~final_boundary_conditions`
            * - :py:meth:`~path_boundary_conditions`
            * - :py:meth:`~log_file_name`
            * - :py:meth:`~export_format`
            * - :py:meth:`~steering_nodes`
            * - :py:meth:`~initial_guess_interpolation_method`
            * - :py:meth:`~should_reinitialize_stm_at_start_of_segment_propagation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuverOptimalFinite


Property detail
---------------

.. py:property:: pressure_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.pressure_mode
    :type: PRESSURE_MODE

    Gets or sets the pressure mode.

.. py:property:: thrust_efficiency
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.thrust_efficiency
    :type: float

    Gets or sets the fraction of ideal thrust applied. Any number above zero is valid, with typical values around 0.98 to 1.02. Dimensionless.

.. py:property:: thrust_efficiency_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.thrust_efficiency_mode
    :type: THRUST_TYPE

    Thrust - the calculations that are effected by the thrust efficiency value.

.. py:property:: number_of_nodes
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.number_of_nodes
    :type: int

    Number of nodes to discretize collocation problem into.

.. py:property:: initial_guess_file_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.initial_guess_file_name
    :type: str

    File containing ephemeris for nodes that serve as an initial guess.

.. py:property:: seed_method
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.seed_method
    :type: OPTIMAL_FINITE_SEED_METHOD

    Initial seed method.

.. py:property:: node_status_message
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.node_status_message
    :type: str

    A message that indicates what nodes are currently held by the segment.

.. py:property:: run_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.run_mode
    :type: OPTIMAL_FINITE_RUN_MODE

    Run mode.

.. py:property:: halt_mission_control_sequence_when_no_convergence
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.halt_mission_control_sequence_when_no_convergence
    :type: bool

    Halt MCS and discard result if optimization is unsuccessful.

.. py:property:: discretization_strategy
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.discretization_strategy
    :type: OPTIMAL_FINITE_DISCRETIZATION_STRATEGY

    Discretization Strategy.

.. py:property:: working_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.working_variables
    :type: OPTIMAL_FINITE_WORKING_VARIABLES

    Working Variables.

.. py:property:: scaling_options
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.scaling_options
    :type: OPTIMAL_FINITE_SCALING_OPTIONS

    Scaling Options.

.. py:property:: enable_unit_vector_controls
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.enable_unit_vector_controls
    :type: bool

    Enable unit vector for thrust direction.

.. py:property:: thrust_axes
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.thrust_axes
    :type: str

    Label reflecting coordinate axes for the thrust vector.

.. py:property:: snopt_optimizer
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.snopt_optimizer
    :type: IAgVAManeuverOptimalFiniteSNOPTOptimizer

    SNOPT Optimizer Options.

.. py:property:: initial_boundary_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.initial_boundary_conditions
    :type: IAgVAManeuverOptimalFiniteInitialBoundaryConditions

    Initial Boundary Conditions.

.. py:property:: final_boundary_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.final_boundary_conditions
    :type: IAgVAManeuverOptimalFiniteFinalBoundaryConditions

    Final Boundary Conditions.

.. py:property:: path_boundary_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.path_boundary_conditions
    :type: IAgVAManeuverOptimalFinitePathBoundaryConditions

    Path Boundary Conditions.

.. py:property:: log_file_name
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.log_file_name
    :type: str

    Log file name for optimal finite maneuver.

.. py:property:: export_format
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.export_format
    :type: OPTIMAL_FINITE_EXPORT_NODES_FORMAT

    Format for exporting collocation control variables.

.. py:property:: steering_nodes
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.steering_nodes
    :type: IAgVAManeuverOptimalFiniteSteeringNodeCollection

    Get the list of steering nodes.

.. py:property:: initial_guess_interpolation_method
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.initial_guess_interpolation_method
    :type: OPTIMAL_FINITE_GUESS_METHOD

    Guess interpolation method.

.. py:property:: should_reinitialize_stm_at_start_of_segment_propagation
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.should_reinitialize_stm_at_start_of_segment_propagation
    :type: bool

    If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.


Method detail
-------------













.. py:method:: run_seed(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.run_seed

    Run seed.

    :Returns:

        :obj:`~None`























.. py:method:: export_nodes(self, fileName: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverOptimalFinite.export_nodes

    Export the current set of collocation nodes to a file.

    :Parameters:

    **fileName** : :obj:`~str`

    :Returns:

        :obj:`~None`





