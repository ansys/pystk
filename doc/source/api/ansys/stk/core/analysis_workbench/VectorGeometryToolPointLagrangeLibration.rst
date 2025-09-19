VectorGeometryToolPointLagrangeLibration
========================================

.. py:class:: ansys.stk.core.analysis_workbench.VectorGeometryToolPointLagrangeLibration

   Bases: :py:class:`~ansys.stk.core.analysis_workbench.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.analysis_workbench.IAnalysisWorkbenchComponent`

   Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

.. py:currentmodule:: VectorGeometryToolPointLagrangeLibration

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointLagrangeLibration.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointLagrangeLibration.point_type`
              - Specify a lagrange point (L1, L2, etc.).
            * - :py:attr:`~ansys.stk.core.analysis_workbench.VectorGeometryToolPointLagrangeLibration.secondary_central_bodies`
              - Specify multiple secondary central bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import VectorGeometryToolPointLagrangeLibration


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointLagrangeLibration.central_body
    :type: AnalysisWorkbenchCentralBodyReference

    Specify a central body.

.. py:property:: point_type
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointLagrangeLibration.point_type
    :type: LagrangeLibrationPointType

    Specify a lagrange point (L1, L2, etc.).

.. py:property:: secondary_central_bodies
    :canonical: ansys.stk.core.analysis_workbench.VectorGeometryToolPointLagrangeLibration.secondary_central_bodies
    :type: AnalysisWorkbenchCentralBodyCollection

    Specify multiple secondary central bodies.


