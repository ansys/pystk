IDirection
==========

.. py:class:: ansys.stk.core.stkutil.IDirection

   object
   
   Interface to set and retrieve direction options for aligned and constrained vectors.

.. py:currentmodule:: IDirection

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.convert_to`
              - Change the direction to the type specified.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.assign`
              - Assign a new direction.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.assign_euler`
              - Set direction using the Euler representation. Params B and C use Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.assign_pr`
              - Set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.assign_ra_dec`
              - Set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.assign_xyz`
              - Set direction using the Cartesian representation. Params X, Y and Z are dimensionless.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.query_euler`
              - Get direction using the Euler representation. Params B and C use Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.query_pr`
              - Get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.query_ra_dec`
              - Get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.query_xyz`
              - Get direction using the Cartesian representation. Params X, Y and Z are dimensionless.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.query_euler_array`
              - Return the Euler elements in an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.query_pr_array`
              - Return the PR elements in an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.query_ra_dec_array`
              - Return the RADec elements in an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.query_xyz_array`
              - Return the XYZ elements in an array.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IDirection.direction_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IDirection


Property detail
---------------

.. py:property:: direction_type
    :canonical: ansys.stk.core.stkutil.IDirection.direction_type
    :type: DIRECTION_TYPE

    Returns the type of direction currently being used.


Method detail
-------------

.. py:method:: convert_to(self, type: DIRECTION_TYPE) -> IDirection
    :canonical: ansys.stk.core.stkutil.IDirection.convert_to

    Change the direction to the type specified.

    :Parameters:

    **type** : :obj:`~DIRECTION_TYPE`

    :Returns:

        :obj:`~IDirection`


.. py:method:: assign(self, pDirection: IDirection) -> None
    :canonical: ansys.stk.core.stkutil.IDirection.assign

    Assign a new direction.

    :Parameters:

    **pDirection** : :obj:`~IDirection`

    :Returns:

        :obj:`~None`

.. py:method:: assign_euler(self, b: typing.Any, c: typing.Any, sequence: EULER_DIRECTION_SEQUENCE) -> None
    :canonical: ansys.stk.core.stkutil.IDirection.assign_euler

    Set direction using the Euler representation. Params B and C use Angle Dimension.

    :Parameters:

    **b** : :obj:`~typing.Any`
    **c** : :obj:`~typing.Any`
    **sequence** : :obj:`~EULER_DIRECTION_SEQUENCE`

    :Returns:

        :obj:`~None`

.. py:method:: assign_pr(self, pitch: typing.Any, roll: typing.Any) -> None
    :canonical: ansys.stk.core.stkutil.IDirection.assign_pr

    Set direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.

    :Parameters:

    **pitch** : :obj:`~typing.Any`
    **roll** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: assign_ra_dec(self, ra: typing.Any, dec: typing.Any) -> None
    :canonical: ansys.stk.core.stkutil.IDirection.assign_ra_dec

    Set direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.

    :Parameters:

    **ra** : :obj:`~typing.Any`
    **dec** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: assign_xyz(self, x: float, y: float, z: float) -> None
    :canonical: ansys.stk.core.stkutil.IDirection.assign_xyz

    Set direction using the Cartesian representation. Params X, Y and Z are dimensionless.

    :Parameters:

    **x** : :obj:`~float`
    **y** : :obj:`~float`
    **z** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: query_euler(self, sequence: EULER_DIRECTION_SEQUENCE) -> typing.Tuple[typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkutil.IDirection.query_euler

    Get direction using the Euler representation. Params B and C use Angle Dimension.

    :Parameters:

    **sequence** : :obj:`~EULER_DIRECTION_SEQUENCE`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any]`

.. py:method:: query_pr(self, sequence: PR_SEQUENCE) -> typing.Tuple[typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkutil.IDirection.query_pr

    Get direction using the Pitch Roll representation. Pitch and Roll use Angle Dimension.

    :Parameters:

    **sequence** : :obj:`~PR_SEQUENCE`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any]`

.. py:method:: query_ra_dec(self) -> typing.Tuple[typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkutil.IDirection.query_ra_dec

    Get direction using the Right Ascension and Declination representation. Param Dec uses Latitude. Param RA uses Longitude.

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any]`

.. py:method:: query_xyz(self) -> typing.Tuple[float, float, float]
    :canonical: ansys.stk.core.stkutil.IDirection.query_xyz

    Get direction using the Cartesian representation. Params X, Y and Z are dimensionless.

    :Returns:

        :obj:`~typing.Tuple[float, float, float]`

.. py:method:: query_euler_array(self, sequence: EULER_DIRECTION_SEQUENCE) -> list
    :canonical: ansys.stk.core.stkutil.IDirection.query_euler_array

    Return the Euler elements in an array.

    :Parameters:

    **sequence** : :obj:`~EULER_DIRECTION_SEQUENCE`

    :Returns:

        :obj:`~list`

.. py:method:: query_pr_array(self, sequence: PR_SEQUENCE) -> list
    :canonical: ansys.stk.core.stkutil.IDirection.query_pr_array

    Return the PR elements in an array.

    :Parameters:

    **sequence** : :obj:`~PR_SEQUENCE`

    :Returns:

        :obj:`~list`

.. py:method:: query_ra_dec_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IDirection.query_ra_dec_array

    Return the RADec elements in an array.

    :Returns:

        :obj:`~list`

.. py:method:: query_xyz_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IDirection.query_xyz_array

    Return the XYZ elements in an array.

    :Returns:

        :obj:`~list`

