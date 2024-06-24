IVectorGeometryToolSystemOnSurface
==================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface

   object
   
   A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

.. py:currentmodule:: IVectorGeometryToolSystemOnSurface

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.central_body`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.azimuth_angle`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.use_msl`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.position`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemOnSurface


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: azimuth_angle
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.azimuth_angle
    :type: float

    An angle by which the topocentric axes is rotated.

.. py:property:: use_msl
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.use_msl
    :type: bool

    Specify whether to use the Mean Sea Level as the reference shape.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.position
    :type: IAnalysisWorkbenchLLAPosition

    Specify the position of the system's origin.


