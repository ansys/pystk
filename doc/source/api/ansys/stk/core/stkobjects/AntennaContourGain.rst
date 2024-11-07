AntennaContourGain
==================

.. py:class:: ansys.stk.core.stkobjects.AntennaContourGain

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaContour`

   Class defining an antenna gain contour properties.

.. py:currentmodule:: AntennaContourGain

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.set_number_of_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.azimuth_start`
              - Gets the azimuth start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.azimuth_stop`
              - Gets the azimuth stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.azimuth_resolution`
              - Gets the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.azimuth_number_of_points`
              - Gets the number of azimuth points.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.elevation_start`
              - Gets the elevation start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.elevation_stop`
              - Gets the elevation stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.elevation_resolution`
              - Gets the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.elevation_number_of_points`
              - Gets the number of elevation points.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourGain.coordinate_system`
              - Gets or sets the coordinate system for defining the resolution of the antenna graphics.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaContourGain


Property detail
---------------

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.azimuth_start
    :type: float

    Gets the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.azimuth_stop
    :type: float

    Gets the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.azimuth_resolution
    :type: float

    Gets the azimuth resolution.

.. py:property:: azimuth_number_of_points
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.azimuth_number_of_points
    :type: int

    Gets the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.elevation_start
    :type: float

    Gets the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.elevation_stop
    :type: float

    Gets the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.elevation_resolution
    :type: float

    Gets the elevation resolution.

.. py:property:: elevation_number_of_points
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.elevation_number_of_points
    :type: int

    Gets the number of elevation points.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.coordinate_system
    :type: ANTENNA_GRAPHICS_COORDINATE_SYSTEM

    Gets or sets the coordinate system for defining the resolution of the antenna graphics.


Method detail
-------------









.. py:method:: set_resolution(self, azimuth_start: float, azimuth_stop: float, azimuth_resolution: float, elevation_start: float, elevation_stop: float, elevation_resolution: float) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.set_resolution

    Set the azimuth/elevation ranges and resolution.

    :Parameters:

    **azimuth_start** : :obj:`~float`
    **azimuth_stop** : :obj:`~float`
    **azimuth_resolution** : :obj:`~float`
    **elevation_start** : :obj:`~float`
    **elevation_stop** : :obj:`~float`
    **elevation_resolution** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: set_number_of_points(self, azimuth_start: float, azimuth_stop: float, azimuth_num_points: int, elevation_start: float, elevation_stop: float, elevation_num_points: int) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaContourGain.set_number_of_points

    Set the azimuth/elevation ranges and number of points.

    :Parameters:

    **azimuth_start** : :obj:`~float`
    **azimuth_stop** : :obj:`~float`
    **azimuth_num_points** : :obj:`~int`
    **elevation_start** : :obj:`~float`
    **elevation_stop** : :obj:`~float`
    **elevation_num_points** : :obj:`~int`

    :Returns:

        :obj:`~None`



