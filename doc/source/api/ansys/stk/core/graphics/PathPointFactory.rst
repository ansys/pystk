PathPointFactory
================

.. py:class:: ansys.stk.core.graphics.PathPointFactory

   Factory creates path points.

.. py:currentmodule:: PathPointFactory

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PathPointFactory.initialize`
              - Initialize a new path point.
            * - :py:attr:`~ansys.stk.core.graphics.PathPointFactory.initialize_with_date`
              - Initialize a new path point with the given date.
            * - :py:attr:`~ansys.stk.core.graphics.PathPointFactory.initialize_with_date_and_position`
              - Initialize a new path point with the given date and position.
            * - :py:attr:`~ansys.stk.core.graphics.PathPointFactory.initialize_with_date_position_and_color`
              - Initialize a new path point with the given date, position and color.
            * - :py:attr:`~ansys.stk.core.graphics.PathPointFactory.initialize_with_date_position_color_and_translucency`
              - Initialize a new path point with the given date, position, color and translucency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PathPointFactory



Method detail
-------------

.. py:method:: initialize(self) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPointFactory.initialize

    Initialize a new path point.

    :Returns:

        :obj:`~PathPoint`

.. py:method:: initialize_with_date(self, path_point_date: IDate) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPointFactory.initialize_with_date

    Initialize a new path point with the given date.

    :Parameters:

    **path_point_date** : :obj:`~IDate`

    :Returns:

        :obj:`~PathPoint`

.. py:method:: initialize_with_date_and_position(self, path_point_date: IDate, position: list) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPointFactory.initialize_with_date_and_position

    Initialize a new path point with the given date and position.

    :Parameters:

    **path_point_date** : :obj:`~IDate`
    **position** : :obj:`~list`

    :Returns:

        :obj:`~PathPoint`

.. py:method:: initialize_with_date_position_and_color(self, path_point_date: IDate, position: list, color: agcolor.Color) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPointFactory.initialize_with_date_position_and_color

    Initialize a new path point with the given date, position and color.

    :Parameters:

    **path_point_date** : :obj:`~IDate`
    **position** : :obj:`~list`
    **color** : :obj:`~agcolor.Color`

    :Returns:

        :obj:`~PathPoint`

.. py:method:: initialize_with_date_position_color_and_translucency(self, path_point_date: IDate, position: list, color: agcolor.Color, translucency: float) -> PathPoint
    :canonical: ansys.stk.core.graphics.PathPointFactory.initialize_with_date_position_color_and_translucency

    Initialize a new path point with the given date, position, color and translucency.

    :Parameters:

    **path_point_date** : :obj:`~IDate`
    **position** : :obj:`~list`
    **color** : :obj:`~agcolor.Color`
    **translucency** : :obj:`~float`

    :Returns:

        :obj:`~PathPoint`

