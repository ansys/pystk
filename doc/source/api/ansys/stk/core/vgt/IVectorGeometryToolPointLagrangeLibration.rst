IVectorGeometryToolPointLagrangeLibration
=========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration

   object
   
   Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

.. py:currentmodule:: IVectorGeometryToolPointLagrangeLibration

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.point_type`
              - Specify a lagrange point (L1, L2, etc.).
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.secondary_central_bodies`
              - Specify multiple secondary central bodies.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointLagrangeLibration


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: point_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.point_type
    :type: CRDN_LAGRANGE_LIBRATION_POINT_TYPE

    Specify a lagrange point (L1, L2, etc.).

.. py:property:: secondary_central_bodies
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.secondary_central_bodies
    :type: IAnalysisWorkbenchCentralBodyCollection

    Specify multiple secondary central bodies.


