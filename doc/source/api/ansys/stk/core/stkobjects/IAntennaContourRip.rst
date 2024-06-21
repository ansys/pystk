IAntennaContourRip
==================

.. py:class:: ansys.stk.core.stkobjects.IAntennaContourRip

   object
   
   IAgAntennaContourRip Interface for a antenna's rip contour properties.

.. py:currentmodule:: IAntennaContourRip

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourRip.set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourRip.azimuth_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourRip.elevation_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourRip.max_elevation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContourRip


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourRip.azimuth_resolution
    :type: typing.Any

    Gets the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourRip.elevation_resolution
    :type: typing.Any

    Gets the elevation resolution.

.. py:property:: max_elevation
    :canonical: ansys.stk.core.stkobjects.IAntennaContourRip.max_elevation
    :type: typing.Any

    Gets the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuthResolution: float, elevationResolution: float, maxElevation: float) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaContourRip.set_resolution

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

    **azimuthResolution** : :obj:`~float`
    **elevationResolution** : :obj:`~float`
    **maxElevation** : :obj:`~float`

    :Returns:

        :obj:`~None`

