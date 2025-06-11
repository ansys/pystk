VectorGeometryToolPointFixedInSystem
====================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFixedInSystem

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Point fixed in a reference coordinate system using the selected coordinate type.

.. py:currentmodule:: VectorGeometryToolPointFixedInSystem

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFixedInSystem.reference`
              - Specify a reference system.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointFixedInSystem.fixed_point`
              - Specify the point's position. The position is relative with respect to the specified reference system.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointFixedInSystem


Property detail
---------------

.. py:property:: reference
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFixedInSystem.reference
    :type: VectorGeometryToolSystemReference

    Specify a reference system.

.. py:property:: fixed_point
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointFixedInSystem.fixed_point
    :type: IPosition

    Specify the point's position. The position is relative with respect to the specified reference system.


