IPosition
=========

.. py:class:: ansys.stk.core.stkutil.IPosition

   IAgPosition provides access to the position of the object.

.. py:currentmodule:: IPosition

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.convert_to`
              - Change the position coordinates to type specified.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.assign`
              - Assign the coordinates into the system.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.assign_geocentric`
              - Assign the position using the Geocentric representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.assign_geodetic`
              - Assign the position using the Geodetic representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.assign_spherical`
              - Assign the position using the Spherical representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.assign_cylindrical`
              - Assign the position using the Cylindrical representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.assign_cartesian`
              - Assign the position using the Cartesian representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.assign_planetocentric`
              - Assign the position using the Planetocentric representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.assign_planetodetic`
              - Assign the position using the Planetodetic representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_planetocentric`
              - Get the position using the Planetocentric representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_planetodetic`
              - Get the position using the Planetodetic representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_spherical`
              - Get the position using the Spherical representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_cylindrical`
              - Get the position using the Cylindrical representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_cartesian`
              - Get the position using the Cartesian representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_planetocentric_array`
              - Return the Planetocentric elements as an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_planetodetic_array`
              - Return the Planetodetic elements as an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_spherical_array`
              - Return the Spherical elements as an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_cylindrical_array`
              - Return the Cylindrical elements as an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.query_cartesian_array`
              - Return the Cartesian elements as an array.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.position_type`
              - Gets the type of position currently being used.
            * - :py:attr:`~ansys.stk.core.stkutil.IPosition.central_body_name`
              - Gets the central body.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IPosition


Property detail
---------------

.. py:property:: position_type
    :canonical: ansys.stk.core.stkutil.IPosition.position_type
    :type: POSITION_TYPE

    Gets the type of position currently being used.

.. py:property:: central_body_name
    :canonical: ansys.stk.core.stkutil.IPosition.central_body_name
    :type: str

    Gets the central body.


Method detail
-------------

.. py:method:: convert_to(self, type: POSITION_TYPE) -> IPosition
    :canonical: ansys.stk.core.stkutil.IPosition.convert_to

    Change the position coordinates to type specified.

    :Parameters:

    **type** : :obj:`~POSITION_TYPE`

    :Returns:

        :obj:`~IPosition`


.. py:method:: assign(self, position: IPosition) -> None
    :canonical: ansys.stk.core.stkutil.IPosition.assign

    Assign the coordinates into the system.

    :Parameters:

    **position** : :obj:`~IPosition`

    :Returns:

        :obj:`~None`

.. py:method:: assign_geocentric(self, lat: typing.Any, lon: typing.Any, alt: float) -> None
    :canonical: ansys.stk.core.stkutil.IPosition.assign_geocentric

    Assign the position using the Geocentric representation.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_geodetic(self, lat: typing.Any, lon: typing.Any, alt: float) -> None
    :canonical: ansys.stk.core.stkutil.IPosition.assign_geodetic

    Assign the position using the Geodetic representation.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_spherical(self, lat: typing.Any, lon: typing.Any, radius: float) -> None
    :canonical: ansys.stk.core.stkutil.IPosition.assign_spherical

    Assign the position using the Spherical representation.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`
    **radius** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_cylindrical(self, radius: float, z: float, lon: typing.Any) -> None
    :canonical: ansys.stk.core.stkutil.IPosition.assign_cylindrical

    Assign the position using the Cylindrical representation.

    :Parameters:

    **radius** : :obj:`~float`
    **z** : :obj:`~float`
    **lon** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: assign_cartesian(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkutil.IPosition.assign_cartesian

    Assign the position using the Cartesian representation.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_planetocentric(self, lat: typing.Any, lon: typing.Any, alt: float) -> None
    :canonical: ansys.stk.core.stkutil.IPosition.assign_planetocentric

    Assign the position using the Planetocentric representation.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_planetodetic(self, lat: typing.Any, lon: typing.Any, alt: float) -> None
    :canonical: ansys.stk.core.stkutil.IPosition.assign_planetodetic

    Assign the position using the Planetodetic representation.

    :Parameters:

    **lat** : :obj:`~typing.Any`
    **lon** : :obj:`~typing.Any`
    **alt** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: query_planetocentric(self) -> typing.Tuple[typing.Any, typing.Any, float]
    :canonical: ansys.stk.core.stkutil.IPosition.query_planetocentric

    Get the position using the Planetocentric representation.

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, float]`

.. py:method:: query_planetodetic(self) -> typing.Tuple[typing.Any, typing.Any, float]
    :canonical: ansys.stk.core.stkutil.IPosition.query_planetodetic

    Get the position using the Planetodetic representation.

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, float]`

.. py:method:: query_spherical(self) -> typing.Tuple[typing.Any, typing.Any, float]
    :canonical: ansys.stk.core.stkutil.IPosition.query_spherical

    Get the position using the Spherical representation.

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, float]`

.. py:method:: query_cylindrical(self) -> typing.Tuple[float, typing.Any, float]
    :canonical: ansys.stk.core.stkutil.IPosition.query_cylindrical

    Get the position using the Cylindrical representation.

    :Returns:

        :obj:`~typing.Tuple[float, typing.Any, float]`

.. py:method:: query_cartesian(self) -> typing.Tuple[float, float, float]
    :canonical: ansys.stk.core.stkutil.IPosition.query_cartesian

    Get the position using the Cartesian representation.

    :Returns:

        :obj:`~typing.Tuple[float, float, float]`


.. py:method:: query_planetocentric_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IPosition.query_planetocentric_array

    Return the Planetocentric elements as an array.

    :Returns:

        :obj:`~list`

.. py:method:: query_planetodetic_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IPosition.query_planetodetic_array

    Return the Planetodetic elements as an array.

    :Returns:

        :obj:`~list`

.. py:method:: query_spherical_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IPosition.query_spherical_array

    Return the Spherical elements as an array.

    :Returns:

        :obj:`~list`

.. py:method:: query_cylindrical_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IPosition.query_cylindrical_array

    Return the Cylindrical elements as an array.

    :Returns:

        :obj:`~list`

.. py:method:: query_cartesian_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IPosition.query_cartesian_array

    Return the Cartesian elements as an array.

    :Returns:

        :obj:`~list`

