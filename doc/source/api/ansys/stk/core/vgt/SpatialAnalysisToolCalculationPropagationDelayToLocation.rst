SpatialAnalysisToolCalculationPropagationDelayToLocation
========================================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume calc propagation delay to location interface.

.. py:currentmodule:: SpatialAnalysisToolCalculationPropagationDelayToLocation

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.distance`
              - The Volume Calc range distance types.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.reference_point`
              - The Volume Calc Range reference point.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.reference_plane`
              - The Volume Calc Range reference plane.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.along_vector`
              - The Volume Calc Range Along Vector.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.speed_type`
              - The Volume Calc range speed types.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.speed`
              - The Volume Calc range speed value.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolCalculationPropagationDelayToLocation


Property detail
---------------

.. py:property:: distance
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.distance
    :type: DISTANCE_TO_LOCATION_TYPE

    The Volume Calc range distance types.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.reference_point
    :type: IVectorGeometryToolPoint

    The Volume Calc Range reference point.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.reference_plane
    :type: IVectorGeometryToolPlane

    The Volume Calc Range reference plane.

.. py:property:: along_vector
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.along_vector
    :type: IVectorGeometryToolVector

    The Volume Calc Range Along Vector.

.. py:property:: speed_type
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.speed_type
    :type: RANGE_SPEED_TYPE

    The Volume Calc range speed types.

.. py:property:: speed
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationPropagationDelayToLocation.speed
    :type: float

    The Volume Calc range speed value.


