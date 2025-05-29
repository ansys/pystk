VectorGeometryToolAxesCommonTasks
=================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks

   Provide methods to create non-persistent VGT axes components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

.. py:currentmodule:: VectorGeometryToolAxesCommonTasks

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks.create_topocentric_axes_quaternion`
              - Create non-persistent axes fixed in axes on the surface of a central body with the location specified by the origin point. The quaternion defines the axes's orientation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks.create_topocentric_axes_euler_angles`
              - Create non-persistent axes fixed in axes on the surface of a central body with the location specified by the origin point. The euler angles define the axes's orientation.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks.create_fixed`
              - Create non-persistent fixed axes based on specified axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks.sample`
              - Compute and returns tabulated orientations and angular velocities of axes with respect to reference axes using specified sampling parameters.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolAxesCommonTasks



Method detail
-------------

.. py:method:: create_topocentric_axes_quaternion(self, origin_point: IVectorGeometryToolPoint, qx: float, qy: float, qz: float, qs: float) -> VectorGeometryToolAxesFixed
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks.create_topocentric_axes_quaternion

    Create non-persistent axes fixed in axes on the surface of a central body with the location specified by the origin point. The quaternion defines the axes's orientation.

    :Parameters:

        **origin_point** : :obj:`~IVectorGeometryToolPoint`

        **qx** : :obj:`~float`

        **qy** : :obj:`~float`

        **qz** : :obj:`~float`

        **qs** : :obj:`~float`


    :Returns:

        :obj:`~VectorGeometryToolAxesFixed`

.. py:method:: create_topocentric_axes_euler_angles(self, origin_point: IVectorGeometryToolPoint, sequence: EulerOrientationSequenceType, a: typing.Any, b: typing.Any, c: typing.Any) -> VectorGeometryToolAxesFixed
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks.create_topocentric_axes_euler_angles

    Create non-persistent axes fixed in axes on the surface of a central body with the location specified by the origin point. The euler angles define the axes's orientation.

    :Parameters:

        **origin_point** : :obj:`~IVectorGeometryToolPoint`

        **sequence** : :obj:`~EulerOrientationSequenceType`

        **a** : :obj:`~typing.Any`

        **b** : :obj:`~typing.Any`

        **c** : :obj:`~typing.Any`


    :Returns:

        :obj:`~VectorGeometryToolAxesFixed`

.. py:method:: create_fixed(self, reference_axes: IVectorGeometryToolAxes) -> VectorGeometryToolAxesFixed
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks.create_fixed

    Create non-persistent fixed axes based on specified axes.

    :Parameters:

        **reference_axes** : :obj:`~IVectorGeometryToolAxes`


    :Returns:

        :obj:`~VectorGeometryToolAxesFixed`

.. py:method:: sample(self, axes: IVectorGeometryToolAxes, reference_axes: IVectorGeometryToolAxes, intervals: list, min_step: float, max_step: float, target_rate: typing.Any) -> TimeToolAxesSamplingResult
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolAxesCommonTasks.sample

    Compute and returns tabulated orientations and angular velocities of axes with respect to reference axes using specified sampling parameters.

    :Parameters:

        **axes** : :obj:`~IVectorGeometryToolAxes`

        **reference_axes** : :obj:`~IVectorGeometryToolAxes`

        **intervals** : :obj:`~list`

        **min_step** : :obj:`~float`

        **max_step** : :obj:`~float`

        **target_rate** : :obj:`~typing.Any`


    :Returns:

        :obj:`~TimeToolAxesSamplingResult`

