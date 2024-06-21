IGeodeticSizeAltitude
=====================

.. py:class:: ansys.stk.core.stkobjects.IGeodeticSizeAltitude

   IGeodeticSize
   
   Interface for Altitude and Altitude Rate (for Geodetic coordinate type).

.. py:currentmodule:: IGeodeticSizeAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IGeodeticSizeAltitude.altitude`
            * - :py:attr:`~ansys.stk.core.stkobjects.IGeodeticSizeAltitude.rate`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IGeodeticSizeAltitude


Property detail
---------------

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.IGeodeticSizeAltitude.altitude
    :type: float

    Measured along an outward normal to the surface of the ellipsoid. Uses Distance Dimension.

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.IGeodeticSizeAltitude.rate
    :type: float

    Rate of change of altitude. Uses Rate Dimension.


