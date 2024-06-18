IVehicleProfileSpinning
=======================

.. py:class:: IVehicleProfileSpinning

   IVehicleAttitudeProfile
   
   Spinning attitude profile.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~body`
            * - :py:meth:`~inertial`
            * - :py:meth:`~rate`
            * - :py:meth:`~offset`
            * - :py:meth:`~smart_epoch`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleProfileSpinning


Property detail
---------------

.. py:property:: body
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileSpinning.body
    :type: "IAgDirection"

    Get the spin axis in the body frame.

.. py:property:: inertial
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileSpinning.inertial
    :type: "IAgDirection"

    Get the spin axis in the inertial frame.

.. py:property:: rate
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileSpinning.rate
    :type: float

    Spin rate: specified in revolutions per minute; positive values indicate rotation in a right-handed sense with respect to the spin axis. Uses AngleRate Dimension.

.. py:property:: offset
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileSpinning.offset
    :type: float

    Initial spin offset: an angular measure of the difference between the satellite orientation at the offset epoch from the orientation achieved by orienting the spin axis. Uses Angle Dimension.

.. py:property:: smart_epoch
    :canonical: ansys.stk.core.stkobjects.IVehicleProfileSpinning.smart_epoch
    :type: "IAgCrdnEventSmartEpoch"

    Epoch of the offset.


