IVehiclePropagatorAviator
=========================

.. py:class:: ansys.stk.core.stkobjects.IVehiclePropagatorAviator

   IVehiclePropagator
   
   Aviator propagator interface.

.. py:currentmodule:: IVehiclePropagatorAviator

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorAviator.get_flight_mission`
              - Return the underlying Flight Mission object.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.IVehiclePropagatorAviator.avtr_propagator`
              - Aviator propagator object.


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects import IVehiclePropagatorAviator


Property detail
---------------

.. py:property:: avtr_propagator
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorAviator.avtr_propagator
    :type: typing.Any

    Aviator propagator object.


Method detail
-------------

.. py:method:: get_flight_mission(self) -> typing.Any
    :canonical: ansys.stk.core.stkobjects.IVehiclePropagatorAviator.get_flight_mission

    Return the underlying Flight Mission object.

    :Returns:

        :obj:`~typing.Any`


