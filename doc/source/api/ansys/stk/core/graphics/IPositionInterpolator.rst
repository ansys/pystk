IPositionInterpolator
=====================

.. py:class:: IPositionInterpolator

   object
   
   Position interpolators compute positions based on a collection of input positions. Position interpolators are used in conjunction with the polyline primitive to render things such as great arcs and rhumb lines.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~interpolate`
              - Compute interpolated positions based on the input positions. Returns an array of positions in the order x, y, z.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~polyline_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IPositionInterpolator


Property detail
---------------

.. py:property:: polyline_type
    :canonical: ansys.stk.core.graphics.IPositionInterpolator.polyline_type
    :type: POLYLINE_TYPE

    Gets the polyline type of positions returned from interpolate.


Method detail
-------------


.. py:method:: interpolate(self, positions: list) -> list
    :canonical: ansys.stk.core.graphics.IPositionInterpolator.interpolate

    Compute interpolated positions based on the input positions. Returns an array of positions in the order x, y, z.

    :Parameters:

    **positions** : :obj:`~list`

    :Returns:

        :obj:`~list`

