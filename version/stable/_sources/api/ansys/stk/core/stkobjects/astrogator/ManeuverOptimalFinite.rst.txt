ManeuverOptimalFinite
=====================

.. py:class:: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite

   Bases: :py:class:`~ansys.stk.core.stkobjects.astrogator.IManeuver`, :py:class:`~ansys.stk.core.stkobjects.astrogator.IRuntimeTypeInfoProvider`

   The Optimal Finite Maneuver.

.. py:currentmodule:: ManeuverOptimalFinite

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.run_seed`
              - Run seed.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.export_nodes`
              - Export the current set of collocation nodes to a file.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.pressure_mode`
              - Get or set the pressure mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.thrust_efficiency`
              - Get or set the fraction of ideal thrust applied. Any number above zero is valid, with typical values around 0.98 to 1.02. Dimensionless.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.thrust_efficiency_mode`
              - Thrust - the calculations that are effected by the thrust efficiency value.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.number_of_nodes`
              - Number of nodes to discretize collocation problem into.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.initial_guess_file_name`
              - File containing ephemeris for nodes that serve as an initial guess.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.seed_method`
              - Initial seed method.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.node_status_message`
              - A message that indicates what nodes are currently held by the segment.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.run_mode`
              - Run mode.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.halt_mission_control_sequence_for_nonconvergence`
              - Halt MCS and discard result if optimization is unsuccessful.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.discretization_strategy`
              - Discretization Strategy.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.working_variables`
              - Working Variables.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.scaling_options`
              - Scaling Options.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.enable_unit_vector_controls`
              - Enable unit vector for thrust direction.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.thrust_axes`
              - Label reflecting coordinate axes for the thrust vector.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.snopt_optimizer`
              - SNOPT Optimizer Options.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.initial_boundary_conditions`
              - Initial Boundary Conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.final_boundary_conditions`
              - Final Boundary Conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.path_boundary_conditions`
              - Path Boundary Conditions.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.log_file_name`
              - Log file name for optimal finite maneuver.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.export_format`
              - Format for exporting collocation control variables.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.steering_nodes`
              - Get the list of steering nodes.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.initial_guess_interpolation_method`
              - Guess interpolation method.
            * - :py:attr:`~ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.should_reinitialize_stm_at_start_of_segment_propagation`
              - If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import ManeuverOptimalFinite


Property detail
---------------

.. py:property:: pressure_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.pressure_mode
    :type: PressureMode

    Get or set the pressure mode.

.. py:property:: thrust_efficiency
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.thrust_efficiency
    :type: float

    Get or set the fraction of ideal thrust applied. Any number above zero is valid, with typical values around 0.98 to 1.02. Dimensionless.

.. py:property:: thrust_efficiency_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.thrust_efficiency_mode
    :type: ThrustType

    Thrust - the calculations that are effected by the thrust efficiency value.

.. py:property:: number_of_nodes
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.number_of_nodes
    :type: int

    Number of nodes to discretize collocation problem into.

.. py:property:: initial_guess_file_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.initial_guess_file_name
    :type: str

    File containing ephemeris for nodes that serve as an initial guess.

.. py:property:: seed_method
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.seed_method
    :type: OptimalFiniteSeedMethod

    Initial seed method.

.. py:property:: node_status_message
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.node_status_message
    :type: str

    A message that indicates what nodes are currently held by the segment.

.. py:property:: run_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.run_mode
    :type: OptimalFiniteRunMode

    Run mode.

.. py:property:: halt_mission_control_sequence_for_nonconvergence
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.halt_mission_control_sequence_for_nonconvergence
    :type: bool

    Halt MCS and discard result if optimization is unsuccessful.

.. py:property:: discretization_strategy
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.discretization_strategy
    :type: OptimalFiniteDiscretizationStrategy

    Discretization Strategy.

.. py:property:: working_variables
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.working_variables
    :type: OptimalFiniteWorkingVariables

    Working Variables.

.. py:property:: scaling_options
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.scaling_options
    :type: OptimalFiniteScalingOptions

    Scaling Options.

.. py:property:: enable_unit_vector_controls
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.enable_unit_vector_controls
    :type: bool

    Enable unit vector for thrust direction.

.. py:property:: thrust_axes
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.thrust_axes
    :type: str

    Label reflecting coordinate axes for the thrust vector.

.. py:property:: snopt_optimizer
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.snopt_optimizer
    :type: ManeuverOptimalFiniteSNOPTOptimizer

    SNOPT Optimizer Options.

.. py:property:: initial_boundary_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.initial_boundary_conditions
    :type: ManeuverOptimalFiniteInitialBoundaryConditions

    Initial Boundary Conditions.

.. py:property:: final_boundary_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.final_boundary_conditions
    :type: ManeuverOptimalFiniteFinalBoundaryConditions

    Final Boundary Conditions.

.. py:property:: path_boundary_conditions
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.path_boundary_conditions
    :type: ManeuverOptimalFinitePathBoundaryConditions

    Path Boundary Conditions.

.. py:property:: log_file_name
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.log_file_name
    :type: str

    Log file name for optimal finite maneuver.

.. py:property:: export_format
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.export_format
    :type: OptimalFiniteExportNodesFormat

    Format for exporting collocation control variables.

.. py:property:: steering_nodes
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.steering_nodes
    :type: ManeuverOptimalFiniteSteeringNodeCollection

    Get the list of steering nodes.

.. py:property:: initial_guess_interpolation_method
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.initial_guess_interpolation_method
    :type: OptimalFiniteGuessMethod

    Guess interpolation method.

.. py:property:: should_reinitialize_stm_at_start_of_segment_propagation
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.should_reinitialize_stm_at_start_of_segment_propagation
    :type: bool

    If this segment is propagating the state transition matrix, reset it to the identity matrix at the start of the segment.


Method detail
-------------













.. py:method:: run_seed(self) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.run_seed

    Run seed.

    :Returns:

        :obj:`~None`























.. py:method:: export_nodes(self, file_name: str) -> None
    :canonical: ansys.stk.core.stkobjects.astrogator.ManeuverOptimalFinite.export_nodes

    Export the current set of collocation nodes to a file.

    :Parameters:

        **file_name** : :obj:`~str`


    :Returns:

        :obj:`~None`





