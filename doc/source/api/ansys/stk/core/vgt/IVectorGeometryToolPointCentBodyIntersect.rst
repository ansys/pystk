IVectorGeometryToolPointCentBodyIntersect
=========================================

.. py:class:: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect

   object
   
   Point on central body surface along direction vector originating at source point.

.. py:currentmodule:: IVectorGeometryToolPointCentBodyIntersect

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.set_range`
              - Set minimum and maximum range. An exception is thrown if Minimum exceeds Maximum. An exception is thrown if UseRangeConstraint is set to true. Applicable only if the range constraint is not used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.central_body`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.reference_point`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.direction_vector`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.intersection_surface`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.altitude`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.use_range_constraint`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.minimum_range`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.maximum_range`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.use_minimum_range`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.use_maximum_range`
            * - :py:attr:`~ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.allow_intersection_from_below`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointCentBodyIntersect


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.central_body
    :type: str

    Central body.

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.reference_point
    :type: IVectorGeometryToolPoint

    A reference point. Can be any point from VGT.

.. py:property:: direction_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.direction_vector
    :type: IVectorGeometryToolVector

    A direction vector. Can be any vector from VGT.

.. py:property:: intersection_surface
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.intersection_surface
    :type: CRDN_INTERSECTION_SURFACE

    An intersection surface.

.. py:property:: altitude
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.altitude
    :type: float

    An altitude.

.. py:property:: use_range_constraint
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.use_range_constraint
    :type: bool

    Whether to use range constraint.

.. py:property:: minimum_range
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.minimum_range
    :type: float

    A minimum range. An exception is thrown if the value exceeds the MaximumRange. Applicable only if the range constraint is not used.

.. py:property:: maximum_range
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.maximum_range
    :type: float

    A maximum range. An exception is thrown if the value is less than the MinimumRange. Applicable only if the range constraint is not used.

.. py:property:: use_minimum_range
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.use_minimum_range
    :type: bool

    Whether the minimum range is used. Applicable only if the range constraint is not used.

.. py:property:: use_maximum_range
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.use_maximum_range
    :type: bool

    Whether the maximum range is used. Applicable only if the range constraint is not used.

.. py:property:: allow_intersection_from_below
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.allow_intersection_from_below
    :type: bool

    Whether intersection is computed when reference point is inside the surface. Applicable when the surface is not defined by terrain.


Method detail
-------------





















.. py:method:: set_range(self, minimum: float, maximum: float) -> None
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCentBodyIntersect.set_range

    Set minimum and maximum range. An exception is thrown if Minimum exceeds Maximum. An exception is thrown if UseRangeConstraint is set to true. Applicable only if the range constraint is not used.

    :Parameters:

    **minimum** : :obj:`~float`
    **maximum** : :obj:`~float`

    :Returns:

        :obj:`~None`



