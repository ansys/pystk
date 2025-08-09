PointType
=========

.. py:class:: ansys.stk.core.analysis_workbench.PointType

   IntEnum


.. py:currentmodule:: PointType

Overview
--------

.. tab-set::

    .. tab-item:: Members

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~UNKNOWN`
              - Unknown or unsupported type.

            * - :py:attr:`~B_PLANE`
              - B-Plane point using the selected target body.

            * - :py:attr:`~GRAZING`
              - The grazing point is the point of closest approach to the surface of the selected central body along a defined direction.

            * - :py:attr:`~COVARIANCE_GRAZING`
              - The point of closest approach to the surface of the specified position covariance ellipsoid surface along a defined direction. Position covariance must be available for a vehicle object to be considered a possible target for this option.

            * - :py:attr:`~FIXED_IN_SYSTEM`
              - Point fixed in a reference coordinate system.

            * - :py:attr:`~GLINT`
              - Point on central body surface that reflects from source to observer.

            * - :py:attr:`~PLANE_INTERSECTION`
              - Point on a plane located along a given direction looking from a given origin.

            * - :py:attr:`~MODEL_ATTACHMENT`
              - Point placed at the specified attachment point of the object's 3D model. The point follows the model as well as any articulations that affect the specified attachment point.

            * - :py:attr:`~PLANE_PROJECTION`
              - The projection of a point onto a reference plane.

            * - :py:attr:`~ON_SURFACE`
              - The detic subpoint of the reference point as projected onto the central body.

            * - :py:attr:`~LAGRANGE_LIBRATION`
              - Libration point using one primary and multiple secondary central bodies.

            * - :py:attr:`~TEMPLATE`
              - Represents a VGT point created from a template. This type of point is not creatable.

            * - :py:attr:`~CENTRAL_BODY_INTERSECTION`
              - Point on central body surface along direction vector originating at source point.

            * - :py:attr:`~AT_TIME_INSTANT`
              - Point fixed relative to reference system based on another point evaluated at specified time instant.

            * - :py:attr:`~PLUGIN`
              - A point plugin point.

            * - :py:attr:`~FILE`
              - Point specified by data from a file.

            * - :py:attr:`~FIXED_ON_CENTRAL_BODY`
              - Point fixed on a central body.

            * - :py:attr:`~SATELLITE_COLLECTION_ENTRY`
              - A point placed at the center of mass of a specified satellite of the satellite collection.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.analysis_workbench import PointType


