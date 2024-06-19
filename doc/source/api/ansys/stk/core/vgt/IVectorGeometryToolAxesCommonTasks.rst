IVectorGeometryToolAxesCommonTasks
==================================

.. py:class:: IVectorGeometryToolAxesCommonTasks

   object
   
   Provide methods to create non-persistent VGT axes components. Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create_topocentric_axes_quaternion`
              - Create non-persistent axes fixed in axes on the surface of a central body with the location specified by the origin point. The quaternion defines the axes's orientation.
            * - :py:meth:`~create_topocentric_axes_euler_angles`
              - Create non-persistent axes fixed in axes on the surface of a central body with the location specified by the origin point. The euler angles define the axes's orientation.
            * - :py:meth:`~create_fixed`
              - Create non-persistent fixed axes based on specified axes.
            * - :py:meth:`~sample`
              - Compute and returns tabulated orientations and angular velocities of axes with respect to reference axes using specified sampling parameters.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesCommonTasks



Method detail
-------------

.. py:method:: create_topocentric_axes_quaternion(self, originPoint: IVectorGeometryToolPoint, qx: float, qy: float, qz: float, qs: float) -> IVectorGeometryToolAxesFixed
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesCommonTasks.create_topocentric_axes_quaternion

    Create non-persistent axes fixed in axes on the surface of a central body with the location specified by the origin point. The quaternion defines the axes's orientation.

    :Parameters:

    **originPoint** : :obj:`~IVectorGeometryToolPoint`
    **qx** : :obj:`~float`
    **qy** : :obj:`~float`
    **qz** : :obj:`~float`
    **qs** : :obj:`~float`

    :Returns:

        :obj:`~IVectorGeometryToolAxesFixed`

.. py:method:: create_topocentric_axes_euler_angles(self, originPoint: IVectorGeometryToolPoint, sequence: EULER_ORIENTATION_SEQUENCE, a: typing.Any, b: typing.Any, c: typing.Any) -> IVectorGeometryToolAxesFixed
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesCommonTasks.create_topocentric_axes_euler_angles

    Create non-persistent axes fixed in axes on the surface of a central body with the location specified by the origin point. The euler angles define the axes's orientation.

    :Parameters:

    **originPoint** : :obj:`~IVectorGeometryToolPoint`
    **sequence** : :obj:`~EULER_ORIENTATION_SEQUENCE`
    **a** : :obj:`~typing.Any`
    **b** : :obj:`~typing.Any`
    **c** : :obj:`~typing.Any`

    :Returns:

        :obj:`~IVectorGeometryToolAxesFixed`

.. py:method:: create_fixed(self, referenceAxes: IVectorGeometryToolAxes) -> IVectorGeometryToolAxesFixed
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesCommonTasks.create_fixed

    Create non-persistent fixed axes based on specified axes.

    :Parameters:

    **referenceAxes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IVectorGeometryToolAxesFixed`

.. py:method:: sample(self, axes: IVectorGeometryToolAxes, referenceAxes: IVectorGeometryToolAxes, intervals: list, minStep: float, maxStep: float, targetRate: typing.Any) -> ITimeToolAxesSamplingResult
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesCommonTasks.sample

    Compute and returns tabulated orientations and angular velocities of axes with respect to reference axes using specified sampling parameters.

    :Parameters:

    **axes** : :obj:`~IVectorGeometryToolAxes`
    **referenceAxes** : :obj:`~IVectorGeometryToolAxes`
    **intervals** : :obj:`~list`
    **minStep** : :obj:`~float`
    **maxStep** : :obj:`~float`
    **targetRate** : :obj:`~typing.Any`

    :Returns:

        :obj:`~ITimeToolAxesSamplingResult`

