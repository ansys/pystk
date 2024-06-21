IAntennaContourFluxDensity
==========================

.. py:class:: ansys.stk.core.stkobjects.IAntennaContourFluxDensity

   object
   
   IAgAntennaContourFluxDensity Interface for a antenna's flux density contour properties.

.. py:currentmodule:: IAntennaContourFluxDensity

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourFluxDensity.set_resolution`
              - Set the azimuth and elevation resolution as well as the maximum elevation angle.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourFluxDensity.azimuth_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourFluxDensity.elevation_resolution`
            * - :py:attr:`~ansys.stk.core.stkobjects.IAntennaContourFluxDensity.max_elevation`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IAntennaContourFluxDensity


Property detail
---------------

.. py:property:: azimuth_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourFluxDensity.azimuth_resolution
    :type: typing.Any

    Gets the azimuth resolution.

.. py:property:: elevation_resolution
    :canonical: ansys.stk.core.stkobjects.IAntennaContourFluxDensity.elevation_resolution
    :type: typing.Any

    Gets the elevation resolution.

.. py:property:: max_elevation
    :canonical: ansys.stk.core.stkobjects.IAntennaContourFluxDensity.max_elevation
    :type: typing.Any

    Gets the maximum elevation.


Method detail
-------------




.. py:method:: set_resolution(self, azimuthResolution: float, elevationResolution: float, maxElevation: float) -> None
    :canonical: ansys.stk.core.stkobjects.IAntennaContourFluxDensity.set_resolution

    Set the azimuth and elevation resolution as well as the maximum elevation angle.

    :Parameters:

    **azimuthResolution** : :obj:`~float`
    **elevationResolution** : :obj:`~float`
    **maxElevation** : :obj:`~float`

    :Returns:

        :obj:`~None`

