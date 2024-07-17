VehicleProfileSpinAboutXXX
==========================

.. py:class:: ansys.stk.core.stkobjects.VehicleProfileSpinAboutXXX

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeProfile`

   Shared for Spin About Nadir and Spin About Sun Vector profile parameters.

.. py:currentmodule:: VehicleProfileSpinAboutXXX

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleProfileSpinAboutXXX.rate`
              - Gets or sets the spin rate in revolutions per minute; positive values indicate rotation in a right-handed sense with respect to the spin axis. Uses AngleRate Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleProfileSpinAboutXXX.offset`
              - Gets or sets the initial spin offset as an angular measure of the difference between the satellite orientation at the offset epoch and the orientation achieved by orienting the spin axis. Uses Angle Dimension.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleProfileSpinAboutXXX.smart_epoch`
              - Epoch of the offset.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleProfileSpinAboutXXX


Property detail
---------------

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.VehicleProfileSpinAboutXXX.rate
    :type: float

    Gets or sets the spin rate in revolutions per minute; positive values indicate rotation in a right-handed sense with respect to the spin axis. Uses AngleRate Dimension.

.. py:property:: offset
    :canonical: ansys.stk.core.stkobjects.VehicleProfileSpinAboutXXX.offset
    :type: float

    Gets or sets the initial spin offset as an angular measure of the difference between the satellite orientation at the offset epoch and the orientation achieved by orienting the spin axis. Uses Angle Dimension.

.. py:property:: smart_epoch
    :canonical: ansys.stk.core.stkobjects.VehicleProfileSpinAboutXXX.smart_epoch
    :type: ITimeToolEventSmartEpoch

    Epoch of the offset.


