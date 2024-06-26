ISpatialAnalysisToolVolumeCalcRange
===================================

.. py:class:: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange

   object
   
   A volume calc distance to location interface.

.. py:currentmodule:: ISpatialAnalysisToolVolumeCalcRange

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.distance`
              - The Volume Calc range distance types.
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.reference_point`
              - The Volume Calc Range reference point.
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.reference_plane`
              - The Volume Calc Range reference plane.
            * - :py:attr:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.along_vector`
              - The Volume Calc Range Along Vector.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ISpatialAnalysisToolVolumeCalcRange


Property detail
---------------

.. py:property:: distance
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.distance
    :type: CRDN_VOLUME_CALC_RANGE_DISTANCE_TYPE

    The Volume Calc range distance types.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.reference_point
    :type: IVectorGeometryToolPoint

    The Volume Calc Range reference point.

.. py:property:: reference_plane
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.reference_plane
    :type: IVectorGeometryToolPlane

    The Volume Calc Range reference plane.

.. py:property:: along_vector
    :canonical: ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalcRange.along_vector
    :type: IVectorGeometryToolVector

    The Volume Calc Range Along Vector.


