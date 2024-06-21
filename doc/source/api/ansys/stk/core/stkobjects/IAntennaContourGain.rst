IAntennaContourGain
===================

.. py:class:: ansys.stk.core.stkobjects.IAntennaContourGain

   object
   
   IAgAntennaContourGain Interface for a antenna's gain contour properties.

.. py:currentmodule:: IAntennaContourGain

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.set_num_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.azimuth_start`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.azimuth_stop`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.azimuth_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.azimuth_num_points`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.elevation_start`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.elevation_stop`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.elevation_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.elevation_num_points`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourGain.coordinate_system`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContourGain


Property detail
---------------

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.azimuth_start
    :type: float

    Gets the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.azimuth_stop
    :type: float

    Gets the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.azimuth_resolution
    :type: float

    Gets the azimuth resolution.

.. py:property:: azimuth_num_points
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.azimuth_num_points
    :type: int

    Gets the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.elevation_start
    :type: float

    Gets the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.elevation_stop
    :type: float

    Gets the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.elevation_resolution
    :type: float

    Gets the elevation resolution.

.. py:property:: elevation_num_points
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.elevation_num_points
    :type: int

    Gets the number of elevation points.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.coordinate_system
    :type: ANTENNA_GRAPHICS_COORDINATE_SYSTEM

    Gets or sets the coordinate system for defining the resolution of the antenna graphics.


Method detail
-------------









.. py:method:: set_resolution(self, azimuthStart: float, azimuthStop: float, azimuthResolution: float, elevationStart: float, elevationStop: float, elevationResolution: float) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.set_resolution

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

.. py:method:: set_num_points(self, azimuthStart: float, azimuthStop: float, azimuthNumPoints: int, elevationStart: float, elevationStop: float, elevationNumPoints: int) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaContourGain.set_num_points

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



