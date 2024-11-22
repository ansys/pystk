VECTOR_TYPE
===========

.. py:class:: ansys.stk.core.vgt.VECTOR_TYPE

   IntEnum


.. py:currentmodule:: VECTOR_TYPE

Overview
--------

.. tab-set::

    .. tab-item:: Members
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported vector type.

            * - :py:attr:`~DISPLACEMENT`
              - Vector defined by its start and end points.

            * - :py:attr:`~APOAPSIS`
              - Vector from the center of the specified central body to the farthest point of an elliptical orbit created from the motion of the specified point.

            * - :py:attr:`~FIXED_AT_EPOCH`
              - Based on another vector fixed at a specified epoch.

            * - :py:attr:`~ANGULAR_VELOCITY`
              - Angular velocity vector of one set of axes computed with respect to the reference set.

            * - :py:attr:`~CONING`
              - Vector created by revolving the Reference vector around the About vector with the specified rate. The vector is aligned with Reference vector at specified epoch. After that it revolves between start/stop angles using either uni- or bi-directional mode.

            * - :py:attr:`~CROSS_PRODUCT`
              - The vector cross product of two vectors.

            * - :py:attr:`~CUSTOM_SCRIPT`
              - Customized vector components defined with respect to reference axes.

            * - :py:attr:`~DERIVATIVE`
              - Derivative of a vector computed with respect to specified axes.

            * - :py:attr:`~ANGLE_RATE`
              - Angle rate vector perpendicular to the plane in which the angle is defined.

            * - :py:attr:`~ECCENTRICITY`
              - Vector directed from the center of the specified central body toward the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:attr:`~FIXED_IN_AXES`
              - Vector fixed in reference axes.

            * - :py:attr:`~TWO_PLANES_INTERSECTION`
              - Defined along the intersection of two planes.

            * - :py:attr:`~LINE_OF_NODES`
              - Unit vector along the line of nodes - the line of intersection of the osculating orbit plane and the inertial equator of the specified central body.

            * - :py:attr:`~MODEL_ATTACHMENT`
              - Unit vector along the specified pointable element of the object's 3D model. The vector's direction follows the model as well as any articulations that affect the specified pointable element.

            * - :py:attr:`~ORBIT_ANGULAR_MOMENTUM`
              - Vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:attr:`~ORBIT_NORMAL`
              - Unit vector perpendicular to the plane of an elliptical orbit created from the motion of the specified point with respect to the center of the specified central body.

            * - :py:attr:`~PERIAPSIS`
              - Vector from the center of the specified central body to the nearest point of an elliptical orbit created from the motion of the specified point.

            * - :py:attr:`~PROJECTION`
              - A projection of a vector computed with respect to a reference plane.

            * - :py:attr:`~REFLECTION`
              - Incident vector reflected using a plane whose normal is the normal vector, scaled by a factor. The selected vector or its opposite can be reflected on just one or on both sides of the plane.

            * - :py:attr:`~SCALED`
              - Scaled version of the input vector.

            * - :py:attr:`~DIRECTION_TO_STAR`
              - Defined with respect to a star object.

            * - :py:attr:`~TEMPLATE`
              - Represents a VGT vector created from a template. This type of vector is not creatable.

            * - :py:attr:`~AT_TIME_INSTANT`
              - Vector fixed relative to reference axes based on another vector evaluated at specified time instant.

            * - :py:attr:`~LINEAR_COMBINATION`
              - Linear combination of two input vectors.

            * - :py:attr:`~PROJECT_ALONG`
              - A projection of a source vector in the direction of another vector.

            * - :py:attr:`~SCALAR_LINEAR_COMBINATION`
              - Linear combination of two input vectors using scalars.

            * - :py:attr:`~SCALAR_SCALED`
              - Scaled version of the input vector using scalar.

            * - :py:attr:`~VELOCITY`
              - Velocity vector of a point in a coordinate system.

            * - :py:attr:`~PLUGIN`
              - A vector plugin point.

            * - :py:attr:`~ROTATION_VECTOR`
              - Rotation vector representing the rotation of one axes relative to reference axes, expressed as angle*rotationAxis.

            * - :py:attr:`~DISPLACEMENT_ON_SURFACE`
              - Displacement between origin and destination points using surface distance and altitude difference.

            * - :py:attr:`~FILE`
              - Vector interpolated from tabulated data from file.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.vgt import VECTOR_TYPE


