IVehicleStandardBasic
=====================

.. py:class:: IVehicleStandardBasic

   object
   
   Basic attitude profile.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~set_profile_type`
              - Set basic attitude profile type.
            * - :py:meth:`~is_profile_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~profile_type`
            * - :py:meth:`~profile_supported_types`
            * - :py:meth:`~profile`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleStandardBasic


Property detail
---------------

.. py:property:: profile_type
    :canonical: ansys.stk.core.stkobjects.IVehicleStandardBasic.profile_type
    :type: VEHICLE_PROFILE

    Get basic attitude profile type.

.. py:property:: profile_supported_types
    :canonical: ansys.stk.core.stkobjects.IVehicleStandardBasic.profile_supported_types
    :type: list

    Returns an array of valid choices.

.. py:property:: profile
    :canonical: ansys.stk.core.stkobjects.IVehicleStandardBasic.profile
    :type: IAgVeAttProfile

    Returns the profile interface.


Method detail
-------------


.. py:method:: set_profile_type(self, profile: VEHICLE_PROFILE) -> None
    :canonical: ansys.stk.core.stkobjects.IVehicleStandardBasic.set_profile_type

    Set basic attitude profile type.

    :Parameters:

    **profile** : :obj:`~VEHICLE_PROFILE`

    :Returns:

        :obj:`~None`

.. py:method:: is_profile_type_supported(self, profile: VEHICLE_PROFILE) -> bool
    :canonical: ansys.stk.core.stkobjects.IVehicleStandardBasic.is_profile_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

    **profile** : :obj:`~VEHICLE_PROFILE`

    :Returns:

        :obj:`~bool`



