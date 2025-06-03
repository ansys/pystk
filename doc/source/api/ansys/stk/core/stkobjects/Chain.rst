Chain
=====

.. py:class:: ansys.stk.core.stkobjects.Chain

   Bases: :py:class:`~ansys.stk.core.stkobjects.IStkObject`, :py:class:`~ansys.stk.core.stkobjects.ILifetimeInformation`

   Chain Class is used to access the methods and properties of the STK Chain Object.

.. py:currentmodule:: Chain

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.set_time_period_type`
              - Set the option used to specify the time period.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.set_access_intervals_file`
              - Opt to produce an .int file containing the strand access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.reset_access_intervals_file`
              - Reset the .int file containing the strand access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.compute_access`
              - Compute access for the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.clear_access`
              - Remove all chain accesses.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.objects`
              - Do not use this property, as it is deprecated. Use the StartObject, EndObject and Connections properties to configure objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.recompute_automatically`
              - Opt to have STK automatically recompute accesses each time that an object on which the chain depends is updated.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.time_period_type`
              - Get the option used to specify the time period for the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.time_period`
              - Get the time period for the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.data_save_mode`
              - Specify the mode for saving or recomputing accesses.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.access_intervals_filename`
              - Name of the .int file containing the strand access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.enable_light_time_delay`
              - Specify whether to take light time delay into account in the computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.maximum_time_step`
              - Get or set the maximum sampling step size used when computing the chain. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.time_convergence`
              - Get or set the time convergence for determining access intervals when computing the chain. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.constraints`
              - Get the constraints applicable to the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.graphics`
              - Get the 2D graphics properties of the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.graphics_3d`
              - Get the 3D graphics properties of the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.event_detection`
              - Event detection strategy used for access calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.sampling`
              - Sampling method used for access calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.detect_events_based_on_samples_only`
              - Flags control whether event times are computed just using the sampling or by sub-sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.const_constraints_mode`
              - Constellation constraints mode, apply to strands or per instance.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.keep_empty_strands`
              - Allow strands with no access intervals to included in reports.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.allow_duplicate_objects_in_strands`
              - Allow a strand to contain an object more than once.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.coverage_asset_mode`
              - When Computing Coverage and the Chain is used as a coverage asset, append the grid instance to the end of the chain or update the grid instance inside the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.start_object`
              - Start object for the Chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.end_object`
              - End object for the Chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.max_strand_depth`
              - Maximum number of objects in all strands for the Chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.connections`
              - Get the collection of connections in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.Chain.optimal_strand_opts`
              - Optimal strands settings for the Chain.



Examples
--------

Print the strand intervals of chain object

.. code-block:: python

    # Chain chain: Chain Object
    # Compute the chain access if not done already.
    chain.compute_access()

    # Considered Start and Stop time
    print(
        "Chain considered start time: %s"
        % chain.analysis_workbench_components.time_instants.item("ConsideredStartTime").find_occurrence().epoch
    )
    print(
        "Chain considered stop time: %s"
        % chain.analysis_workbench_components.time_instants.item("ConsideredStopTime").find_occurrence().epoch
    )

    objectParticipationIntervals = chain.analysis_workbench_components.time_interval_collections.item(
        "StrandAccessIntervals"
    )
    intervalListResult = objectParticipationIntervals.find_interval_collection()

    for i in range(0, intervalListResult.interval_collections.count):
        if intervalListResult.IsValid:
            print("Link Name: %s" % objectParticipationIntervals.Labels(i + 1))
            print("--------------")
            for j in range(0, intervalListResult.IntervalCollections.Item(i).Count):
                startTime = intervalListResult.IntervalCollections.Item(i).Item(j).Start
                stopTime = intervalListResult.IntervalCollections.Item(i).Item(j).Stop
                print("Start: %s Stop: %s" % (startTime, stopTime))


Define and compute a chain (advanced)

.. code-block:: python

    # Chain chain: Chain object
    # Satellite satellite: Satellite object

    # Remove all previous accesses
    chain.clear_access()

    # Add some objects to chain
    chain.objects.add("Facility/MyFacility")
    chain.objects.add_object(satellite)

    # Configure chain parameters
    chain.recompute_automatically = False
    chain.enable_light_time_delay = False
    chain.time_convergence = 0.001
    chain.data_save_mode = DataSaveMode.SAVE_ACCESSES

    # Specify our own time period
    chain.set_time_period_type(ChainTimePeriodType.SPECIFIED_TIME_PERIOD)

    # Get chain time period interface
    chainUserTimePeriod = chain.time_period
    chainUserTimePeriod.time_interval.set_explicit_interval(
        root.current_scenario.analysis_interval.find_start_time(),
        root.current_scenario.analysis_interval.find_stop_time(),
    )  # Set to scenario period

    # Compute the chain
    chain.compute_access()


Define and compute a chain (basic)

.. code-block:: python

    # Chain chain: Chain object

    # Add some objects to chain (using STK path)
    chain.objects.add("Facility/MyFacility")
    chain.objects.add("Satellite/MySatellite")

    # Compute the chain
    chain.compute_access()


Create a chain (on the current scenario central body)

.. code-block:: python

    # StkObjectRoot root: STK Object Model Root
    # Create the Chain on the current scenario central body (use
    # NewOnCentralBody to specify explicitly the central body)
    chain = root.current_scenario.children.new(STKObjectType.CHAIN, "MyChain")


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import Chain


Property detail
---------------

.. py:property:: objects
    :canonical: ansys.stk.core.stkobjects.Chain.objects
    :type: ObjectLinkCollection

    Do not use this property, as it is deprecated. Use the StartObject, EndObject and Connections properties to configure objects in the chain.

.. py:property:: recompute_automatically
    :canonical: ansys.stk.core.stkobjects.Chain.recompute_automatically
    :type: bool

    Opt to have STK automatically recompute accesses each time that an object on which the chain depends is updated.

.. py:property:: time_period_type
    :canonical: ansys.stk.core.stkobjects.Chain.time_period_type
    :type: ChainTimePeriodType

    Get the option used to specify the time period for the chain.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.Chain.time_period
    :type: IChainTimePeriod

    Get the time period for the chain.

.. py:property:: data_save_mode
    :canonical: ansys.stk.core.stkobjects.Chain.data_save_mode
    :type: DataSaveMode

    Specify the mode for saving or recomputing accesses.

.. py:property:: access_intervals_filename
    :canonical: ansys.stk.core.stkobjects.Chain.access_intervals_filename
    :type: str

    Name of the .int file containing the strand access intervals.

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.Chain.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the computation.

.. py:property:: maximum_time_step
    :canonical: ansys.stk.core.stkobjects.Chain.maximum_time_step
    :type: float

    Get or set the maximum sampling step size used when computing the chain. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.

.. py:property:: time_convergence
    :canonical: ansys.stk.core.stkobjects.Chain.time_convergence
    :type: float

    Get or set the time convergence for determining access intervals when computing the chain. Uses Time Dimension.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.Chain.constraints
    :type: ChainConstraints

    Get the constraints applicable to the chain.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.Chain.graphics
    :type: ChainGraphics

    Get the 2D graphics properties of the chain.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.Chain.graphics_3d
    :type: ChainGraphics3D

    Get the 3D graphics properties of the chain.

.. py:property:: event_detection
    :canonical: ansys.stk.core.stkobjects.Chain.event_detection
    :type: AccessEventDetection

    Event detection strategy used for access calculations.

.. py:property:: sampling
    :canonical: ansys.stk.core.stkobjects.Chain.sampling
    :type: AccessSampling

    Sampling method used for access calculations.

.. py:property:: detect_events_based_on_samples_only
    :canonical: ansys.stk.core.stkobjects.Chain.detect_events_based_on_samples_only
    :type: bool

    Flags control whether event times are computed just using the sampling or by sub-sampling.

.. py:property:: const_constraints_mode
    :canonical: ansys.stk.core.stkobjects.Chain.const_constraints_mode
    :type: ChainConstellationConstraintsMode

    Constellation constraints mode, apply to strands or per instance.

.. py:property:: keep_empty_strands
    :canonical: ansys.stk.core.stkobjects.Chain.keep_empty_strands
    :type: bool

    Allow strands with no access intervals to included in reports.

.. py:property:: allow_duplicate_objects_in_strands
    :canonical: ansys.stk.core.stkobjects.Chain.allow_duplicate_objects_in_strands
    :type: bool

    Allow a strand to contain an object more than once.

.. py:property:: coverage_asset_mode
    :canonical: ansys.stk.core.stkobjects.Chain.coverage_asset_mode
    :type: ChainCoverageAssetMode

    When Computing Coverage and the Chain is used as a coverage asset, append the grid instance to the end of the chain or update the grid instance inside the chain.

.. py:property:: start_object
    :canonical: ansys.stk.core.stkobjects.Chain.start_object
    :type: IStkObject

    Start object for the Chain.

.. py:property:: end_object
    :canonical: ansys.stk.core.stkobjects.Chain.end_object
    :type: IStkObject

    End object for the Chain.

.. py:property:: max_strand_depth
    :canonical: ansys.stk.core.stkobjects.Chain.max_strand_depth
    :type: int

    Maximum number of objects in all strands for the Chain.

.. py:property:: connections
    :canonical: ansys.stk.core.stkobjects.Chain.connections
    :type: ChainConnectionCollection

    Get the collection of connections in the chain.

.. py:property:: optimal_strand_opts
    :canonical: ansys.stk.core.stkobjects.Chain.optimal_strand_opts
    :type: ChainOptimalStrandOpts

    Optimal strands settings for the Chain.


Method detail
-------------





.. py:method:: set_time_period_type(self, time_period_type: ChainTimePeriodType) -> None
    :canonical: ansys.stk.core.stkobjects.Chain.set_time_period_type

    Set the option used to specify the time period.

    :Parameters:

        **time_period_type** : :obj:`~ChainTimePeriodType`


    :Returns:

        :obj:`~None`




.. py:method:: set_access_intervals_file(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.Chain.set_access_intervals_file

    Opt to produce an .int file containing the strand access intervals.

    :Parameters:

        **filename** : :obj:`~str`


    :Returns:

        :obj:`~None`

.. py:method:: reset_access_intervals_file(self) -> None
    :canonical: ansys.stk.core.stkobjects.Chain.reset_access_intervals_file

    Reset the .int file containing the strand access intervals.

    :Returns:

        :obj:`~None`











.. py:method:: compute_access(self) -> None
    :canonical: ansys.stk.core.stkobjects.Chain.compute_access

    Compute access for the chain.

    :Returns:

        :obj:`~None`

.. py:method:: clear_access(self) -> None
    :canonical: ansys.stk.core.stkobjects.Chain.clear_access

    Remove all chain accesses.

    :Returns:

        :obj:`~None`





















