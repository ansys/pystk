IManeuverFinite
===============

.. py:class:: IManeuverFinite

   IManeuver
   
   Engine properties for a Finite Maneuver.

.. py:currentmodule:: ansys.stk.core.stkobjects.astrogator

Overview
--------

.. tab-set::

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:meth:`~pressure_mode`
            * - :py:meth:`~thrust_efficiency`
            * - :py:meth:`~thrust_efficiency_mode`
            * - :py:meth:`~propagator`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.astrogator import IManeuverFinite


Property detail
---------------

.. py:property:: pressure_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinite.pressure_mode
    :type: PRESSURE_MODE

    Gets or sets the pressure mode.

.. py:property:: thrust_efficiency
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinite.thrust_efficiency
    :type: float

    Gets or sets the thrust efficiency value. Any number above zero is valid, with typical values around 0.98 to 1.02. Dimensionless.

.. py:property:: thrust_efficiency_mode
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinite.thrust_efficiency_mode
    :type: THRUST_TYPE

    Thrust - the calculations that are effected by the thrust efficiency value.

.. py:property:: propagator
    :canonical: ansys.stk.core.stkobjects.astrogator.IManeuverFinite.propagator
    :type: IAgVAManeuverFinitePropagator

    Get the propagator.


