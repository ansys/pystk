PathPoint
=========

.. py:class:: ansys.stk.core.graphics.PathPoint

   Represents a path point used in conjunction with the Path Primitive.

.. py:currentmodule:: PathPoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.PathPoint.position`
              - A path point position as a one-dimensional array of three elements corresponding to (X,Y,Z) cartesian coordinates.
            * - :py:attr:`~ansys.stk.core.graphics.PathPoint.date`
              - A date/time of the path point.
            * - :py:attr:`~ansys.stk.core.graphics.PathPoint.color`
              - The path point color.
            * - :py:attr:`~ansys.stk.core.graphics.PathPoint.translucency`
              - The path point translucency.
            * - :py:attr:`~ansys.stk.core.graphics.PathPoint.outline_color`
              - The path point outline color.
            * - :py:attr:`~ansys.stk.core.graphics.PathPoint.outline_translucency`
              - The path point outline translucency.
            * - :py:attr:`~ansys.stk.core.graphics.PathPoint.is_translucent`
              - Whether the path point is translucent.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import PathPoint


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.graphics.PathPoint.position
    :type: list

    A path point position as a one-dimensional array of three elements corresponding to (X,Y,Z) cartesian coordinates.

.. py:property:: date
    :canonical: ansys.stk.core.graphics.PathPoint.date
    :type: Date

    A date/time of the path point.

.. py:property:: color
    :canonical: ansys.stk.core.graphics.PathPoint.color
    :type: agcolor.Color

    The path point color.

.. py:property:: translucency
    :canonical: ansys.stk.core.graphics.PathPoint.translucency
    :type: float

    The path point translucency.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.PathPoint.outline_color
    :type: agcolor.Color

    The path point outline color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.PathPoint.outline_translucency
    :type: float

    The path point outline translucency.

.. py:property:: is_translucent
    :canonical: ansys.stk.core.graphics.PathPoint.is_translucent
    :type: bool

    Whether the path point is translucent.


