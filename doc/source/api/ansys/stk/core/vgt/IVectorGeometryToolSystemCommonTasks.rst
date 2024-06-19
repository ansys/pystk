IVectorGeometryToolSystemCommonTasks
====================================

.. py:class:: IVectorGeometryToolSystemCommonTasks

   object
   
   Provide methods to create non-persistent VGT coordinate reference frames (systems). Non-persistent components do not have names, do not get saved/loaded and are not shown in the VGT browser.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~create_east_north_up_cartographic`
              - Create a non-persistent East-North-Up (ENU) reference frame with the origin at the specified geodetic location.
            * - :py:meth:`~create_assembled`
              - Create a non-persistent system component assembled from an origin point and a set of reference axes.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemCommonTasks



Method detail
-------------

.. py:method:: create_east_north_up_cartographic(self, latitude: typing.Any, longitude: typing.Any, altitude: float) -> IVectorGeometryToolSystemAssembled
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemCommonTasks.create_east_north_up_cartographic

    Create a non-persistent East-North-Up (ENU) reference frame with the origin at the specified geodetic location.

    :Parameters:

    **latitude** : :obj:`~typing.Any`
    **longitude** : :obj:`~typing.Any`
    **altitude** : :obj:`~float`

    :Returns:

        :obj:`~IVectorGeometryToolSystemAssembled`

.. py:method:: create_assembled(self, originPoint: IVectorGeometryToolPoint, referenceAxes: IVectorGeometryToolAxes) -> IVectorGeometryToolSystemAssembled
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemCommonTasks.create_assembled

    Create a non-persistent system component assembled from an origin point and a set of reference axes.

    :Parameters:

    **originPoint** : :obj:`~IVectorGeometryToolPoint`
    **referenceAxes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~IVectorGeometryToolSystemAssembled`

