IChain
======

.. py:class:: ansys.stk.core.stkobjects.IChain

   object
   
   Configuration options for chains.

.. py:currentmodule:: IChain

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.set_time_period_type`
              - Set the option used to specify the time period.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.set_access_intervals_file`
              - Opt to produce an .int file containing the strand access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.reset_access_intervals_file`
              - Reset the .int file containing the strand access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.compute_access`
              - Compute access for the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.clear_access`
              - Remove all chain accesses.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.objects`
              - This property is deprecated. Use the StartObject, EndObject and Connections properties to configure objects in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.auto_recompute`
              - Opt to have STK automatically recompute accesses each time that an object on which the chain depends is updated.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.time_period_type`
              - Get the option used to specify the time period for the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.time_period`
              - Get the time period for the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.data_save_mode`
              - Specify the mode for saving or recomputing accesses.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.access_intervals_file`
              - Name of the .int file containing the strand access intervals.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.enable_light_time_delay`
              - Specify whether to take light time delay into account in the computation.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.max_time_step`
              - Gets or sets the maximum sampling step size used when computing the chain. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.time_convergence`
              - Gets or sets the time convergence for determining access intervals when computing the chain. Uses Time Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.constraints`
              - Get the constraints applicable to the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.graphics`
              - Get the 2D graphics properties of the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.graphics_3d`
              - Get the 3D graphics properties of the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.event_detection`
              - Event detection strategy used for access calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.sampling`
              - Sampling method used for access calculations.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.detect_events_based_on_samples_only`
              - Flags control whether event times are computed just using the sampling or by sub-sampling.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.const_constraints_mode`
              - Constellation constraints mode, apply to strands or per instance.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.keep_empty_strands`
              - Allow strands with no access intervals to included in reports.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.allow_dup_objs_in_strands`
              - Allow a strand to contain an object more than once.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.cov_asset_mode`
              - When Computing Coverage and the Chain is used as a coverage asset, append the grid instance to the end of the chain or update the grid instance inside the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.start_object`
              - Start object for the Chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.end_object`
              - End object for the Chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.max_strand_depth`
              - Maximum number of objects in all strands for the Chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.connections`
              - Get the collection of connections in the chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.IChain.optimal_strand_opts`
              - Optimal strands settings for the Chain.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IChain


Property detail
---------------

.. py:property:: objects
    :canonical: ansys.stk.core.stkobjects.IChain.objects
    :type: IObjectLinkCollection

    This property is deprecated. Use the StartObject, EndObject and Connections properties to configure objects in the chain.

.. py:property:: auto_recompute
    :canonical: ansys.stk.core.stkobjects.IChain.auto_recompute
    :type: bool

    Opt to have STK automatically recompute accesses each time that an object on which the chain depends is updated.

.. py:property:: time_period_type
    :canonical: ansys.stk.core.stkobjects.IChain.time_period_type
    :type: CHAIN_TIME_PERIOD_TYPE

    Get the option used to specify the time period for the chain.

.. py:property:: time_period
    :canonical: ansys.stk.core.stkobjects.IChain.time_period
    :type: IChainTimePeriodBase

    Get the time period for the chain.

.. py:property:: data_save_mode
    :canonical: ansys.stk.core.stkobjects.IChain.data_save_mode
    :type: DATA_SAVE_MODE

    Specify the mode for saving or recomputing accesses.

.. py:property:: access_intervals_file
    :canonical: ansys.stk.core.stkobjects.IChain.access_intervals_file
    :type: str

    Name of the .int file containing the strand access intervals.

.. py:property:: enable_light_time_delay
    :canonical: ansys.stk.core.stkobjects.IChain.enable_light_time_delay
    :type: bool

    Specify whether to take light time delay into account in the computation.

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.IChain.max_time_step
    :type: float

    Gets or sets the maximum sampling step size used when computing the chain. The maximum step size limits the amount of time that is allowed to elapse between sampling of the constraint functions during access computations. Uses Time Dimension.

.. py:property:: time_convergence
    :canonical: ansys.stk.core.stkobjects.IChain.time_convergence
    :type: float

    Gets or sets the time convergence for determining access intervals when computing the chain. Uses Time Dimension.

.. py:property:: constraints
    :canonical: ansys.stk.core.stkobjects.IChain.constraints
    :type: IChainConstraints

    Get the constraints applicable to the chain.

.. py:property:: graphics
    :canonical: ansys.stk.core.stkobjects.IChain.graphics
    :type: IChainGraphics

    Get the 2D graphics properties of the chain.

.. py:property:: graphics_3d
    :canonical: ansys.stk.core.stkobjects.IChain.graphics_3d
    :type: IChainGraphics3D

    Get the 3D graphics properties of the chain.

.. py:property:: event_detection
    :canonical: ansys.stk.core.stkobjects.IChain.event_detection
    :type: IAccessEventDetection

    Event detection strategy used for access calculations.

.. py:property:: sampling
    :canonical: ansys.stk.core.stkobjects.IChain.sampling
    :type: IAccessSampling

    Sampling method used for access calculations.

.. py:property:: detect_events_based_on_samples_only
    :canonical: ansys.stk.core.stkobjects.IChain.detect_events_based_on_samples_only
    :type: bool

    Flags control whether event times are computed just using the sampling or by sub-sampling.

.. py:property:: const_constraints_mode
    :canonical: ansys.stk.core.stkobjects.IChain.const_constraints_mode
    :type: CHAIN_CONST_CONSTRAINTS_MODE

    Constellation constraints mode, apply to strands or per instance.

.. py:property:: keep_empty_strands
    :canonical: ansys.stk.core.stkobjects.IChain.keep_empty_strands
    :type: bool

    Allow strands with no access intervals to included in reports.

.. py:property:: allow_dup_objs_in_strands
    :canonical: ansys.stk.core.stkobjects.IChain.allow_dup_objs_in_strands
    :type: bool

    Allow a strand to contain an object more than once.

.. py:property:: cov_asset_mode
    :canonical: ansys.stk.core.stkobjects.IChain.cov_asset_mode
    :type: CHAIN_COV_ASSET_MODE

    When Computing Coverage and the Chain is used as a coverage asset, append the grid instance to the end of the chain or update the grid instance inside the chain.

.. py:property:: start_object
    :canonical: ansys.stk.core.stkobjects.IChain.start_object
    :type: IStkObject

    Start object for the Chain.

.. py:property:: end_object
    :canonical: ansys.stk.core.stkobjects.IChain.end_object
    :type: IStkObject

    End object for the Chain.

.. py:property:: max_strand_depth
    :canonical: ansys.stk.core.stkobjects.IChain.max_strand_depth
    :type: int

    Maximum number of objects in all strands for the Chain.

.. py:property:: connections
    :canonical: ansys.stk.core.stkobjects.IChain.connections
    :type: IChainConnectionCollection

    Get the collection of connections in the chain.

.. py:property:: optimal_strand_opts
    :canonical: ansys.stk.core.stkobjects.IChain.optimal_strand_opts
    :type: IChainOptimalStrandOpts

    Optimal strands settings for the Chain.


Method detail
-------------





.. py:method:: set_time_period_type(self, timePeriodType: CHAIN_TIME_PERIOD_TYPE) -> None
    :canonical: ansys.stk.core.stkobjects.IChain.set_time_period_type

    Set the option used to specify the time period.

    :Parameters:

    **timePeriodType** : :obj:`~CHAIN_TIME_PERIOD_TYPE`

    :Returns:

        :obj:`~None`




.. py:method:: set_access_intervals_file(self, filename: str) -> None
    :canonical: ansys.stk.core.stkobjects.IChain.set_access_intervals_file

    Opt to produce an .int file containing the strand access intervals.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~None`

.. py:method:: reset_access_intervals_file(self) -> None
    :canonical: ansys.stk.core.stkobjects.IChain.reset_access_intervals_file

    Reset the .int file containing the strand access intervals.

    :Returns:

        :obj:`~None`











.. py:method:: compute_access(self) -> None
    :canonical: ansys.stk.core.stkobjects.IChain.compute_access

    Compute access for the chain.

    :Returns:

        :obj:`~None`

.. py:method:: clear_access(self) -> None
    :canonical: ansys.stk.core.stkobjects.IChain.clear_access

    Remove all chain accesses.

    :Returns:

        :obj:`~None`





















