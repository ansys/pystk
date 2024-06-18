ILLAGeocentric
==============

.. py:class:: ILLAGeocentric

   ILLAPosition
   
   Geocentric LLA position interface:.

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
            * - :py:meth:`~rad`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILLAGeocentric


Property detail
---------------

.. py:property:: lat
    :canonical: ansys.stk.core.stkobjects.ILLAGeocentric.lat
    :type: float

    Latitude: angle above the x-y plane. Uses Latitude Dimension.

.. py:property:: lon
    :canonical: ansys.stk.core.stkobjects.ILLAGeocentric.lon
    :type: float

    Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.

.. py:property:: rad
    :canonical: ansys.stk.core.stkobjects.ILLAGeocentric.rad
    :type: float

    Radius measured from the center of mass of the central body. Uses Distance Dimension.


