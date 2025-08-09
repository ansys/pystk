VectorGeometryToolPointCommonTasks
==================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointCommonTasks

   Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

.. py:currentmodule:: VectorGeometryToolPointCommonTasks

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCommonTasks.create_fixed_in_system_cartographic`
              - Create a non-persistent point fixed in a specified reference system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCommonTasks.create_fixed_in_system_cartesian`
              - Create a non-persistent point fixed in a specified reference system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointCommonTasks.sample`
              - Compute and returns tabulated positions and velocities of a point with respect to reference system using specified sampling parameters.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointCommonTasks



Method detail
-------------

.. py:method:: create_fixed_in_system_cartographic(self, reference_system: IVectorGeometryToolSystem, latitude: typing.Any, longitude: typing.Any, altitude: float) -> VectorGeometryToolPointFixedInSystem
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointCommonTasks.create_fixed_in_system_cartographic

    Create a non-persistent point fixed in a specified reference system.

    :Parameters:

        **reference_system** : :obj:`~IVectorGeometryToolSystem`

        **latitude** : :obj:`~typing.Any`

        **longitude** : :obj:`~typing.Any`

        **altitude** : :obj:`~float`


    :Returns:

        :obj:`~VectorGeometryToolPointFixedInSystem`

.. py:method:: create_fixed_in_system_cartesian(self, reference_system: IVectorGeometryToolSystem, x: float, y: float, z: float) -> VectorGeometryToolPointFixedInSystem
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointCommonTasks.create_fixed_in_system_cartesian

    Create a non-persistent point fixed in a specified reference system.

    :Parameters:

        **reference_system** : :obj:`~IVectorGeometryToolSystem`

        **x** : :obj:`~float`

        **y** : :obj:`~float`

        **z** : :obj:`~float`


    :Returns:

        :obj:`~VectorGeometryToolPointFixedInSystem`

.. py:method:: sample(self, point: IVectorGeometryToolPoint, reference_system: IVectorGeometryToolSystem, intervals: list, min_step: float, max_step: float, target_rate: typing.Any) -> TimeToolPointSamplingResult
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointCommonTasks.sample

    Compute and returns tabulated positions and velocities of a point with respect to reference system using specified sampling parameters.

    :Parameters:

        **point** : :obj:`~IVectorGeometryToolPoint`

        **reference_system** : :obj:`~IVectorGeometryToolSystem`

        **intervals** : :obj:`~list`

        **min_step** : :obj:`~float`

        **max_step** : :obj:`~float`

        **target_rate** : :obj:`~typing.Any`


    :Returns:

        :obj:`~TimeToolPointSamplingResult`

