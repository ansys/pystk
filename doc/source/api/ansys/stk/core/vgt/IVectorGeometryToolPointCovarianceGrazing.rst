IVectorGeometryToolPointCovarianceGrazing
=========================================

.. py:class:: IVectorGeometryToolPointCovarianceGrazing

   object
   
   The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

.. py:currentmodule:: ansys.stk.core.vgt

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~reference_point`
            * - :py:meth:`~direction_vector`
            * - :py:meth:`~target_name`
            * - :py:meth:`~distance`
            * - :py:meth:`~probability`
            * - :py:meth:`~scale`
            * - :py:meth:`~use_probability`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import IVectorGeometryToolPointCovarianceGrazing


Property detail
---------------

.. py:property:: reference_point
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCovarianceGrazing.reference_point
    :type: "IAgCrdnPointRefTo"

    Specify a reference point which will serve as the starting location for the line along which the grazing point will be computed.

.. py:property:: direction_vector
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCovarianceGrazing.direction_vector
    :type: "IAgCrdnVectorRefTo"

    Specify a direction vector to be used in conjunction with the displacement vector from the selected target object to the reference point to define a plane in which the line will lie.

.. py:property:: target_name
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCovarianceGrazing.target_name
    :type: str

    Specify a target object about which the covariance ellipsoid is centered.

.. py:property:: distance
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCovarianceGrazing.distance
    :type: float

    The point of closest approach to the covariance ellipsoid surface occurs at the specified distance.

.. py:property:: probability
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCovarianceGrazing.probability
    :type: float

    Specify a probability that the true position is inside the ellipsoid boundary.

.. py:property:: scale
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCovarianceGrazing.scale
    :type: float

    Specify a scale factor which is applied to the one sigma ellipsoid.

.. py:property:: use_probability
    :canonical: ansys.stk.core.vgt.IVectorGeometryToolPointCovarianceGrazing.use_probability
    :type: bool

    A flag controlling whether to use probability or scale factor.


