IVehicleAttitudePointing
========================

.. py:class:: IVehicleAttitudePointing

   IVehiclePointing
   
   Target pointing attitude parameters.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~advanced`
            * - :py:meth:`~target_slew`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleAttitudePointing


Property detail
---------------

.. py:property:: advanced
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudePointing.advanced
    :type: "IAgVeAccessAdvanced"

    Returns advanced targeting access computation properties.

.. py:property:: target_slew
    :canonical: ansys.stk.core.stkobjects.IVehicleAttitudePointing.target_slew
    :type: "IAgVeAttTargetSlew"

    Define the time required for the vehicle to move from its basic attitude to its target pointing attitude, and to change from the target pointing attitude back to the basic attitude.


