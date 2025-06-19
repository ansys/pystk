VectorGeometryToolVectorDisplacement
====================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolVector`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Vector defined by its start and end points.

.. py:currentmodule:: VectorGeometryToolVectorDisplacement

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.origin`
              - Specify the vector's origin point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.destination`
              - Specify the vector's destination point.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.apparent`
              - Control whether to take a light speed delay into account.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.ignore_aberration`
              - Set to true if you do not want to calculate the aberration correction. This property is read-only if Apparent is set to false.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.signal_sense`
              - Specify a sense of signal transmission. This property is read-only if Apparent is set to false.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.reference_system`
              - Specify a frame in which the light time delay is computed. This property is read-only if Apparent is set to false.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolVectorDisplacement


Property detail
---------------

.. py:property:: origin
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.origin
    :type: VectorGeometryToolPointReference

    Specify the vector's origin point.

.. py:property:: destination
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.destination
    :type: VectorGeometryToolPointReference

    Specify the vector's destination point.

.. py:property:: apparent
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.apparent
    :type: bool

    Control whether to take a light speed delay into account.

.. py:property:: ignore_aberration
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.ignore_aberration
    :type: bool

    Set to true if you do not want to calculate the aberration correction. This property is read-only if Apparent is set to false.

.. py:property:: signal_sense
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.signal_sense
    :type: SignalDirectionType

    Specify a sense of signal transmission. This property is read-only if Apparent is set to false.

.. py:property:: reference_system
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolVectorDisplacement.reference_system
    :type: VectorGeometryToolSystemReference

    Specify a frame in which the light time delay is computed. This property is read-only if Apparent is set to false.


