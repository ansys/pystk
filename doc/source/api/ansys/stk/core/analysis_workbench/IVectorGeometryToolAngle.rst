IVectorGeometryToolAngle
========================

.. py:class:: ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle

   The interface defines methods and properties common to all angles.

.. py:currentmodule:: IVectorGeometryToolAngle

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.find_angle`
              - Find an angle at the specified epoch.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.find_angle_with_rate`
              - Find an angle and angle rate.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.find_coordinates`
              - Find the angle value and three vectors that define the angle in a specified input axes.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.find_coordinates_with_rate`
              - Find the angle value, the angle rate and three vectors that define the angle in a specified input axes.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.type`
              - Return a type of the angle object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import IVectorGeometryToolAngle


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.type
    :type: AngleType

    Return a type of the angle object.


Method detail
-------------

.. py:method:: find_angle(self, epoch: typing.Any) -> AnalysisWorkbenchAngleFindAngleResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.find_angle

    Find an angle at the specified epoch.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~AnalysisWorkbenchAngleFindAngleResult`

.. py:method:: find_angle_with_rate(self, epoch: typing.Any) -> AnalysisWorkbenchAngleFindAngleWithRateResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.find_angle_with_rate

    Find an angle and angle rate.

    :Parameters:

        **epoch** : :obj:`~typing.Any`


    :Returns:

        :obj:`~AnalysisWorkbenchAngleFindAngleWithRateResult`

.. py:method:: find_coordinates(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchAngleFindResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.find_coordinates

    Find the angle value and three vectors that define the angle in a specified input axes.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **axes** : :obj:`~IVectorGeometryToolAxes`


    :Returns:

        :obj:`~AnalysisWorkbenchAngleFindResult`

.. py:method:: find_coordinates_with_rate(self, epoch: typing.Any, axes: IVectorGeometryToolAxes) -> AnalysisWorkbenchAngleFindWithRateResult
    :canonical: ansys.stk.core.analysis_workbench.IVectorGeometryToolAngle.find_coordinates_with_rate

    Find the angle value, the angle rate and three vectors that define the angle in a specified input axes.

    :Parameters:

        **epoch** : :obj:`~typing.Any`

        **axes** : :obj:`~IVectorGeometryToolAxes`


    :Returns:

        :obj:`~AnalysisWorkbenchAngleFindWithRateResult`


