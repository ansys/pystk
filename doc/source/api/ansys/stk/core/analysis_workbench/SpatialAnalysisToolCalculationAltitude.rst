SpatialAnalysisToolCalculationAltitude
======================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume calc altitude interface.

.. py:currentmodule:: SpatialAnalysisToolCalculationAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude.central_body`
              - Get the central body for the volume calc. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume calc.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude.shape_model`
              - The Volume Calc Altitude Reference Type.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude.use_custom_reference`
              - Whether to use custom reference.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude.reference_point`
              - A reference point. Can be any point from VGT.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolCalculationAltitude


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude.central_body
    :type: str

    Get the central body for the volume calc. Both the central body reference shape and its CBF (central body centered fixed) system are used by this volume calc.

.. py:property:: shape_model
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude.shape_model
    :type: SpatialCalculationAltitudeReferenceType

    The Volume Calc Altitude Reference Type.

.. py:property:: use_custom_reference
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude.use_custom_reference
    :type: bool

    Whether to use custom reference.

.. py:property:: reference_point
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationAltitude.reference_point
    :type: IVectorGeometryToolPoint

    A reference point. Can be any point from VGT.


