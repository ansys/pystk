IGreatArcInterpolator
=====================

.. py:class:: ansys.stk.core.graphics.IGreatArcInterpolator

   object
   
   The great arc interpolator computes interpolated positions along a great arc. A great arc is the shortest path between two positions on an ellipsoid.

.. py:currentmodule:: IGreatArcInterpolator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.IGreatArcInterpolator.central_body`
            * - :py:attr:`~ansys.stk.core.graphics.IGreatArcInterpolator.granularity`


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


