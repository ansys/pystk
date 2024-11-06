SurfaceShapesInitializer
========================

.. py:class:: ansys.stk.core.graphics.SurfaceShapesInitializer

   Compute boundary positions for shapes on the surface such as circles, ellipses, and sectors.

.. py:currentmodule:: SurfaceShapesInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_circle_with_granularity`
              - Compute boundary positions for a circle on the specified centralBody with the specified center, radius and granularity.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_circle`
              - Compute boundary positions for a circle on the specified centralBody with the specified center and radius. This is equivalent to calling ComputeCircle with a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_circle_cartographic_with_granularity`
              - For convenience. Computes boundary positions for a circle on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeCircle.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_circle_cartographic`
              - For convenience. Computes boundary positions for a circle on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeCircle.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_ellipse_with_granularity`
              - Compute boundary positions for an ellipse on the specified centralBody.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_ellipse`
              - Compute boundary positions for an ellipse on the specified centralBody. This is equivalent to calling ComputeEllipse with a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_ellipse_cartographic_with_granularity`
              - For convenience. Computes boundary positions for an ellipse on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeEllipse.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_ellipse_cartographic`
              - For convenience. Computes boundary positions for an ellipse on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeEllipse.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_sector_with_granularity`
              - Compute boundary positions for a sector on the specified centralBody.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_sector`
              - Compute boundary positions for a sector on the specified centralBody. This is equivalent to calling ComputeSector with a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_sector_cartographic_with_granularity`
              - For convenience. Computes boundary positions for a sector on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeSector.
            * - :py:attr:`~ansys.stk.core.graphics.SurfaceShapesInitializer.compute_sector_cartographic`
              - For convenience. Computes boundary positions for a sector on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeSector.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import SurfaceShapesInitializer



Method detail
-------------

.. py:method:: compute_circle_with_granularity(self, central_body: str, center: list, radius: float, granularity: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_circle_with_granularity

    Compute boundary positions for a circle on the specified centralBody with the specified center, radius and granularity.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **radius** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_circle(self, central_body: str, center: list, radius: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_circle

    Compute boundary positions for a circle on the specified centralBody with the specified center and radius. This is equivalent to calling ComputeCircle with a granularity of 1 degree.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_circle_cartographic_with_granularity(self, central_body: str, center: list, radius: float, granularity: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_circle_cartographic_with_granularity

    For convenience. Computes boundary positions for a circle on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeCircle.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **radius** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_circle_cartographic(self, central_body: str, center: list, radius: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_circle_cartographic

    For convenience. Computes boundary positions for a circle on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeCircle.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_ellipse_with_granularity(self, central_body: str, center: list, major_axis_radius: float, minor_axis_radius: float, bearing: float, granularity: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_ellipse_with_granularity

    Compute boundary positions for an ellipse on the specified centralBody.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **major_axis_radius** : :obj:`~float`
    **minor_axis_radius** : :obj:`~float`
    **bearing** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_ellipse(self, central_body: str, center: list, major_axis_radius: float, minor_axis_radius: float, bearing: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_ellipse

    Compute boundary positions for an ellipse on the specified centralBody. This is equivalent to calling ComputeEllipse with a granularity of 1 degree.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **major_axis_radius** : :obj:`~float`
    **minor_axis_radius** : :obj:`~float`
    **bearing** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_ellipse_cartographic_with_granularity(self, central_body: str, center: list, major_axis_radius: float, minor_axis_radius: float, bearing: float, granularity: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_ellipse_cartographic_with_granularity

    For convenience. Computes boundary positions for an ellipse on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeEllipse.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **major_axis_radius** : :obj:`~float`
    **minor_axis_radius** : :obj:`~float`
    **bearing** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_ellipse_cartographic(self, central_body: str, center: list, major_axis_radius: float, minor_axis_radius: float, bearing: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_ellipse_cartographic

    For convenience. Computes boundary positions for an ellipse on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeEllipse.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **major_axis_radius** : :obj:`~float`
    **minor_axis_radius** : :obj:`~float`
    **bearing** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_sector_with_granularity(self, central_body: str, center: list, inner_radius: float, outer_radius: float, start_bearing: float, end_bearing: float, granularity: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_sector_with_granularity

    Compute boundary positions for a sector on the specified centralBody.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **inner_radius** : :obj:`~float`
    **outer_radius** : :obj:`~float`
    **start_bearing** : :obj:`~float`
    **end_bearing** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_sector(self, central_body: str, center: list, inner_radius: float, outer_radius: float, start_bearing: float, end_bearing: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_sector

    Compute boundary positions for a sector on the specified centralBody. This is equivalent to calling ComputeSector with a granularity of 1 degree.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **inner_radius** : :obj:`~float`
    **outer_radius** : :obj:`~float`
    **start_bearing** : :obj:`~float`
    **end_bearing** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_sector_cartographic_with_granularity(self, central_body: str, center: list, inner_radius: float, outer_radius: float, start_bearing: float, end_bearing: float, granularity: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_sector_cartographic_with_granularity

    For convenience. Computes boundary positions for a sector on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeSector.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **inner_radius** : :obj:`~float`
    **outer_radius** : :obj:`~float`
    **start_bearing** : :obj:`~float`
    **end_bearing** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

.. py:method:: compute_sector_cartographic(self, central_body: str, center: list, inner_radius: float, outer_radius: float, start_bearing: float, end_bearing: float) -> SurfaceShapesResult
    :canonical: ansys.stk.core.graphics.SurfaceShapesInitializer.compute_sector_cartographic

    For convenience. Computes boundary positions for a sector on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeSector.

    :Parameters:

    **central_body** : :obj:`~str`
    **center** : :obj:`~list`
    **inner_radius** : :obj:`~float`
    **outer_radius** : :obj:`~float`
    **start_bearing** : :obj:`~float`
    **end_bearing** : :obj:`~float`

    :Returns:

        :obj:`~SurfaceShapesResult`

