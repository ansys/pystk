IVectorGeometryToolPlane
========================

.. py:class:: ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane

   The interface defines methods and properties common to all VGT planes.

.. py:currentmodule:: IVectorGeometryToolPlane

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.find_in_axes`
              - Compute the plane's axes vectors in a specified reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.find_in_axes_with_rate`
              - Compute the plane's axes vectors and their rates in a specified reference axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.find_in_system`
              - Compute the position and X and Y axes in the specified coordinate system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.find_in_system_with_rate`
              - Compute the position, X and Y axes and their rates of change in the specified coordinate system.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.type`
              - Return a type of the plane object.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.labels`
              - Allow configuring the plane's X and Y axes labels.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import IVectorGeometryToolPlane


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.type
    :type: PlaneType

    Return a type of the plane object.

.. py:property:: labels
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.labels
    :type: VectorGeometryToolPlaneLabels

    Allow configuring the plane's X and Y axes labels.


Method detail
-------------


.. py:method:: find_in_axes(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchPlaneFindInAxesResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.find_in_axes

    Compute the plane's axes vectors in a specified reference axes.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **axes** : :obj:`~IVectorGeometryToolAxes`


    :Returns:

        :obj:`~AnalysisWorkbenchPlaneFindInAxesResult`

.. py:method:: find_in_axes_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchPlaneFindInAxesWithRateResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.find_in_axes_with_rate

    Compute the plane's axes vectors and their rates in a specified reference axes.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **axes** : :obj:`~IVectorGeometryToolAxes`


    :Returns:

        :obj:`~AnalysisWorkbenchPlaneFindInAxesWithRateResult`

.. py:method:: find_in_system(self, epoch: typing.Any, system: IVectorGeometryToolSystem) -> AnalysisWorkbenchPlaneFindInSystemResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.find_in_system

    Compute the position and X and Y axes in the specified coordinate system.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **system** : :obj:`~IVectorGeometryToolSystem`


    :Returns:

        :obj:`~AnalysisWorkbenchPlaneFindInSystemResult`

.. py:method:: find_in_system_with_rate(self, epoch: typing.Any, system: IVectorGeometryToolSystem) -> AnalysisWorkbenchPlaneFindInSystemWithRateResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolPlane.find_in_system_with_rate

    Compute the position, X and Y axes and their rates of change in the specified coordinate system.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **system** : :obj:`~IVectorGeometryToolSystem`


    :Returns:

        :obj:`~AnalysisWorkbenchPlaneFindInSystemWithRateResult`


