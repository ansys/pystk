AnalysisWorkbenchProvider
=========================

.. py:class:: ansys.stk.core.vgt.AnalysisWorkbenchProvider

   Allow accessing existing Vector Geometry Tool components.

.. py:currentmodule:: AnalysisWorkbenchProvider

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.supports`
              - Test whether the specified VGT feature is supported.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.import_components`
              - Import Analysis Workbench components from a file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.vectors`
              - Returns a group of vectors.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.points`
              - Returns a group of points.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.angles`
              - Returns a group of angles.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.axes`
              - Returns a group of axes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.planes`
              - Returns a group of planes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.systems`
              - Returns a group of systems.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.well_known_systems`
              - Returns well-known systems.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.well_known_axes`
              - Returns well-known axes.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.events`
              - Returns a group of events.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.event_intervals`
              - Returns a group of event intervals.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.calc_scalars`
              - Returns a group of calc scalars.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.event_arrays`
              - Returns a group of event arrays.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.event_interval_lists`
              - Returns a group of event interval lists.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.event_interval_collections`
              - Returns a group of event interval collections.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.parameter_sets`
              - Access, add new or remove existing parameter set components.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.conditions`
              - Returns a group of condition objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.condition_sets`
              - Returns a group of condition set objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.volume_grids`
              - Returns a group of volume grid objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.volumes`
              - Returns a group of volume objects.
            * - :py:attr:`~ansys.stk.core.vgt.AnalysisWorkbenchProvider.volume_calcs`
              - Returns a group of volume calc objects.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import AnalysisWorkbenchProvider


Property detail
---------------

.. py:property:: vectors
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.vectors
    :type: VectorGeometryToolVectorGroup

    Returns a group of vectors.

.. py:property:: points
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.points
    :type: VectorGeometryToolPointGroup

    Returns a group of points.

.. py:property:: angles
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.angles
    :type: VectorGeometryToolAngleGroup

    Returns a group of angles.

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.axes
    :type: VectorGeometryToolAxesGroup

    Returns a group of axes.

.. py:property:: planes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.planes
    :type: VectorGeometryToolPlaneGroup

    Returns a group of planes.

.. py:property:: systems
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.systems
    :type: VectorGeometryToolSystemGroup

    Returns a group of systems.

.. py:property:: well_known_systems
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.well_known_systems
    :type: VectorGeometryToolWellKnownSystems

    Returns well-known systems.

.. py:property:: well_known_axes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.well_known_axes
    :type: VectorGeometryToolWellKnownAxes

    Returns well-known axes.

.. py:property:: events
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.events
    :type: TimeToolEventGroup

    Returns a group of events.

.. py:property:: event_intervals
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.event_intervals
    :type: TimeToolEventIntervalGroup

    Returns a group of event intervals.

.. py:property:: calc_scalars
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.calc_scalars
    :type: CalculationToolScalarGroup

    Returns a group of calc scalars.

.. py:property:: event_arrays
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.event_arrays
    :type: TimeToolEventArrayGroup

    Returns a group of event arrays.

.. py:property:: event_interval_lists
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.event_interval_lists
    :type: TimeToolEventIntervalListGroup

    Returns a group of event interval lists.

.. py:property:: event_interval_collections
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.event_interval_collections
    :type: TimeToolEventIntervalCollectionGroup

    Returns a group of event interval collections.

.. py:property:: parameter_sets
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.parameter_sets
    :type: CalculationToolParameterSetGroup

    Access, add new or remove existing parameter set components.

.. py:property:: conditions
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.conditions
    :type: CalculationToolConditionGroup

    Returns a group of condition objects.

.. py:property:: condition_sets
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.condition_sets
    :type: CalculationToolConditionSetGroup

    Returns a group of condition set objects.

.. py:property:: volume_grids
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.volume_grids
    :type: SpatialAnalysisToolVolumeGridGroup

    Returns a group of volume grid objects.

.. py:property:: volumes
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.volumes
    :type: SpatialAnalysisToolVolumeGroup

    Returns a group of volume objects.

.. py:property:: volume_calcs
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.volume_calcs
    :type: SpatialAnalysisToolVolumeCalcGroup

    Returns a group of volume calc objects.


Method detail
-------------

















.. py:method:: supports(self, feature: CRDN_KIND) -> bool
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.supports

    Test whether the specified VGT feature is supported.

    :Parameters:

    **feature** : :obj:`~CRDN_KIND`

    :Returns:

        :obj:`~bool`


.. py:method:: import_components(self, filename: str) -> AnalysisWorkbenchCollection
    :canonical: ansys.stk.core.vgt.AnalysisWorkbenchProvider.import_components

    Import Analysis Workbench components from a file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~AnalysisWorkbenchCollection`




