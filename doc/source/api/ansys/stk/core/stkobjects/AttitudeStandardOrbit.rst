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


