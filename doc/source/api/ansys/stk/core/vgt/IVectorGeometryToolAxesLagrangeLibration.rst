IVectorGeometryToolAxesLagrangeLibration
========================================

.. py:class:: IVectorGeometryToolAxesLagrangeLibration

   object
   
   Libration point axes using one primary and multiple secondary central bodies. Set primary and secondary bodies, and point type.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~primary_central_body`
            * - :py:meth:`~point_type`
            * - :py:meth:`~secondary_central_bodies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesLagrangeLibration


Property detail
---------------

.. py:property:: primary_central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesLagrangeLibration.primary_central_body
    :type: IAgCrdnCentralBodyRefTo

    Specify a primary central body.

.. py:property:: point_type
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesLagrangeLibration.point_type
    :type: CRDN_LAGRANGE_LIBRATION_POINT_TYPE

    Specify a lagrange point (L1, L2, etc.).

.. py:property:: secondary_central_bodies
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesLagrangeLibration.secondary_central_bodies
    :type: IAgCrdnCentralBodyCollection

    Specify secondary central bodies.


