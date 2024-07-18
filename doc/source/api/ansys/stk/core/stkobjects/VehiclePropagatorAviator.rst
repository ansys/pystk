VehiclePropagatorAviator
========================

.. py:class:: ansys.stk.core.stkobjects.VehiclePropagatorAviator

   Bases: :py:class:`~ansys.stk.core.stkobjects.IVehiclePropagator`

   Class defining the Mission Modler propagator for an Aircraft.

.. py:currentmodule:: VehiclePropagatorAviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorAviator.get_flight_mission`
              - Return the underlying Flight Mission object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.VehiclePropagatorAviator.avtr_propagator`
              - Aviator propagator object.



Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import VehiclePropagatorAviator


Property detail
---------------

.. py:property:: avtr_propagator
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorAviator.avtr_propagator
    :type: typing.Any

    Aviator propagator object.


Method detail
-------------

.. py:method:: get_flight_mission(self) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.VehiclePropagatorAviator.get_flight_mission

    Return the underlying Flight Mission object.

    :Returns:

        :obj:`~typing.Any`


