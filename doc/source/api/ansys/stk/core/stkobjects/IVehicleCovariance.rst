IVehicleCovariance
==================

.. py:class:: IVehicleCovariance

   object
   
   HPOP covariance interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~validate`
              - Validate.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute_covariance`
            * - :py:meth:`~frame`
            * - :py:meth:`~representation`
            * - :py:meth:`~gravity`
            * - :py:meth:`~position_velocity`
            * - :py:meth:`~include_consider_analysis`
            * - :py:meth:`~consider_analysis_list`
            * - :py:meth:`~include_consider_cross_correlation`
            * - :py:meth:`~correlation_list`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleCovariance


Property detail
---------------

.. py:property:: compute_covariance
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.compute_covariance
    :type: bool

    Opt whether to compute covariance.

.. py:property:: frame
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.frame
    :type: "VEHICLE_FRAME"

    Frame in which covariance is input.

.. py:property:: representation
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.representation
    :type: str

    Get the representation for the covariance.

.. py:property:: gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.gravity
    :type: "IAgVeGravity"

    Get the gravity parameters for the covariance.

.. py:property:: position_velocity
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.position_velocity
    :type: "IAgVePositionVelocityCollection"

    Get the covariance matrix.

.. py:property:: include_consider_analysis
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.include_consider_analysis
    :type: bool

    Opt whether to include Consider Analysis.

.. py:property:: consider_analysis_list
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.consider_analysis_list
    :type: "IAgVeConsiderAnalysisCollection"

    Get the Consider Analysis list.

.. py:property:: include_consider_cross_correlation
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.include_consider_cross_correlation
    :type: bool

    Opt whether to include Consider Cross Correlation.

.. py:property:: correlation_list
    :canonical: ansys.stk.core.stkobjects.IVehicleCovariance.correlation_list
    :type: "IAgVeCorrelationListCollection"

    Get the Consider Cross Correlation list.


Method detail
-------------














.. py:method:: validate(self) -> None

    Validate.

    :Returns:

        :obj:`~None`

