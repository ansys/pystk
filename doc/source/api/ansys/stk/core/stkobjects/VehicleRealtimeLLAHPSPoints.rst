VehicleRealtimeLLAHPSPoints
===========================

.. py:class:: ansys.stk.core.stkobjects.VehicleRealtimeLLAHPSPoints

   Add one ephemeris point using latitude/longitude/altitude coordinate system.

.. py:currentmodule:: VehicleRealtimeLLAHPSPoints

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleRealtimeLLAHPSPoints.add`
              - Add an ephemeris point using position, heading, pitch and speed. Epoch uses DateFormat dimension. Lat uses Latitude dimension. Lon uses Longitude dimension. Alt uses Distance dimension. Heading/Pitch use Angle dimension.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleRealtimeLLAHPSPoints



Method detail
-------------

.. py:method:: add(self, time: typing.Any, lat: float, lon: float, alt: float, heading: float, pitch: float, speed: float) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleRealtimeLLAHPSPoints.add

    Add an ephemeris point using position, heading, pitch and speed. Epoch uses DateFormat dimension. Lat uses Latitude dimension. Lon uses Longitude dimension. Alt uses Distance dimension. Heading/Pitch use Angle dimension.

    :Parameters:

    **time** : :obj:`~typing.Any`
    **lat** : :obj:`~float`
    **lon** : :obj:`~float`
    **alt** : :obj:`~float`
    **heading** : :obj:`~float`
    **pitch** : :obj:`~float`
    **speed** : :obj:`~float`

    :Returns:

        :obj:`~None`

