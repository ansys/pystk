SpatialAnalysisToolVolumeCalcAltitude
=====================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolVolumeCalc`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume calc altitude interface.

.. py:currentmodule:: SpatialAnalysisToolVolumeCalcAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude.central_body`
              - Get the central body for the volume calc. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume calc.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude.shape_model`
              - The Volume Calc Altitude Reference Type.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude.use_custom_reference`
              - Whether to use custom reference.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude.reference_point`
              - A reference point. Can be any point from VGT.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolVolumeCalcAltitude


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude.central_body
    :type: str

    Get the central body for the volume calc. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume calc.

.. py:property:: shape_model
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude.shape_model
    :type: CRDN_VOLUME_CALC_ALTITUDE_REFERENCE_TYPE

    The Volume Calc Altitude Reference Type.

.. py:property:: use_custom_reference
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude.use_custom_reference
    :type: bool

    Whether to use custom reference.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolVolumeCalcAltitude.reference_point
    :type: IVectorGeometryToolPoint

    A reference point. Can be any point from VGT.


