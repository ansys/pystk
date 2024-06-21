IProcedureFormationFlyer
========================

.. py:class:: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer

   object
   
   Interface used to access the options for an enroute procedure.

.. py:currentmodule:: IProcedureFormationFlyer

Overview
--------

.. tab-set::

    .. tab-item:: Methods
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.get_as_procedure`
              - Get the procedure interface.

    .. tab-item:: Properties
        
        .. list-table::
            :header-rows: 0
            :widths: auto

            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.min_time_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.max_time_step`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.cross_range_close_rate`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.initial_close_max_speed_advantage`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_condition`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_time`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_down_range`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_fuel_state`
            * - :py:attr:`~ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_on_hover`


Import detail
-------------

.. code-block:: python

    from ansys.stk.core.stkobjects.aviator import IProcedureFormationFlyer


Property detail
---------------

.. py:property:: min_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.min_time_step
    :type: float

    Get Min time Step.

.. py:property:: max_time_step
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.max_time_step
    :type: float

    Get Max time Step.

.. py:property:: cross_range_close_rate
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.cross_range_close_rate
    :type: float

    Get Cross Range close rate.

.. py:property:: initial_close_max_speed_advantage
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.initial_close_max_speed_advantage
    :type: float

    Get Initial Close Max Speed Advantage.

.. py:property:: stop_condition
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_condition
    :type: FORMATION_FLYER_STOP_CONDITION

    Get Stop condition.

.. py:property:: stop_time
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_time
    :type: float

    Get stop time.

.. py:property:: stop_down_range
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_down_range
    :type: float

    Get stop downrange.

.. py:property:: stop_fuel_state
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_fuel_state
    :type: float

    Get stop fuel state.

.. py:property:: stop_on_hover
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.stop_on_hover
    :type: None

    Set Stop on hover mode.


Method detail
-------------

















.. py:method:: get_as_procedure(self) -> IProcedure
    :canonical: ansys.stk.core.stkobjects.aviator.IProcedureFormationFlyer.get_as_procedure

    Get the procedure interface.

    :Returns:

        :obj:`~IProcedure`



