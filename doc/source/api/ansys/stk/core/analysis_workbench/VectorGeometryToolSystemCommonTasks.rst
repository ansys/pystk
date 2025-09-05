VectorGeometryToolSystemCommonTasks
===================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolSystemCommonTasks

   Provide methods to create non-persistent VGT coordinate reference frames (systems). Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

.. py:currentmodule:: VectorGeometryToolSystemCommonTasks

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemCommonTasks.create_assembled`
              - Create a non-persistent system component assembled from an origin point and a set of reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolSystemCommonTasks.create_east_north_up_cartographic`
              - Create a non-persistent East-North-Up (ENU) reference frame with the origin at the specified geodetic location.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolSystemCommonTasks



Method detail
-------------

.. py:method:: create_assembled(self, origin_point: IVectorGeometryToolPoint, reference_axes: IVectorGeometryToolAxes) -> VectorGeometryToolSystemAssembled
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolSystemCommonTasks.create_assembled

    Create a non-persistent system component assembled from an origin point and a set of reference axes.

    :Parameters:

        **origin_point** : :obj:`~IVectorGeometryToolPoint`

        **reference_axes** : :obj:`~IVectorGeometryToolAxes`


    :Returns:

        :obj:`~VectorGeometryToolSystemAssembled`

.. py:method:: create_east_north_up_cartographic(self, latitude: typing.Any, longitude: typing.Any, altitude: float) -> VectorGeometryToolSystemAssembled
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolSystemCommonTasks.create_east_north_up_cartographic

    Create a non-persistent East-North-Up (ENU) reference frame with the origin at the specified geodetic location.

    :Parameters:

        **latitude** : :obj:`~typing.Any`

        **longitude** : :obj:`~typing.Any`

        **altitude** : :obj:`~float`


    :Returns:

        :obj:`~VectorGeometryToolSystemAssembled`

