IAnalysisWorkbenchProvider
==========================

.. py:class:: IAnalysisWorkbenchProvider

   object
   
   Allow accessing existing Vector Geometry Tool components.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~supports`
              - Test whether the specified VGT feature is supported.
            * - :py:meth:`~import_method`
              - Import Analysis Workbench components from a file.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~vectors`
            * - :py:meth:`~points`
            * - :py:meth:`~angles`
            * - :py:meth:`~axes`
            * - :py:meth:`~planes`
            * - :py:meth:`~systems`
            * - :py:meth:`~well_known_systems`
            * - :py:meth:`~well_known_axes`
            * - :py:meth:`~events`
            * - :py:meth:`~event_intervals`
            * - :py:meth:`~calc_scalars`
            * - :py:meth:`~event_arrays`
            * - :py:meth:`~event_interval_lists`
            * - :py:meth:`~event_interval_collections`
            * - :py:meth:`~parameter_sets`
            * - :py:meth:`~conditions`
            * - :py:meth:`~condition_sets`
            * - :py:meth:`~volume_grids`
            * - :py:meth:`~volumes`
            * - :py:meth:`~volume_calcs`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IAnalysisWorkbenchProvider


Property detail
---------------

.. py:property:: vectors
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.vectors
    :type: "IAgCrdnVectorGroup"

    Returns a group of vectors.

.. py:property:: points
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.points
    :type: "IAgCrdnPointGroup"

    Returns a group of points.

.. py:property:: angles
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.angles
    :type: "IAgCrdnAngleGroup"

    Returns a group of angles.

.. py:property:: axes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.axes
    :type: "IAgCrdnAxesGroup"

    Returns a group of axes.

.. py:property:: planes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.planes
    :type: "IAgCrdnPlaneGroup"

    Returns a group of planes.

.. py:property:: systems
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.systems
    :type: "IAgCrdnSystemGroup"

    Returns a group of systems.

.. py:property:: well_known_systems
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.well_known_systems
    :type: "IAgCrdnWellKnownSystems"

    Returns well-known systems.

.. py:property:: well_known_axes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.well_known_axes
    :type: "IAgCrdnWellKnownAxes"

    Returns well-known axes.

.. py:property:: events
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.events
    :type: "IAgCrdnEventGroup"

    Returns a group of events.

.. py:property:: event_intervals
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_intervals
    :type: "IAgCrdnEventIntervalGroup"

    Returns a group of event intervals.

.. py:property:: calc_scalars
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.calc_scalars
    :type: "IAgCrdnCalcScalarGroup"

    Returns a group of calc scalars.

.. py:property:: event_arrays
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_arrays
    :type: "IAgCrdnEventArrayGroup"

    Returns a group of event arrays.

.. py:property:: event_interval_lists
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_interval_lists
    :type: "IAgCrdnEventIntervalListGroup"

    Returns a group of event interval lists.

.. py:property:: event_interval_collections
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.event_interval_collections
    :type: "IAgCrdnEventIntervalCollectionGroup"

    Returns a group of event interval collections.

.. py:property:: parameter_sets
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.parameter_sets
    :type: "IAgCrdnParameterSetGroup"

    Access, add new or remove existing parameter set components.

.. py:property:: conditions
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.conditions
    :type: "IAgCrdnConditionGroup"

    Returns a group of condition objects.

.. py:property:: condition_sets
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.condition_sets
    :type: "IAgCrdnConditionSetGroup"

    Returns a group of condition set objects.

.. py:property:: volume_grids
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volume_grids
    :type: "IAgCrdnVolumeGridGroup"

    Returns a group of volume grid objects.

.. py:property:: volumes
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volumes
    :type: "IAgCrdnVolumeGroup"

    Returns a group of volume objects.

.. py:property:: volume_calcs
    :canonical: ansys.stk.core.vgt.IAnalysisWorkbenchProvider.volume_calcs
    :type: "IAgCrdnVolumeCalcGroup"

    Returns a group of volume calc objects.


Method detail
-------------

















.. py:method:: supports(self, feature:"CRDN_KIND") -> bool

    Test whether the specified VGT feature is supported.

    :Parameters:

    **feature** : :obj:`~"CRDN_KIND"`

    :Returns:

        :obj:`~bool`


.. py:method:: import_method(self, filename:str) -> "IAnalysisWorkbenchCollection"

    Import Analysis Workbench components from a file.

    :Parameters:

    **filename** : :obj:`~str`

    :Returns:

        :obj:`~"IAnalysisWorkbenchCollection"`




