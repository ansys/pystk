IOrientation
============

.. py:class:: ansys.stk.core.stkutil.IOrientation

   object
   
   Interface to set and retrieve the orientation method.

.. py:currentmodule:: IOrientation

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.convert_to`
              - Change the orientation method to the type specified.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.assign`
              - Assign a new orientation method.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.assign_az_el`
              - Set orientation using the AzEl representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.assign_euler_angles`
              - Set orientation using the Euler angles representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.assign_quaternion`
              - Set orientation using the Quaternion representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.assign_ypr_angles`
              - Set orientation using the YPR angles representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.query_az_el`
              - Get orientation using the AzEl representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.query_euler_angles`
              - Get orientation using the Euler angles representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.query_quaternion`
              - Get orientation using the Quaternion representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.query_ypr_angles`
              - Get orientation using the YPR angles representation.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.query_az_el_array`
              - Return the AzEl elements as an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.query_euler_angles_array`
              - Return the Euler elements as an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.query_quaternion_array`
              - Return the Quaternion elements as an array.
            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.query_ypr_angles_array`
              - Return the YPR Angles elements as an array.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkutil.IOrientation.orientation_type`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkutil import IOrientation


Property detail
---------------

.. py:property:: orientation_type
    :canonical: ansys.stk.core.stkutil.IOrientation.orientation_type
    :type: ORIENTATION_TYPE

    Returns the orientation method currently being used.


Method detail
-------------

.. py:method:: convert_to(self, type: ORIENTATION_TYPE) -> IOrientation
    :canonical: ansys.stk.core.stkutil.IOrientation.convert_to

    Change the orientation method to the type specified.

    :Parameters:

    **type** : :obj:`~ORIENTATION_TYPE`

    :Returns:

        :obj:`~IOrientation`


.. py:method:: assign(self, pOrientation: IOrientation) -> None
    :canonical: ansys.stk.core.stkutil.IOrientation.assign

    Assign a new orientation method.

    :Parameters:

    **pOrientation** : :obj:`~IOrientation`

    :Returns:

        :obj:`~None`

.. py:method:: assign_az_el(self, azimuth: typing.Any, elevation: typing.Any, aboutBoresight: AZ_EL_ABOUT_BORESIGHT) -> None
    :canonical: ansys.stk.core.stkutil.IOrientation.assign_az_el

    Set orientation using the AzEl representation.

    :Parameters:

    **azimuth** : :obj:`~typing.Any`
    **elevation** : :obj:`~typing.Any`
    **aboutBoresight** : :obj:`~AZ_EL_ABOUT_BORESIGHT`

    :Returns:

        :obj:`~None`

.. py:method:: assign_euler_angles(self, sequence: EULER_ORIENTATION_SEQUENCE, a: typing.Any, b: typing.Any, c: typing.Any) -> None
    :canonical: ansys.stk.core.stkutil.IOrientation.assign_euler_angles

    Set orientation using the Euler angles representation.

    :Parameters:

    **sequence** : :obj:`~EULER_ORIENTATION_SEQUENCE`
    **a** : :obj:`~typing.Any`
    **b** : :obj:`~typing.Any`
    **c** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: assign_quaternion(self, qx: float, qy: float, qz: float, qs: float) -> None
    :canonical: ansys.stk.core.stkutil.IOrientation.assign_quaternion

    Set orientation using the Quaternion representation.

    :Parameters:

    **qx** : :obj:`~float`
    **qy** : :obj:`~float`
    **qz** : :obj:`~float`
    **qs** : :obj:`~float`

    :Returns:

        :obj:`~None`

.. py:method:: assign_ypr_angles(self, sequence: YPR_ANGLES_SEQUENCE, yaw: typing.Any, pitch: typing.Any, roll: typing.Any) -> None
    :canonical: ansys.stk.core.stkutil.IOrientation.assign_ypr_angles

    Set orientation using the YPR angles representation.

    :Parameters:

    **sequence** : :obj:`~YPR_ANGLES_SEQUENCE`
    **yaw** : :obj:`~typing.Any`
    **pitch** : :obj:`~typing.Any`
    **roll** : :obj:`~typing.Any`

    :Returns:

        :obj:`~None`

.. py:method:: query_az_el(self) -> typing.Tuple[typing.Any, typing.Any, AZ_EL_ABOUT_BORESIGHT]
    :canonical: ansys.stk.core.stkutil.IOrientation.query_az_el

    Get orientation using the AzEl representation.

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, AZ_EL_ABOUT_BORESIGHT]`

.. py:method:: query_euler_angles(self, sequence: EULER_ORIENTATION_SEQUENCE) -> typing.Tuple[typing.Any, typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkutil.IOrientation.query_euler_angles

    Get orientation using the Euler angles representation.

    :Parameters:

    **sequence** : :obj:`~EULER_ORIENTATION_SEQUENCE`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, typing.Any]`

.. py:method:: query_quaternion(self) -> typing.Tuple[float, float, float, float]
    :canonical: ansys.stk.core.stkutil.IOrientation.query_quaternion

    Get orientation using the Quaternion representation.

    :Returns:

        :obj:`~typing.Tuple[float, float, float, float]`

.. py:method:: query_ypr_angles(self, sequence: YPR_ANGLES_SEQUENCE) -> typing.Tuple[typing.Any, typing.Any, typing.Any]
    :canonical: ansys.stk.core.stkutil.IOrientation.query_ypr_angles

    Get orientation using the YPR angles representation.

    :Parameters:

    **sequence** : :obj:`~YPR_ANGLES_SEQUENCE`

    :Returns:

        :obj:`~typing.Tuple[typing.Any, typing.Any, typing.Any]`

.. py:method:: query_az_el_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IOrientation.query_az_el_array

    Return the AzEl elements as an array.

    :Returns:

        :obj:`~list`

.. py:method:: query_euler_angles_array(self, sequence: EULER_ORIENTATION_SEQUENCE) -> list
    :canonical: ansys.stk.core.stkutil.IOrientation.query_euler_angles_array

    Return the Euler elements as an array.

    :Parameters:

    **sequence** : :obj:`~EULER_ORIENTATION_SEQUENCE`

    :Returns:

        :obj:`~list`

.. py:method:: query_quaternion_array(self) -> list
    :canonical: ansys.stk.core.stkutil.IOrientation.query_quaternion_array

    Return the Quaternion elements as an array.

    :Returns:

        :obj:`~list`

.. py:method:: query_ypr_angles_array(self, sequence: YPR_ANGLES_SEQUENCE) -> list
    :canonical: ansys.stk.core.stkutil.IOrientation.query_ypr_angles_array

    Return the YPR Angles elements as an array.

    :Parameters:

    **sequence** : :obj:`~YPR_ANGLES_SEQUENCE`

    :Returns:

        :obj:`~list`

