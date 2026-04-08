ChainStrandAnalysisOpts
=======================

.. py:class:: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts

   Class defining Chain strand analysis options.

.. py:currentmodule:: ChainStrandAnalysisOpts

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.calc_scalar_file_name`
              - Strand analysis AWB calculation scalar file (.awb) to evaluate to determine strand analytics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.calc_scalar_name`
              - Strand analysis AWB calculation scalar to evaluate to determine strand analytics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.calc_scalar_type`
              - Strand analysis AWB calculation scalar type used when the strand analysis type is set to use a calculation scalar.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.compute`
              - Compute strands analytics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.compute_type`
              - Strand analysis type.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.include_access_edge_times_in_samples`
              - Include all chain connection access pairs when computing sample times for strand analytics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.link_comparison_type`
              - Strand analysis comparison type (min, max or sum) used when comparing connections of a strand when computing an overall value of the metric for a strand.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.num_strands_to_store`
              - Maximum number of objects in all strands for the Chain.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.sampling_time_step`
              - Time step used to sample strand metric when computing strand analytics.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.strand_comparison_type`
              - Strand analysis comparison type (min or max) used when comparing strands.
            * - :py:attr:`~ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.type`
              - Strand analysis type.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ChainStrandAnalysisOpts


Property detail
---------------

.. py:property:: calc_scalar_file_name
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.calc_scalar_file_name
    :type: str

    Strand analysis AWB calculation scalar file (.awb) to evaluate to determine strand analytics.

.. py:property:: calc_scalar_name
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.calc_scalar_name
    :type: str

    Strand analysis AWB calculation scalar to evaluate to determine strand analytics.

.. py:property:: calc_scalar_type
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.calc_scalar_type
    :type: ChainOptimalStrandCalculationScalarMetricType

    Strand analysis AWB calculation scalar type used when the strand analysis type is set to use a calculation scalar.

.. py:property:: compute
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.compute
    :type: bool

    Compute strands analytics.

.. py:property:: compute_type
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.compute_type
    :type: ChainStrandAnalysisComputeType

    Strand analysis type.

.. py:property:: include_access_edge_times_in_samples
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.include_access_edge_times_in_samples
    :type: bool

    Include all chain connection access pairs when computing sample times for strand analytics.

.. py:property:: link_comparison_type
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.link_comparison_type
    :type: ChainOptimalStrandLinkCompareType

    Strand analysis comparison type (min, max or sum) used when comparing connections of a strand when computing an overall value of the metric for a strand.

.. py:property:: num_strands_to_store
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.num_strands_to_store
    :type: int

    Maximum number of objects in all strands for the Chain.

.. py:property:: sampling_time_step
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.sampling_time_step
    :type: float

    Time step used to sample strand metric when computing strand analytics.

.. py:property:: strand_comparison_type
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.strand_comparison_type
    :type: ChainOptimalStrandCompareStrandsType

    Strand analysis comparison type (min or max) used when comparing strands.

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.ChainStrandAnalysisOpts.type
    :type: ChainOptimalStrandMetricType

    Strand analysis type.


