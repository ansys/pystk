ConversionUtility
=================

.. py:class:: ansys.stk.core.stkutil.ConversionUtility

   Object that contains a unit conversion utility.

.. py:currentmodule:: ConversionUtility

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.convert_quantity`
              - Convert the specified quantity value from a given unit to another unit.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.convert_date`
              - Convert the specified date from a given unit to another unit.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.convert_quantity_array`
              - Convert the specified quantity values from a given unit to another unit.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.convert_date_array`
              - Convert the specified dates from a given unit to another unit.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_quantity`
              - Create an Quantity interface with the given dimension, unit and value.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_date`
              - Create an Date interface with the given unit and value.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_position_on_earth`
              - Create an IPosition interface with earth as its central body.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.convert_position_array`
              - Convert the specified position values from a given position type to another position type.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_direction`
              - Create an IDirection interface.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_orientation`
              - Create an IOrientation interface.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_orbit_state_on_earth`
              - Create an IOrbitState interface with earth as its central body.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_position_on_cb`
              - Create an IPosition interface using the supplied central body.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_orbit_state_on_cb`
              - Create an IOrbitState interface using the supplied central body.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.query_direction_cosine_matrix`
              - Return a Direction Cosine Matrix (DCM).
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.query_direction_cosine_matrix_array`
              - Return a Direction Cosine Matrix (DCM) as an array.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_cartesian3_vector`
              - Create a cartesian vector.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_cartesian3_vector_from_direction`
              - Convert the direction to cartesian vector.
            * - :py:attr:`~ansys.stk.core.stkutil.ConversionUtility.new_cartesian3_vector_from_position`
              - Convert the position to cartesian vector.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import ConversionUtility



Method detail
-------------

.. py:method:: convert_quantity(self, dimension_name: str, from_unit: str, to_unit: str, from_value: float) -> float
    :canonical: ansys.stk.core.stkutil.ConversionUtility.convert_quantity

    Convert the specified quantity value from a given unit to another unit.

    :Parameters:

        **dimension_name** : :obj:`~str`

        **from_unit** : :obj:`~str`

        **to_unit** : :obj:`~str`

        **from_value** : :obj:`~float`


    :Returns:

        :obj:`~float`

.. py:method:: convert_date(self, from_unit: str, to_unit: str, from_value: str) -> str
    :canonical: ansys.stk.core.stkutil.ConversionUtility.convert_date

    Convert the specified date from a given unit to another unit.

    :Parameters:

        **from_unit** : :obj:`~str`

        **to_unit** : :obj:`~str`

        **from_value** : :obj:`~str`


    :Returns:

        :obj:`~str`

.. py:method:: convert_quantity_array(self, dimension_name: str, from_unit: str, to_unit: str, quantity_values: list) -> list
    :canonical: ansys.stk.core.stkutil.ConversionUtility.convert_quantity_array

    Convert the specified quantity values from a given unit to another unit.

    :Parameters:

        **dimension_name** : :obj:`~str`

        **from_unit** : :obj:`~str`

        **to_unit** : :obj:`~str`

        **quantity_values** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: convert_date_array(self, from_unit: str, to_unit: str, from_values: list) -> list
    :canonical: ansys.stk.core.stkutil.ConversionUtility.convert_date_array

    Convert the specified dates from a given unit to another unit.

    :Parameters:

        **from_unit** : :obj:`~str`

        **to_unit** : :obj:`~str`

        **from_values** : :obj:`~list`


    :Returns:

        :obj:`~list`

.. py:method:: new_quantity(self, dimension: str, unit_abbrv: str, value: float) -> Quantity
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_quantity

    Create an Quantity interface with the given dimension, unit and value.

    :Parameters:

        **dimension** : :obj:`~str`

        **unit_abbrv** : :obj:`~str`

        **value** : :obj:`~float`


    :Returns:

        :obj:`~Quantity`

.. py:method:: new_date(self, unit_abbrv: str, value: str) -> Date
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_date

    Create an Date interface with the given unit and value.

    :Parameters:

        **unit_abbrv** : :obj:`~str`

        **value** : :obj:`~str`


    :Returns:

        :obj:`~Date`

.. py:method:: new_position_on_earth(self) -> IPosition
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_position_on_earth

    Create an IPosition interface with earth as its central body.

    :Returns:

        :obj:`~IPosition`

.. py:method:: convert_position_array(self, position_type: PositionType, position_array: list, convert_to: PositionType) -> list
    :canonical: ansys.stk.core.stkutil.ConversionUtility.convert_position_array

    Convert the specified position values from a given position type to another position type.

    :Parameters:

        **position_type** : :obj:`~PositionType`

        **position_array** : :obj:`~list`

        **convert_to** : :obj:`~PositionType`


    :Returns:

        :obj:`~list`

.. py:method:: new_direction(self) -> IDirection
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_direction

    Create an IDirection interface.

    :Returns:

        :obj:`~IDirection`

.. py:method:: new_orientation(self) -> IOrientation
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_orientation

    Create an IOrientation interface.

    :Returns:

        :obj:`~IOrientation`

.. py:method:: new_orbit_state_on_earth(self) -> IOrbitState
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_orbit_state_on_earth

    Create an IOrbitState interface with earth as its central body.

    :Returns:

        :obj:`~IOrbitState`

.. py:method:: new_position_on_cb(self, central_body_name: str) -> IPosition
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_position_on_cb

    Create an IPosition interface using the supplied central body.

    :Parameters:

        **central_body_name** : :obj:`~str`


    :Returns:

        :obj:`~IPosition`

.. py:method:: new_orbit_state_on_cb(self, central_body_name: str) -> IOrbitState
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_orbit_state_on_cb

    Create an IOrbitState interface using the supplied central body.

    :Parameters:

        **central_body_name** : :obj:`~str`


    :Returns:

        :obj:`~IOrbitState`

.. py:method:: query_direction_cosine_matrix(self, input_orientation: IOrientation) -> typing.Tuple[ICartesian3Vector, ICartesian3Vector, ICartesian3Vector]
    :canonical: ansys.stk.core.stkutil.ConversionUtility.query_direction_cosine_matrix

    Return a Direction Cosine Matrix (DCM).

    :Parameters:

        **input_orientation** : :obj:`~IOrientation`


    :Returns:

        :obj:`~typing.Tuple[ICartesian3Vector, ICartesian3Vector, ICartesian3Vector]`

.. py:method:: query_direction_cosine_matrix_array(self, input_orientation: IOrientation) -> list
    :canonical: ansys.stk.core.stkutil.ConversionUtility.query_direction_cosine_matrix_array

    Return a Direction Cosine Matrix (DCM) as an array.

    :Parameters:

        **input_orientation** : :obj:`~IOrientation`


    :Returns:

        :obj:`~list`

.. py:method:: new_cartesian3_vector(self) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_cartesian3_vector

    Create a cartesian vector.

    :Returns:

        :obj:`~ICartesian3Vector`

.. py:method:: new_cartesian3_vector_from_direction(self, input_direction: IDirection) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_cartesian3_vector_from_direction

    Convert the direction to cartesian vector.

    :Parameters:

        **input_direction** : :obj:`~IDirection`


    :Returns:

        :obj:`~ICartesian3Vector`

.. py:method:: new_cartesian3_vector_from_position(self, input_position: IPosition) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkutil.ConversionUtility.new_cartesian3_vector_from_position

    Convert the position to cartesian vector.

    :Parameters:

        **input_position** : :obj:`~IPosition`


    :Returns:

        :obj:`~ICartesian3Vector`

