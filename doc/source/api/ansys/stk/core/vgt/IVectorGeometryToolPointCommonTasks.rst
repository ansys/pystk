IVectorGeometryToolPointCommonTasks
===================================

.. py:class:: IVectorGeometryToolPointCommonTasks

   object
   
   Provide methods to create non-persistent VGT point components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create_fixed_in_system_cartographic`
              - Create a non-persistent point fixed in a specified reference system.
            * - :py:meth:`~create_fixed_in_system_cartesian`
              - Create a non-persistent point fixed in a specified reference system.
            * - :py:meth:`~sample`
              - Compute and returns tabulated positions and velocities of a point with respect to reference system using specified sampling parameters.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointCommonTasks



Method detail
-------------

.. py:method:: create_fixed_in_system_cartographic(self, referenceSystem: IVectorGeometryToolSystem, latitude: typing.Any, longitude: typing.Any, altitude: float) -> IVectorGeometryToolPointFixedInSystem
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCommonTasks.create_fixed_in_system_cartographic

    Create a non-persistent point fixed in a specified reference system.

    :Parameters:

    **referenceSystem** : :obj:`~IVectorGeometryToolSystem`
    **latitude** : :obj:`~typing.Any`
    **longitude** : :obj:`~typing.Any`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~IVectorGeometryToolPointFixedInSystem`

.. py:method:: create_fixed_in_system_cartesian(self, referenceSystem: IVectorGeometryToolSystem, x: float, y: float, z: float) -> IVectorGeometryToolPointFixedInSystem
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCommonTasks.create_fixed_in_system_cartesian

    Create a non-persistent point fixed in a specified reference system.

    :Parameters:

    **referenceSystem** : :obj:`~IVectorGeometryToolSystem`
    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~IVectorGeometryToolPointFixedInSystem`

.. py:method:: sample(self, point: IVectorGeometryToolPoint, referenceSystem: IVectorGeometryToolSystem, intervals: list, minStep: float, maxStep: float, targetRate: typing.Any) -> ITimeToolPointSamplingResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCommonTasks.sample

    Compute and returns tabulated positions and velocities of a point with respect to reference system using specified sampling parameters.

    :Parameters:

    **point** : :obj:`~IVectorGeometryToolPoint`
    **referenceSystem** : :obj:`~IVectorGeometryToolSystem`
    **intervals** : :obj:`~list`
    **minStep** : :obj:`~float`
    **maxStep** : :obj:`~float`
    **targetRate** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ITimeToolPointSamplingResult`

