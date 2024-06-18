IVectorGeometryToolPointGrazing
===============================

.. py:class:: IVectorGeometryToolPointGrazing

   object
   
   The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~reference_point`
            * - :py:meth:`~direction_vector`
            * - :py:meth:`~altitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointGrazing


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGrazing.central_body
    :type: "IAgCrdnCentralBodyRefTo"

    Specify a central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGrazing.reference_point
    :type: "IAgCrdnPointRefTo"

    Specify a reference point which will serve as the starting location for the line along which the grazing point will be computed.

.. py:property:: direction_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGrazing.direction_vector
    :type: "IAgCrdnVectorRefTo"

    Specify a direction vector to be used in conjunction with the position vector from the selected central body to the reference point to define a plane in which the line will lie.

.. py:property:: altitude
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointGrazing.altitude
    :type: float

    The point of closest approach to the central body surface occurs at the specified altitude.


