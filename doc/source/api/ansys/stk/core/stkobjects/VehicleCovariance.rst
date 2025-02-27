VehicleCovariance
=================

.. py:class:: ansys.stk.core.stkobjects.VehicleCovariance

   Class defining HPOP covariance.

.. py:currentmodule:: VehicleCovariance

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.validate`
              - Validate.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.compute_covariance`
              - Opt whether to compute covariance.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.frame`
              - Frame in which covariance is input.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.representation`
              - Get the representation for the covariance.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.gravity`
              - Get the gravity parameters for the covariance.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.position_velocity`
              - Get the covariance matrix.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.include_consider_analysis`
              - Opt whether to include Consider Analysis.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.consider_analysis_list`
              - Get the Consider Analysis list.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.include_consider_cross_correlation`
              - Opt whether to include Consider Cross Correlation.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleCovariance.correlation_list`
              - Get the Consider Cross Correlation list.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleCovariance


Property detail
---------------

.. py:property:: compute_covariance
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.compute_covariance
    :type: bool

    Opt whether to compute covariance.

.. py:property:: frame
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.frame
    :type: VehicleFrame

    Frame in which covariance is input.

.. py:property:: representation
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.representation
    :type: str

    Get the representation for the covariance.

.. py:property:: gravity
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.gravity
    :type: VehicleGravity

    Get the gravity parameters for the covariance.

.. py:property:: position_velocity
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.position_velocity
    :type: VehiclePositionVelocityCollection

    Get the covariance matrix.

.. py:property:: include_consider_analysis
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.include_consider_analysis
    :type: bool

    Opt whether to include Consider Analysis.

.. py:property:: consider_analysis_list
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.consider_analysis_list
    :type: VehicleConsiderAnalysisCollection

    Get the Consider Analysis list.

.. py:property:: include_consider_cross_correlation
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.include_consider_cross_correlation
    :type: bool

    Opt whether to include Consider Cross Correlation.

.. py:property:: correlation_list
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.correlation_list
    :type: VehicleCorrelationListCollection

    Get the Consider Cross Correlation list.


Method detail
-------------














.. py:method:: validate(self) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleCovariance.validate

    Validate.

    :Returns:

        :obj:`~None`

