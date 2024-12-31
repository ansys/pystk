AnalysisWorkbenchComponentProvider
==================================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider

   Allow accessing existing Vector Geometry Tool components.

.. py:currentmodule:: AnalysisWorkbenchComponentProvider

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.supports`
              - Test whether the specified VGT feature is supported.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.import_components`
              - Import Analysis Workbench components from a file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.vectors`
              - Returns a group of vectors.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.points`
              - Returns a group of points.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.angles`
              - Returns a group of angles.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.axes`
              - Returns a group of axes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.planes`
              - Returns a group of planes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.systems`
              - Returns a group of systems.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.well_known_systems`
              - Returns well-known systems.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.well_known_axes`
              - Returns well-known axes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_instants`
              - Returns a group of events.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_intervals`
              - Returns a group of event intervals.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.calculation_scalars`
              - Returns a group of calc scalars.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_arrays`
              - Returns a group of event arrays.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_interval_lists`
              - Returns a group of event interval lists.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_interval_collections`
              - Returns a group of event interval collections.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.parameter_sets`
              - Access, add new or remove existing parameter set components.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.conditions`
              - Returns a group of condition objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.condition_sets`
              - Returns a group of condition set objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.volume_grids`
              - Returns a group of volume grid objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.volumes`
              - Returns a group of volume objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.spatial_calculations`
              - Returns a group of volume calc objects.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchComponentProvider


Property detail
---------------

.. py:property:: vectors
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.vectors
    :type: VectorGeometryToolVectorGroup

    Returns a group of vectors.

.. py:property:: points
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.points
    :type: VectorGeometryToolPointGroup

    Returns a group of points.

.. py:property:: angles
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.angles
    :type: VectorGeometryToolAngleGroup

    Returns a group of angles.

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.axes
    :type: VectorGeometryToolAxesGroup

    Returns a group of axes.

.. py:property:: planes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.planes
    :type: VectorGeometryToolPlaneGroup

    Returns a group of planes.

.. py:property:: systems
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.systems
    :type: VectorGeometryToolSystemGroup

    Returns a group of systems.

.. py:property:: well_known_systems
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.well_known_systems
    :type: VectorGeometryToolWellKnownSystems

    Returns well-known systems.

.. py:property:: well_known_axes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.well_known_axes
    :type: VectorGeometryToolWellKnownAxes

    Returns well-known axes.

.. py:property:: time_instants
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_instants
    :type: TimeToolInstantGroup

    Returns a group of events.

.. py:property:: time_intervals
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_intervals
    :type: TimeToolTimeIntervalGroup

    Returns a group of event intervals.

.. py:property:: calculation_scalars
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.calculation_scalars
    :type: CalculationToolScalarGroup

    Returns a group of calc scalars.

.. py:property:: time_arrays
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_arrays
    :type: TimeToolTimeArrayGroup

    Returns a group of event arrays.

.. py:property:: time_interval_lists
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_interval_lists
    :type: TimeToolTimeIntervalListGroup

    Returns a group of event interval lists.

.. py:property:: time_interval_collections
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.time_interval_collections
    :type: TimeToolTimeIntervalCollectionGroup

    Returns a group of event interval collections.

.. py:property:: parameter_sets
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.parameter_sets
    :type: CalculationToolParameterSetGroup

    Access, add new or remove existing parameter set components.

.. py:property:: conditions
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.conditions
    :type: CalculationToolConditionGroup

    Returns a group of condition objects.

.. py:property:: condition_sets
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.condition_sets
    :type: CalculationToolConditionSetGroup

    Returns a group of condition set objects.

.. py:property:: volume_grids
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.volume_grids
    :type: SpatialAnalysisToolVolumeGridGroup

    Returns a group of volume grid objects.

.. py:property:: volumes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.volumes
    :type: SpatialAnalysisToolConditionGroup

    Returns a group of volume objects.

.. py:property:: spatial_calculations
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.spatial_calculations
    :type: SpatialAnalysisToolCalculationGroup

    Returns a group of volume calc objects.


Method detail
-------------

















.. py:method:: supports(self, feature: VectorGeometryToolComponentType) -> bool
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.supports

    Test whether the specified VGT feature is supported.

    :Parameters:

    **feature** : :obj:`~VectorGeometryToolComponentType`

    :Returns:

        :obj:`~bool`


.. py:method:: import_components(self, filename: str) -> AnalysisWorkbenchComponentCollection
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchComponentProvider.import_components

    Import Analysis Workbench components from a file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~AnalysisWorkbenchComponentCollection`




