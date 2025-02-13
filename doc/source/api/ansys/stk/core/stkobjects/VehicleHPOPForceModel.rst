VehicleHPOPForceModel
=====================

.. py:class:: ansys.stk.core.stkobjects.VehicleHPOPForceModel

   Class defining HPOP force models.

.. py:currentmodule:: VehicleHPOPForceModel

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModel.central_body_gravity`
              - Get the central body gravity properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModel.solar_radiation_pressure`
              - Get the solar radiation pressure properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModel.drag`
              - Get the atmospheric drag properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModel.third_body_gravity`
              - Get the 3rd-body gravity properties.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModel.more_options`
              - Get the additional force model options.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleHPOPForceModel.eclipsing_bodies`
              - Get the eclipsing bodies.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleHPOPForceModel


Property detail
---------------

.. py:property:: central_body_gravity
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModel.central_body_gravity
    :type: VehicleHPOPCentralBodyGravity

    Get the central body gravity properties.

.. py:property:: solar_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModel.solar_radiation_pressure
    :type: VehicleHPOPSolarRadiationPressure

    Get the solar radiation pressure properties.

.. py:property:: drag
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModel.drag
    :type: VehicleHPOPForceModelDrag

    Get the atmospheric drag properties.

.. py:property:: third_body_gravity
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModel.third_body_gravity
    :type: PropagatorHPOPThirdBodyGravityCollection

    Get the 3rd-body gravity properties.

.. py:property:: more_options
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModel.more_options
    :type: VehicleHPOPForceModelMoreOptions

    Get the additional force model options.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.VehicleHPOPForceModel.eclipsing_bodies
    :type: VehicleEclipsingBodies

    Get the eclipsing bodies.


