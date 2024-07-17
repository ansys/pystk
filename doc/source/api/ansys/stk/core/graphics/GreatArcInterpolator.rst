GreatArcInterpolator
====================

.. py:class:: ansys.stk.core.graphics.GreatArcInterpolator

   Bases: :py:class:`~ansys.stk.core.graphics.IPositionInterpolator`

   The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

.. py:currentmodule:: GreatArcInterpolator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.GreatArcInterpolator.central_body`
              - Gets or sets the central body used when interpolating with interpolate.
            * - :py:attr:`~ansys.stk.core.graphics.GreatArcInterpolator.granularity`
              - Gets or sets the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import GreatArcInterpolator


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.graphics.GreatArcInterpolator.central_body
    :type: str

    Gets or sets the central body used when interpolating with interpolate.

.. py:property:: granularity
    :canonical: ansys.stk.core.graphics.GreatArcInterpolator.granularity
    :type: float

    Gets or sets the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.


