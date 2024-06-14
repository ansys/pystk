IGreatArcInterpolator
=====================

.. py:class:: IGreatArcInterpolator

   object
   
   The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

.. py:currentmodule:: ansys.stk.core.graphics

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body`
            * - :py:meth:`~granularity`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import IGreatArcInterpolator


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.graphics.IGreatArcInterpolator.central_body
    :type: str

    Gets or sets the central body used when interpolating with interpolate.

.. py:property:: granularity
    :canonical: ansys.stk.core.graphics.IGreatArcInterpolator.granularity
    :type: float

    Gets or sets the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.


