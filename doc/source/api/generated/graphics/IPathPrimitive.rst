IPathPrimitive
==============

.. py:class:: IPathPrimitive

   object
   
   Render a line to the 3D scene. Similar to the polyline primitive; however, the PathPrimitive was designed for the efficient addition/removal of points to/from the front or back of the line.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~item`
              - Return the point at the given zero-based index.
            * - :py:meth:`~add_front`
              - Add a path point to the front of the line.
            * - :py:meth:`~add_range_to_front`
              - Add the range of path points to the front of the line.
            * - :py:meth:`~add_back`
              - Add a path point to the back of the line.
            * - :py:meth:`~add_range_to_back`
              - Add the range of path points to the back of the line.
            * - :py:meth:`~remove_front`
              - Remove a path point to the front of the line.
            * - :py:meth:`~remove_all_before`
              - Remove all points before index.
            * - :py:meth:`~remove_back`
              - Remove a path point to the back of the line.
            * - :py:meth:`~remove_all_after`
              - Remove all points after index.
            * - :py:meth:`~front`
              - Access the path point at the front of the line.
            * - :py:meth:`~back`
              - Access the path point at the back of the line.
            * - :py:meth:`~clear`
              - Remove all of the points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~count`
            * - :py:meth:`~capacity`
            * - :py:meth:`~update_policy`
            * - :py:meth:`~polyline_type`
            * - :py:meth:`~width`
            * - :py:meth:`~minimum_width_supported`
            * - :py:meth:`~maximum_width_supported`
            * - :py:meth:`~display_outline`
            * - :py:meth:`~outline_width`
            * - :py:meth:`~per_item_picking_enabled`
            * - :py:meth:`~_NewEnum`
            * - :py:meth:`~central_body_clipped`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPathPrimitive


Property detail
---------------

.. py:property:: count
    :canonical: ansys.stk.core.graphics.IPathPrimitive.count
    :type: int

    Returns the number of points.

.. py:property:: capacity
    :canonical: ansys.stk.core.graphics.IPathPrimitive.capacity
    :type: int

    Returns the capacity that was set during object construction. The capacity is the amount of memory reserved for storing the points on the path. This will be automatically updated when adding/removing points.

.. py:property:: update_policy
    :canonical: ansys.stk.core.graphics.IPathPrimitive.update_policy
    :type: "IAgStkGraphicsPathPrimitiveUpdatePolicy"

    Gets or sets how the primitive will be updated based on the current animation time.

.. py:property:: polyline_type
    :canonical: ansys.stk.core.graphics.IPathPrimitive.polyline_type
    :type: "POLYLINE_TYPE"

    Gets or sets how the primitive interprets the positions.

.. py:property:: width
    :canonical: ansys.stk.core.graphics.IPathPrimitive.width
    :type: float

    Gets or sets the line width, in pixels.

.. py:property:: minimum_width_supported
    :canonical: ansys.stk.core.graphics.IPathPrimitive.minimum_width_supported
    :type: float

    Gets the minimum width, in pixels, supported by the video card.

.. py:property:: maximum_width_supported
    :canonical: ansys.stk.core.graphics.IPathPrimitive.maximum_width_supported
    :type: float

    Gets the maximum width, in pixels, supported by the video card.

.. py:property:: display_outline
    :canonical: ansys.stk.core.graphics.IPathPrimitive.display_outline
    :type: bool

    Gets or sets whether an outline is rendered around the line.

.. py:property:: outline_width
    :canonical: ansys.stk.core.graphics.IPathPrimitive.outline_width
    :type: float

    Gets or sets the width, in pixels, of the outline around the line.

.. py:property:: per_item_picking_enabled
    :canonical: ansys.stk.core.graphics.IPathPrimitive.per_item_picking_enabled
    :type: bool

    Gets or sets whether individual line indices will be included in the pick results returned from the scene's Pick method. Each line index that is picked will be returned as a batch primitive index.

.. py:property:: _NewEnum
    :canonical: ansys.stk.core.graphics.IPathPrimitive._NewEnum
    :type: EnumeratorProxy

    Returns an enumerator that iterates through the collection.

.. py:property:: central_body_clipped
    :canonical: ansys.stk.core.graphics.IPathPrimitive.central_body_clipped
    :type: bool

    Gets or sets whether the polyline will be clipped by the central body.


Method detail
-------------

















.. py:method:: item(self, index:int) -> "IPathPoint"

    Return the point at the given zero-based index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~"IPathPoint"`


.. py:method:: add_front(self, pathPoint:"IPathPoint") -> None

    Add a path point to the front of the line.

    :Parameters:

    **pathPoint** : :obj:`~"IPathPoint"`

    :Returns:

        :obj:`~None`

.. py:method:: add_range_to_front(self, positions:list) -> None

    Add the range of path points to the front of the line.

    :Parameters:

    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: add_back(self, pathPoint:"IPathPoint") -> None

    Add a path point to the back of the line.

    :Parameters:

    **pathPoint** : :obj:`~"IPathPoint"`

    :Returns:

        :obj:`~None`

.. py:method:: add_range_to_back(self, positions:list) -> None

    Add the range of path points to the back of the line.

    :Parameters:

    **positions** : :obj:`~list`

    :Returns:

        :obj:`~None`

.. py:method:: remove_front(self) -> None

    Remove a path point to the front of the line.

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_before(self, index:int) -> None

    Remove all points before index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: remove_back(self) -> None

    Remove a path point to the back of the line.

    :Returns:

        :obj:`~None`

.. py:method:: remove_all_after(self, index:int) -> None

    Remove all points after index.

    :Parameters:

    **index** : :obj:`~int`

    :Returns:

        :obj:`~None`

.. py:method:: front(self) -> "IPathPoint"

    Access the path point at the front of the line.

    :Returns:

        :obj:`~"IPathPoint"`

.. py:method:: back(self) -> "IPathPoint"

    Access the path point at the back of the line.

    :Returns:

        :obj:`~"IPathPoint"`

.. py:method:: clear(self) -> None

    Remove all of the points.

    :Returns:

        :obj:`~None`



