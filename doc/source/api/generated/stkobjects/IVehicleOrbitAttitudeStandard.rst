IVehicleOrbitAttitudeStandard
=============================

.. py:class:: IVehicleOrbitAttitudeStandard

   IVehicleAttitudeStandard
   
   Standard attitude profile for satellite.

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
            * - :py:meth:`~integrated_attitude`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehicleOrbitAttitudeStandard


Property detail
---------------

.. py:property:: basic
    :canonical: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.basic
    :type: "IAgVeStandardBasic"

    Get the basic attitude properties.

.. py:property:: pointing
    :canonical: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.pointing
    :type: "IAgVeAttPointing"

    Get the target pointing attitude properties.

.. py:property:: external
    :canonical: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.external
    :type: "IAgVeAttExternal"

    Get the precomputed (external) attitude properties.

.. py:property:: integrated_attitude
    :canonical: ansys.stk.core.stkobjects.IVehicleOrbitAttitudeStandard.integrated_attitude
    :type: "IAgVeIntegratedAttitude"

    Returns a reference to the Integrated Attitude Tool.


