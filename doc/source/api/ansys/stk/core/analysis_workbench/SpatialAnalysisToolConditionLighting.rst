SpatialAnalysisToolConditionLighting
====================================

.. py:class:: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionLighting

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.ISpatialAnalysisToolVolume`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   A lighting volume interface.

.. py:currentmodule:: SpatialAnalysisToolConditionLighting

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionLighting.eclipsing_bodies`
              - A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionLighting.lighting_conditions`
              - Get or set the lighting conditions.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionLighting.use_object_eclipsing_bodies`
              - When true, configure eclipsing bodies list based on that of parent STK Object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import SpatialAnalysisToolConditionLighting


Property detail
---------------

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionLighting.eclipsing_bodies
    :type: list

    A custom list of eclipsing bodies. This list is used if UseObjectEclipsingBodies is set to false.

.. py:property:: lighting_conditions
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionLighting.lighting_conditions
    :type: LightingConditionsType

    Get or set the lighting conditions.

.. py:property:: use_object_eclipsing_bodies
    :canonical: ansys.stk.core.analysis_workbench.SpatialAnalysisToolConditionLighting.use_object_eclipsing_bodies
    :type: bool

    When true, configure eclipsing bodies list based on that of parent STK Object.


