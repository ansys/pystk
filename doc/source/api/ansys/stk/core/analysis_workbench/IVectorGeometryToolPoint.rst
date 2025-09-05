IVectorGeometryToolPoint
========================

.. py:class:: ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint

   The interface defines methods and properties common to all points.

.. py:currentmodule:: IVectorGeometryToolPoint

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint.locate_in_system`
              - Locates the point's position in a specified coordinate system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint.locate_in_system_with_rate`
              - Locates the point's position and velocity in a specified coordinate system.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint.type`
              - Return a type of the point object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import IVectorGeometryToolPoint


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint.type
    :type: PointType

    Return a type of the point object.


Method detail
-------------

.. py:method:: locate_in_system(self, epoch: typing.Any, system: IVectorGeometryToolSystem) -> AnalysisWorkbenchPointLocateInSystemResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint.locate_in_system

    Locates the point's position in a specified coordinate system.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **system** : :obj:`~IVectorGeometryToolSystem`


    :Returns:

        :obj:`~AnalysisWorkbenchPointLocateInSystemResult`

.. py:method:: locate_in_system_with_rate(self, epoch: typing.Any, system: IVectorGeometryToolSystem) -> AnalysisWorkbenchPointLocateInSystemWithRateResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint.locate_in_system_with_rate

    Locates the point's position and velocity in a specified coordinate system.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **system** : :obj:`~IVectorGeometryToolSystem`


    :Returns:

        :obj:`~AnalysisWorkbenchPointLocateInSystemWithRateResult`


