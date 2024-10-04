VectorGeometryToolPointCentralBodyIntersect
===========================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect

   Bases: :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponentTimeProperties`, :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`

   Point on central body surface along direction vector originating at source point.

.. py:currentmodule:: VectorGeometryToolPointCentralBodyIntersect

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.set_range`
              - Set minimum and maximum range. An exception is thrown if Minimum exceeds Maximum. An exception is thrown if UseRangeConstraint is set to true. Applicable only if the range constraint is not used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.central_body`
              - Central body.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.reference_point`
              - A reference point. Can be any point from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.direction_vector`
              - A direction vector. Can be any vector from VGT.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.intersection_surface`
              - An intersection surface.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.altitude`
              - An altitude.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.use_range_constraint`
              - Whether to use range constraint.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.minimum_range`
              - A minimum range. An exception is thrown if the value exceeds the MaximumRange. Applicable only if the range constraint is not used.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.maximum_range`
              - A maximum range. An exception is thrown if the value is less than the MinimumRange. Applicable only if the range constraint is not used.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.use_minimum_range`
              - Whether the minimum range is used. Applicable only if the range constraint is not used.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.use_maximum_range`
              - Whether the maximum range is used. Applicable only if the range constraint is not used.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.allow_intersection_from_below`
              - Whether intersection is computed when reference point is inside the surface. Applicable when the surface is not defined by terrain.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointCentralBodyIntersect


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.central_body
    :type: str

    Central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.reference_point
    :type: IVectorGeometryToolPoint

    A reference point. Can be any point from VGT.

.. py:property:: direction_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.direction_vector
    :type: IVectorGeometryToolVector

    A direction vector. Can be any vector from VGT.

.. py:property:: intersection_surface
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.intersection_surface
    :type: INTERSECTION_SURFACE_TYPE

    An intersection surface.

.. py:property:: altitude
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.altitude
    :type: float

    An altitude.

.. py:property:: use_range_constraint
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.use_range_constraint
    :type: bool

    Whether to use range constraint.

.. py:property:: minimum_range
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.minimum_range
    :type: float

    A minimum range. An exception is thrown if the value exceeds the MaximumRange. Applicable only if the range constraint is not used.

.. py:property:: maximum_range
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.maximum_range
    :type: float

    A maximum range. An exception is thrown if the value is less than the MinimumRange. Applicable only if the range constraint is not used.

.. py:property:: use_minimum_range
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.use_minimum_range
    :type: bool

    Whether the minimum range is used. Applicable only if the range constraint is not used.

.. py:property:: use_maximum_range
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.use_maximum_range
    :type: bool

    Whether the maximum range is used. Applicable only if the range constraint is not used.

.. py:property:: allow_intersection_from_below
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.allow_intersection_from_below
    :type: bool

    Whether intersection is computed when reference point is inside the surface. Applicable when the surface is not defined by terrain.


Method detail
-------------





















.. py:method:: set_range(self, minimum: float, maximum: float) -> None
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCentralBodyIntersect.set_range

    Set minimum and maximum range. An exception is thrown if Minimum exceeds Maximum. An exception is thrown if UseRangeConstraint is set to true. Applicable only if the range constraint is not used.

    :Parameters:

    **minimum** : :obj:`~float`
    **maximum** : :obj:`~float`

    :Returns:

        :obj:`~None`



