VectorGeometryToolPointCovarianceGrazing
========================================

.. py:class:: ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing

   Bases: :py:class:`~ansys.stk.core.vgt.IVectorGeometryToolPoint`, :py:class:`~ansys.stk.core.vgt.ITimeToolTimeProperties`, :py:class:`~ansys.stk.core.vgt.IAnalysisWorkbenchComponent`

   The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

.. py:currentmodule:: VectorGeometryToolPointCovarianceGrazing

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.reference_point`
              - Specify a reference point which will serve as the starting location for the line along which the grazing point will be computed.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.direction_vector`
              - Specify a direction vector to be used in conjunction with the displacement vector from the selected target object to the reference point to define a plane in which the line will lie.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.target_name`
              - Specify a target object about which the covariance ellipsoid is centered.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.distance`
              - The point of closest approach to the covariance ellipsoid surface occurs at the specified distance.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.probability`
              - Specify a probability that the true position is inside the ellipsoid boundary.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.scale`
              - Specify a scale factor which is applied to the one sigma ellipsoid.
            * - :py:attr:`~ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.use_probability`
              - A flag controlling whether to use probability or scale factor.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VectorGeometryToolPointCovarianceGrazing


Property detail
---------------

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.reference_point
    :type: VectorGeometryToolPointRefTo

    Specify a reference point which will serve as the starting location for the line along which the grazing point will be computed.

.. py:property:: direction_vector
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.direction_vector
    :type: VectorGeometryToolVectorRefTo

    Specify a direction vector to be used in conjunction with the displacement vector from the selected target object to the reference point to define a plane in which the line will lie.

.. py:property:: target_name
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.target_name
    :type: str

    Specify a target object about which the covariance ellipsoid is centered.

.. py:property:: distance
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.distance
    :type: float

    The point of closest approach to the covariance ellipsoid surface occurs at the specified distance.

.. py:property:: probability
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.probability
    :type: float

    Specify a probability that the true position is inside the ellipsoid boundary.

.. py:property:: scale
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.scale
    :type: float

    Specify a scale factor which is applied to the one sigma ellipsoid.

.. py:property:: use_probability
    :canonical: ansys.stk.core.vgt.VectorGeometryToolPointCovarianceGrazing.use_probability
    :type: bool

    A flag controlling whether to use probability or scale factor.


