SpatialAnalysisToolCalculationSolarIntensity
============================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationSolarIntensity

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A volume calc solar intensityn interface.

.. py:currentmodule:: SpatialAnalysisToolCalculationSolarIntensity

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationSolarIntensity.eclipsing_bodies`
              - A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationSolarIntensity.use_object_eclipsing_bodies`
              - When true, configure eclipsing bodies list based on that of parent STK Object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import (
        SpatialAnalysisToolCalculationSolarIntensity,
    )


Property detail
---------------

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationSolarIntensity.eclipsing_bodies
    :type: list

    A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.

.. py:property:: use_object_eclipsing_bodies
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolCalculationSolarIntensity.use_object_eclipsing_bodies
    :type: bool

    When true, configure eclipsing bodies list based on that of parent STK Object.


