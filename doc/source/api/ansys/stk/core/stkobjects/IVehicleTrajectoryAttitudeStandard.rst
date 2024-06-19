IVehicleTrajectoryAttitudeStandard
==================================

.. py:class:: IVehicleTrajectoryAttitudeStandard

   IVehicleAttitudeStandard
   
   Standard attitude profile for launch vehicle or missile.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~basic`
            * - :py:meth:`~pointing`
            * - :py:meth:`~external`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTrajectoryAttitudeStandard


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.basic
    :type: IAgVeStandardBasic

    Get the basic attitude properties.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.pointing
    :type: IAgVeAttPointing

    Get the target pointing attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.external
    :type: IAgVeAttExternal

    Get the precomputed (external) attitude properties.


