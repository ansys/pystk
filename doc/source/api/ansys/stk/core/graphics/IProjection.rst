IProjection
===========

.. py:class:: ansys.stk.core.graphics.IProjection

   A projection represents a simplified camera with a position, orientation, and field of view horizontal and field of view vertical...

.. py:currentmodule:: IProjection

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IProjection.far_plane`
              - Get or set the far plane associated with the projection.
            * - :py:attr:`~ansys.stk.core.graphics.IProjection.field_of_view_horizontal`
              - Get or set the horizontal field of view associated with the projection.
            * - :py:attr:`~ansys.stk.core.graphics.IProjection.field_of_view_vertical`
              - Get or set the vertical field of view associated with the projection.
            * - :py:attr:`~ansys.stk.core.graphics.IProjection.near_plane`
              - Get or set the near plane associated with the projection.
            * - :py:attr:`~ansys.stk.core.graphics.IProjection.orientation`
              - Get or set the unit quaternion defining the orientation of the projection in the central body's fixed reference frame.
            * - :py:attr:`~ansys.stk.core.graphics.IProjection.position`
              - Get or set the cartesian defining the position of the projection in the central body's fixed reference frame. The array contains the components of the position arranged in the order x, y, z.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IProjection


Property detail
---------------

.. py:property:: far_plane
    :canonical: ansys.stk.core.graphics.IProjection.far_plane
    :type: float

    Get or set the far plane associated with the projection.

.. py:property:: field_of_view_horizontal
    :canonical: ansys.stk.core.graphics.IProjection.field_of_view_horizontal
    :type: float

    Get or set the horizontal field of view associated with the projection.

.. py:property:: field_of_view_vertical
    :canonical: ansys.stk.core.graphics.IProjection.field_of_view_vertical
    :type: float

    Get or set the vertical field of view associated with the projection.

.. py:property:: near_plane
    :canonical: ansys.stk.core.graphics.IProjection.near_plane
    :type: float

    Get or set the near plane associated with the projection.

.. py:property:: orientation
    :canonical: ansys.stk.core.graphics.IProjection.orientation
    :type: IOrientation

    Get or set the unit quaternion defining the orientation of the projection in the central body's fixed reference frame.

.. py:property:: position
    :canonical: ansys.stk.core.graphics.IProjection.position
    :type: list

    Get or set the cartesian defining the position of the projection in the central body's fixed reference frame. The array contains the components of the position arranged in the order x, y, z.


