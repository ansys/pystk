IVehicleHPOPForceModel
======================

.. py:class:: IVehicleHPOPForceModel

   object
   
   Interface for HPOP force models.

.. py:currentmodule:: ansys.stk.core.stkobjects

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~central_body_gravity`
            * - :py:meth:`~solar_radiation_pressure`
            * - :py:meth:`~drag`
            * - :py:meth:`~third_body_gravity`
            * - :py:meth:`~more_options`
            * - :py:meth:`~eclipsing_bodies`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleHPOPForceModel


Property detail
---------------

.. py:property:: central_body_gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.central_body_gravity
    :type: "IAgVeHPOPCentralBodyGravity"

    Get the central body gravity properties.

.. py:property:: solar_radiation_pressure
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.solar_radiation_pressure
    :type: "IAgVeHPOPSolarRadiationPressure"

    Get the solar radiation pressure properties.

.. py:property:: drag
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.drag
    :type: "IAgVeHPOPForceModelDrag"

    Get the atmospheric drag properties.

.. py:property:: third_body_gravity
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.third_body_gravity
    :type: "IAgVeThirdBodyGravityCollection"

    Get the 3rd-body gravity properties.

.. py:property:: more_options
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.more_options
    :type: "IAgVeHPOPForceModelMoreOptions"

    Get the additional force model options.

.. py:property:: eclipsing_bodies
    :canonical: ansys.stk.core.stkobjects.IVehicleHPOPForceModel.eclipsing_bodies
    :type: "IAgVeEclipsingBodies"

    Get the eclipsing bodies.


