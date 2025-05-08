IVectorGeometryToolAxes
=======================

.. py:class:: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes

   The interface defines methods and properties common to all axes.

.. py:currentmodule:: IVectorGeometryToolAxes

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.find_in_axes_with_rate`
              - Find an angular velocity and orientation in the specified axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.find_in_axes`
              - Find an orientation in the specified axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.transform`
              - Transform the input vector from this axes into the output axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.transform_with_rate`
              - Transform the input vector and vector's rate from this axes into the output axes.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.type`
              - Return a type of the axes object.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.labels`
              - Return an object that allows modifying the axes labels.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.x_axis`
              - Return the X axis of the component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.y_axis`
              - Return the Y axis of the component.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.z_axis`
              - Return the Z axis of the component.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import IVectorGeometryToolAxes


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.type
    :type: AxesType

    Return a type of the axes object.

.. py:property:: labels
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.labels
    :type: VectorGeometryToolAxesLabels

    Return an object that allows modifying the axes labels.

.. py:property:: x_axis
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.x_axis
    :type: IVectorGeometryToolVector

    Return the X axis of the component.

.. py:property:: y_axis
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.y_axis
    :type: IVectorGeometryToolVector

    Return the Y axis of the component.

.. py:property:: z_axis
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.z_axis
    :type: IVectorGeometryToolVector

    Return the Z axis of the component.


Method detail
-------------


.. py:method:: find_in_axes_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchAxesFindInAxesWithRateResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.find_in_axes_with_rate

    Find an angular velocity and orientation in the specified axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~AnalysisWorkbenchAxesFindInAxesWithRateResult`

.. py:method:: find_in_axes(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchAxesFindInAxesResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.find_in_axes

    Find an orientation in the specified axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **axes** : :obj:`~IVectorGeometryToolAxes`

    :Returns:

        :obj:`~AnalysisWorkbenchAxesFindInAxesResult`





.. py:method:: transform(self, epoch: typing.Any, output_axes: IVectorGeometryToolAxes, vector_in_my_axes: ICartesian3Vector) -> AnalysisWorkbenchAxesTransformResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.transform

    Transform the input vector from this axes into the output axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **output_axes** : :obj:`~IVectorGeometryToolAxes`
    **vector_in_my_axes** : :obj:`~ICartesian3Vector`

    :Returns:

        :obj:`~AnalysisWorkbenchAxesTransformResult`

.. py:method:: transform_with_rate(self, epoch: typing.Any, output_axes: IVectorGeometryToolAxes, vector_in_my_axes: ICartesian3Vector, rate_in_my_axes: ICartesian3Vector) -> AnalysisWorkbenchAxesTransformWithRateResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAxes.transform_with_rate

    Transform the input vector and vector's rate from this axes into the output axes.

    :Parameters:

    **epoch** : :obj:`~typing.Any`
    **output_axes** : :obj:`~IVectorGeometryToolAxes`
    **vector_in_my_axes** : :obj:`~ICartesian3Vector`
    **rate_in_my_axes** : :obj:`~ICartesian3Vector`

    :Returns:

        :obj:`~AnalysisWorkbenchAxesTransformWithRateResult`

