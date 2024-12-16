VehicleAttitudeRealTimeDataReference
====================================

.. py:class:: ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference

   Reference attitude profile for the incoming attitude data.

.. py:currentmodule:: VehicleAttitudeRealTimeDataReference

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.set_profile_type`
              - Set realtime data reference profile type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.is_profile_type_supported`
              - Get a value indicating whether the specified profile type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile_type`
              - Get realtime data reference profile type.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile_supported_types`
              - Returns an array of valid profiles.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile`
              - Returns a data reference profile or null if no data reference profile has yet been selected.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleAttitudeRealTimeDataReference


Property detail
---------------

.. py:property:: profile_type
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile_type
    :type: AttitudeProfile

    Get realtime data reference profile type.

.. py:property:: profile_supported_types
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile_supported_types
    :type: list

    Returns an array of valid profiles.

.. py:property:: profile
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.profile
    :type: IVehicleAttitudeProfile

    Returns a data reference profile or null if no data reference profile has yet been selected.


Method detail
-------------


.. py:method:: set_profile_type(self, profile: AttitudeProfile) -> None
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.set_profile_type

    Set realtime data reference profile type.

    :Parameters:

    **profile** : :obj:`~AttitudeProfile`

    :Returns:

        :obj:`~None`

.. py:method:: is_profile_type_supported(self, profile: AttitudeProfile) -> bool
    :canonical: ansys.stk.core.stkobjects.VehicleAttitudeRealTimeDataReference.is_profile_type_supported

    Get a value indicating whether the specified profile type can be used.

    :Parameters:

    **profile** : :obj:`~AttitudeProfile`

    :Returns:

        :obj:`~bool`



