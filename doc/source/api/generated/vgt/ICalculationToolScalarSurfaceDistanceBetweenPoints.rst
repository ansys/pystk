ICalculationToolScalarSurfaceDistanceBetweenPoints
==================================================

.. py:class:: ICalculationToolScalarSurfaceDistanceBetweenPoints

   object
   
   Surface distance along the specified central body ellipsoid between two points (or their respective projections if specified at altitude).

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~point1`
            * - :py:meth:`~point2`
            * - :py:meth:`~surface_central_body`
            * - :py:meth:`~differencing_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import ICalculationToolScalarSurfaceDistanceBetweenPoints


Property detail
---------------

.. py:property:: point1
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarSurfaceDistanceBetweenPoints.point1
    :type: "IAgCrdnPoint"

    Starting point on the central body ellipsoid (or projection of point at altitude onto the ellipsoid).

.. py:property:: point2
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarSurfaceDistanceBetweenPoints.point2
    :type: "IAgCrdnPoint"

    Terminating point on the central body ellipsoid (or projection of point at altitude onto the ellipsoid).

.. py:property:: surface_central_body
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarSurfaceDistanceBetweenPoints.surface_central_body
    :type: str

    Central body on which the surface distance between points is to be calculated.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.ICalculationToolScalarSurfaceDistanceBetweenPoints.differencing_time_step
    :type: float

    Time step used in numerical evaluation of scalar calculation time rate of change (derivatives using central differencing).


