AttitudeStandardOrbit
=====================

.. py:class:: ansys.stk.core.stkobjects.AttitudeStandardOrbit

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeStandard`, :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitude`

   Standard attitude profile for satellite.

.. py:currentmodule:: AttitudeStandardOrbit

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardOrbit.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardOrbit.pointing`
              - Get the target pointing attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardOrbit.external`
              - Get the precomputed (external) attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardOrbit.integrated_attitude`
              - Return a reference to the Integrated Attitude Tool.



Examples
--------

Set satellite attitude external

.. code-block:: python

    # Satellite satellite: Satellite object
    installPath = (
        r"C:\Program Files\AGI\STK 12" if os.name == "nt" else os.environ["STK_INSTALL_DIR"]
    )
    satellite.attitude.external.load(
        os.path.join(
            installPath,
            "Data",
            "Resources",
            "stktraining",
            "text",
            "AttitudeTimeEulerAngles_Example.a",
        )
    )


Set satellite attitude targeting

.. code-block:: python

    # Satellite satellite: Satellite object
    attitudePointing = satellite.attitude.pointing
    attitudePointing.use_target_pointing = True
    attitudePointing.targets.remove_all()
    attitudePointing.targets.add("AreaTarget/MyAreaTarget")
    attitudePointing.target_times.use_access_times = True


Set satellite attitude basic spinning

.. code-block:: python

    # Satellite satellite: Satellite object
    basic = satellite.attitude.basic
    basic.set_profile_type(AttitudeProfile.SPINNING)
    basic.profile.body.assign_xyz(0, 0, 1)
    basic.profile.inertial.assign_xyz(0, 1, 0)
    basic.profile.rate = 6  # rev/sec


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeStandardOrbit


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardOrbit.basic
    :type: AttitudeStandardBasic

    Get the basic attitude properties.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardOrbit.pointing
    :type: VehicleAttitudePointing

    Get the target pointing attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardOrbit.external
    :type: VehicleAttitudeExternal

    Get the precomputed (external) attitude properties.

.. py:property:: integrated_attitude
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardOrbit.integrated_attitude
    :type: VehicleIntegratedAttitude

    Return a reference to the Integrated Attitude Tool.


