LLAGeocentric
=============

.. py:class:: ansys.stk.core.stkobjects.LLAGeocentric

   Bases: :py:class:`~ansys.stk.core.stkobjects.ILLAPosition`

   Geocentric LLA position.

.. py:currentmodule:: LLAGeocentric

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.LLAGeocentric.lat`
              - Latitude: angle above the x-y plane. Uses Latitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LLAGeocentric.lon`
              - Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.LLAGeocentric.rad`
              - Radius measured from the center of mass of the central body. Uses Distance Dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import LLAGeocentric


Property detail
---------------

.. py:property:: lat
    :canonical: ansys.stk.core.stkobjects.LLAGeocentric.lat
    :type: float

    Latitude: angle above the x-y plane. Uses Latitude Dimension.

.. py:property:: lon
    :canonical: ansys.stk.core.stkobjects.LLAGeocentric.lon
    :type: float

    Longitude: angle in x-y plane from x towards y. Uses Longitude Dimension.

.. py:property:: rad
    :canonical: ansys.stk.core.stkobjects.LLAGeocentric.rad
    :type: float

    Radius measured from the center of mass of the central body. Uses Distance Dimension.


