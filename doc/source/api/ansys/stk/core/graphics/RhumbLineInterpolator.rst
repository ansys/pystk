RhumbLineInterpolator
=====================

.. py:class:: ansys.stk.core.graphics.RhumbLineInterpolator

   Bases: :py:class:`~ansys.stk.core.graphics.IPositionInterpolator`

   The rhumb line interpolator computes interpolated positions along a rhumb line. Rhumb lines are lines of constant bearing. They appear as straight lines on a Mercator 2D map projection and are well suited to navigation.

.. py:currentmodule:: RhumbLineInterpolator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.graphics.RhumbLineInterpolator.central_body`
              - Gets or sets the central body used when interpolating with interpolate.
            * - :py:attr:`~ansys.stk.core.graphics.RhumbLineInterpolator.granularity`
              - Gets or sets the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.graphics import RhumbLineInterpolator


Property detail
---------------

.. py:property:: central_body
    :canonical: ansys.stk.core.graphics.RhumbLineInterpolator.central_body
    :type: str

    Gets or sets the central body used when interpolating with interpolate.

.. py:property:: granularity
    :canonical: ansys.stk.core.graphics.RhumbLineInterpolator.granularity
    :type: float

    Gets or sets the granularity used when interpolating with interpolate. Lower granularities are more precise but create more positions.


