VectorGeometryToolPointLagrangeLibration
========================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

.. py:currentmodule:: VectorGeometryToolPointLagrangeLibration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration.point_type`
              - Specify a lagrange point (L1, L2, etc.).
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration.secondary_central_bodies`
              - Specify multiple secondary central bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointLagrangeLibration


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration.central_body
    :type: AnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: point_type
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration.point_type
    :type: CRDN_LAGRANGE_LIBRATION_POINT_TYPE

    Specify a lagrange point (L1, L2, etc.).

.. py:property:: secondary_central_bodies
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointLagrangeLibration.secondary_central_bodies
    :type: AnalysisWorkbenchCentralBodyCollection

    Specify multiple secondary central bodies.


