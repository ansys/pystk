GeodeticSizeAltitude
====================

.. py:class:: ansys.stk.core.stkobjects.GeodeticSizeAltitude

   Bases: :py:class:`~ansys.stk.core.stkobjects.IGeodeticSize`

   Altitude and Altitude Rate (for Geodetic coordinate type).

.. py:currentmodule:: GeodeticSizeAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.GeodeticSizeAltitude.altitude`
              - Measured along an outward normal to the surface of the ellipsoid. Uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.GeodeticSizeAltitude.rate`
              - Rate of change of altitude. Uses Rate Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import GeodeticSizeAltitude


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.GeodeticSizeAltitude.altitude
    :type: float

    Measured along an outward normal to the surface of the ellipsoid. Uses Distance Dimension.

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.GeodeticSizeAltitude.rate
    :type: float

    Rate of change of altitude. Uses Rate Dimension.


