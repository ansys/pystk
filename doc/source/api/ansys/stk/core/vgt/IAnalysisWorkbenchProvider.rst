IAnalysisWorkbenchProvider
==========================

.. py:class:: ansys.stk.core.vgt.IAnalysisWorkbenchProvider

   object
   
   Allow accessing existing Vector Geometry Tool components.

.. py:currentmodule:: IAnalysisWorkbenchProvider

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.supports`
              - Test whether the specified VGT feature is supported.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.import_method`
              - Import Analysis Workbench components from a file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.vectors`
              - Returns a group of vectors.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.points`
              - Returns a group of points.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.angles`
              - Returns a group of angles.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.axes`
              - Returns a group of axes.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.planes`
              - Returns a group of planes.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.systems`
              - Returns a group of systems.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.well_known_systems`
              - Returns well-known systems.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.well_known_axes`
              - Returns well-known axes.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.events`
              - Returns a group of events.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_intervals`
              - Returns a group of event intervals.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.calc_scalars`
              - Returns a group of calc scalars.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_arrays`
              - Returns a group of event arrays.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_interval_lists`
              - Returns a group of event interval lists.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_interval_collections`
              - Returns a group of event interval collections.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.parameter_sets`
              - Access, add new or remove existing parameter set components.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.conditions`
              - Returns a group of condition objects.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.condition_sets`
              - Returns a group of condition set objects.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volume_grids`
              - Returns a group of volume grid objects.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volumes`
              - Returns a group of volume objects.
            * - :py:attr:`~ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volume_calcs`
              - Returns a group of volume calc objects.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAnalysisWorkbenchProvider


Property detail
---------------

.. py:property:: vectors
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.vectors
    :type: IVectorGeometryToolVectorGroup

    Returns a group of vectors.

.. py:property:: points
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.points
    :type: IVectorGeometryToolPointGroup

    Returns a group of points.

.. py:property:: angles
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.angles
    :type: IVectorGeometryToolAngleGroup

    Returns a group of angles.

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.axes
    :type: IVectorGeometryToolAxesGroup

    Returns a group of axes.

.. py:property:: planes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.planes
    :type: IVectorGeometryToolPlaneGroup

    Returns a group of planes.

.. py:property:: systems
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.systems
    :type: IVectorGeometryToolSystemGroup

    Returns a group of systems.

.. py:property:: well_known_systems
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.well_known_systems
    :type: IVectorGeometryToolWellKnownSystems

    Returns well-known systems.

.. py:property:: well_known_axes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.well_known_axes
    :type: IVectorGeometryToolWellKnownAxes

    Returns well-known axes.

.. py:property:: events
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.events
    :type: ITimeToolEventGroup

    Returns a group of events.

.. py:property:: event_intervals
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_intervals
    :type: ITimeToolEventIntervalGroup

    Returns a group of event intervals.

.. py:property:: calc_scalars
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.calc_scalars
    :type: ICalculationToolScalarGroup

    Returns a group of calc scalars.

.. py:property:: event_arrays
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_arrays
    :type: ITimeToolEventArrayGroup

    Returns a group of event arrays.

.. py:property:: event_interval_lists
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_interval_lists
    :type: ITimeToolEventIntervalListGroup

    Returns a group of event interval lists.

.. py:property:: event_interval_collections
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_interval_collections
    :type: ITimeToolEventIntervalCollectionGroup

    Returns a group of event interval collections.

.. py:property:: parameter_sets
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.parameter_sets
    :type: ICalculationToolParameterSetGroup

    Access, add new or remove existing parameter set components.

.. py:property:: conditions
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.conditions
    :type: ICalculationToolConditionGroup

    Returns a group of condition objects.

.. py:property:: condition_sets
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.condition_sets
    :type: ICalculationToolConditionSetGroup

    Returns a group of condition set objects.

.. py:property:: volume_grids
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volume_grids
    :type: ISpatialAnalysisToolVolumeGridGroup

    Returns a group of volume grid objects.

.. py:property:: volumes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volumes
    :type: ISpatialAnalysisToolVolumeGroup

    Returns a group of volume objects.

.. py:property:: volume_calcs
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volume_calcs
    :type: ISpatialAnalysisToolVolumeCalcGroup

    Returns a group of volume calc objects.


Method detail
-------------

















.. py:method:: supports(self, feature: CRDN_KIND) -> bool
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.supports

    Test whether the specified VGT feature is supported.

    :Parameters:

    **feature** : :obj:`~CRDN_KIND`

    :Returns:

        :obj:`~bool`


.. py:method:: import_method(self, filename: str) -> IAnalysisWorkbenchCollection
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.import_method

    Import Analysis Workbench components from a file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~IAnalysisWorkbenchCollection`




