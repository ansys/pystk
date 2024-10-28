AntennaContourRIP
=================

.. py:class:: ansys.stk.core.stkobjects.AntennaContourRIP

   Bases: :py:class:`~ansys.stk.core.stkobjects.IAntennaContour`

   Class defining an antenna rip contour properties.

.. py:currentmodule:: AntennaContourRIP

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourRIP.set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourRIP.azimuth_resolution`
              - Gets the azimuth resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourRIP.elevation_resolution`
              - Gets the elevation resolution.
            * - :py:attr:`~ansys.stk.core.stkobjects.AntennaContourRIP.maximum_elevation_angle`
              - Gets the maximum elevation.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AntennaContourRIP


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourRIP.azimuth_resolution
    :type: typing.Any

    Gets the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.AntennaContourRIP.elevation_resolution
    :type: typing.Any

    Gets the elevation resolution.

.. py:property:: maximum_elevation_angle
    :canonical: ansys.stk.core.stkobjects.AntennaContourRIP.maximum_elevation_angle
    :type: typing.Any

    Gets the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuthResolution: float, elevationResolution: float, maxElevation: float) -> None
    :canonical: ansys.stk.core.stkobjects.AntennaContourRIP.set_resolution

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

    **azimuthResolution** : :obj:`~float`
    **elevationResolution** : :obj:`~float`
    **maxElevation** : :obj:`~float`

    :Returns:

        :obj:`~None`

