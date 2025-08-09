ILatitudeLongitudeAltitudePosition
==================================

.. py:class:: ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition

   Interface to set and retrieve the LLA position type.

.. py:currentmodule:: ILatitudeLongitudeAltitudePosition

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.convert_to`
              - Change the position representation.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.assign`
              - Assign a new position.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.assign_centric`
              - Assign the position using geocentric representation. Lat uses Latitude Dimension. Lon Uses Longitude Dimension. Rad uses Distance Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.assign_detic`
              - Assign the position using geodetic representation.  Lat uses Latitude Dimension. Lon Uses Longitude Dimension. Alt uses Distance Dimension.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.type`
              - Return the position type currently being used.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import ILatitudeLongitudeAltitudePosition


Property detail
---------------

.. py:property:: type
    :canonical: ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.type
    :type: DeticPositionType

    Return the position type currently being used.


Method detail
-------------

.. py:method:: convert_to(self, type: DeticPositionType) -> ILatitudeLongitudeAltitudePosition
    :canonical: ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.convert_to

    Change the position representation.

    :Parameters:

        **type** : :obj:`~DeticPositionType`


    :Returns:

        :obj:`~ILatitudeLongitudeAltitudePosition`


.. py:method:: assign(self, pos: ILatitudeLongitudeAltitudePosition) -> None
    :canonical: ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.assign

    Assign a new position.

    :Parameters:

        **pos** : :obj:`~ILatitudeLongitudeAltitudePosition`


    :Returns:

        :obj:`~None`

.. py:method:: assign_centric(self, lat: float, lon: float, rad: float) -> None
    :canonical: ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.assign_centric

    Assign the position using geocentric representation. Lat uses Latitude Dimension. Lon Uses Longitude Dimension. Rad uses Distance Dimension.

    :Parameters:

        **lat** : :obj:`~float`

        **lon** : :obj:`~float`

        **rad** : :obj:`~float`


    :Returns:

        :obj:`~None`

.. py:method:: assign_detic(self, lat: float, lon: float, alt: float) -> None
    :canonical: ansys.stk.core.stkobjects.ILatitudeLongitudeAltitudePosition.assign_detic

    Assign the position using geodetic representation.  Lat uses Latitude Dimension. Lon Uses Longitude Dimension. Alt uses Distance Dimension.

    :Parameters:

        **lat** : :obj:`~float`

        **lon** : :obj:`~float`

        **alt** : :obj:`~float`


    :Returns:

        :obj:`~None`

