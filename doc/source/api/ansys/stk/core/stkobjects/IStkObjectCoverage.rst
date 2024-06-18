IStkObjectCoverage
==================

.. py:class:: IStkObjectCoverage

   object
   
   Provide access to the Data Providers on an ObjectCoverage Object.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute`
              - Compute the object coverage.
            * - :py:meth:`~clear`
              - Remove the computation on the object coverage.
            * - :py:meth:`~clear_coverage`
              - Clear object coverage.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~data_providers`
            * - :py:meth:`~start_time`
            * - :py:meth:`~stop_time`
            * - :py:meth:`~assets`
            * - :py:meth:`~figure_of_merit`
            * - :py:meth:`~access_interval`
            * - :py:meth:`~use_object_times`
            * - :py:meth:`~is_coverage_configuration_saved`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IStkObjectCoverage


Property detail
---------------

.. py:property:: data_providers
    :canonical: ansys.stk.core.stkobjects.IStkObjectCoverage.data_providers
    :type: "IAgDataProviderCollection"

    Returns the object representing a list of available data providers for the object.

.. py:property:: start_time
    :canonical: ansys.stk.core.stkobjects.IStkObjectCoverage.start_time
    :type: typing.Any

    Gets or sets the start time of object coverage. Uses DateFormat Dimension.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.IStkObjectCoverage.stop_time
    :type: typing.Any

    Gets or sets the stop time of object coverage. Uses DateFormat Dimension.

.. py:property:: assets
    :canonical: ansys.stk.core.stkobjects.IStkObjectCoverage.assets
    :type: "IAgCvAssetListCollection"

    Get the asset list collection.

.. py:property:: figure_of_merit
    :canonical: ansys.stk.core.stkobjects.IStkObjectCoverage.figure_of_merit
    :type: "IAgObjectCoverageFOM"

    Get the figure of merit on the object coverage.

.. py:property:: access_interval
    :canonical: ansys.stk.core.stkobjects.IStkObjectCoverage.access_interval
    :type: "IAgCrdnEventIntervalSmartInterval"

    The object coverage's access interval.

.. py:property:: use_object_times
    :canonical: ansys.stk.core.stkobjects.IStkObjectCoverage.use_object_times
    :type: bool

    Use object interval times.

.. py:property:: is_coverage_configuration_saved
    :canonical: ansys.stk.core.stkobjects.IStkObjectCoverage.is_coverage_configuration_saved
    :type: bool

    Save the single-object coverage definitions when the scenario is saved to disk, if a compute has been done.


Method detail
-------------








.. py:method:: compute(self) -> None

    Compute the object coverage.

    :Returns:

        :obj:`~None`

.. py:method:: clear(self) -> None

    Remove the computation on the object coverage.

    :Returns:

        :obj:`~None`






.. py:method:: clear_coverage(self) -> None

    Clear object coverage.

    :Returns:

        :obj:`~None`

