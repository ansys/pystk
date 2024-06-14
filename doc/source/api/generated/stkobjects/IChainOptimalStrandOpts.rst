IChainOptimalStrandOpts
=======================

.. py:class:: IChainOptimalStrandOpts

   object
   
   Chain optimal strand options.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute`
            * - :py:meth:`~sampling_time_step`
            * - :py:meth:`~include_access_edge_times_in_samples`
            * - :py:meth:`~num_strands_to_store`
            * - :py:meth:`~type`
            * - :py:meth:`~link_comparison_type`
            * - :py:meth:`~strand_comparison_type`
            * - :py:meth:`~calc_scalar_type`
            * - :py:meth:`~calc_scalar_name`
            * - :py:meth:`~calc_scalar_file_name`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IChainOptimalStrandOpts


Property detail
---------------

.. py:property:: compute
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.compute
    :type: bool

    Compute optimal strands.

.. py:property:: sampling_time_step
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.sampling_time_step
    :type: float

    Time step used to sample optimal strand metric when computing optimal strands.

.. py:property:: include_access_edge_times_in_samples
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.include_access_edge_times_in_samples
    :type: bool

    Include all chain connection access pairs when computing sample times for optimal strands.

.. py:property:: num_strands_to_store
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.num_strands_to_store
    :type: int

    Maximum number of objects in all strands for the Chain.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.type
    :type: "CHAIN_OPTIMAL_STRAND_METRIC_TYPE"

    Optimal path type.

.. py:property:: link_comparison_type
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.link_comparison_type
    :type: "CHAIN_OPTIMAL_STRAND_LINK_COMPARE_TYPE"

    Optimal path comparison type (min, max or sum) used when comparing connections of a strand when computing an overall value of the metric for a strand.

.. py:property:: strand_comparison_type
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.strand_comparison_type
    :type: "CHAIN_OPTIMAL_STRAND_COMPARE_STRANDS_TYPE"

    Optimal path comparison type (min or max) used when comparing strands.

.. py:property:: calc_scalar_type
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.calc_scalar_type
    :type: "CHAIN_OPTIMAL_STRAND_CALCULATION_SCALAR_METRIC_TYPE"

    Optimal path AWB calculation scalar type used when the optiml path type is set to use a calculation scalar.

.. py:property:: calc_scalar_name
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.calc_scalar_name
    :type: str

    Optimal path AWB calculation scalar to evaluate to determine optimal strands.

.. py:property:: calc_scalar_file_name
    :canonical: ansys.stk.core.stkobjects.IChainOptimalStrandOpts.calc_scalar_file_name
    :type: str

    Optimal path AWB calculation scalar file (.awb) to evaluate to determine optimal strands.


