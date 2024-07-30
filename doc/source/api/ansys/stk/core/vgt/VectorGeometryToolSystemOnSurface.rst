VectorGeometryToolSystemOnSurface
=================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolSystem`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

.. py:currentmodule:: VectorGeometryToolSystemOnSurface

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface.central_body`
              - Specify a central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface.azimuth_angle`
              - An angle by which the topocentric axes is rotated.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface.use_msl`
              - Specify whether to use the Mean Sea Level as the reference shape.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface.position`
              - Specify the position of the system's origin.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolSystemOnSurface


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface.central_body
    :type: IAnalysisWorkbenchCentralBodyRefTo

    Specify a central body.

.. py:property:: azimuth_angle
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface.azimuth_angle
    :type: float

    An angle by which the topocentric axes is rotated.

.. py:property:: use_msl
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface.use_msl
    :type: bool

    Specify whether to use the Mean Sea Level as the reference shape.

.. py:property:: position
    :canonical: ansys.stk.core.vgt.VectorGeometryToolSystemOnSurface.position
    :type: IAnalysisWorkbenchLLAPosition

    Specify the position of the system's origin.


