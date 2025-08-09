AttitudeProfileSpinning
=======================

.. py:class:: ansys.stk.core.stkobjects.AttitudeProfileSpinning

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`

   Spinning attitude profile.

.. py:currentmodule:: AttitudeProfileSpinning

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileSpinning.body`
              - Get the spin axis in the body frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileSpinning.inertial`
              - Get the spin axis in the inertial frame.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileSpinning.rate`
              - Spin rate: specified in revolutions per minute; positive values indicate rotation in a right-handed sense with respect to the spin axis. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileSpinning.offset`
              - Initial spin offset: an angular measure of the difference between the satellite orientation at the offset epoch from the orientation achieved by orienting the spin axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeProfileSpinning.smart_epoch`
              - Epoch of the offset.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeProfileSpinning


Property detail
---------------

.. py:property:: body
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileSpinning.body
    :type: IDirection

    Get the spin axis in the body frame.

.. py:property:: inertial
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileSpinning.inertial
    :type: IDirection

    Get the spin axis in the inertial frame.

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileSpinning.rate
    :type: float

    Spin rate: specified in revolutions per minute; positive values indicate rotation in a right-handed sense with respect to the spin axis. Uses AngleRate Dimension.

.. py:property:: offset
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileSpinning.offset
    :type: float

    Initial spin offset: an angular measure of the difference between the satellite orientation at the offset epoch from the orientation achieved by orienting the spin axis. Uses Angle Dimension.

.. py:property:: smart_epoch
    :canonical: ansys.stk.core.stkobjects.AttitudeProfileSpinning.smart_epoch
    :type: ITimeToolInstantSmartEpoch

    Epoch of the offset.


