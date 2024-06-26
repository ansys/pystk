IVehicleProfilePrecessingSpin
=============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin

   IVehicleAttitudeProfile
   
   Precessing Spin attitude profile, in which the spin axis of the satellite specified in the body frame is offset through the nutation angle away from the angular momentum direction specified in the inertial frame.

.. py:currentmodule:: IVehicleProfilePrecessingSpin

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.body`
              - Get the spin axis in the body frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.inertial_precession`
              - Get the precession in the inertial frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.precession`
              - Get the precession rate and offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.spin`
              - Get the spin rate and offset.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.nutation_angle`
              - Nutation angle by which the spin axis is offset from the angular momentum direction defined in the inertial frame. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.reference_axes`
              - Reference axes with respect to which precessing spin is defined. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.smart_epoch`
              - Get the epoch of the attitude profile.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleProfilePrecessingSpin


Property detail
---------------

.. py:property:: body
    :canonical: ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.body
    :type: IDirection

    Get the spin axis in the body frame.

.. py:property:: inertial_precession
    :canonical: ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.inertial_precession
    :type: IDirection

    Get the precession in the inertial frame.

.. py:property:: precession
    :canonical: ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.precession
    :type: IVehicleRateOffset

    Get the precession rate and offset.

.. py:property:: spin
    :canonical: ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.spin
    :type: IVehicleRateOffset

    Get the spin rate and offset.

.. py:property:: nutation_angle
    :canonical: ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.nutation_angle
    :type: float

    Nutation angle by which the spin axis is offset from the angular momentum direction defined in the inertial frame. Uses Angle Dimension.

.. py:property:: reference_axes
    :canonical: ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.reference_axes
    :type: str

    Reference axes with respect to which precessing spin is defined. The satellite's body axes or any axes dependent upon the satellite's body axes are invalid for this attitude profile; all other axes are valid choices for the reference axes.

.. py:property:: smart_epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleProfilePrecessingSpin.smart_epoch
    :type: ITimeToolEventSmartEpoch

    Get the epoch of the attitude profile.


