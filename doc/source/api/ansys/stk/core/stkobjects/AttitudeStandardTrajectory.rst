AttitudeStandardTrajectory
==========================

.. py:class:: ansys.stk.core.stkobjects.AttitudeStandardTrajectory

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeStandard`, :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitude`

   Standard attitude profile for launch vehicle or missile.

.. py:currentmodule:: AttitudeStandardTrajectory

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardTrajectory.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardTrajectory.external`
              - Get the precomputed (external) attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.AttitudeStandardTrajectory.pointing`
              - Get the target pointing attitude properties.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import AttitudeStandardTrajectory


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardTrajectory.basic
    :type: AttitudeStandardBasic

    Get the basic attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardTrajectory.external
    :type: VehicleAttitudeExternal

    Get the precomputed (external) attitude properties.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.AttitudeStandardTrajectory.pointing
    :type: VehicleAttitudePointing

    Get the target pointing attitude properties.


