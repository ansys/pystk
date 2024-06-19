IConversionUtility
==================

.. py:class:: IConversionUtility

   object
   
   Provide conversion utilities.

.. py:currentmodule:: ansys.stk.core.stkutil

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~convert_quantity`
              - Convert the specified quantity value from a given unit to another unit.
            * - :py:meth:`~convert_date`
              - Convert the specified date from a given unit to another unit.
            * - :py:meth:`~convert_quantity_array`
              - Convert the specified quantity values from a given unit to another unit.
            * - :py:meth:`~convert_date_array`
              - Convert the specified dates from a given unit to another unit.
            * - :py:meth:`~new_quantity`
              - Create an IAgQuantity interface with the given dimension, unit and value.
            * - :py:meth:`~new_date`
              - Create an IAgDate interface with the given unit and value.
            * - :py:meth:`~new_position_on_earth`
              - Create an IAgPosition interface with earth as its central body.
            * - :py:meth:`~convert_position_array`
              - Convert the specified position values from a given position type to another position type.
            * - :py:meth:`~new_direction`
              - Create an IAgDirection interface.
            * - :py:meth:`~new_orientation`
              - Create an IAgOrientation interface.
            * - :py:meth:`~new_orbit_state_on_earth`
              - Create an IAgOrbitState interface with earth as its central body.
            * - :py:meth:`~new_position_on_cb`
              - Create an IAgPosition interface using the supplied central body.
            * - :py:meth:`~new_orbit_state_on_cb`
              - Create an IAgOrbitState interface using the supplied central body.
            * - :py:meth:`~query_direction_cosine_matrix`
              - Return a Direction Cosine Matrix (DCM).
            * - :py:meth:`~query_direction_cosine_matrix_array`
              - Return a Direction Cosine Matrix (DCM) as an array.
            * - :py:meth:`~new_cartesian3_vector`
              - Create a cartesian vector.
            * - :py:meth:`~new_cartesian3_vector_from_direction`
              - Convert the direction to cartesian vector.
            * - :py:meth:`~new_cartesian3_vector_from_position`
              - Convert the position to cartesian vector.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IConversionUtility



Method detail
-------------

.. py:method:: convert_quantity(self, dimensionName: str, fromUnit: str, toUnit: str, fromValue: float) -> float
    :canonical: ansys.stk.core.stkutil.IConversionUtility.convert_quantity

    Convert the specified quantity value from a given unit to another unit.

    :Parameters:

    **dimensionName** : :obj:`~str`
    **fromUnit** : :obj:`~str`
    **toUnit** : :obj:`~str`
    **fromValue** : :obj:`~float`

    :Returns:

        :obj:`~float`

.. py:method:: convert_date(self, fromUnit: str, toUnit: str, fromValue: str) -> str
    :canonical: ansys.stk.core.stkutil.IConversionUtility.convert_date

    Convert the specified date from a given unit to another unit.

    :Parameters:

    **fromUnit** : :obj:`~str`
    **toUnit** : :obj:`~str`
    **fromValue** : :obj:`~str`

    :Returns:

        :obj:`~str`

.. py:method:: convert_quantity_array(self, dimensionName: str, fromUnit: str, toUnit: str, quantityValues: list) -> list
    :canonical: ansys.stk.core.stkutil.IConversionUtility.convert_quantity_array

    Convert the specified quantity values from a given unit to another unit.

    :Parameters:

    **dimensionName** : :obj:`~str`
    **fromUnit** : :obj:`~str`
    **toUnit** : :obj:`~str`
    **quantityValues** : :obj:`~list`

    :Returns:

        :obj:`~list`

.. py:method:: convert_date_array(self, fromUnit: str, toUnit: str, fromValues: list) -> list
    :canonical: ansys.stk.core.stkutil.IConversionUtility.convert_date_array

    Convert the specified dates from a given unit to another unit.

    :Parameters:

    **fromUnit** : :obj:`~str`
    **toUnit** : :obj:`~str`
    **fromValues** : :obj:`~list`

    :Returns:

        :obj:`~list`

.. py:method:: new_quantity(self, dimension: str, unitAbbrv: str, value: float) -> IQuantity
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_quantity

    Create an IAgQuantity interface with the given dimension, unit and value.

    :Parameters:

    **dimension** : :obj:`~str`
    **unitAbbrv** : :obj:`~str`
    **value** : :obj:`~float`

    :Returns:

        :obj:`~IQuantity`

.. py:method:: new_date(self, unitAbbrv: str, value: str) -> IDate
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_date

    Create an IAgDate interface with the given unit and value.

    :Parameters:

    **unitAbbrv** : :obj:`~str`
    **value** : :obj:`~str`

    :Returns:

        :obj:`~IDate`

.. py:method:: new_position_on_earth(self) -> IPosition
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_position_on_earth

    Create an IAgPosition interface with earth as its central body.

    :Returns:

        :obj:`~IPosition`

.. py:method:: convert_position_array(self, positionType: POSITION_TYPE, positionArray: list, convertTo: POSITION_TYPE) -> list
    :canonical: ansys.stk.core.stkutil.IConversionUtility.convert_position_array

    Convert the specified position values from a given position type to another position type.

    :Parameters:

    **positionType** : :obj:`~POSITION_TYPE`
    **positionArray** : :obj:`~list`
    **convertTo** : :obj:`~POSITION_TYPE`

    :Returns:

        :obj:`~list`

.. py:method:: new_direction(self) -> IDirection
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_direction

    Create an IAgDirection interface.

    :Returns:

        :obj:`~IDirection`

.. py:method:: new_orientation(self) -> IOrientation
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_orientation

    Create an IAgOrientation interface.

    :Returns:

        :obj:`~IOrientation`

.. py:method:: new_orbit_state_on_earth(self) -> IOrbitState
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_orbit_state_on_earth

    Create an IAgOrbitState interface with earth as its central body.

    :Returns:

        :obj:`~IOrbitState`

.. py:method:: new_position_on_cb(self, centralBodyName: str) -> IPosition
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_position_on_cb

    Create an IAgPosition interface using the supplied central body.

    :Parameters:

    **centralBodyName** : :obj:`~str`

    :Returns:

        :obj:`~IPosition`

.. py:method:: new_orbit_state_on_cb(self, centralBodyName: str) -> IOrbitState
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_orbit_state_on_cb

    Create an IAgOrbitState interface using the supplied central body.

    :Parameters:

    **centralBodyName** : :obj:`~str`

    :Returns:

        :obj:`~IOrbitState`

.. py:method:: query_direction_cosine_matrix(self, inputOrientation: IOrientation) -> typing.Tuple[ICartesian3Vector, ICartesian3Vector, ICartesian3Vector]
    :canonical: ansys.stk.core.stkutil.IConversionUtility.query_direction_cosine_matrix

    Return a Direction Cosine Matrix (DCM).

    :Parameters:

    **inputOrientation** : :obj:`~IOrientation`

    :Returns:

        :obj:`~typing.Tuple[ICartesian3Vector, ICartesian3Vector, ICartesian3Vector]`

.. py:method:: query_direction_cosine_matrix_array(self, inputOrientation: IOrientation) -> list
    :canonical: ansys.stk.core.stkutil.IConversionUtility.query_direction_cosine_matrix_array

    Return a Direction Cosine Matrix (DCM) as an array.

    :Parameters:

    **inputOrientation** : :obj:`~IOrientation`

    :Returns:

        :obj:`~list`

.. py:method:: new_cartesian3_vector(self) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_cartesian3_vector

    Create a cartesian vector.

    :Returns:

        :obj:`~ICartesian3Vector`

.. py:method:: new_cartesian3_vector_from_direction(self, inputDirection: IDirection) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_cartesian3_vector_from_direction

    Convert the direction to cartesian vector.

    :Parameters:

    **inputDirection** : :obj:`~IDirection`

    :Returns:

        :obj:`~ICartesian3Vector`

.. py:method:: new_cartesian3_vector_from_position(self, inputPosition: IPosition) -> ICartesian3Vector
    :canonical: ansys.stk.core.stkutil.IConversionUtility.new_cartesian3_vector_from_position

    Convert the position to cartesian vector.

    :Parameters:

    **inputPosition** : :obj:`~IPosition`

    :Returns:

        :obj:`~ICartesian3Vector`

