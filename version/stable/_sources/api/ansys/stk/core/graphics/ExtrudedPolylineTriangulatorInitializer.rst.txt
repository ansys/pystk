ExtrudedPolylineTriangulatorInitializer
=======================================

.. py:class:: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer

   Triangulates a polyline into an extrusion with bottom and top boundaries.

.. py:currentmodule:: ExtrudedPolylineTriangulatorInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute`
              - Compute an extrusion between bottomPositions and topPositions on the specified centralBody. This is equivalent to calling Compute with a positionsWindingOrder of compute.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_with_winding_order`
              - Compute an extrusion between bottomPositions and topPositions on the specified centralBody.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_cartographic`
              - For convenience. Computes an extrusion between bottomPositions and topPositions on the specified centralBody using cartographic positions. This is equivalent to converting each position in bottomPositions and topPositions to cartesian and calling Compute.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_cartographic_with_winding_order`
              - For convenience. Computes an extrusion between bottomPositions and topPositions on the specified centralBody using cartographic positions. This is equivalent to converting each position in bottomPositions and topPositions to cartesian and calling Compute.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_with_altitudes`
              - Compute an extrusion of positions on the specified centralBody with a constant bottomAltitude and topAltitude. This is equivalent to calling Compute with a positionsWindingOrder of compute.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_with_altitudes_and_winding_order`
              - Compute an extrusion of positions on the specified centralBody with a constant bottomAltitude and topAltitude.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_cartographic_with_altitudes`
              - For convenience. Computes an extrusion of positions on the specified centralBody with a constant bottomAltitude and topAltitude using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_cartographic_with_altitudes_and_winding_order`
              - For convenience. Computes an extrusion of positions on the specified centralBody with a constant bottomAltitude and topAltitude using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_single_constant_altitude`
              - Compute an extrusion of positions on the specified centralBody. One side of the extrusion has a constant altitude and the other has the original altitudes from positions...
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_single_constant_altitude_with_winding_order`
              - Compute an extrusion of positions on the specified centralBody. One side of the extrusion has a constant altitude and the other has the original altitudes from positions.
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_single_constant_altitude_cartographic`
              - For convenience. Computes an extrusion of positions on the specified centralBody using cartographic positions. One side of the extrusion has a constant altitude and the other has the original altitudes from positions...
            * - :py:attr:`~ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_single_constant_altitude_cartographic_with_winding_order`
              - For convenience. Computes an extrusion of positions on the specified centralBody using cartographic positions. One side of the extrusion has a constant altitude and the other has the original altitudes from positions...


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ExtrudedPolylineTriangulatorInitializer



Method detail
-------------

.. py:method:: compute(self, central_body: str, bottom_positions: list, top_positions: list) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute

    Compute an extrusion between bottomPositions and topPositions on the specified centralBody. This is equivalent to calling Compute with a positionsWindingOrder of compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **bottom_positions** : :obj:`~list`

        **top_positions** : :obj:`~list`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_with_winding_order(self, central_body: str, bottom_positions: list, top_positions: list, positions_winding_order: WindingOrder) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_with_winding_order

    Compute an extrusion between bottomPositions and topPositions on the specified centralBody.

    :Parameters:

        **central_body** : :obj:`~str`

        **bottom_positions** : :obj:`~list`

        **top_positions** : :obj:`~list`

        **positions_winding_order** : :obj:`~WindingOrder`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_cartographic(self, central_body: str, bottom_positions: list, top_positions: list) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_cartographic

    For convenience. Computes an extrusion between bottomPositions and topPositions on the specified centralBody using cartographic positions. This is equivalent to converting each position in bottomPositions and topPositions to cartesian and calling Compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **bottom_positions** : :obj:`~list`

        **top_positions** : :obj:`~list`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_cartographic_with_winding_order(self, central_body: str, bottom_positions: list, top_positions: list, positions_winding_order: WindingOrder) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_cartographic_with_winding_order

    For convenience. Computes an extrusion between bottomPositions and topPositions on the specified centralBody using cartographic positions. This is equivalent to converting each position in bottomPositions and topPositions to cartesian and calling Compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **bottom_positions** : :obj:`~list`

        **top_positions** : :obj:`~list`

        **positions_winding_order** : :obj:`~WindingOrder`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_with_altitudes(self, central_body: str, positions: list, bottom_altitude: float, top_altitude: float) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_with_altitudes

    Compute an extrusion of positions on the specified centralBody with a constant bottomAltitude and topAltitude. This is equivalent to calling Compute with a positionsWindingOrder of compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **bottom_altitude** : :obj:`~float`

        **top_altitude** : :obj:`~float`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_with_altitudes_and_winding_order(self, central_body: str, positions: list, bottom_altitude: float, top_altitude: float, positions_winding_order: WindingOrder) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_with_altitudes_and_winding_order

    Compute an extrusion of positions on the specified centralBody with a constant bottomAltitude and topAltitude.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **bottom_altitude** : :obj:`~float`

        **top_altitude** : :obj:`~float`

        **positions_winding_order** : :obj:`~WindingOrder`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_cartographic_with_altitudes(self, central_body: str, positions: list, bottom_altitude: float, top_altitude: float) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_cartographic_with_altitudes

    For convenience. Computes an extrusion of positions on the specified centralBody with a constant bottomAltitude and topAltitude using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **bottom_altitude** : :obj:`~float`

        **top_altitude** : :obj:`~float`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_cartographic_with_altitudes_and_winding_order(self, central_body: str, positions: list, bottom_altitude: float, top_altitude: float, positions_winding_order: WindingOrder) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_cartographic_with_altitudes_and_winding_order

    For convenience. Computes an extrusion of positions on the specified centralBody with a constant bottomAltitude and topAltitude using cartographic positions. This is equivalent to converting each position in positions to cartesian and calling Compute.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **bottom_altitude** : :obj:`~float`

        **top_altitude** : :obj:`~float`

        **positions_winding_order** : :obj:`~WindingOrder`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_single_constant_altitude(self, central_body: str, positions: list, altitude: float) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_single_constant_altitude

    Compute an extrusion of positions on the specified centralBody. One side of the extrusion has a constant altitude and the other has the original altitudes from positions...

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **altitude** : :obj:`~float`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_single_constant_altitude_with_winding_order(self, central_body: str, positions: list, altitude: float, positions_winding_order: WindingOrder) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_single_constant_altitude_with_winding_order

    Compute an extrusion of positions on the specified centralBody. One side of the extrusion has a constant altitude and the other has the original altitudes from positions.

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **altitude** : :obj:`~float`

        **positions_winding_order** : :obj:`~WindingOrder`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_single_constant_altitude_cartographic(self, central_body: str, positions: list, altitude: float) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_single_constant_altitude_cartographic

    For convenience. Computes an extrusion of positions on the specified centralBody using cartographic positions. One side of the extrusion has a constant altitude and the other has the original altitudes from positions...

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **altitude** : :obj:`~float`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

.. py:method:: compute_single_constant_altitude_cartographic_with_winding_order(self, central_body: str, positions: list, altitude: float, positions_winding_order: WindingOrder) -> ExtrudedPolylineTriangulatorResult
    :canonical: ansys.stk.core.graphics.ExtrudedPolylineTriangulatorInitializer.compute_single_constant_altitude_cartographic_with_winding_order

    For convenience. Computes an extrusion of positions on the specified centralBody using cartographic positions. One side of the extrusion has a constant altitude and the other has the original altitudes from positions...

    :Parameters:

        **central_body** : :obj:`~str`

        **positions** : :obj:`~list`

        **altitude** : :obj:`~float`

        **positions_winding_order** : :obj:`~WindingOrder`


    :Returns:

        :obj:`~ExtrudedPolylineTriangulatorResult`

