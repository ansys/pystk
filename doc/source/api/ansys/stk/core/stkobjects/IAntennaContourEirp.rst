IAntennaContourEirp
===================

.. py:class:: IAntennaContourEirp

   object
   
   IAgAntennaContourEirp Interface for a antenna's eirp contour properties.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:meth:`~set_num_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~azimuth_start`
            * - :py:meth:`~azimuth_stop`
            * - :py:meth:`~azimuth_resolution`
            * - :py:meth:`~azimuth_num_points`
            * - :py:meth:`~elevation_start`
            * - :py:meth:`~elevation_stop`
            * - :py:meth:`~elevation_resolution`
            * - :py:meth:`~elevation_num_points`
            * - :py:meth:`~coordinate_system`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContourEirp


Property detail
---------------

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.azimuth_start
    :type: float

    Gets the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.azimuth_stop
    :type: float

    Gets the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.azimuth_resolution
    :type: float

    Gets the azimuth resolution.

.. py:property:: azimuth_num_points
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.azimuth_num_points
    :type: int

    Gets the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.elevation_start
    :type: float

    Gets the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.elevation_stop
    :type: float

    Gets the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.elevation_resolution
    :type: float

    Gets the elevation resolution.

.. py:property:: elevation_num_points
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.elevation_num_points
    :type: int

    Gets the number of elevation points.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IAntennaContourEirp.coordinate_system
    :type: "ANTENNA_GRAPHICS_COORDINATE_SYSTEM"

    Gets or sets the coordinate system for defining the resolution of the antenna graphics.


Method detail
-------------









.. py:method:: set_resolution(self, azimuthStart:float, azimuthStop:float, azimuthResolution:float, elevationStart:float, elevationStop:float, elevationResolution:float) -> None

    Set the azimuth/elevation ranges and resolution.

    :Parameters:

    **azimuthStart** : :obj:`~float`
    **azimuthStop** : :obj:`~float`
    **azimuthResolution** : :obj:`~float`
    **elevationStart** : :obj:`~float`
    **elevationStop** : :obj:`~float`
    **elevationResolution** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: set_num_points(self, azimuthStart:float, azimuthStop:float, azimuthNumPoints:int, elevationStart:float, elevationStop:float, elevationNumPoints:int) -> None

    Set the azimuth/elevation ranges and number of points.

    :Parameters:

    **azimuthStart** : :obj:`~float`
    **azimuthStop** : :obj:`~float`
    **azimuthNumPoints** : :obj:`~int`
    **elevationStart** : :obj:`~float`
    **elevationStop** : :obj:`~float`
    **elevationNumPoints** : :obj:`~int`

    :Returns:

        :obj:`~None`



