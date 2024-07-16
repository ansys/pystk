SpatialAnalysisToolVolumeCalcRange
==================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalc`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume calc distance to location interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeCalcRange

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange.distance`
              - The Volume Calc range distance types.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange.reference_point`
              - The Volume Calc Range reference point.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange.reference_plane`
              - The Volume Calc Range reference plane.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange.along_vector`
              - The Volume Calc Range Along Vector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeCalcRange


Property detail
---------------

.. py:property:: distance
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange.distance
    :type: CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE

    The Volume Calc range distance types.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange.reference_point
    :type: IVectorGeometryToolPoint

    The Volume Calc Range reference point.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange.reference_plane
    :type: IVectorGeometryToolPlane

    The Volume Calc Range reference plane.

.. py:property:: along_vector
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcRange.along_vector
    :type: IVectorGeometryToolVector

    The Volume Calc Range Along Vector.


