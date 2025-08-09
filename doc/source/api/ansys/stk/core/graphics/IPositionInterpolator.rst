IPositionInterpolator
=====================

.. py:class:: ansys.stk.core.graphics.IPositionInterpolator

   Position interpolators compute positions based on a collection of input positions. Position interpolators are used in conjunction with the polyline primitive to render things such as great arcs and rhumb lines.

.. py:currentmodule:: IPositionInterpolator

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPositionInterpolator.interpolate`
              - Compute interpolated positions based on the input positions. Returns an array of positions in the order x, y, z.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IPositionInterpolator.polyline_type`
              - Get the polyline type of positions returned from interpolate.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPositionInterpolator


Property detail
---------------

.. py:property:: polyline_type
    :canonical: ansys.stk.core.graphics.IPositionInterpolator.polyline_type
    :type: PolylineType

    Get the polyline type of positions returned from interpolate.


Method detail
-------------

.. py:method:: interpolate(self, positions: list) -> list
    :canonical: ansys.stk.core.graphics.IPositionInterpolator.interpolate

    Compute interpolated positions based on the input positions. Returns an array of positions in the order x, y, z.

    :Parameters:

        **positions** : :obj:`~list`


    :Returns:

        :obj:`~list`


