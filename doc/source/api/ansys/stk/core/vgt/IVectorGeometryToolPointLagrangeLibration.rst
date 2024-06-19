IVectorGeometryToolPointLagrangeLibration
=========================================

.. py:class:: IVectorGeometryToolPointLagrangeLibration

   object
   
   Libration point using one primary and multiple secondary central bodies. Set the central body, secondary central bodies, and point type.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~point_type`
            * - :py:meth:`~secondary_central_bodies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointLagrangeLibration


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.central_body
    :type: IAgCrdnCentralBodyRefTo

    Specify a central body.

.. py:property:: point_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.point_type
    :type: CRDN_LAGRANGE_LIBRATION_POINT_TYPE

    Specify a lagrange point (L1, L2, etc.).

.. py:property:: secondary_central_bodies
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointLagrangeLibration.secondary_central_bodies
    :type: IAgCrdnCentralBodyCollection

    Specify multiple secondary central bodies.


