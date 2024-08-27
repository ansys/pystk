LLAGeodetic
===========

.. py:class:: ansys.stk.core.stkobjects.LLAGeodetic

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILLAPosition`

   Geodetic LLA position.

.. py:currentmodule:: LLAGeodetic

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LLAGeodetic.lat`
              - Latitude: angle above the x-y plane. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LLAGeodetic.lon`
              - Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LLAGeodetic.altitude`
              - Altitude measured along the normal to the surface of an ellipsoid defined with reference to the central body. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LLAGeodetic


Property detail
---------------

.. py:property:: lat
    :canonical: ansys.stk.core.stkobjects.LLAGeodetic.lat
    :type: float

    Latitude: angle above the x-y plane. Uses Latitude Dimension.

.. py:property:: lon
    :canonical: ansys.stk.core.stkobjects.LLAGeodetic.lon
    :type: float

    Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.

.. py:property:: altitude
    :canonical: ansys.stk.core.stkobjects.LLAGeodetic.altitude
    :type: float

    Altitude measured along the normal to the surface of an ellipsoid defined with reference to the central body. Uses Distance Dimension.


