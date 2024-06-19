IPathPointFactory
=================

.. py:class:: IPathPointFactory

   object
   
   Create Path Primitive's path points.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~initialize`
              - Initialize a new path point.
            * - :py:meth:`~initialize_with_date`
              - Initialize a new path point with the given date.
            * - :py:meth:`~initialize_with_date_and_position`
              - Initialize a new path point with the given date and position.
            * - :py:meth:`~initialize_with_date_position_and_color`
              - Initialize a new path point with the given date, position and color.
            * - :py:meth:`~initialize_with_date_position_color_and_translucency`
              - Initialize a new path point with the given date, position, color and translucency.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPathPointFactory



Method detail
-------------

.. py:method:: initialize(self) -> IPathPoint
    :canonical: ansys.stk.core.graphics.IPathPointFactory.initialize

    Initialize a new path point.

    :Returns:

        :obj:`~IPathPoint`

.. py:method:: initialize_with_date(self, pathPointDate: IDate) -> IPathPoint
    :canonical: ansys.stk.core.graphics.IPathPointFactory.initialize_with_date

    Initialize a new path point with the given date.

    :Parameters:

    **pathPointDate** : :obj:`~IDate`

    :Returns:

        :obj:`~IPathPoint`

.. py:method:: initialize_with_date_and_position(self, pathPointDate: IDate, position: list) -> IPathPoint
    :canonical: ansys.stk.core.graphics.IPathPointFactory.initialize_with_date_and_position

    Initialize a new path point with the given date and position.

    :Parameters:

    **pathPointDate** : :obj:`~IDate`
    **position** : :obj:`~list`

    :Returns:

        :obj:`~IPathPoint`

.. py:method:: initialize_with_date_position_and_color(self, pathPointDate: IDate, position: list, color: agcolor.Color) -> IPathPoint
    :canonical: ansys.stk.core.graphics.IPathPointFactory.initialize_with_date_position_and_color

    Initialize a new path point with the given date, position and color.

    :Parameters:

    **pathPointDate** : :obj:`~IDate`
    **position** : :obj:`~list`
    **color** : :obj:`~agcolor.Color`

    :Returns:

        :obj:`~IPathPoint`

.. py:method:: initialize_with_date_position_color_and_translucency(self, pathPointDate: IDate, position: list, color: agcolor.Color, translucency: float) -> IPathPoint
    :canonical: ansys.stk.core.graphics.IPathPointFactory.initialize_with_date_position_color_and_translucency

    Initialize a new path point with the given date, position, color and translucency.

    :Parameters:

    **pathPointDate** : :obj:`~IDate`
    **position** : :obj:`~list`
    **color** : :obj:`~agcolor.Color`
    **translucency** : :obj:`~float`

    :Returns:

        :obj:`~IPathPoint`

