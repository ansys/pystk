VehicleTrajectoryAttitudeStandard
=================================

.. py:class:: ansys.stk.core.stkobjects.VehicleTrajectoryAttitudeStandard

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeStandard`, :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitude`

   Standard attitude profile for launch vehicle or missile.

.. py:currentmodule:: VehicleTrajectoryAttitudeStandard

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTrajectoryAttitudeStandard.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTrajectoryAttitudeStandard.pointing`
              - Get the target pointing attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleTrajectoryAttitudeStandard.external`
              - Get the precomputed (external) attitude properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleTrajectoryAttitudeStandard


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.VehicleTrajectoryAttitudeStandard.basic
    :type: IVehicleStandardBasic

    Get the basic attitude properties.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.VehicleTrajectoryAttitudeStandard.pointing
    :type: IVehicleAttitudePointing

    Get the target pointing attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.VehicleTrajectoryAttitudeStandard.external
    :type: IVehicleAttitudeExternal

    Get the precomputed (external) attitude properties.


