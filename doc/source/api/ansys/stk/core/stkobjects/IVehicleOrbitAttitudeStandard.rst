IVehicleOrbitAttitudeStandard
=============================

.. py:class:: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard

   IVehicleAttitudeStandard
   
   Standard attitude profile for satellite.

.. py:currentmodule:: IVehicleOrbitAttitudeStandard

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.basic`
              - Get the basic attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.pointing`
              - Get the target pointing attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.external`
              - Get the precomputed (external) attitude properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.integrated_attitude`
              - Returns a reference to the Integrated Attitude Tool.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleOrbitAttitudeStandard


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.basic
    :type: IVehicleStandardBasic

    Get the basic attitude properties.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.pointing
    :type: IVehicleAttitudePointing

    Get the target pointing attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.external
    :type: IVehicleAttitudeExternal

    Get the precomputed (external) attitude properties.

.. py:property:: integrated_attitude
    :canonical: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.integrated_attitude
    :type: IVehicleIntegratedAttitude

    Returns a reference to the Integrated Attitude Tool.


