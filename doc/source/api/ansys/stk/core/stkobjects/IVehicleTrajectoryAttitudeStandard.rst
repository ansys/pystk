IVehicleTrajectoryAttitudeStandard
==================================

.. py:class:: ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard

   IVehicleAttitudeStandard
   
   Standard attitude profile for launch vehicle or missile.

.. py:currentmodule:: IVehicleTrajectoryAttitudeStandard

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.pointing`
              - Get the target pointing attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.external`
              - Get the precomputed (external) attitude properties.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleTrajectoryAttitudeStandard


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.basic
    :type: IVehicleStandardBasic

    Get the basic attitude properties.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.pointing
    :type: IVehicleAttitudePointing

    Get the target pointing attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.IVehicleTrajectoryAttitudeStandard.external
    :type: IVehicleAttitudeExternal

    Get the precomputed (external) attitude properties.


