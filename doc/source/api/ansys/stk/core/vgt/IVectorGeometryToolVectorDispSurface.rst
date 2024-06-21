IVectorGeometryToolVectorDispSurface
====================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface

   object
   
   Displacement between origin and destination points using surface distance and altitude difference.

.. py:currentmodule:: IVectorGeometryToolVectorDispSurface

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface.origin_point`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface.destination_point`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface.surface_central_body`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface.differencing_time_step`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolVectorDispSurface


Property detail
---------------

.. py:property:: origin_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface.origin_point
    :type: IVectorGeometryToolPoint

    An origin point.

.. py:property:: destination_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface.destination_point
    :type: IVectorGeometryToolPoint

    Destination point.

.. py:property:: surface_central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface.surface_central_body
    :type: str

    Gets or sets the surface central body property.

.. py:property:: differencing_time_step
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolVectorDispSurface.differencing_time_step
    :type: float

    Time step used in displacement on surface vector. (derivatives using central differencing).


