ISurfacePolygonTriangulatorInitializer
======================================

.. py:class:: ISurfacePolygonTriangulatorInitializer

   object
   
   Triangulates a polygon, with an optional hole, on a central body, into a triangle mesh and a surrounding boundary. The mesh is commonly visualized with the triangle mesh primitive or surface mesh primitive...

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~compute`
              - Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions. This is equivalent to calling Compute with an altitude of 0, a granularity of 1 degree, and a positionsWindingOrder of compute.
            * - :py:meth:`~compute_cartographic`
              - For convenience. Computes the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.
            * - :py:meth:`~compute_with_hole`
              - Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions with a hole specified by holePositions. This is equivalent to calling Compute with an altitude of 0 and a granularity of 1 degree.
            * - :py:meth:`~compute_with_hole_altitude_and_granularity`
              - Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions with a hole specified by holePositions.
            * - :py:meth:`~compute_with_altitude_and_granularity`
              - Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions.
            * - :py:meth:`~compute_cartographic_with_altitude_and_granularity`
              - For convenience. Computes the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISurfacePolygonTriangulatorInitializer



Method detail
-------------

.. py:method:: compute(self, centralBody:str, positions:list) -> "ISurfaceTriangulatorResult"

    Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions. This is equivalent to calling Compute with an altitude of 0, a granularity of 1 degree, and a positionsWindingOrder of compute.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`

    :Returns:

        :obj:`~"ISurfaceTriangulatorResult"`

.. py:method:: compute_cartographic(self, centralBody:str, positions:list) -> "ISurfaceTriangulatorResult"

    For convenience. Computes the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`

    :Returns:

        :obj:`~"ISurfaceTriangulatorResult"`

.. py:method:: compute_with_hole(self, centralBody:str, positions:list, holePositions:list) -> "ISurfaceTriangulatorResult"

    Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions with a hole specified by holePositions. This is equivalent to calling Compute with an altitude of 0 and a granularity of 1 degree.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **holePositions** : :obj:`~list`

    :Returns:

        :obj:`~"ISurfaceTriangulatorResult"`

.. py:method:: compute_with_hole_altitude_and_granularity(self, centralBody:str, positions:list, holePositions:list, altitude:float, granularity:float) -> "ISurfaceTriangulatorResult"

    Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions with a hole specified by holePositions.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **holePositions** : :obj:`~list`
    **altitude** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~"ISurfaceTriangulatorResult"`

.. py:method:: compute_with_altitude_and_granularity(self, centralBody:str, positions:list, altitude:float, granularity:float, positionsWindingOrder:"WINDING_ORDER") -> "ISurfaceTriangulatorResult"

    Compute the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified positions.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **altitude** : :obj:`~float`
    **granularity** : :obj:`~float`
    **positionsWindingOrder** : :obj:`~"WINDING_ORDER"`

    :Returns:

        :obj:`~"ISurfaceTriangulatorResult"`

.. py:method:: compute_cartographic_with_altitude_and_granularity(self, centralBody:str, positions:list, altitude:float, granularity:float, positionsWindingOrder:"WINDING_ORDER") -> "ISurfaceTriangulatorResult"

    For convenience. Computes the triangulation on the specified centralBody for a polygon whose boundary is defined by the specified cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.

    :Parameters:

    **centralBody** : :obj:`~str`
    **positions** : :obj:`~list`
    **altitude** : :obj:`~float`
    **granularity** : :obj:`~float`
    **positionsWindingOrder** : :obj:`~"WINDING_ORDER"`

    :Returns:

        :obj:`~"ISurfaceTriangulatorResult"`

