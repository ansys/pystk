VehicleStandardBasic
====================

.. py:class:: ansys.stk.core.stkobjects.VehicleStandardBasic

   Basic attitude profile.

.. py:currentmodule:: VehicleStandardBasic

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStandardBasic.set_profile_type`
              - Set basic attitude profile type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStandardBasic.is_profile_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStandardBasic.profile_type`
              - Get basic attitude profile type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStandardBasic.profile_supported_types`
              - Returns an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleStandardBasic.profile`
              - Returns the profile interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleStandardBasic


Property detail
---------------

.. py:property:: profile_type
    :canonical: ansys.stk.core.stkobjects.VehicleStandardBasic.profile_type
    :type: VEHICLE_PROFILE

    Get basic attitude profile type.

.. py:property:: profile_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleStandardBasic.profile_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: profile
    :canonical: ansys.stk.core.stkobjects.VehicleStandardBasic.profile
    :type: IVehicleAttitudeProfile

    Returns the profile interface.


Method detail
-------------


.. py:method:: set_profile_type(self, profile: VEHICLE_PROFILE) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleStandardBasic.set_profile_type

    Set basic attitude profile type.

    :Parameters:

    **profile** : :obj:`~VEHICLE_PROFILE`

    :Returns:

        :obj:`~None`

.. py:method:: is_profile_type_supported(self, profile: VEHICLE_PROFILE) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleStandardBasic.is_profile_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **profile** : :obj:`~VEHICLE_PROFILE`

    :Returns:

        :obj:`~bool`



