ILLAGeodetic
============

.. py:class:: ansys.stk.core.stkobjects.ILLAGeodetic

   ILLAPosition
   
   Geodetic LLA position interface.

.. py:currentmodule:: ILLAGeodetic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILLAGeodetic.lat`
              - Latitude: angle above the x-y plane. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILLAGeodetic.lon`
              - Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILLAGeodetic.altitude`
              - Altitude measured along the normal to the surface of an ellipsoid defined with reference to the central body. Uses Distance Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILLAGeodetic


Property detail
---------------

.. py:property:: lat
    :canonical: ansys.stk.core.stkobjects.ILLAGeodetic.lat
    :type: float

    Latitude: angle above the x-y plane. Uses Latitude Dimension.

.. py:property:: lon
    :canonical: ansys.stk.core.stkobjects.ILLAGeodetic.lon
    :type: float

    Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.ILLAGeodetic.altitude
    :type: float

    Altitude measured along the normal to the surface of an ellipsoid defined with reference to the central body. Uses Distance Dimension.


