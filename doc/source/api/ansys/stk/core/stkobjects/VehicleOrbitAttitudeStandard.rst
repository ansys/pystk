VehicleOrbitAttitudeStandard
============================

.. py:class:: ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitudeStandard`, :py:class:`~ansys.stk.core.stkobjects.IVehicleAttitude`

   Standard attitude profile for satellite.

.. py:currentmodule:: VehicleOrbitAttitudeStandard

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard.pointing`
              - Get the target pointing attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard.external`
              - Get the precomputed (external) attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard.integrated_attitude`
              - Returns a reference to the Integrated Attitude Tool.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleOrbitAttitudeStandard


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard.basic
    :type: VehicleStandardBasic

    Get the basic attitude properties.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard.pointing
    :type: VehicleAttitudePointing

    Get the target pointing attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard.external
    :type: VehicleAttitudeExternal

    Get the precomputed (external) attitude properties.

.. py:property:: integrated_attitude
    :canonical: ansys.stk.core.stkobjects.VehicleOrbitAttitudeStandard.integrated_attitude
    :type: VehicleIntegratedAttitude

    Returns a reference to the Integrated Attitude Tool.


