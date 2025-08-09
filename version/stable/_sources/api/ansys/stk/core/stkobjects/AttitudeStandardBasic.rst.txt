AttitudeStandardBasic
=====================

.. py:class:: ansys.stk.core.stkobjects.AttitudeStandardBasic

   Basic attitude profile.

.. py:currentmodule:: AttitudeStandardBasic

Overview
--------

.. tab-set::

    .. tab-item:: Methods

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardBasic.set_profile_type`
              - Set basic attitude profile type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardBasic.is_profile_type_supported`
              - Get a value indicating whether the specified type can be used.

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardBasic.profile_type`
              - Get basic attitude profile type.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardBasic.profile_supported_types`
              - Return an array of valid choices.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardBasic.profile`
              - Return the profile interface.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeStandardBasic


Property detail
---------------

.. py:property:: profile_type
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardBasic.profile_type
    :type: AttitudeProfile

    Get basic attitude profile type.

.. py:property:: profile_supported_types
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardBasic.profile_supported_types
    :type: list

    Return an array of valid choices.

.. py:property:: profile
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardBasic.profile
    :type: IVehicleAttitudeProfile

    Return the profile interface.


Method detail
-------------


.. py:method:: set_profile_type(self, profile: AttitudeProfile) -> None
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardBasic.set_profile_type

    Set basic attitude profile type.

    :Parameters:

        **profile** : :obj:`~AttitudeProfile`


    :Returns:

        :obj:`~None`

.. py:method:: is_profile_type_supported(self, profile: AttitudeProfile) -> bool
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardBasic.is_profile_type_supported

    Get a value indicating whether the specified type can be used.

    :Parameters:

        **profile** : :obj:`~AttitudeProfile`


    :Returns:

        :obj:`~bool`



