PathPrimitive
=============

.. py:class:: ansys.stk.core.graphics.PathPrimitive

   Bases: :py:class:`~ansys.stk.core.graphics.IPrimitive`

   Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

.. py:currentmodule:: PathPrimitive

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.item`
              - Return the point at the given zero-based index.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.add_front`
              - Add a path point to the front of the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.add_range_to_front`
              - Add the range of path points to the front of the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.add_back`
              - Add a path point to the back of the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.add_range_to_back`
              - Add the range of path points to the back of the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.remove_front`
              - Remove a path point to the front of the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.remove_all_before`
              - Remove all points before index.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.remove_back`
              - Remove a path point to the back of the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.remove_all_after`
              - Remove all points after index.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.front`
              - Access the path point at the front of the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.back`
              - Access the path point at the back of the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.clear`
              - Remove all of the points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.count`
              - Returns the number of points.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.capacity`
              - Returns the capacity that was set during object construction. The capacity is the amount of memory reserved for storing the points on the path. This will be automatically updated when adding/removing points.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.update_policy`
              - Gets or sets how the primitive will be updated based on the current animation time.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.polyline_type`
              - Gets or sets how the primitive interprets the positions.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.width`
              - Gets or sets the line width, in pixels.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.minimum_width_supported`
              - Gets the minimum width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.maximum_width_supported`
              - Gets the maximum width, in pixels, supported by the video card.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.display_outline`
              - Gets or sets whether an outline is rendered around the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.outline_width`
              - Gets or sets the width, in pixels, of the outline around the line.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.per_item_picking_enabled`
              - Gets or sets whether individual line indices will be included in the pick results returned from the scene's Pick method. Each line index that is picked will be returned as a batch primitive index.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive._new_enum`
              - Returns an enumerator that iterates through the collection.
            * - :py:attr:`~ansys.stk.core.graphics.PathPrimitive.central_body_clipped`
              - Gets or sets whether the polyline will be clipped by the central body.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PathPrimitive


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.PathPrimitive.count
    :type: int

    Returns the number of points.

.. py:property:: capacity
    :canonical: ansys.stk.core.graphics.PathPrimitive.capacity
    :type: int

    Returns the capacity that was set during object construction. The capacity is the amount of memory reserved for storing the points on the path. This will be automatically updated when adding/removing points.

.. py:property:: update_policy
    :canonical: ansys.stk.core.graphics.PathPrimitive.update_policy
    :type: IPathPrimitiveUpdatePolicy

    Gets or sets how the primitive will be updated based on the current animation time.

.. py:property:: polyline_type
    :canonical: ansys.stk.core.graphics.PathPrimitive.polyline_type
    :type: PolylineType

    Gets or sets how the primitive interprets the positions.

.. py:property:: width
    :canonical: ansys.stk.core.graphics.PathPrimitive.width
    :type: float

    Gets or sets the line width, in pixels.

.. py:property:: minimum_width_supported
    :canonical: ansys.stk.core.graphics.PathPrimitive.minimum_width_supported
    :type: float

    Gets the minimum width, in pixels, supported by the video card.

.. py:property:: maximum_width_supported
    :canonical: ansys.stk.core.graphics.PathPrimitive.maximum_width_supported
    :type: float

    Gets the maximum width, in pixels, supported by the video card.

.. py:property:: display_outline
    :canonical: ansys.stk.core.graphics.PathPrimitive.display_outline
    :type: bool

    Gets or sets whether an outline is rendered around the line.

.. py:property:: outline_width
    :canonical: ansys.stk.core.graphics.PathPrimitive.outline_width
    :type: float

    Gets or sets the width, in pixels, of the outline around the line.

.. py:property:: per_item_picking_enabled
    :canonical: ansys.stk.core.graphics.PathPrimitive.per_item_picking_enabled
    :type: bool

    Gets or sets whether individual line indices will be included in the pick results returned from the scene's Pick method. Each line index that is picked will be returned as a batch primitive index.

.. py:property:: _new_enum
    :canonical: ansys.stk.core.graphics.PathPrimitive._new_enum
    :type: EnumeratorProxy

    Returns an enumerator that iterates through the collection.

.. py:property:: central_body_clipped
    :canonical: ansys.stk.core.graphics.PathPrimitive.central_body_clipped
    :type: bool

    Gets or sets whether the polyline will be clipped by the central body.


Method detail
-------------

















.. py:method:: item(self, index: int) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPrimitive.item

    Return the point at the given zero-based index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~PathPoint`


.. py:method:: add_front(self, path_point: PathPoint) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.add_front

    Add a path point to the front of the line.

    :Parameters:

    **path_point** : :obj:`~PathPoint`

    :Returns:

        :obj:`~None`

.. py:method:: add_range_to_front(self, positions: list) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.add_range_to_front

    Add the range of path points to the front of the line.

    :Parameters:

    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: add_back(self, path_point: PathPoint) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.add_back

    Add a path point to the back of the line.

    :Parameters:

    **path_point** : :obj:`~PathPoint`

    :Returns:

        :obj:`~None`

.. py:method:: add_range_to_back(self, positions: list) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.add_range_to_back

    Add the range of path points to the back of the line.

    :Parameters:

    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: remove_front(self) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.remove_front

    Remove a path point to the front of the line.

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_before(self, index: int) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.remove_all_before

    Remove all points before index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_back(self) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.remove_back

    Remove a path point to the back of the line.

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_after(self, index: int) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.remove_all_after

    Remove all points after index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: front(self) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPrimitive.front

    Access the path point at the front of the line.

    :Returns:

        :obj:`~PathPoint`

.. py:method:: back(self) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPrimitive.back

    Access the path point at the back of the line.

    :Returns:

        :obj:`~PathPoint`

.. py:method:: clear(self) -> None
    :canonical: ansys.stk.core.graphics.PathPrimitive.clear

    Remove all of the points.

    :Returns:

        :obj:`~None`



