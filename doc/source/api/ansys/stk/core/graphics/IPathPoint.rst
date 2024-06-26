IPathPoint
==========

.. py:class:: ansys.stk.core.graphics.IPathPoint

   object
   
   A path point used with the Path Primitive.

.. py:currentmodule:: IPathPoint

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPathPoint.position`
              - A path point position as a one-dimensional array of three elements corresponding to (X,Y,Z) cartesian coordinates.
            * - :py:attr:`~ansys.stk.core.graphics.IPathPoint.date`
              - A date/time of the path point.
            * - :py:attr:`~ansys.stk.core.graphics.IPathPoint.color`
              - The path point color.
            * - :py:attr:`~ansys.stk.core.graphics.IPathPoint.translucency`
              - The path point translucency.
            * - :py:attr:`~ansys.stk.core.graphics.IPathPoint.outline_color`
              - The path point outline color.
            * - :py:attr:`~ansys.stk.core.graphics.IPathPoint.outline_translucency`
              - The path point outline translucency.
            * - :py:attr:`~ansys.stk.core.graphics.IPathPoint.is_translucent`
              - Whether the path point is translucent.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPathPoint


Property detail
---------------

.. py:property:: position
    :canonical: ansys.stk.core.graphics.IPathPoint.position
    :type: list

    A path point position as a one-dimensional array of three elements corresponding to (X,Y,Z) cartesian coordinates.

.. py:property:: date
    :canonical: ansys.stk.core.graphics.IPathPoint.date
    :type: IDate

    A date/time of the path point.

.. py:property:: color
    :canonical: ansys.stk.core.graphics.IPathPoint.color
    :type: agcolor.Color

    The path point color.

.. py:property:: translucency
    :canonical: ansys.stk.core.graphics.IPathPoint.translucency
    :type: float

    The path point translucency.

.. py:property:: outline_color
    :canonical: ansys.stk.core.graphics.IPathPoint.outline_color
    :type: agcolor.Color

    The path point outline color.

.. py:property:: outline_translucency
    :canonical: ansys.stk.core.graphics.IPathPoint.outline_translucency
    :type: float

    The path point outline translucency.

.. py:property:: is_translucent
    :canonical: ansys.stk.core.graphics.IPathPoint.is_translucent
    :type: bool

    Whether the path point is translucent.


