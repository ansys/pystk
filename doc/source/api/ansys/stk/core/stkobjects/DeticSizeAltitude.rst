DeticSizeAltitude
=================

.. py:class:: ansys.stk.core.stkobjects.DeticSizeAltitude

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGeodeticSize`

   Altitude and Altitude Rate (for Geodetic coordinate type).

.. py:currentmodule:: DeticSizeAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.DeticSizeAltitude.altitude`
              - Measured along an outward normal to the surface of the ellipsoid. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.DeticSizeAltitude.rate`
              - Rate of change of altitude. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import DeticSizeAltitude


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.DeticSizeAltitude.altitude
    :type: float

    Measured along an outward normal to the surface of the ellipsoid. Uses Distance Dimension.

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.DeticSizeAltitude.rate
    :type: float

    Rate of change of altitude. Uses Rate Dimension.


