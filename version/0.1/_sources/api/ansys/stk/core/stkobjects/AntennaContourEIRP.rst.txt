AntennaContourEIRP
==================

.. py:class:: ansys.stk.core.stkobjects.AntennaContourEIRP

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaContour`

   Class defining an antenna eirp contour properties.

.. py:currentmodule:: AntennaContourEIRP

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.set_resolution`
              - Set the azimuth/elevation ranges and resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.set_number_of_points`
              - Set the azimuth/elevation ranges and number of points.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.azimuth_start`
              - Get the azimuth start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.azimuth_stop`
              - Get the azimuth stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.azimuth_resolution`
              - Get the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.azimuth_number_of_points`
              - Get the number of azimuth points.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.elevation_start`
              - Get the elevation start value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.elevation_stop`
              - Get the elevation stop value.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.elevation_resolution`
              - Get the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.elevation_number_of_points`
              - Get the number of elevation points.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourEIRP.coordinate_system`
              - Get or set the coordinate system for defining the resolution of the antenna graphics.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaContourEIRP


Property detail
---------------

.. py:property:: azimuth_start
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.azimuth_start
    :type: float

    Get the azimuth start value.

.. py:property:: azimuth_stop
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.azimuth_stop
    :type: float

    Get the azimuth stop value.

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.azimuth_resolution
    :type: float

    Get the azimuth resolution.

.. py:property:: azimuth_number_of_points
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.azimuth_number_of_points
    :type: int

    Get the number of azimuth points.

.. py:property:: elevation_start
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.elevation_start
    :type: float

    Get the elevation start value.

.. py:property:: elevation_stop
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.elevation_stop
    :type: float

    Get the elevation stop value.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.elevation_resolution
    :type: float

    Get the elevation resolution.

.. py:property:: elevation_number_of_points
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.elevation_number_of_points
    :type: int

    Get the number of elevation points.

.. py:property:: coordinate_system
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.coordinate_system
    :type: AntennaGraphicsCoordinateSystem

    Get or set the coordinate system for defining the resolution of the antenna graphics.


Method detail
-------------









.. py:method:: set_resolution(self, azimuth_start: float, azimuth_stop: float, azimuth_resolution: float, elevation_start: float, elevation_stop: float, elevation_resolution: float) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.set_resolution

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
    :canonical: ansys.stk.core.stkobjects.AntennaContourEIRP.set_number_of_points

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



