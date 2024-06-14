IVectorGeometryToolSystemOnSurface
==================================

.. py:class:: IVectorGeometryToolSystemOnSurface

   object
   
   A system with an origin on the surface of the central body with topocentric axes rotated on a clock angle. Specify the central body, angle, and the latitude, longitude, and altitude of the origin.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~azimuth_angle`
            * - :py:meth:`~use_msl`
            * - :py:meth:`~position`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolSystemOnSurface


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolSystemOnSurface.central_body
    :type: "IAgCrdnCentralBodyRefTo"

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
    :type: "IAgCrdnLLAPosition"

    Specify the position of the system's origin.


