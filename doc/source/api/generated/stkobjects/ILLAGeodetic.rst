ILLAGeodetic
============

.. py:class:: ILLAGeodetic

   ILLAPosition
   
   Geodetic LLA position interface.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~lat`
            * - :py:meth:`~lon`
            * - :py:meth:`~altitude`


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


