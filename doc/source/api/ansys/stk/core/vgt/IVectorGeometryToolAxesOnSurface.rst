IVectorGeometryToolAxesOnSurface
================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolAxesOnSurface

   object
   
   Topocentric axes located at the reference point's projection on the central body.

.. py:currentmodule:: IVectorGeometryToolAxesOnSurface

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesOnSurface.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesOnSurface.reference_point`
              - Specify a reference point.
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolAxesOnSurface.use_msl`
              - Specify whether the reference shape is at the Mean Sea Level.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolAxesOnSurface


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesOnSurface.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesOnSurface.reference_point
    :type: IVectorGeometryToolPointRefTo

    Specify a reference point.

.. py:property:: use_msl
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolAxesOnSurface.use_msl
    :type: bool

    Specify whether the reference shape is at the Mean Sea Level.


