ISensorPointingGrazingAltitude
==============================

.. py:class:: ansys.stk.core.stkobjects.ISensorPointingGrazingAltitude

   object
   
   IAgSnPtGrazingAlt Interface for a sensor pointed in such a way that the boresight vector will graze the central body at a specified altitude.

.. py:currentmodule:: ISensorPointingGrazingAltitude

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingGrazingAltitude.azimuth_offset`
              - The azimuth offset, defining the plane in the parent object's body-fixed frame in which the sensor boresight lies. It is the angle between the X axis and the azimuth vector in the XY plane. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ISensorPointingGrazingAltitude.grazing_altitude`
              - The altitude at which the boresight vector grazes the central body. Uses Distance Dimension.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ISensorPointingGrazingAltitude


Property detail
---------------

.. py:property:: azimuth_offset
    :canonical: ansys.stk.core.stkobjects.ISensorPointingGrazingAltitude.azimuth_offset
    :type: typing.Any

    The azimuth offset, defining the plane in the parent object's body-fixed frame in which the sensor boresight lies. It is the angle between the X axis and the azimuth vector in the XY plane. Uses Angle Dimension.

.. py:property:: grazing_altitude
    :canonical: ansys.stk.core.stkobjects.ISensorPointingGrazingAltitude.grazing_altitude
    :type: float

    The altitude at which the boresight vector grazes the central body. Uses Distance Dimension.


