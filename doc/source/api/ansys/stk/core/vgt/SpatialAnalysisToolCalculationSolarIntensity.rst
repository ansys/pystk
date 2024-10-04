SpatialAnalysisToolCalculationSolarIntensity
============================================

.. py:class:: ansys.stk.core.vgt.SpatialAnalysisToolCalculationSolarIntensity

   Bases: :py:class:`~ansys.stk.core.vgt.ISpatialAnalysisToolSpatialCalculation`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A volume calc solar intensityn interface.

.. py:currentmodule:: SpatialAnalysisToolCalculationSolarIntensity

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationSolarIntensity.eclipsing_bodies`
              - A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.
            * - :py:attr:`~ansys.stk.core.vgt.SpatialAnalysisToolCalculationSolarIntensity.use_object_eclipsing_bodies`
              - When true, configure eclipsing bodies list based on that of parent STK Object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import SpatialAnalysisToolCalculationSolarIntensity


Property detail
---------------

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationSolarIntensity.eclipsing_bodies
    :type: list

    A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.

.. py:property:: use_object_eclipsing_bodies
    :canonical: ansys.stk.core.vgt.SpatialAnalysisToolCalculationSolarIntensity.use_object_eclipsing_bodies
    :type: bool

    When true, configure eclipsing bodies list based on that of parent STK Object.


