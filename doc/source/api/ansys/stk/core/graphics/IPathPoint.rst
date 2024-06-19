IPathPoint
==========

.. py:class:: IPathPoint

   object
   
   A path point used with the Path Primitive.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~position`
            * - :py:meth:`~date`
            * - :py:meth:`~color`
            * - :py:meth:`~translucency`
            * - :py:meth:`~outline_color`
            * - :py:meth:`~outline_translucency`
            * - :py:meth:`~is_translucent`


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
    :type: IAgDate

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


