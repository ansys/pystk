ISurfaceShapesInitializer
=========================

.. py:class:: ansys.stk.core.graphics.ISurfaceShapesInitializer

   object
   
   Compute boundary positions for shapes on the surface such as circles, ellipses, and sectors.

.. py:currentmodule:: ISurfaceShapesInitializer

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_circle_with_granularity`
              - Compute boundary positions for a circle on the specified centralBody with the specified center, radius and granularity.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_circle`
              - Compute boundary positions for a circle on the specified centralBody with the specified center and radius. This is equivalent to calling ComputeCircle with a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_circle_cartographic_with_granularity`
              - For convenience. Computes boundary positions for a circle on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeCircle.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_circle_cartographic`
              - For convenience. Computes boundary positions for a circle on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeCircle.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_ellipse_with_granularity`
              - Compute boundary positions for an ellipse on the specified centralBody.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_ellipse`
              - Compute boundary positions for an ellipse on the specified centralBody. This is equivalent to calling ComputeEllipse with a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_ellipse_cartographic_with_granularity`
              - For convenience. Computes boundary positions for an ellipse on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeEllipse.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_ellipse_cartographic`
              - For convenience. Computes boundary positions for an ellipse on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeEllipse.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_sector_with_granularity`
              - Compute boundary positions for a sector on the specified centralBody.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_sector`
              - Compute boundary positions for a sector on the specified centralBody. This is equivalent to calling ComputeSector with a granularity of 1 degree.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_sector_cartographic_with_granularity`
              - For convenience. Computes boundary positions for a sector on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeSector.
            * - :py:attr:`~ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_sector_cartographic`
              - For convenience. Computes boundary positions for a sector on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeSector.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import ISurfaceShapesInitializer



Method detail
-------------

.. py:method:: compute_circle_with_granularity(self, centralBody: str, center: list, radius: float, granularity: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_circle_with_granularity

    Compute boundary positions for a circle on the specified centralBody with the specified center, radius and granularity.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **radius** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_circle(self, centralBody: str, center: list, radius: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_circle

    Compute boundary positions for a circle on the specified centralBody with the specified center and radius. This is equivalent to calling ComputeCircle with a granularity of 1 degree.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_circle_cartographic_with_granularity(self, centralBody: str, center: list, radius: float, granularity: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_circle_cartographic_with_granularity

    For convenience. Computes boundary positions for a circle on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeCircle.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **radius** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_circle_cartographic(self, centralBody: str, center: list, radius: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_circle_cartographic

    For convenience. Computes boundary positions for a circle on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeCircle.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_ellipse_with_granularity(self, centralBody: str, center: list, majorAxisRadius: float, minorAxisRadius: float, bearing: float, granularity: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_ellipse_with_granularity

    Compute boundary positions for an ellipse on the specified centralBody.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **majorAxisRadius** : :obj:`~float`
    **minorAxisRadius** : :obj:`~float`
    **bearing** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_ellipse(self, centralBody: str, center: list, majorAxisRadius: float, minorAxisRadius: float, bearing: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_ellipse

    Compute boundary positions for an ellipse on the specified centralBody. This is equivalent to calling ComputeEllipse with a granularity of 1 degree.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **majorAxisRadius** : :obj:`~float`
    **minorAxisRadius** : :obj:`~float`
    **bearing** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_ellipse_cartographic_with_granularity(self, centralBody: str, center: list, majorAxisRadius: float, minorAxisRadius: float, bearing: float, granularity: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_ellipse_cartographic_with_granularity

    For convenience. Computes boundary positions for an ellipse on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeEllipse.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **majorAxisRadius** : :obj:`~float`
    **minorAxisRadius** : :obj:`~float`
    **bearing** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_ellipse_cartographic(self, centralBody: str, center: list, majorAxisRadius: float, minorAxisRadius: float, bearing: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_ellipse_cartographic

    For convenience. Computes boundary positions for an ellipse on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeEllipse.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **majorAxisRadius** : :obj:`~float`
    **minorAxisRadius** : :obj:`~float`
    **bearing** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_sector_with_granularity(self, centralBody: str, center: list, innerRadius: float, outerRadius: float, startBearing: float, endBearing: float, granularity: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_sector_with_granularity

    Compute boundary positions for a sector on the specified centralBody.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **innerRadius** : :obj:`~float`
    **outerRadius** : :obj:`~float`
    **startBearing** : :obj:`~float`
    **endBearing** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_sector(self, centralBody: str, center: list, innerRadius: float, outerRadius: float, startBearing: float, endBearing: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_sector

    Compute boundary positions for a sector on the specified centralBody. This is equivalent to calling ComputeSector with a granularity of 1 degree.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **innerRadius** : :obj:`~float`
    **outerRadius** : :obj:`~float`
    **startBearing** : :obj:`~float`
    **endBearing** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_sector_cartographic_with_granularity(self, centralBody: str, center: list, innerRadius: float, outerRadius: float, startBearing: float, endBearing: float, granularity: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_sector_cartographic_with_granularity

    For convenience. Computes boundary positions for a sector on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeSector.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **innerRadius** : :obj:`~float`
    **outerRadius** : :obj:`~float`
    **startBearing** : :obj:`~float`
    **endBearing** : :obj:`~float`
    **granularity** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

.. py:method:: compute_sector_cartographic(self, centralBody: str, center: list, innerRadius: float, outerRadius: float, startBearing: float, endBearing: float) -> ISurfaceShapesResult
    :canonical: ansys.stk.core.graphics.ISurfaceShapesInitializer.compute_sector_cartographic

    For convenience. Computes boundary positions for a sector on the specified centralBody using a cartographic center. This is equivalent to converting center to cartesian and calling ComputeSector.

    :Parameters:

    **centralBody** : :obj:`~str`
    **center** : :obj:`~list`
    **innerRadius** : :obj:`~float`
    **outerRadius** : :obj:`~float`
    **startBearing** : :obj:`~float`
    **endBearing** : :obj:`~float`

    :Returns:

        :obj:`~ISurfaceShapesResult`

