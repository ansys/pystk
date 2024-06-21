IVehicleAttitudeRealTimeDataReference
=====================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference

   object
   
   Real time attitude data reference.

.. py:currentmodule:: IVehicleAttitudeRealTimeDataReference

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.set_profile_type`
              - Set realtime data reference profile type.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.is_profile_type_supported`
              - Get a value indicating whether the specified profile type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.profile_type`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.profile_supported_types`
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.profile`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudeRealTimeDataReference


Property detail
---------------

.. py:property:: profile_type
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.profile_type
    :type: VEHICLE_PROFILE

    Get realtime data reference profile type.

.. py:property:: profile_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.profile_supported_types
    :type: list

    Returns an array of valid profiles.

.. py:property:: profile
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.profile
    :type: IVehicleAttitudeProfile

    Returns a data reference profile or null if no data reference profile has yet been selected.


Method detail
-------------


.. py:method:: set_profile_type(self, profile: VEHICLE_PROFILE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.set_profile_type

    Set realtime data reference profile type.

    :Parameters:

    **profile** : :obj:`~VEHICLE_PROFILE`

    :Returns:

        :obj:`~None`

.. py:method:: is_profile_type_supported(self, profile: VEHICLE_PROFILE) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudeRealTimeDataReference.is_profile_type_supported

    Get a value indicating whether the specified profile type can be used.

    :Parameters:

    **profile** : :obj:`~VEHICLE_PROFILE`

    :Returns:

        :obj:`~bool`



