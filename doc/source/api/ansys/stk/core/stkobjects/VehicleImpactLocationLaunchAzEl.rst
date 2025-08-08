VehicleImpactLocationLaunchAzEl
===============================

.. py:class:: ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehicleImpactLocation`

   Class defining the option to use azimuth and elevation to specify the Missile's impact location.

.. py:currentmodule:: VehicleImpactLocationLaunchAzEl

Overview
--------

.. tab-set::

    .. tab-item:: Properties

        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl.azimuth`
              - Launch azimuth. Uses Angle Dimension. If this property is set, please set the other properties of this interface explicitly.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl.delta_v`
              - Fixed Delta V. Uses Rate Dimension. If this property is set, please set the other properties of this interface explicitly.
            * - :py:attr:`~ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl.elevation`
              - Launch elevation. Uses Angle Dimension. If this property is set, please set the other properties of this interface explicitly.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehicleImpactLocationLaunchAzEl


Property detail
---------------

.. py:property:: azimuth
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl.azimuth
    :type: float

    Launch azimuth. Uses Angle Dimension. If this property is set, please set the other properties of this interface explicitly.

.. py:property:: delta_v
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl.delta_v
    :type: float

    Fixed Delta V. Uses Rate Dimension. If this property is set, please set the other properties of this interface explicitly.

.. py:property:: elevation
    :canonical: ansys.stk.core.stkobjects.VehicleImpactLocationLaunchAzEl.elevation
    :type: float

    Launch elevation. Uses Angle Dimension. If this property is set, please set the other properties of this interface explicitly.


